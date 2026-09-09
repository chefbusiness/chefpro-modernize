# LENTE 3 — Bloque normativo para abrir y operar una pastelería con obrador en España

**Producto:** «Cómo Montar una Pastelería» (producto nuevo nº 4 del ciclo; hermano de `guia-panaderia-obrador`)
**Fecha del informe:** 2026-09-09 · **Todas las consultas web se hicieron el 2026-09-09**
**Autor del bloque:** subagente L3 (research normativo). **Esto NO es contenido de producto**: es research y propuesta.

---

## 0. Método, niveles de verificación y limitaciones declaradas

### 0.1 Método

1. Cada norma se buscó por su identificador y se abrió su **texto consolidado en `boe.es`** (`buscar/act.php?id=…`) o su ficha en `boe.es` para normas de la UE.
2. Cuando el HTML del BOE no servía el articulado (pasa con normas largas: la página sirve sólo el índice), se descargó el **PDF consolidado** y se extrajo el texto localmente con `pypdf`. Así se obtuvo el articulado literal del **RD 1021/2022** y de dos publicaciones del **BOCM**.
3. Los boletines autonómicos se leyeron en PDF por el mismo procedimiento (BOCM núm. 73 de 27/03/2026 y BOCM núm. 50 de 28/02/2026).
4. Todo dato numérico lleva **URL + fecha de consulta**. Lo que sólo pude sostener con fuente secundaria (blog, consultora, prensa) va marcado **«sin fuente primaria»** y NO debe entrar en el producto como dato.

### 0.2 Restricciones que condicionaron el trabajo

- **No se pudo leer el articulado completo de la Ley 1/2025** (desperdicio alimentario) desde el BOE: la página sirve el índice y el PDF no se llegó a descargar. Los artículos 6 y 8 se transcriben desde la lectura parcial del BOE; **el régimen sancionador y la fecha exacta de entrada en vigor quedan SIN verificar contra el texto** (ver PA-31 y §0.3).
- **No se pudo leer literalmente el artículo 91 de la Ley 37/1992** (IVA): la página consolidada del BOE trunca antes de llegar ahí y la URL de la sede de la AEAT devolvió 404. El contenido del art. 91 se sostiene sobre la **Resolución DGT de 24-feb-2025 (BOE-A-2025-3950)**, que lo reproduce — fuente oficial, pero indirecta.
- **No se pudo leer el articulado del RD 496/2010** (norma de calidad de confitería/pastelería). Las definiciones se recogieron de la lectura del BOE que sí devolvió contenido, pero **no pude confirmar por lectura directa si el decreto regula o no los términos «artesano», «artesanal», «casero»**; la lectura disponible dice que no aparecen. Marcado como verificación de nivel B.
- **Cataluña, Andalucía y Comunitat Valenciana**: los decretos autonómicos de registro se identificaron y se describen, pero **`noticias.juridicas.com` devolvió error de certificado TLS** en dos intentos, así que el Decreto 13/2025 valenciano y el Decreto 85/2024 catalán están a nivel B (identificados y descritos por fuente secundaria/agregador, no leídos en su boletín).
- **No existe fuente primaria para los costes de inversión.** Todo lo que circula (200.000 €, 81.000 € de obra, 46.000 € de equipamiento) sale de blogs comerciales y de una entrevista de prensa. Va todo en §11 como «sin fuente primaria».

### 0.3 Niveles de verificación usados en las fichas

| Nivel | Qué significa |
|---|---|
| **A** | Texto literal leído en el boletín oficial (BOE/BOCM) o en su PDF consolidado. Se puede citar entrecomillado. |
| **B** | Norma identificada por su referencia oficial, contenido descrito por fuente oficial indirecta (ficha del BOE, resolución que la reproduce) o agregador jurídico. **No citar entrecomillado.** |
| **C** | Sólo fuente secundaria (consultora, blog, prensa). **No entra en el producto como dato.** |

---

## 1. Bloque A — Registro sanitario: cuándo RGSEAA y cuándo registro autonómico

Éste es el punto donde más se equivocan las fuentes gratuitas, y es el que decide el trámite de arranque de una pastelería.

### PA-01 · La pastelería con obrador que vende al consumidor final NO va al RGSEAA — nivel A

**Norma:** RD 191/2011, art. 2.2, **en la redacción dada por la disposición final primera del RD 1021/2022**.
**Texto literal** (leído en el PDF consolidado del RD 1021/2022):

> «2. Quedan excluidos de la obligación de inscripción en el Registro, sin perjuicio de los controles oficiales correspondientes, los establecimientos de comercio al por menor definidos en el artículo 2 del Real Decreto 1021/2022, de 13 de diciembre […]
> Todos los establecimientos de comercio al por menor deberán inscribirse en los registros de las autoridades competentes de las comunidades autónomas establecidos al efecto, **previa comunicación o declaración responsable, que no será habilitante**, del operador de la empresa alimentaria a las autoridades competentes del lugar de ubicación del establecimiento.»

- **URL:** https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681 · PDF consolidado: https://www.boe.es/buscar/pdf/2022/BOE-A-2022-21681-consolidado.pdf · consultado 2026-09-09.
- **RD 191/2011 consolidado:** https://www.boe.es/buscar/act.php?id=BOE-A-2011-4293 · consultado 2026-09-09.
- **Aplica a:** obrador con venta directa · cafetería-pastelería · pastelería sin obrador · obrador en casa. **NO** aplica al obrador B2B (ver PA-03).
- **Consecuencia práctica que hay que decir en el producto:** el número «RGSEAA» que muchos blogs presentan como obligatorio **no lo es** para la pastelería minorista típica. Lo que hay es una **comunicación (o declaración responsable) autonómica que no habilita** para abrir: no se espera resolución, pero tampoco protege de nada.
- **Materializa en:** checklist «Trámites de apertura» (hoja de ruta con responsable y plazo) + xlsx `01_tramites_apertura` con columna de comunidad autónoma.

### PA-02 · Cuándo SÍ hay que inscribirse en el RGSEAA — nivel A

Cuando el suministro a otros establecimientos deja de ser **marginal, localizado y restringido**. Texto literal del **art. 3 del RD 1021/2022**:

> «1. Los establecimientos de comercio al por menor sólo podrán suministrar alimentos de producción propia y productos de origen animal a establecimientos de comercio al por menor de distinta titularidad si este suministro es marginal, localizado y restringido, cumpliendo todos los requisitos de los apartados 2, 3 y 4.
> 2. Una actividad se considerará **marginal** cuando: a) El suministro de alimentos a otros establecimientos de comercio al por menor es inferior o igual al **25 %** del volumen anual de alimentos comercializados, o b) Supone una comercialización total de un máximo de **500 kg a la semana**, incluyendo el suministro a consumidor final y a otros establecimientos de comercio al por menor.
> 3. Una actividad se considerará **localizada** si el establecimiento […] suministra productos alimenticios a otros establecimientos […] ubicados en la unidad sanitaria local, zona de salud o territorio de iguales características […] o entre zonas limítrofes. En el caso de comercio entre establecimientos de diferentes comunidades autónomas, el suministro podrá realizarse en un radio **inferior o igual a 50 km** desde el establecimiento de origen […]
> 4. Una actividad se considerará **restringida** cuando no se suministren productos alimenticios a establecimientos inscritos en el Registro General Sanitario de Empresas Alimentarias y Alimentos (RGSEAA) […]
> 5. Si un operador […] suministra a otros establecimientos […] deberá presentar una **declaración responsable** […] Contará con la documentación o registros que incluyan los datos de los establecimientos a los que suministra, las cantidades de alimentos suministradas y fechas de suministro.»

- **URL:** PDF consolidado citado en PA-01 · consultado 2026-09-09.
- **Aplica a:** obrador que vende a cafeterías, hoteles, tiendas gourmet; marca blanca; cualquier B2B.
- **Trampa de diseño que hay que meter en el producto:** los tres requisitos son **acumulativos** («cumpliendo todos los requisitos»). Vender el 10 % de la producción (marginal) a una cadena inscrita en el RGSEAA rompe el requisito de **restringido** y obliga a inscribirse. Y el límite de 500 kg/semana **incluye la venta a consumidor final**, no sólo el B2B: una pastelería que despacha mucho mostrador puede pasarse sin haber vendido nada a otro negocio.
- **Materializa en:** xlsx `04_control_suministro_b2b` — registro de suministros con destinatario, kg, fecha, semáforo de los tres umbrales (25 %, 500 kg/semana, radio) y alerta de «te toca RGSEAA».

### PA-03 · Establecimiento central, obrador y sucursales — nivel A

**Art. 3.6 del RD 1021/2022:**

> «Los establecimientos de comercio al por menor que dispongan de un establecimiento central con obrador y sucursales se considerarán una única unidad comercial, pero se inscribirán en el registro de las comunidades autónomas de manera independiente. En estos casos está permitido el suministro de productos alimenticios desde el establecimiento central con obrador a las sucursales, **no considerándose suministro entre establecimientos de comercio al por menor**.»

Definiciones literales del **art. 2.2** (mismo RD):
- **Obrador:** «la parte de un establecimiento de comercio al por menor, **inaccesible al público**, destinada a las actividades de manipulación, preparación, elaboración propia, envasado y, en su caso, almacenamiento de productos alimenticios. Tendrá la misma titularidad que el establecimiento central.»
- **Establecimiento central:** «aquel establecimiento que cuenta con uno o varios obradores, anexos o no, pero ubicados en el mismo municipio o bien en la unidad sanitaria local, zona de salud o territorio definido por la autoridad competente.»
- **Sucursales:** «los establecimientos que incorporan a su comercialización habitual los productos […] elaborados o envasados en el establecimiento central u obrador, de igual titularidad […] y localizados en el municipio donde esté ubicado el establecimiento central o bien en la unidad sanitaria local […]»

- **Consecuencia:** el modelo «obrador central + 2 o 3 despachos» **no consume la cuota del 25 %/500 kg** siempre que la titularidad sea la misma y estén en el mismo municipio o zona de salud. Es una palanca de crecimiento que casi ninguna fuente gratuita explica.
- **Materializa en:** capítulo de modelos de negocio + xlsx de escenarios (obrador único vs central+sucursales).

### PA-04 · El registro autonómico: cada CCAA tiene el suyo, y Madrid lo acaba de crear — nivel A (Madrid) / B (resto)

**Madrid — DECRETO 26/2026, de 25 de marzo, del Consejo de Gobierno**, por el que se crea el **Registro de Empresas Alimentarias de Comercio al por Menor de Productos Alimenticios de la Comunidad de Madrid**. BOCM núm. 73, de **27 de marzo de 2026**, pág. 8.

- **URL:** https://www.bocm.es/boletin/CM_Orden_BOCM/2026/03/27/BOCM-20260327-1.PDF · consultado 2026-09-09 (leído íntegro).
- **Estructura:** preámbulo, **11 artículos en 4 capítulos**, una disposición transitoria, una derogatoria y dos finales.
- **Secciones del registro (art. 6):** a) minoristas de alimentación · b) minoristas de restauración (sin elaboración / con elaboración / a colectividades / otros) · c) sin ubicación fija · d) **viviendas privadas donde se elaboran alimentos para su venta**.
- **Procedimiento (art. 8.1), literal:** «Los operadores […] estarán obligados a presentar la **comunicación** o, en el caso de los locales utilizados principalmente como vivienda privada, una **declaración responsable** […] La presentación de la comunicación o de la declaración responsable para la inscripción en el Registro **no será habilitante para el inicio de la actividad** […]»
- **Datos obligatorios (art. 8.3):** nombre o razón social; domicilio social; correo electrónico; teléfono; **objeto de todas sus actividades**; domicilio del establecimiento.
- **Momento (art. 9.1):** «El obligado presentará la comunicación o, en su defecto, la declaración responsable, **simultáneamente al inicio de la actividad**».
- **Régimen transitorio (D.T. única):** las ya inscritas en el registro de carne fresca pasan **de oficio**; para el resto, «se establece un período transitorio de **un año**, a contar desde la entrada en vigor de este decreto, para notificar mediante comunicación o declaración responsable su inscripción».
- **Entrada en vigor:** día siguiente a su publicación → **28 de marzo de 2026**. Por tanto **el plazo transitorio vence el 28 de marzo de 2027**.
- **Deroga:** la Orden 1531/2005 (registro de comercio al por menor de carne fresca).
- **Sanciones (art. 11):** remite al Capítulo II del Título XIII de la Ley 12/2001 de Ordenación Sanitaria de la Comunidad de Madrid.

> **Esto es oro para el producto y tiene fecha de caducidad comercial**: una pastelería madrileña abierta antes de marzo de 2026 tiene hasta el **28-mar-2027** para inscribirse. Un producto publicado en otoño de 2026 llega justo a tiempo de avisar. Después de esa fecha, la frase hay que reescribirla (ver §14, riesgo R-03).

**Resto de CCAA de ejemplo (nivel B):**

| CCAA | Registro | Referencia localizada | URL |
|---|---|---|---|
| Cataluña | **RSIPAC** (Registre sanitari d'indústries i productes alimentaris de Catalunya), gestionado por la Agència de Salut Pública; notificación electrónica **antes de iniciar la actividad** | Trámite Gencat | https://exteriors.gencat.cat/es/tramits/tramits-temes/Registre-sanitari-dindustries-i-productes-alimentaris-de-Catalunya-RSIPAC-00001 (consultado 2026-09-09) |
| Andalucía | Registro Sanitario de Empresas y Establecimientos Alimentarios; **comunicación previa de inicio de actividad e inscripción** para todo el comercio al por menor | Portal Junta de Andalucía | https://www.juntadeandalucia.es/organismos/presidenciasanidadyemergencias/areas/sanidad/seguridad-alimentaria/tramites-seguridad-alimentaria/paginas/registro-sanitario-alimentos.html (consultado 2026-09-09) |
| C. Valenciana | **REM** — Registro Sanitario de Establecimientos Alimentarios Menores, creado por el **Decreto 13/2025, de 28 de enero, del Consell**, que además regula el suministro entre establecimientos menores y la elaboración en viviendas privadas | Ficha GVA + agregador | https://www.san.gva.es/es/web/salut-publica/registro-de-establecimientos-menores y https://www.gva.es/en/inicio/procedimientos?id_proc=14013&version=red (consultados 2026-09-09) |

- **Pendiente de verificación:** el articulado del Decreto 13/2025 valenciano (TLS roto en el agregador). **No citar su articulado hasta leerlo en el DOGV.**
- **Materializa en:** xlsx `02_registro_sanitario_por_ccaa` con una fila por CCAA (nombre del registro, norma, vía, si es habilitante, enlace), y una nota de mantenimiento: **este cuadro caduca**.

---

## 2. Bloque B — Licencia de actividad, apertura y local

### PA-05 · Régimen general: declaración responsable, no licencia previa — nivel B

- **Marco:** Directiva 2006/123/CE (servicios) + **Ley 20/2013 de garantía de la unidad de mercado** + **Ley 39/2015, art. 69** (declaración responsable y comunicación). El propio Decreto 26/2026 de Madrid los invoca en su preámbulo (leído, nivel A para la cita del preámbulo): «la Ley 20/2013 […] limita la exigencia de autorización […] a que estas razones no puedan salvaguardarse mediante la presentación de una declaración responsable o de una comunicación».
- **Municipal:** Madrid tramita por **declaración responsable** desde la Ordenanza de Apertura de Actividades Económicas (2014), hoy en el marco de la **Ordenanza 6/2022, de 26 de abril, de Licencias Urbanísticas y Declaraciones Responsables** del Ayuntamiento de Madrid.
- **URL de trámite:** https://www.madrid.es/portales/munimadrid/es/Declaracion-responsable-de-actividades-economicas-comerciales-y-de-servicios/ (consultado 2026-09-09).
- **Aviso de método para el producto:** cada municipio tiene su ordenanza. **No se puede escribir «en España se pide X»**; hay que escribir el procedimiento genérico + una plantilla para que el lector rellene el de su ayuntamiento.

### PA-06 · Pastelería CON obrador ≠ tienda: cambia la clasificación urbanística — nivel C (fuente secundaria)

Las fuentes de licencias coinciden en que un local que **sólo vende** es actividad inocua y va por declaración responsable simple, mientras que un local que **elabora** (obrador, horno, extracción) se clasifica de otro modo — en Madrid, como uso industrial en la categoría de *industria artesanal* del PGOUM.

- **Fuentes (secundarias, comerciales):** https://www.madridlicencias.com/blog/como-obtener-la-licencia-o-declaracion-responsable-para-una-panaderia-con-obrador/ · https://www.estudio-l.es/licencia-obrador-panaderia-madrid/ (consultadas 2026-09-09).
- **Marcado «sin fuente primaria».** Para el producto: hay que decirlo como *pregunta a hacer en el ayuntamiento* («¿mi actividad se clasifica como comercio o como industria artesanal en el planeamiento?»), no como afirmación normativa.
- **Materializa en:** checklist «Antes de firmar el alquiler» — 12 preguntas al ayuntamiento y al propietario ANTES de la señal.

### PA-07 · Salida de humos: es el punto que tumba locales — nivel B

- **CTE, Documento Básico HS 3 «Calidad del aire interior»** (Real Decreto 314/2006 y modificaciones): la salida debe estar **en cubierta**, separada **≥ 3 m** de cualquier toma de ventilación y de espacios donde se reúnan personas; sección uniforme, sin obstáculos, acabado que impida el ensuciamiento.
- Conductos por el interior del edificio o por fachada a **< 1,50 m** de zonas de fachada no EI 30, o de balcones/terrazas/huecos: deben ser **EI 30**.
- **URL del DB-HS3:** https://www.profesionales.ventanaskline.com/wp-content/uploads/2016/04/CTE-DB-HS3-calidad-aire.pdf · resumen consultado 2026-09-09. **Para el producto hay que citar el DB-HS oficial del CTE, no este PDF de tercero.**
- **Añadir siempre:** la salida a cubierta exige acuerdo de la comunidad de propietarios y a menudo obra en patio o fachada. Muchos locales «con salida de humos» sólo tienen conducto a fachada.
- **Materializa en:** ficha «Viabilidad del local» — hoja con 3 semáforos: potencia eléctrica, salida de humos a cubierta, altura libre y carga de forjado del obrador.

### PA-08 · Horno eléctrico vs horno de gas — nivel C, PENDIENTE

No he podido verificar con fuente primaria qué cambia normativamente entre un obrador con horno eléctrico y uno con horno de gas (RITE, instalación receptora de gas, RD 919/2006, revisión periódica, certificado de instalador). **No lo escribas todavía.** Es un ítem que exige una pasada específica sobre el RD 919/2006 y el RITE (RD 1027/2007).

---

## 3. Bloque C — Higiene, autocontrol y formación

### PA-09 · El marco es el Rgto. (CE) 852/2004, modificado por el Rgto. (UE) 2021/382 — nivel B

Tres novedades del **Reglamento (UE) 2021/382 de la Comisión, de 3 de marzo de 2021**, en vigor desde el **24 de marzo de 2021**:

1. **Cultura de la seguridad alimentaria** — nuevo **Capítulo XI bis del Anexo II**: compromiso de la dirección, implicación de toda la plantilla, conocimiento de los peligros, comunicación interna clara, recursos suficientes, y aplicación **proporcionada al tamaño y naturaleza** de la empresa.
2. **Gestión de alérgenos** — nuevo punto en el **Capítulo IX del Anexo II**: los equipos, medios de transporte o recipientes usados con sustancias que causan alergias o intolerancias no se reutilizan para alimentos sin ese alérgeno salvo limpieza y verificación de ausencia de residuos visibles.
3. **Redistribución de alimentos** — nuevo **Capítulo V bis del Anexo II**.

- **URL:** https://www.boe.es/buscar/doc.php?id=DOUE-L-2021-80261 · ficha AESAN: https://www.aesan.gob.es/AECOSAN/web/noticias_y_actualizaciones/novedades_legislativas/2021/reglamento_2021_382.htm · consultados 2026-09-09.
- **Nivel B**: la ficha del BOE devolvió el contenido resumido, no el texto completo. **No citar entrecomillado hasta leerlo en EUR-Lex consolidado** (`CELEX:02004R0852`).
- **Por qué importa a una pastelería:** el capítulo de alérgenos es exactamente el problema del obrador (harina, huevo, leche, frutos secos, sésamo, altramuz, sulfitos en frutas confitadas). Y «cultura de seguridad alimentaria» significa que la inspección puede preguntar por la **formación y la comunicación interna**, no sólo por los papeles.
- **Materializa en:** xlsx `05_matriz_alergenos_obrador` (materias primas × 14 alérgenos UE, con producción por lote y orden de elaboración) + un docx corto de «política de cultura de seguridad alimentaria» firmable.

### PA-10 · APPCC simplificado: es legal y está escrito — nivel A

**Art. 20 del RD 1021/2022**, literal:

> «Los establecimientos de comercio al por menor deberán crear, aplicar y mantener actualizado un procedimiento permanente basado en los principios del Análisis de Peligros y Puntos de Control Crítico (en adelante, APPCC), conforme a lo establecido en el artículo 5 del Reglamento (CE) n.º 852/2004 […], **debiendo contar con una persona responsable de su aplicación**.
> Estos procedimientos o sistemas de gestión de la seguridad alimentaria **se podrán aplicar de manera simplificada**, tal y como se establece en la Comunicación de la Comisión con directrices sobre los sistemas de gestión de la seguridad alimentaria para las actividades de los minoristas del sector de la alimentación, incluida la donación de alimentos (**2020/C 199/01**).
> La aplicación voluntaria de **guías de prácticas correctas de higiene** […] puede ser un medio para garantizar que se cumplen las normas sanitarias […]»

- Dos datos que el copy suele perderse: hay que **designar a una persona responsable** (nombre y apellidos, no «la empresa»), y las guías sectoriales son **voluntarias**, no obligatorias.
- **Guías sectoriales localizadas** (nivel B, para citar como recurso, no como obligación): guía unificada del sector de panadería, bollería, pastelería, confitería y repostería (https://www.icoval.org/es/2-Todo-guias-APPCC/2693-GUIA-UNIFICADA-DE-PRACTICAS-CORRECTAS-DE-HIGIENE-DEL-SECTOR-DE-PANADERIA-BOLLERIA-PASTELERIA-CONFITERIA-Y-REPOSTERIA.htm); guía de prácticas correctas para obradores de Aragón (https://www.aragon.es/documents/20127/674325/GUIA+PRACTICAS+OBRADORES.PDF/7579fd55-503f-a24d-213e-9bb598586ec4); listado oficial de guías en AESAN (https://www.aesan.gob.es/AECOSAN/web/seguridad_alimentaria/detalle/guias_practicas.htm). Consultados 2026-09-09.
- **Materializa en:** el APPCC del producto se entrega como **prerrequisitos + 5 registros**, no como manual de 80 páginas. Y con la designación nominal del responsable en la portada.

### PA-11 · Formación de manipuladores: el «carnet» NO existe, y no está en el RD 1021/2022 — nivel A (ausencia) + B (derogación)

- **Verificado A:** el índice completo del RD 1021/2022 (22 artículos, leído en el PDF consolidado) **no contiene ningún artículo sobre formación de manipuladores**. Ese decreto no regula la formación.
- **Verificado B:** el **RD 202/2000** (normas relativas a los manipuladores de alimentos) fue **derogado por el RD 109/2010, de 5 de febrero**. Desde entonces no existe un «carnet de manipulador» expedido por la Administración ni entidades de formación autorizadas previamente: la obligación es del **operador de la empresa alimentaria**, por el **Anexo II, Capítulo XII del Rgto. 852/2004**, que le exige garantizar la supervisión, instrucción y formación de sus manipuladores en función de su actividad, y **poder acreditarlo ante el control oficial**.
- **URLs:** https://www.boe.es/buscar/doc.php?id=BOE-A-2010-2696 · https://www.boe.es/buscar/doc.php?id=BOE-A-2000-3761 · consultados 2026-09-09.
- **Esto corrige un error masivo de la SERP** (ver §13, E-02).
- **Materializa en:** plantilla `registro_formacion_personal.xlsx` — quién, qué formación, fecha, evidencia, reciclaje. Que es exactamente lo que pide la inspección.

### PA-12 · Temperaturas: la fila que importa a una pastelería está en la tabla — nivel A

**Art. 4.1 del RD 1021/2022**, tabla literal (extracto relevante y contexto):

| # | Alimento | Temperatura |
|---|---|---|
| 1 | Carne de ungulados domésticos y de caza mayor | ≤ 7 °C |
| 2 | Despojos | ≤ 3 °C |
| 3 | Carne de aves, lagomorfos, caza menor, ratites | ≤ 4 °C |
| 4 | Preparados de carne | ≤ 4 °C |
| 5 | Carne picada | ≤ 2 °C |
| 7 | Pesca fresca, descongelada, crustáceos y moluscos cocidos | próxima a fusión del hielo (0-4 °C) |
| 8 | Leche cruda | 1-4 °C |
| **9** | **«Productos de pastelería rellenos (salvo que sean estables a temperatura ambiente)»** | **≤ 4 °C** |
| 10 | Frutas/vegetales cortados o pelados y zumos no pasteurizados listos para consumo elaborados en el minorista | ≤ 4 °C |
| 11 | Alimentos congelados o ultracongelados | ≤ –18 °C |

Además, **art. 4.2**: los productos sin temperatura fijada se conservan «a las temperaturas indicadas en la etiqueta». Y **art. 4.3**: el transporte del establecimiento al consumidor o a otro establecimiento debe mantener esas temperaturas.

- **URL:** PDF consolidado del RD 1021/2022 · consultado 2026-09-09.
- **La fila 9 es la fila del producto**: ≤ 4 °C para tarta rellena, milhojas, pastel de nata montada, bomba… y la excepción de los estables a temperatura ambiente es lo que salva a un bizcocho, un mantecado o un hojaldre seco. **La frontera «relleno vs estable a temperatura ambiente» es el criterio que hay que enseñar a decidir**, porque de ella depende si necesitas vitrina refrigerada o no.
- **Materializa en:** xlsx `06_registro_temperaturas` (vitrina, cámara, abatidor, congelador; con la fila 9 preconfigurada) + una **tabla de clasificación de producto** (relleno / estable) en el manual.

### PA-13 · Congelación, descongelación y recongelación — nivel A

**Art. 5 del RD 1021/2022** (extractos literales):
- El equipo de congelación debe tener «la suficiente potencia para congelar los alimentos, de manera que alcancen una temperatura central no superior a **–18 °C** siguiendo un descenso ininterrumpido de la temperatura».
- «Solo se podrá llevar a cabo la congelación en arcones o cámaras de mantenimiento de productos congelados si se garantiza que cumplen los requisitos del apartado anterior.» → **un arcón doméstico no vale como abatidor**.
- Registros mínimos de congelación: «descripción del producto, cantidad, fecha de caducidad o consumo preferente previas, fecha de congelación, nueva fecha de consumo preferente y, en el caso de que se donen, el destino de los productos». Se pueden sustituir por etiqueta con toda esa información.
- Descongelación: **en refrigeración**, evitando contaminación cruzada y el contacto con los líquidos; a temperatura ambiente sólo «por razones tecnológicas, debidamente justificadas»; en microondas o agua corriente fría si se cocina inmediatamente después.
- Venta de descongelado: la denominación «vaya acompañada de la palabra **“descongelado”**».
- **Recongelación prohibida** salvo que el producto haya sufrido una transformación posterior a la primera congelación.
- **Materializa en:** xlsx `07_registro_congelacion` con las 6 columnas literales del artículo + etiqueta imprimible «descongelado».

### PA-14 · Huevo y ovoproductos: el RD 1254/1991 está DEROGADO — nivel A

**Verificado en el propio BOE:** el texto consolidado del RD 1254/1991 lleva la nota «Norma derogada, con efectos de **22 de diciembre de 2022**, por la disposición derogatoria única.d) del Real Decreto 1021/2022, de 13 de diciembre».

- **URL:** https://www.boe.es/buscar/act.php?id=BOE-A-1991-19830 · consultado 2026-09-09.
- Y la **disposición derogatoria única del RD 1021/2022** lo confirma literalmente: «d) El Real Decreto 1254/1991, de 2 de agosto, por el que se dictan normas para la preparación y conservación de la mayonesa de elaboración propia y otros alimentos de consumo inmediato en los que figure el huevo como ingrediente.»

**Lo que rige HOY es el art. 9 del RD 1021/2022**, literal:

> «1. Los establecimientos de comercio al por menor podrán usar huevo crudo para elaborar alimentos que:
> a) Se sometan a un tratamiento térmico donde se alcance una temperatura **igual o superior a 70 °C durante dos segundos** en el centro del producto o cualquier otra combinación de condiciones de tiempo y temperatura con la que se obtenga un efecto equivalente.
> b) Se sometan a un tratamiento térmico donde se alcance una temperatura de **63 °C durante veinte segundos** en el centro del producto y **se sirvan para su consumo inmediato**, como huevos fritos, tortillas u otras preparaciones.
> 2. Para elaborar productos que se van a consumir sin sufrir un tratamiento térmico que cumpla las condiciones del apartado 1, se deberá **sustituir el huevo crudo por ovoproductos procedentes de establecimientos autorizados**.
> 3. Los alimentos elaborados conforme a lo establecido en los apartados 1.a), que no sean estables a temperatura ambiente, y conforme al apartado 2, se conservarán a una temperatura **igual o inferior a 8 °C** y se consumirán en un máximo de **veinticuatro horas** a partir de su elaboración. **Se deberá registrar la fecha y hora de elaboración.**»

- **Esto es el corazón técnico de una pastelería** y donde más se equivocan las fuentes gratuitas (siguen citando el RD 1254/1991, derogado hace casi cuatro años). Merengue italiano, crema pastelera, mousse, tiramisú, buttercream con merengue suizo: **cada elaboración cae en 1.a), 1.b) o 2**, y el producto debe llevar la **tabla de decisión**.
- **Ojo a la coherencia interna:** el art. 4.1 fila 9 exige **≤ 4 °C** a los productos de pastelería rellenos; el art. 9.3 exige **≤ 8 °C** a los alimentos elaborados con huevo. Una tarta rellena de crema pastelera cumple las dos: **manda la más estricta, 4 °C**. Hay que decirlo explícitamente o el lector aplicará 8 °C.
- **Materializa en:** xlsx `08_decision_huevo` — una fila por elaboración del recetario tipo, con columna «vía legal» (70 °C/2 s · 63 °C/20 s + consumo inmediato · ovoproducto), temperatura de conservación resultante y vida útil.

### PA-15 · Vida útil de 24 horas: qué obliga y qué no — nivel A

El límite de **24 horas** del art. 9.3 aplica **sólo** a los alimentos de los apartados 1.a) no estables a temperatura ambiente y a los del apartado 2 (los hechos con ovoproducto sin tratamiento térmico). **No es una vida útil universal de 24 h para toda la pastelería.** Un bizcocho, un hojaldre seco o unas pastas de té estables a temperatura ambiente no caen ahí.

- **Materializa en:** tabla de vida útil por familia de producto, con la base legal por fila y una columna «esto es criterio propio, no norma» para lo demás.

### PA-16 · Zonas de degustación (la pastelería-cafetería) — nivel A

**Art. 10 del RD 1021/2022**, literal:

> «En los comercios al por menor podrán existir zonas de degustación de los productos que comercializan.
> En el caso de que elaboren comidas preparadas, deberán cumplir con lo establecido en el artículo 30 del Real Decreto 1086/2020 […] y contarán con el equipo necesario, **en una zona separada de la zona de ventas**, donde elaboren las comidas de manera que se evite la contaminación cruzada entre los alimentos cocinados y aquellos expuestos a la venta en fresco, así como condensaciones que afecten negativamente a los productos expuestos.»

Y **art. 6:** los minoristas que intervengan en cualquier fase de **comidas preparadas** deben cumplir el **art. 30 del RD 1086/2020**.

- **Consecuencia para la variante pastelería-cafetería:** en cuanto se hacen tostadas, bocadillos o platos, ya hay «comidas preparadas» y entra otro régimen. Es un salto de categoría, no un detalle.
- **PENDIENTE:** no he leído el art. 30 del RD 1086/2020. **Verificar antes de escribir el capítulo de la cafetería.**
- **Materializa en:** capítulo «Pastelería-cafetería: qué cambia» + un aviso de que el APPCC crece.

### PA-17 · Identificación «elaboración propia» / «elaborado por» — nivel A

**Art. 11 del RD 1021/2022**, literal:

> «Los productos alimenticios elaborados por los establecimientos de comercio al por menor se presentarán y etiquetarán de acuerdo con la normativa vigente de información alimentaria al consumidor […]
> Además, dichos alimentos, podrán incluir **de manera voluntaria**:
> a) La expresión «**ELABORADO POR**» seguido del tipo y el nombre del establecimiento elaborador en la etiqueta, placa o marchamo del producto.
> b) La mención «**ELABORACIÓN PROPIA**» en un cartel o rótulo próximo al producto […] Cuando presenten esta mención **solo podrán venderse en el establecimiento donde se han elaborado o en las sucursales del mismo**.
> A tales efectos, **no se considerará elaboración el fraccionamiento o el envasado** de un producto alimenticio elaborado por otro fabricante […]»

- **Palanca comercial real y verificada**: «ELABORACIÓN PROPIA» es una mención legalmente definida, gratuita, y **prohibida** para quien compra congelado y hornea de terceros y lo vende como propio.
- **Materializa en:** cartelería imprimible + el capítulo de posicionamiento («qué puedes decir en el escaparate y qué no»).

### PA-18 · Recipientes del cliente y «lo que sobra, para casa» — nivel A

**Art. 18 del RD 1021/2022** (literal, extractos):
- «Los operadores **podrán** servir los productos alimenticios en recipientes reutilizables aptos para el contacto con alimentos aportados por la propia clientela en el momento de hacer la compra.» → es **potestativo** para el minorista.
- «La persona compradora será responsable de la higiene de los recipientes que aporta […] No obstante, quien vende **siempre podrá rechazar** el uso de un recipiente si considera que el estado higiénico del mismo no es adecuado […]»
- «Los operadores […] quedarán **exentos de la responsabilidad** por los problemas de seguridad alimentaria que se pudieran derivar de la utilización de recipientes aportados por la propia clientela.»
- **Art. 18.5**: «Los establecimientos de **restauración y hostelería** deberán facilitar a la clientela que pueda llevarse, **sin coste adicional alguno**, los alimentos que no hayan consumido, salvo en los formatos de servicio de bufé libre o similares […] e informar de esta posibilidad de forma clara y visible en el propio establecimiento.»
- **Distinción que hay que explicar:** el apartado 5 obliga a **restauración y hostelería**, no al despacho de pastelería. Una pastelería-cafetería con servicio de mesa sí queda dentro.

### PA-19 · Donación de alimentos — nivel A

**Art. 16 del RD 1021/2022**: se puede donar conforme al **Capítulo V bis del Anexo II del Rgto. 852/2004**; y para los **huevos**, se pueden donar «una vez superado el límite de veintiún días a partir de la puesta, siempre que el operador […] receptor transforme los huevos (con tratamiento térmico suficiente) antes de ofrecerlos […], pero no se podrán donar una vez superada su fecha de consumo preferente».

### PA-20 · Venta de producto con defectos — nivel A

**Art. 17**: se pueden vender productos con **defectos de forma y tamaño** (no aplicable a frutas y hortalizas) y **defectos gráficos de etiquetado o envasado** (salvo conservas abombadas), bajo responsabilidad del vendedor y **informando al consumidor**. Es la base legal del «rincón de los feos» / packs anti-desperdicio.

---

## 4. Bloque D — Alérgenos e información al consumidor

### PA-21 · Los 14 alérgenos en producto NO envasado (la vitrina) — nivel B

**RD 126/2015**, norma general de información alimentaria de alimentos sin envasar, envasados a petición del comprador y envasados por el minorista.

- **Obligatorio en no envasado (art. 4):** denominación del alimento + «las menciones específicas a las que se refiere el artículo 9, apartado 1, letra c)» del Rgto. 1169/2011 (= **los 14 alérgenos del Anexo II**) + cantidad de ingredientes cuando proceda + grado alcohólico > 1,2 %.
- **Forma (art. 6.2):** «escrita en etiquetas adheridas al alimento o rotulada en carteles colocados en el lugar donde los alimentos se presenten».
- **Vía oral (art. 6.5.a):** admisible «siempre y cuando la información se pueda suministrar fácilmente cuando sea solicitada», **debiendo existir constancia por escrito en el establecimiento** y un cartel que informe de que la información está disponible.
- **Idioma (art. 10):** «se expresarán, al menos, en castellano».
- **Producto envasado por el propio minorista (art. 5):** información completa del Rgto. 1169/2011, **excepto la identificación de lote**.
- **URL:** https://www.boe.es/buscar/act.php?id=BOE-A-2015-2293 · consultado 2026-09-09. Corrección de errores: BOE-A-2015-3904.
- **Nivel B**: el articulado se leyó en la ficha del BOE, no completo. **Verificar art. 6.5 literal antes de imprimirlo en el producto.**
- **Materializa en:** matriz de alérgenos de vitrina + cartel + etiquetas (**ojo, esto ya existe en `kit-tareas-pasteleria` de 12 €** — ver §16, canibalización).

### PA-22 · Alérgenos en el obrador (no es lo mismo que en la vitrina) — nivel B

El **Capítulo IX del Anexo II del Rgto. 852/2004**, tras el Rgto. 2021/382 (PA-09), añade el requisito de que equipos, transportes y recipientes usados con alérgenos no se reutilicen para alimentos sin ese alérgeno salvo limpieza verificada. Esto es **producción**, no información. Los dos bloques se confunden constantemente.

### PA-23 · «Sin gluten»: 20 mg/kg, y no es una declaración libre — nivel B

**Reglamento de Ejecución (UE) 828/2014 de la Comisión, de 30 de julio de 2014**:
- «**sin gluten**»: sólo si el alimento, tal como se vende al consumidor final, **no contiene más de 20 mg/kg de gluten**.
- «**muy bajo en gluten**»: alimentos con trigo, centeno, cebada, avena o híbridos procesados específicamente para reducir el gluten, **≤ 100 mg/kg**.
- **Avena**: en un producto «sin gluten» o «muy bajo en gluten» debe haber sido elaborada/procesada evitando contaminación por trigo, centeno o cebada, y **≤ 20 mg/kg**.
- Se pueden acompañar de «adecuado para las personas con intolerancia al gluten» / «adecuado para celíacos».
- **URL:** https://www.boe.es/buscar/doc.php?id=DOUE-L-2014-81720 · https://www.aesan.gob.es/AECOSAN/web/seguridad_alimentaria/subdetalle/informacion_gluten.htm · consultados 2026-09-09.
- **Lo que hay que decir sin adornos:** un obrador con harina de trigo en el aire **no puede declarar «sin gluten»** sin validar analíticamente que está por debajo de 20 mg/kg. La certificación FACE es voluntaria y **adicional**, no sustituye al reglamento.
- **Materializa en:** capítulo «línea sin gluten: lo que cuesta de verdad» + checklist de segregación.

---

## 5. Bloque E — Normas de calidad, denominaciones y artesanía

### PA-24 · RD 496/2010 — norma de calidad de confitería, pastelería, bollería y repostería — nivel B, VIGENTE

- **Referencia:** Real Decreto 496/2010, de 30 de abril. BOE de 14/05/2010. Entrada en vigor **15/05/2010**. Derogó el RD 2419/1978.
- **URL:** https://www.boe.es/buscar/act.php?id=BOE-A-2010-7714 · consultado 2026-09-09. **Vigente**: no consta nota de derogación en el consolidado.
- **Definiciones recogidas (nivel B — leídas en la ficha, NO transcribir entrecomilladas sin re-verificar):**
  - *Productos de confitería*: productos alimenticios cuyos ingredientes fundamentales son los azúcares, junto con otros ingredientes incluidos los aditivos autorizados, y que en alguna fase de la elaboración se someten a un tratamiento térmico adecuado.
  - *Productos de bollería*: elaborados básicamente con masa de harinas fermentada, sometidos a tratamiento térmico adecuado.
  - *Productos de pastelería y repostería*: elaborados básicamente con masa de harina, fermentada o no, rellena o no, cuyos ingredientes principales son harinas, aceites o grasas, agua.
  - Clasificación: bollería **ordinaria** y **rellena/guarnecida**; pastelería/repostería por **masas básicas** (hojaldre, azucaradas, escaldadas, batidas, de repostería); **semielaborados** crudos y precocidos.
- **Hallazgo que hay que comprobar antes de usarlo:** según la lectura disponible, **el RD 496/2010 no regula los términos «artesano», «artesanal», «casero» ni «natural»**. Si se confirma, es un dato de valor: significa que **el «artesano» de pastelería no tiene definición estatal** y depende de la CCAA (PA-26). **Estado: verificación pendiente de lectura del PDF completo.**
- **Materializa en:** un capítulo corto de «vocabulario legal»: qué es legalmente bollería, qué es pastelería, y por qué importa (afecta a la denominación de venta y al IVA).

### PA-25 · Si la pastelería vende pan, entra el RD 308/2019 — nivel B

**Real Decreto 308/2019, de 26 de abril**, norma de calidad para el pan. BOE núm. 113, de 11/05/2019 (**BOE-A-2019-6994**). **Entrada en vigor: 1 de julio de 2019.** Consolidado con al menos dos actualizaciones anotadas (derogación del art. 12 en 2023; actualización de 27/02/2026 relativa a panes sin gluten — **este último extremo hay que releerlo, es reciente y no lo he verificado en el texto**).

- **URL:** https://www.boe.es/buscar/act.php?id=BOE-A-2019-6994 · consultado 2026-09-09.
- Datos recogidos (nivel B):
  - **Pan común**: producto de consumo habitual en las 24 horas siguientes a su cocción, elaborado con harina o harina integral de cereales.
  - **Pan especial**: el no incluido en pan común (harinas tratadas, ingredientes especiales, procedimientos tecnológicos especiales).
  - **Pan artesano** (art. 10): «primará el factor humano sobre el mecánico», fermentación en bloque y formado manual.
  - **Pan de masa madre** (art. 14.5): incorporación **≥ 5 %** del peso de harina, **pH < 4,2** en la masa madre, **≤ 0,2 %** de levadura panadera.
  - **Pan integral** (art. 4.3): sólo con harina exclusivamente integral, o indicando porcentaje.
  - **Pan multicereal** (art. 6.2): tres o más harinas diferentes.
  - **Venta a granel** (art. 15.2): indicación del peso de la pieza en etiqueta o cartel.
- **Aviso para el copy:** el RD 308/2019 define «**pan** artesano», **no** «pastelería artesana». Extrapolarlo es un error.

### PA-26 · «Artesano» en pastelería: es competencia AUTONÓMICA — nivel B

- No hay definición europea de artesanía alimentaria; se regula por Estado o CCAA.
- **Cataluña**: **Decreto 85/2024, de 30 de abril**, sistema de acreditación de la artesanía alimentaria (DOGC de 3 de mayo de 2024). Repertorio de oficios que **incluye la pastelería** (elaboración de confitería, pastelería, panadería y repostería, incluidos turrones y chocolates). Requisitos: elaboración **principalmente manual** con mecanización justificada en operaciones discontinuas; **responsable con carné de artesano** vinculado a la empresa; inscripción en censo tributario y registro sanitario; sin sanciones graves de seguridad alimentaria en los **últimos 3 años**; al corriente con Hacienda y Seguridad Social. **Distintivo de vigencia indefinida** mientras se mantengan los requisitos.
  - **URLs:** https://laadministracionaldia.inap.es/noticia.asp?id=1243743 · trámite: https://tramits.gencat.cat/es/tramits/tramits-temes/Qualificacio-dEmpresa-Artesanal-Alimentaria · consultados 2026-09-09.
- **Andalucía**: Decreto 352/2011, de 29 de noviembre, de artesanía alimentaria (nivel C, identificado por fuente secundaria).
- **Madrid**: hay un **proyecto de decreto** sobre ordenación y regulación de la artesanía alimentaria y alimentos de montaña — **PROYECTO, no norma**; no se puede citar como vigente. https://participa.comunidad.madrid/content/proyecto-decreto-sobre-ordenacion-regulacion-artesania-alimentaria-los-alimentos-montana (consultado 2026-09-09).
- **Materializa en:** cuadro «¿puedo llamarme artesano?» por CCAA, con la advertencia de que en muchas comunidades **no hay norma** y el término queda sujeto sólo a la prohibición general de prácticas engañosas.

---

## 6. Bloque F — Venta a distancia, online y a domicilio

### PA-27 · La venta a distancia ya está dentro de la definición de minorista — nivel A

**Art. 2.2.a) del RD 1021/2022** define establecimiento de comercio al por menor incluyendo la entrega «**in situ o a distancia**». No hay un régimen sanitario aparte: se aplica el mismo, más el transporte del **art. 4.3** (mantener temperaturas durante el transporte al consumidor).

### PA-28 · Información alimentaria en venta a distancia — nivel B

**Rgto. (UE) 1169/2011, art. 14**: en venta a distancia, la información alimentaria obligatoria (salvo la fecha de duración mínima/caducidad) debe estar disponible **antes de que se realice la compra** — en la práctica, como tarde en la página de pedido — y **toda** la información obligatoria del art. 9 debe entregarse **en el momento de la entrega**. Los **alérgenos** siguen siendo obligatorios (art. 44 en relación con el art. 14).

- **URLs:** https://www.boe.es/buscar/doc.php?id=DOUE-L-2011-82311 · nota del Ministerio de Consumo: https://www.dsca.gob.es/es/publicacion/venta-distancia-reglamento-ue-no-11692011-informacion-alimentaria-facilitada-al · consultados 2026-09-09.
- **PENDIENTE:** no he verificado si la venta online obliga además a inscripción distinta o a RGSEAA. **Hipótesis a refutar:** una pastelería que vende online **a consumidor final** y entrega dentro de su zona sigue siendo minorista (PA-27); si envía por mensajería a toda España, hay que revisar si eso rompe el requisito de «localizado» — pero el art. 3 regula el suministro **a otros establecimientos**, no al consumidor final. **Esto hay que resolverlo con una consulta expresa antes de escribir el capítulo de e-commerce**; es la duda más peligrosa del bloque.
- **Además, y fuera del ámbito alimentario:** venta online = **RDL 1/2007** (derecho de desistimiento y sus excepciones para bienes perecederos), **Ley 34/2002 (LSSI)** y **RGPD**. No verificados aquí; bloque propio.

---

## 7. Bloque G — «Obrador en casa»: lo que dice la norma, no los blogs

### PA-29 · Art. 13 del RD 1021/2022 — el régimen completo, verificado literal — nivel A

Es el artículo que más se cita mal en toda la SERP. Transcripción literal de lo esencial:

> «2. Cuando se lleve a cabo la actividad de preparación de alimentos en locales utilizados principalmente como vivienda privada, **las zonas de la vivienda destinadas a dicha actividad tendrán la consideración de establecimiento de comercio al por menor** […]
> 3. Cuando el operador inicie la actividad deberá presentar a la autoridad competente, a los efectos de su inscripción en el correspondiente registro autonómico, una **declaración responsable** […] que deberá incluir: a) Horario en que se va a operar. b) Productos que se van a elaborar. c) **Plano de la vivienda** que refleje las estancias o zonas destinadas a dicha actividad. d) Compromiso de asumir las obligaciones de someterse a los controles oficiales […] e) Compromiso de contar con la justificación documental contenida en el apartado 9.
> 4. Los alimentos preparados en locales utilizados principalmente como vivienda privada **solo se podrán suministrar a la persona consumidora directamente en mercados ocasionales o periódicos, o mediante el reparto a domicilio** siempre que el suministro se realice dentro de la unidad sanitaria local, zona de salud o territorio […] donde radique la vivienda.
> 5. Los alimentos preparados en estos locales: a) **No se podrán servir para su consumo in situ**, salvo que la autoridad competente de la comunidad autónoma lo permita. b) **No se podrán suministrar a colectividades ni en eventos.** c) **No se podrán suministrar en el propio establecimiento**, salvo que la autoridad competente […] lo permita. d) **No se podrán suministrar a otros establecimientos de comercio al por menor**, salvo que la autoridad competente […] lo permita […] e) **No se podrán congelar**, ni tampoco las materias primas empleadas para elaborarlos. Solo se podrán mantener en congelación las materias primas que se adquieran ya congeladas.
> 6. Cuando los alimentos destinados a la venta se elaboren en las mismas instalaciones que aquellos destinados al consumo doméstico privado, será necesaria, al menos, una **separación temporal** y cuando resulte necesario […] una **separación espacial** […]
> 7. Durante la elaboración de alimentos destinados a la venta **no se permitirá el acceso de personas ajenas** […] En ningún caso se permitirá el **acceso de animales domésticos** a las zonas de la vivienda destinadas a la elaboración de alimentos.
> 8. Los alimentos preparados estarán limitados a: a) Comidas preparadas sometidas a un tratamiento térmico suficiente […] b) **Productos de panadería y repostería estables a temperatura ambiente.** c) Mermeladas, confituras y jaleas, siempre que tras el envasado se sometan a un tratamiento térmico […] d) Conservas de frutas, hortalizas o vegetales, siempre que tengan un **pH inferior a 4,5**. e) Otros alimentos que las autoridades competentes de las comunidades autónomas permitan en sus territorios.
> 9. El volumen total de alimentos preparados deberá ser proporcional al tamaño de las instalaciones […] y **en ningún caso podrán superar los 100 kilogramos semanales**, lo cual se demostrará documentalmente.
> 10. Los alimentos preparados se presentarán y etiquetarán […] y se deberá indicar la mención «**Elaborado en vivienda particular**» y la **fecha de elaboración**.»

- **URL:** PDF consolidado del RD 1021/2022 · consultado 2026-09-09.
- **Lo demoledor para el nicho «tartas por encargo desde casa»:** el apartado 8.b) sólo permite **repostería estable a temperatura ambiente**. **Una tarta rellena de nata o de crema pastelera NO entra** — es exactamente el producto del art. 4.1 fila 9 que exige ≤ 4 °C. Y el apartado 5.e) prohíbe congelar. El «negocio de tartas desde casa» que vende la SERP (uno de los PAA medidos: «¿Cómo empezar un negocio de repostería desde casa?») **es legal sólo para una gama muy concreta**: galletas, bizcochos secos, mantecados, hojaldres secos, pastas de té, mermeladas.
- Confirmado además en la práctica autonómica: el **Decreto 26/2026 de Madrid** crea una **sección específica** para viviendas privadas (art. 6.d) y exige exactamente los cinco puntos del art. 13.3 en su art. 8.4 (leído literal, PA-04). La **Comunitat Valenciana** regula lo mismo en su Decreto 13/2025 (nivel B).
- **Materializa en:** un capítulo entero «Obrador en casa: qué puedes vender y qué no», con la **lista blanca del art. 13.8**, el contador de los 100 kg/semana en xlsx, la plantilla de declaración responsable y el modelo de etiqueta con la mención obligatoria.

---

## 8. Bloque H — Envases, residuos y desperdicio alimentario

### PA-30 · Envases: Ley 7/2022 y RD 1055/2022 — nivel B

**Ley 7/2022, de 8 de abril, de residuos y suelos contaminados para una economía circular** (https://www.boe.es/buscar/act.php?id=BOE-A-2022-5809, consultado 2026-09-09):
- **Agua no envasada gratuita** en hostelería y restauración (medida de prevención del sector servicios).
- **Objetivos de reducción de plásticos de un solo uso** (vasos y recipientes alimentarios): **–25 % en 2025** y **–30 % en 2030** respecto a 2021.
- **Cobro obligatorio** de los envases de plástico de un solo uso — remitido expresamente por el art. 18.5 del RD 1021/2022 (esto sí, nivel A: «la obligación de su cobro»).
- **Impuesto especial sobre envases de plástico no reutilizables**: base = kg de plástico **no reciclado**; tipo **0,45 €/kg**; contribuyentes: fabricantes, importadores y adquirentes intracomunitarios; exención por debajo de **5 kg** en adquisiciones intracomunitarias.
- **Prohibiciones** de determinados plásticos de un solo uso (cubiertos, platos, vasos de poliestireno expandido, oxodegradables, microesferas).

**RD 1055/2022, de 27 de diciembre, de envases y residuos de envases** (https://www.boe.es/buscar/act.php?id=BOE-A-2022-22690, consultado 2026-09-09):
- **Referencias de bebida en envase reutilizable en el comercio minorista de alimentación** (art. 9.4):

| Superficie del establecimiento | Referencias mínimas | Desde |
|---|---|---|
| < 120 m² | 1 | **1-ene-2027** |
| 120–300 m² | 3 | **1-ene-2027** |
| 300–1.000 m² | 4 | 1-ene-2025 |
| 1.000–2.500 m² | 5 | 1-ene-2025 |
| > 2.500 m² | 7 | 1-ene-2025 |

- **Aceptación de recipientes del cliente en venta a granel** (art. 9.3), en línea con el art. 18 del RD 1021/2022.
- **Productor de producto** (art. 2.t): «los envasadores o los agentes económicos dedicados a la importación o adquisición en otros Estados miembros […] de productos envasados para su puesta en el mercado». **Una pastelería que envasa su producto encaja en «envasador»** → registro de productores, responsabilidad ampliada, declaraciones. **ESTO HAY QUE VERIFICARLO CON MUCHO CUIDADO**: es la diferencia entre un trámite anual y ninguno, y la lectura disponible es de nivel B. Es la duda de mayor impacto económico del bloque H.
- **Nivel B** en todo el bloque: el articulado se leyó en la ficha del BOE, no completo.
- **Materializa en:** checklist de envases (bandeja, caja de tarta, bolsa, film) con columna «¿me convierte en envasador?» — y **con un aviso de que ese punto está por confirmar**.

### PA-31 · Ley 1/2025 de desperdicio alimentario — nivel B, con la FECHA EN DISPUTA

**Ley 1/2025, de 1 de abril, de prevención de las pérdidas y el desperdicio alimentario.** BOE núm. 80, de **02/04/2025** (BOE-A-2025-6597).

- **URL:** https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597 · consultado 2026-09-09.
- **Exención por superficie (art. 6.4.c), leída:** «Quedan exceptuadas de las obligaciones del presente apartado cuatro las actividades de transformación, comercio minorista, distribución alimentaria, hostelería o restauración desarrolladas en establecimientos **iguales o inferiores a 1.300 m²**…» + regla de acumulación por mismo CIF.
- **Microempresas (art. 6.6):** «quedan excluidas de las obligaciones a las que se refieren los apartados anteriores».
- **Art. 8 (hostelería), literal leído:** «Los agentes de la cadena alimentaria que sean empresas de la hostelería y otros proveedores de servicios alimentarios tendrán la obligación de facilitar al consumidor que pueda llevarse, sin coste adicional alguno […] los alimentos que no haya consumido, salvo en los formatos de servicio de bufé libre o similares […] así como informar de esta posibilidad de forma clara y visible en el propio establecimiento, **preferentemente en la carta o el menú**.»
- **Consecuencia práctica:** **prácticamente ninguna pastelería llega a 1.300 m²** ni deja de ser microempresa. El plan de prevención y la obligación de convenios de donación **no le aplican**. Lo que sí le aplica, si tiene servicio de cafetería, es la obligación de llevarse lo no consumido — que además ya está en el art. 18.5 del RD 1021/2022 (nivel A).

> ⚠️ **FECHA DE ENTRADA EN VIGOR: NO RESUELTA.** El bloque de metadatos del BOE devuelve, leído dos veces, «Entrada en vigor: **02/01/2025**», que es **anterior a la publicación (02/04/2025)** y por tanto imposible: o el campo está mal leído (lo más probable: 02/01/**2026**, nueve meses después de publicar) o hay un error de metadato. Fuentes secundarias dan tres versiones distintas: «entró en vigor el 3 de abril de 2026» (economistjurist), «2 de enero de 2025» (pactomundial), y «las obligaciones del art. 6 al año de la publicación, abril de 2026». **NO SE PUEDE IMPRIMIR NINGUNA FECHA EN EL PRODUCTO hasta leer la disposición final del texto en el PDF del BOE.** Ver §13, E-05 y §18.
- **Sanciones:** rango citado por secundarias de **2.000 € a 500.000 €**, con graves «hasta 60.000 €». **Sin verificar contra el articulado.** No usar.

---

## 9. Bloque I — Laboral

### PA-32 · SMI 2026 — nivel A

**Real Decreto 126/2026, de 18 de febrero**, por el que se fija el salario mínimo interprofesional para 2026 (**BOE-A-2026-3815**).

- **URL:** https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815 · consultado 2026-09-09.
- **40,70 €/día · 1.221 €/mes · 17.094 €/año** (14 pagas). Vigencia: **1-ene-2026 a 31-dic-2026**, con efectos retroactivos a 1 de enero.
- Subida del **3,1 %** respecto a los 1.184 €/mes de 2025.
- **Eventuales y temporeros con contrato ≤ 120 días (art. 4.1): 57,82 €** por jornada legal.
- **Empleadas de hogar (art. 4.2): 9,55 €/hora** en régimen externo.
- **Compensación y absorción (art. 3):** el SMI es una **referencia anual de 17.094 €** en cómputo global, no un mínimo por concepto.
- **Corrección importante para el copy:** «1.221 € × 14» es el SMI. **No es el coste de un pastelero**: en la mayoría de convenios del sector el salario de convenio ya supera el SMI (ver PA-33).

### PA-33 · Sí existe convenio PROPIO de pastelería, por provincia/CCAA — nivel A (Madrid) / B (Barcelona)

**Madrid — Convenio Colectivo del Sector de Comercio e Industria de Confitería, Pastelería, Bollería, Repostería, Heladería y Platos Cocinados de la Comunidad de Madrid** (código **28001025011981**). Revisión salarial 2026 suscrita el 27-ene-2026, inscrita por Resolución de 7-feb-2026 de la D.G. de Trabajo, publicada en **BOCM núm. 50, de 28 de febrero de 2026**.

- **URL:** https://www.bocm.es/boletin/CM_Orden_BOCM/2026/02/28/BOCM-20260228-2.PDF · consultado 2026-09-09 (**leído íntegro**).
- **Incremento 2026: +2,9 %** (IPC de 2025), con efectos desde 1-ene-2026.
- **Tablas salariales 1-ene-2026 a 31-dic-2026 — literal, 15 pagas:**

| Grupo profesional | Mensual 2026 (15 pagas) | Anual 2026 |
|---|---|---|
| Técnicos y titulados superiores | 1.733,88 € | 26.008,20 € |
| Dirección, jefes y encargados (incl. **maestro de obrador**) | 1.427,89 € | 21.418,35 € |
| Personal especialista (**oficial 1ª producción**, encargado de sección, dependiente mayor) | 1.376,91 € | 20.653,65 € |
| Personal cualificado (**oficial 2ª producción**, oficial 1ª envasado, **dependiente**, conductor) | 1.249,42 € | 18.741,30 € |
| Personal de apoyo (**ayudante de producción**, oficial de acabado, ayudante de comercio) | 1.192,42 € | 17.886,30 € |
| Personal de ayuda en servicios auxiliares (peón, limpiador, almacenero) | 1.192,42 € | 17.886,30 € |

- **Estructura por áreas funcionales:** OBRADOR / COMERCIO / ADMINISTRACIÓN, con niveles 2, 3A, 5A, 8, 9 y 15-19. **Esto es exactamente el esqueleto de una plantilla de pastelería** y da el escandallo de personal sin inventar nada.
- **Dato de contraste:** el grupo más bajo (17.886,30 €/año) queda **por encima** del SMI anual (17.094 €). Es decir: **en Madrid el convenio manda, no el SMI**.
- **Barcelona** — Convenio del sector de Confitería, Pastelería y Bollería de Barcelona y provincia (REGCON 08001025011994), convenio 2023-2025 publicado en el BOPB el 29-jul-2026. Dato localizado (nivel C, agregador): dependiente de rama mercantil **988,57 € de salario base + 545,39 € de plus de convenio = 1.533,98 €/mes** en la tabla de 2025. **Las tablas 2026 de Barcelona NO están verificadas.**
  - https://cartaslaborales.app/novedades-convenios/convenio/08001025011994 · consultado 2026-09-09.
- **Valencia y Sevilla: NO verificados.** Hay convenios provinciales del sector pero no he leído sus tablas. **No inventar.**
- **Y ojo con la variante cafetería:** si el negocio es pastelería-cafetería, puede caer el **convenio de hostelería** provincial en lugar del de pastelería, o convivir los dos por áreas funcionales. **Este punto NO está resuelto y es de dinero.** Ver §17, pregunta 4.
- **Materializa en:** xlsx `09_coste_plantilla` con las 6 filas de Madrid cargadas por defecto, celdas verdes para sustituir por el convenio del lector, y cálculo de coste empresa (base + SS + pagas).

### PA-34 · Registro de jornada — nivel B, con reforma EN CURSO

- **Vigente hoy:** obligación de registro diario de jornada desde 2019 (art. 34.9 del Estatuto de los Trabajadores, RD-ley 8/2019). Formatos admitidos: papel, hoja de cálculo o electrónico, siempre que sea objetivo, fiable, accesible, y se **conserve 4 años**.
- **En tramitación:** un real decreto de **registro horario digital**, con tramitación urgente aprobada en Consejo de Ministros el 30-sep-2025; el Ministerio de Trabajo apunta a presentar el texto final durante 2026 y las previsiones sitúan la exigibilidad **entre marzo y abril de 2027**. Eliminaría el papel y el Excel.
- **Fuentes (secundarias, todas):** https://www.cuatrecasas.com/es/spain/laboral/art/registro-jornada-laboral-espana-rd · https://teamsystem.es/magazine/control-horario-2026/ · consultados 2026-09-09.
- **Cómo escribirlo:** «hoy vale un Excel; hay una reforma en trámite que lo prohibiría — comprueba el estado antes de comprar un sistema». **No dar fecha como cierta.**

### PA-35 · PRL en obrador: la harina es un sensibilizante — nivel B

- **Marco:** Ley 31/1995 de PRL + RD 39/1997 (servicios de prevención) + **RD 486/1997** (lugares de trabajo) + **RD 374/2001** (agentes químicos) + **RD 1644/2008** (máquinas, marcado CE de amasadora, laminadora, batidora).
- **Riesgo específico documentado por el INSST:** el polvo de harina en suspensión provoca **asma del panadero** y rinitis; la harina es **sensibilizante** (basta una exposición muy baja una vez sensibilizado). Alérgenos implicados: gliadina, glutenina, Tri a 14, inhibidores de amilasas, amilasas añadidas (fúngicas o sintéticas), levadura, lecitina, sésamo.
- **URLs (INSST, fuente oficial):** https://www.insst.es/stp/basequim/030-elaboracion-de-productos-alimenticios-en-panaderias-y-pastelerias-artesanales-exposicion-a-harina-2020 · https://www.insst.es/documents/94886/791398/BASEQUIM_030.pdf · https://www.insst.es/documentacion/material-divulgativo-y-audiovisual/folletos/folleto-polvo-de-harina-riesgo-panaderos-2012 · consultados 2026-09-09.
- **Materializa en:** ficha de PRL de obrador (harina, hornos, laminadora, cargas, suelos húmedos) y checklist de compra de maquinaria (marcado CE, declaración de conformidad, manual en castellano).

---

## 10. Bloque J — Fiscal y administrativo

### PA-36 · IVA: 10 % casi todo, 4 % sólo el pan común y las harinas panificables — nivel B (art. 91 leído a través de resolución oficial)

- **Norma:** art. 91 de la **Ley 37/1992** del IVA.
- **Fuente utilizada:** **Resolución de 24 de febrero de 2025, de la Dirección General de Tributos, sobre el tipo del IVA aplicable al pan** (**BOE-A-2025-3950**), que reproduce el precepto. https://www.boe.es/buscar/doc.php?id=BOE-A-2025-3950 · consultado 2026-09-09.
- **Al 4 %** (art. 91.Dos.1.1.º a)): «El pan común, así como la masa de pan común congelada y el pan común congelado destinados exclusivamente a la elaboración del pan común», y las **harinas panificables**. La resolución extiende el 4 % a los productos incluidos en el RD 308/2019 y a los panes elaborados con harina sin gluten.
- **Al 10 %** (art. 91.Uno.1.1.º): los productos alimenticios en general → **bollería, pastelería, confitería y repostería van al 10 %**.
- **La resolución NO menciona bollería ni pastelería explícitamente**: su alcance es el pan. **Por tanto, la afirmación «pastelería al 10 %» es una inferencia del régimen general, no una cita.** Nivel B. **Antes de imprimir tipos de IVA en el producto hay que leer el art. 91 literal** (BOE-A-1992-28740, consolidado, apartados Uno.1.1.º, Uno.2.2.º y Dos.1.1.º).
- **PENDIENTE de verificar y necesario para el producto:**
  1. tipo aplicable a los **servicios de hostelería/restauración** (art. 91.Uno.2.2.º) → afecta a la pastelería-cafetería: **la misma tarta puede llevar un tipo si se la lleva y otro si se la come en la mesa**. Es un punto de dinero y de caja.
  2. la **exclusión de las bebidas con azúcares o edulcorantes añadidos** del tipo reducido.
- **Materializa en:** xlsx de tarifario con columna de tipo de IVA por familia — **sólo cuando esté verificado**.

### PA-37 · Verifactu: no es 2026, es 2027 — nivel B

- **Norma base:** **RD 1007/2023** (requisitos de los sistemas informáticos de facturación) + **Orden HAC/1177/2024**.
- **Prórrogas:** el **RD 254/2025** (abril 2025) llevó los plazos a 1-ene-2026 / 1-jul-2026; y el **Real Decreto-ley 15/2025, de 2 de diciembre** (BOE de 3-dic-2025, convalidado el 16-dic-2025) los aplazó **un año más**:
  - **Contribuyentes del Impuesto sobre Sociedades: 1 de enero de 2027.**
  - **Resto de obligados (autónomos en IRPF, IRNR con EP, entidades en atribución de rentas): 1 de julio de 2027.**
- **Obligación ya vigente para los fabricantes de software:** desde el **29 de julio de 2025**, todo SIF que se comercialice debe cumplir el RD 1007/2023.
- **Fuentes (secundarias, coincidentes):** https://noticias.juridicas.com/actualidad/noticias/20735-nueva-prorroga:-verifactu-no-sera-obligatorio-hasta-2027-para-sociedades-y-otros-contribuyentes/ · https://www.hosteleriamadrid.com/blog/fiscal/real-decreto-aplazamiento-verifactu/ · consultados 2026-09-09.
- **Sin fuente primaria leída.** Antes de publicar hay que abrir el RD-ley 15/2025 en el BOE.
- **Cómo escribirlo:** «tu TPV tiene que estar listo antes del 1-ene-2027 si eres SL y del 1-jul-2027 si eres autónomo — pero el software que compres hoy ya debe cumplir la norma». Esto ordena una decisión de compra real (el TPV es de las primeras compras).

### PA-38 · Epígrafes de IAE — nivel B

| Epígrafe | Descripción | Uso típico en pastelería |
|---|---|---|
| **419.2** | Industrias de bollería, pastelería y galletas | El **obrador**: elaboración propia. Habilita venta al por mayor y al por menor de lo propio |
| **644.1** | Comercio al por menor de pan, pastelería, confitería y similares y de leche y productos lácteos | El **despacho** |
| **644.2** | Despachos de pan, panes especiales y bollería | Despacho de pan |

- **URLs (sede AEAT):** https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2021/apendice/epigrafe-iae-644_1-comercio-menor-confiteria.html · https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2021/apendice/epigrafe-iae-644_2-despachos-pan-bolleria.html · consultados 2026-09-09.
- **Nota:** las fichas de la AEAT localizadas son del manual del IRPF 2021. **Verificar la redacción vigente de las tarifas** (RDL 1175/1990) antes de publicar.
- **Alta:** modelo **036/037** ante la AEAT + alta en el RETA o en el régimen general de la Seguridad Social. **No verificado en este informe**; bloque estándar.

---

## 11. Bloque K — Accesibilidad, ruido, horarios, seguros y costes

### PA-39 · Horarios comerciales: la pastelería tiene LIBERTAD HORARIA por ley estatal — nivel A

**Ley 1/2004, de 21 de diciembre, de Horarios Comerciales** (**BOE-A-2004-21421**), consolidada; modificada por el **RD-ley 20/2012**. https://www.boe.es/buscar/act.php?id=BOE-A-2004-21421 · consultado 2026-09-09.

- **Art. 5.1, literal:** «Los establecimientos dedicados **principalmente a la venta de pastelería y repostería, pan**, platos preparados, prensa, combustibles y carburantes, floristerías…» → tienen «plena libertad para determinar los días y horas en que permanecerán abiertos». También tiendas de conveniencia y establecimientos de **menos de 300 m²** (con matices por titularidad).
- **Art. 3.1** (tras el RD-ley 20/2012): el horario global semanal en días laborables no podrá restringirse a **menos de 90 horas**.
- **Art. 4.1** (tras el RD-ley 20/2012): el número mínimo de **domingos y festivos** de apertura será de **dieciséis**.
- **Art. 2:** la regulación concreta corresponde a las **comunidades autónomas**.
- **Esto es un argumento comercial verificado y poco conocido:** una pastelería puede abrir domingos y festivos **sin pedir permiso ni consumir los 16 domingos habilitados**, por su propio régimen especial. Es directamente un capítulo de estrategia (el domingo es el día de la tarta).
- **Cautela:** la ley estatal fija el mínimo; la CCAA puede ampliar, no reducir. **Y el régimen del art. 5 exige que la venta de pastelería/pan sea la actividad PRINCIPAL.** Una pastelería-cafetería con más facturación de cafetería que de pastelería podría quedar fuera. Punto a matizar en el producto.

### PA-40 · Accesibilidad — nivel B, con calendario que hay que mirar dos veces

- **Marco:** **RD Legislativo 1/2013** (texto refundido de la Ley General de derechos de las personas con discapacidad), cuya D.A. 3ª fijó el **4 de diciembre de 2017** como fecha máxima de exigibilidad de las condiciones de accesibilidad en entornos y edificios existentes **susceptibles de ajustes razonables**.
- **Norma nueva y relevante:** **RD 193/2023, de 21 de marzo**, por el que se regulan las condiciones básicas de accesibilidad y no discriminación para el acceso y utilización de los bienes y servicios a disposición del público (**BOE-A-2023-7417**). https://www.boe.es/buscar/act.php?id=BOE-A-2023-7417 · consultado 2026-09-09.
  - Aplica a comercio minorista (art. 17) y a hostelería y restauración (art. 25).
  - Calendario de exigibilidad leído (nivel B, **verificar antes de publicar**): bienes/servicios **nuevos** de titularidad privada → **1-ene-2029**; **existentes** de titularidad privada → **1-ene-2030**; públicos, 2025 y 2026 respectivamente.
  - Umbrales por superficie (art. 17): > 2.500 m² servicio de atención y apoyo; > 150 m² vestuarios/probadores accesibles. **Una pastelería no llega a ninguno de los dos.**
- **Lo que sí aplica desde ya a una pastelería:** los **ajustes razonables** y el **CTE DB-SUA** en obra nueva o reforma. La pendiente máxima de rampa (10 %, 12 % si < 3 m) que circula en la SERP es **fuente secundaria** — el dato bueno está en el DB-SUA, no verificado aquí.

### PA-41 · Seguro de responsabilidad civil — nivel C, y depende de la CCAA

- **No hay un seguro de RC obligatorio estatal para un comercio de alimentación.** Lo que sí existe es la exigencia autonómica en la normativa de **espectáculos públicos y actividades recreativas**: en Madrid, la **Ley 17/1997** condiciona la licencia a tener suscrito un seguro que cubra incendio del local y RC por daños a concurrentes y terceros. Se cita un capital mínimo de **42.071 €** para aforo ≤ 50 personas (disposición transitoria tercera).
- **Todo esto es nivel C** (fuentes de correduría). **URL de contraste:** https://gie.es/blog/estos-son-los-seguros-para-estar-protegido-si-eres-hostelero-en-la-comunidad-madrid/ · consultado 2026-09-09.
- **Lo relevante para el producto:** una **pastelería sin consumo en sala** probablemente no entre en el ámbito de espectáculos públicos; una **pastelería-cafetería con terraza**, sí. La frontera hay que verificarla en la ley autonómica antes de afirmar nada.

### PA-42 · Ruido y contaminación acústica — PENDIENTE

No verificado. Marco: **Ley 37/2003 del Ruido** + **RD 1367/2007** + ordenanza municipal. En un obrador el foco son las máquinas (amasadora, extractor, compresor de la cámara) y el horario nocturno de producción, que es lo normal en pastelería. **Bloque a investigar en una pasada específica.**

### PA-43 · Costes de inversión: NO HAY FUENTE PRIMARIA — todo nivel C

Recogido sólo como mapa de lo que dice la SERP, **para poder contradecirlo con método**, no para citarlo:

| Cifra que circula | Fuente | Naturaleza |
|---|---|---|
| Obrador de pastelería ≈ **200.000 €**; rentabilidad **8-12 %** | El Español / Cocinillas, 13-nov-2025 (https://www.elespanol.com/cocinillas/reportajes-gastronomicos/20251113/matias-dueno-pasteleria-espana-montar-obrador-cuesta-eur-rentabilidad-kw/1003744012399_0.html) | Declaración de un empresario en prensa |
| Inversión total **60.000–200.000 €** | plandenegocio.es (https://plandenegocio.es/cuanto-cuesta-abrir-pasteleria/) | Blog comercial |
| Proyecto **5.000 €**, obra media **81.000 €**, equipamiento **46.000 €**, marketing **5.000 €** | lahostelera.com (aparece en la SERP de «como montar una pasteleria») | Blog comercial |
| Reforma **16.000–40.000 €**; horno **400–35.000 €**; mobiliario/vitrinas **7.000–15.000 €**; licencias **1.000–6.000 €** | ayudatpymes.com, plandenegocio.es, hostelmarkt.com | Blogs comerciales |
| Licencia de obrador/panadería en Madrid «desde **1.690 € + IVA**» | estudio-l.es (https://www.estudio-l.es/licencia-obrador-panaderia-madrid/) | Tarifa comercial de un despacho |

Todos consultados 2026-09-09.

> **Recomendación fuerte para el producto:** no publicar «montar una pastelería cuesta X». Publicar un **xlsx de CAPEX abierto** con las 9 partidas y **tres escenarios que el lector rellena con presupuestos reales**, más un capítulo de «cómo pedir tres presupuestos comparables». Es más honesto, más útil y no caduca. Es además exactamente lo que hace `guia-panaderia-obrador` (CAPEX + P&L 3 escenarios), así que hay motor.

---

## 12. Tabla de vigencia (resumen ejecutivo)

| id | Norma | Estado a 2026-09-09 | Nivel | Fecha clave |
|---|---|---|---|---|
| PA-01/02/03 | **RD 1021/2022** higiene minorista | **Vigente** desde 22-dic-2022 | A | — |
| PA-01 | **RD 191/2011** RGSEAA | **Vigente**, modificado por RD 682/2014 y por la D.F. 1ª del RD 1021/2022 | A/B | — |
| PA-04 | **Decreto 26/2026** CM registro minorista | **Vigente** desde 28-mar-2026 | A | **Transitorio hasta 28-mar-2027** |
| PA-04 | **Decreto 13/2025** C. Valenciana (REM) | Vigente | B | — |
| PA-09/22 | **Rgto. (CE) 852/2004** + **Rgto. (UE) 2021/382** | Vigente; modificación aplicable desde 24-mar-2021 | B | — |
| PA-11 | **RD 202/2000** manipuladores | **DEROGADO** por RD 109/2010 | B | 2010 |
| PA-14 | **RD 1254/1991** mayonesa/huevo | **DEROGADO** con efectos 22-dic-2022 por RD 1021/2022 D.D.ú.d) | **A** | 22-dic-2022 |
| — | **RD 3484/2000** comidas preparadas | **DEROGADO** por RD 1021/2022 D.D.ú.f) | A | 22-dic-2022 |
| — | **RD 1420/2006** anisakis | **DEROGADO** por RD 1021/2022 D.D.ú.h) | A | 22-dic-2022 |
| PA-21 | **RD 126/2015** información sin envasar | Vigente desde 05-mar-2015 (corr. errores 11-abr-2015) | B | — |
| PA-23 | **Rgto. Ejec. (UE) 828/2014** sin gluten | Vigente | B | — |
| PA-24 | **RD 496/2010** calidad confitería/pastelería | **Vigente** desde 15-may-2010; derogó el RD 2419/1978 | B | — |
| PA-25 | **RD 308/2019** calidad del pan | Vigente desde 1-jul-2019; consolidado con modificaciones (art. 12 derogado en 2023; actualización 27-feb-2026 **por verificar**) | B | — |
| PA-26 | **Decreto 85/2024** artesanía alimentaria Cataluña | Vigente (DOGC 3-may-2024) | B | — |
| PA-26 | Decreto de artesanía alimentaria de **Madrid** | **PROYECTO — no vigente** | C | — |
| PA-30 | **Ley 7/2022** residuos | Vigente | B | objetivos 2025 y 2030 |
| PA-30 | **RD 1055/2022** envases | Vigente | B | **1-ene-2027** para < 300 m² |
| PA-31 | **Ley 1/2025** desperdicio alimentario | Vigente; **fecha de entrada en vigor NO RESUELTA** | B | ⚠️ |
| PA-32 | **RD 126/2026** SMI 2026 | Vigente 1-ene-2026 a 31-dic-2026 | A | **caduca 31-dic-2026** |
| PA-33 | Convenio Confitería/Pastelería **Madrid**, revisión 2026 | Vigente 1-ene-2026 a 31-dic-2026 | A | **caduca 31-dic-2026** |
| PA-34 | Registro de jornada (art. 34.9 ET) | Vigente; **reforma digital en tramitación** | B | exigibilidad estimada 2027 |
| PA-36 | Art. 91 **Ley 37/1992** IVA | Vigente | B | — |
| PA-37 | **RD 1007/2023** Verifactu + **RD-ley 15/2025** | Vigente con plazos aplazados | B | **1-ene-2027 / 1-jul-2027** |
| PA-39 | **Ley 1/2004** horarios comerciales | Vigente, modificada por RD-ley 20/2012 | A | — |
| PA-40 | **RDLeg 1/2013** + **RD 193/2023** accesibilidad | Vigentes; exigibilidad progresiva | B | **1-ene-2029 / 1-ene-2030** privados |

---

## 13. Los 5 errores normativos más repetidos en las fuentes gratuitas de la SERP

Los cinco están vivos en la SERP medida de «como montar una pasteleria» y «requisitos obrador pastelería» (consultada 2026-09-09).

### E-01 · «Necesitas el Registro Sanitario (RGSEAA) para abrir tu obrador»

- **Dónde se dice:** es el mensaje por defecto de las páginas de consultoras de registro sanitario (p. ej. https://itabe.es/registro-sanitario-cataluna/, https://aizea.es/registro-sanitario/es-obligatoria-la-informacion-alimentaria-en-la-venta-por-internet/), que venden el trámite.
- **Corrección (PA-01):** el RD 191/2011 art. 2.2, en la redacción del RD 1021/2022, **excluye del RGSEAA a los establecimientos de comercio al por menor**. Lo que hay es una comunicación o declaración responsable **autonómica**, que además **no es habilitante**. Sólo se vuelve al RGSEAA si el suministro a otros establecimientos deja de ser marginal, localizado y restringido (art. 3).
- **Por qué importa:** el lector paga un trámite que no le corresponde, o cree que ya está registrado cuando no lo está en su CCAA.

### E-02 · «Hay que sacarse el carnet de manipulador de alimentos»

- **Dónde se dice:** manipulador-alimentos.net, manipulador-de-alimentos.com y similares aparecen en la propia SERP de «como montar una pasteleria»; su modelo de negocio es vender el curso.
- **Corrección (PA-11):** el **RD 202/2000 está derogado por el RD 109/2010**. No existe carnet oficial ni entidades de formación autorizadas previamente. La obligación es del **empresario**, por el Anexo II, Cap. XII del Rgto. 852/2004: garantizar y **poder acreditar** la formación adecuada de cada manipulador. Un certificado de curso vale como evidencia, pero **el «carnet» no es un requisito legal**.
- **Por qué importa:** cambia el entregable. Lo que hay que darle al lector no es un curso, es un **registro de formación** que aguante una inspección.

### E-03 · «Los alimentos con huevo, a 8 °C y 24 horas (RD 1254/1991)»

- **Dónde se dice:** sigue apareciendo en páginas de higiene y de proveedores (p. ej. https://www.supercash.es/blog-hosteleria/se-puede-utilizar-huevo-fresco-en-hosteleria/, https://higieneambiental.com/huevo-fresco-establecimientos-por-menor).
- **Corrección (PA-14):** el RD 1254/1991 está **derogado desde el 22 de diciembre de 2022**. Hoy manda el **art. 9 del RD 1021/2022**, que cambia el criterio: introduce la vía de los **70 °C/2 s**, la vía de los **63 °C/20 s con consumo inmediato**, y mantiene los 8 °C/24 h **sólo** para los productos del apartado 1.a) no estables y los del apartado 2. Y **para un producto de pastelería relleno la temperatura buena no es 8 °C sino 4 °C** (art. 4.1, fila 9).
- **Por qué importa:** es literalmente la temperatura de la vitrina y la vida útil del producto. Equivocarse aquí es un riesgo sanitario y una sanción.

### E-04 · «Puedes montar tu negocio de tartas desde casa»

- **Dónde se dice:** es uno de los tres People Also Ask medidos («¿Cómo empezar un negocio de repostería desde casa?») y el enfoque de al menos dos resultados de la SERP (ayudatpymes.com «online desde casa», y la familia de keywords «montar una pastelería en casa», «requisitos para montar un obrador en casa», «vender repostería desde casa España»).
- **Corrección (PA-29):** el **art. 13.8 del RD 1021/2022** limita lo que se puede elaborar en vivienda a: comidas preparadas con tratamiento térmico suficiente; **productos de panadería y repostería estables a temperatura ambiente**; mermeladas/confituras/jaleas con tratamiento térmico posterior al envasado; conservas vegetales con **pH < 4,5**. Además **prohíbe congelar** (art. 13.5.e), prohíbe suministrar a colectividades y eventos (13.5.b), limita la venta a mercados ocasionales/periódicos o reparto a domicilio **dentro de la zona de salud** (13.4), topa el volumen en **100 kg/semana** (13.9) y obliga a la mención «**Elaborado en vivienda particular**» + fecha (13.10).
- **Traducción brutal:** **la tarta de nata por encargo desde casa no es legal.** Las galletas decoradas y los bizcochos secos, sí. Ninguna de las páginas de la SERP lo dice.

### E-05 · Las fechas de las normas nuevas se copian mal (Ley 1/2025 y Verifactu)

- **Dónde se dice:** sobre la **Ley 1/2025** he encontrado **tres fechas incompatibles** en tres fuentes distintas (2-ene-2025 en pactomundial.org; 3-abr-2026 en economistjurist.es; «al año de la publicación, abril de 2026» para el art. 6 en varias). Sobre **Verifactu**, sigue circulando «obligatorio en 2026» pese al **RD-ley 15/2025** que lo llevó a 2027.
- **Corrección:** en Verifactu, **1-ene-2027 para sociedades y 1-jul-2027 para autónomos** (PA-37). En la Ley 1/2025, **la fecha no está resuelta ni siquiera con el metadato del BOE** (que devuelve una fecha anterior a la publicación) → **este producto no puede imprimir una fecha ahí** sin leer la disposición final (§18).
- **Por qué importa:** una guía «Cómo Montar» se compra por las fechas. Publicar una fecha equivocada es el fallo que más caro sale en una guía de este tipo.

---

## 14. Lo que NO se puede afirmar en el copy (landing, email, Stripe, blog)

1. **«Cumple la normativa española»** / «tu pastelería quedará 100 % legal». No es verificable y la responsabilidad es del operador. Fórmula segura: «el mapa normativo completo, con la norma, el artículo y el enlace, para que sepas exactamente qué te pide cada administración».
2. **Cifras de inversión** («montar una pastelería cuesta 60.000 €»). No hay fuente primaria (PA-43). Se entrega un modelo, no un número.
3. **Cifras de rentabilidad** («8-12 % de margen», «el postre más rentable»). Idem — es una declaración en prensa, no un dato sectorial.
4. **Volúmenes de búsqueda o promesas de tráfico.** La SERP medida es de 10-20 búsquedas/mes en España para la intención de apertura. **El producto no se vende por SEO** (mismo patrón que los tres anteriores).
5. **«Válido en toda Hispanoamérica».** Marco español (regla de John del 5-sep). El copy va sin siglas españolas en titulares; la FAQ «¿me sirve fuera de España?» ofrece la adaptación como servicio.
6. **Fechas de la Ley 1/2025** hasta resolver §18.
7. **«Verifactu es obligatorio en 2026».** Falso desde el RD-ley 15/2025.
8. **«Incluye el carnet de manipulador»** o cualquier referencia a él como requisito.
9. **«Podrás llamarte artesano»**. Depende de la CCAA; en muchas no hay norma y en Cataluña hay carné y acreditación.
10. **«Podrás vender tus tartas desde casa»**. Ver E-04. Si se menciona el obrador en casa, se menciona **con su lista blanca**.
11. **Precio tachado, ratings o testimonios** en producto nuevo (norma de la casa).
12. **Nombres de agentes de la plataforma** sin comprobarlos contra el catálogo real (`fase8c-agentes/catalogo-hub.json`). Los que tocan aquí: «Pastelero Consultor Pro», «Pastelería Creativa», «Hotel Pastry & Bakery Pro» — **el bloque de hotelería va en inglés siempre**.
13. **«AI Chef Pro tiene plan gratuito»**. No lo tiene desde el 15-ago-2025: «desde 10 €, 10.000 créditos».

---

## 15. Las 10 normas cuyo cambio invalidaría el producto (riesgo de caducidad)

Ordenadas por probabilidad × daño.

| # | Norma / dato | Qué se rompe | Ventana |
|---|---|---|---|
| **R-01** | **RD 126/2026 (SMI 2026)** | Todo el xlsx de coste de plantilla y los ejemplos de nómina | **Caduca el 31-dic-2026.** Se sustituye cada febrero. Riesgo alto y seguro |
| **R-02** | **Revisión salarial 2026 del convenio de Madrid** (y sus hermanos provinciales) | Las 6 filas de la tabla salarial, base del escandallo de personal | **Caduca el 31-dic-2026.** Además el convenio marco vence y puede renegociarse |
| **R-03** | **Decreto 26/2026 CM — período transitorio de 1 año** | La frase «tienes de plazo hasta…» y el capítulo de trámite en Madrid | **28-mar-2027** |
| **R-04** | **RD 1055/2022 art. 9.4** — referencias de envase reutilizable en < 300 m² | Un requisito que hoy es futuro pasa a ser presente | **1-ene-2027** |
| **R-05** | **Verifactu (RD 1007/2023 + RD-ley 15/2025)** | El capítulo de TPV y facturación. Ya se ha aplazado **dos veces**: probabilidad real de una tercera | **1-ene-2027 / 1-jul-2027** |
| **R-06** | **Registro horario digital** (RD en tramitación) | El capítulo de control de jornada y la recomendación de herramienta | Estimado 2027 |
| **R-07** | **Ley 1/2025** — obligaciones y sanciones | El bloque de desperdicio; hoy con la fecha en disputa | Inmediato (hay que resolverlo antes de publicar) |
| **R-08** | **RD 496/2010** — norma de calidad de confitería/pastelería | Definiciones legales de bollería/pastelería/repostería y denominaciones de venta. Es de 2010 y **el pan ya se actualizó en 2019**: una actualización análoga es plausible | Sin fecha, riesgo medio |
| **R-09** | **Art. 91 Ley 37/1992 (IVA)** | Tipos por familia de producto. Ha habido rebajas y restituciones temporales de tipos en alimentación en los últimos ejercicios | Cada Ley de Presupuestos |
| **R-10** | **Registros sanitarios autonómicos** | El cuadro por CCAA (PA-04). Madrid ha legislado en 2026 y Valencia en 2025: **las CCAA están adaptándose al RD 1021/2022 ahora mismo** y en los próximos 24 meses saldrán más decretos | Continuo |

> **Consecuencia de diseño, no de contenido:** todo lo de la tabla debe vivir en **celdas de parámetro o en un anexo fechado**, nunca cosido en la prosa de un capítulo. Un «Anexo normativo — actualizado a <fecha>» de 6-8 páginas permite reeditar el producto cambiando un fichero, igual que la familia de kits v2.0.

---

## 16. Mapa norma → entregable propuesto (y control de canibalización)

### 16.1 Entregables que salen directamente del bloque normativo

| Entregable | Formato | Normas que lo sostienen |
|---|---|---|
| `01_hoja_de_ruta_tramites` | xlsx | PA-01, PA-04, PA-05, PA-38 |
| `02_registro_sanitario_por_ccaa` | xlsx | PA-04 |
| `03_viabilidad_del_local` (semáforos) | xlsx + checklist | PA-06, PA-07, PA-40 |
| `04_control_suministro_b2b` (25 % / 500 kg / 50 km) | xlsx | PA-02, PA-03 |
| `05_matriz_alergenos_obrador` | xlsx | PA-09, PA-21, PA-22, PA-23 |
| `06_registro_temperaturas` (fila 9 precargada) | xlsx | PA-12 |
| `07_registro_congelacion` | xlsx | PA-13 |
| `08_decision_huevo` (70/63/ovoproducto) | xlsx | PA-14, PA-15 |
| `09_coste_plantilla` (6 grupos de Madrid) | xlsx | PA-32, PA-33 |
| `registro_formacion_personal` | xlsx | PA-11 |
| Checklist «obrador en casa: lista blanca» | checklist | PA-29 |
| Cartelería «ELABORACIÓN PROPIA» + alérgenos | docx/pdf | PA-17, PA-21 |
| Anexo normativo fechado | docx | todo el bloque |

Todos los xlsx respetan las prohibiciones del pipeline (sin INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA ni referencias entre libros; cero constantes dentro de fórmulas; parámetros en celda verde).

### 16.2 ⚠️ Canibalización real con activos propios — hay que decidirlo ANTES del guion

| Activo propio | Solape detectado | Propuesta |
|---|---|---|
| **`kit-tareas-pasteleria` (12 €)** | Ya trae **matriz de alérgenos de vitrina (14 UE) + cartel + etiquetas** y **registro de temperaturas**. Es solape directo con `05` y `06` | La guía **no repite** la matriz de vitrina: entrega la **matriz de OBRADOR** (materias primas × alérgenos × orden de elaboración, PA-22), que es otra cosa, y **enlaza** al kit para la parte de vitrina. Upsell natural 65 € → 12 € |
| **`guia-panaderia-obrador` (65 €)** | Comparte CAPEX, P&L, cash-flow, turnos, business plan y manual del obrador; y comparte el RD 308/2019 si la pastelería vende pan | Reutilizar el **motor** (molde B de checklists, estructura de xlsx), **no el contenido**. La pastelería tiene tres bloques que la panadería no tiene: **huevo/ovoproductos (art. 9)**, **temperatura de producto relleno (fila 9)** y **encargos/tartas personalizadas**. Ahí está la diferencia de producto |
| **`plan-negocio-panaderia` (35 €)** | El business plan | La guía «Cómo Montar» no es un plan de negocio: es el **proceso de apertura**. Mantener la frontera explícita y enlazar |
| **`pack-appcc` (14 €)** | El APPCC | La guía entrega **prerrequisitos + 5 registros del obrador**, y enlaza al pack para el sistema completo |
| **Guía Food Cost, cap. 17** (costeo por lote en obrador) | Escandallo | No repetir escandallo: enlazar |

### 16.3 Encaje de precio

La escalera del catálogo sitúa las guías «Cómo Montar» en **65 €** (gastronómico 85 €). El hermano directo `guia-panaderia-obrador` está en **65 €**. **Propuesta: 65 €**, sin tachado, con pago cripto desde el nacimiento (allowlist `CRYPTO_PRODUCTS`) además de Stripe.

---

## 17. Preguntas para John

1. **Alcance de variantes.** ¿Entran las siete variantes del brief (obrador+tienda, pastelería-cafetería, sin obrador, B2B/online, boutique de autor, cake design, obrador en casa) o el producto se centra en **obrador+tienda** y las otras van como capítulos cortos? La cafetería abre un frente entero (comidas preparadas, art. 30 del RD 1086/2020, otro convenio, otro IVA) y puede duplicar el trabajo.
2. **El producto lleva 4 meses anunciado como «Próximamente · Mayo 2026»** en los dos hubs. ¿Se corrige el rótulo a una fecha nueva, se quita la fecha, o se deja hasta el lanzamiento?
3. **Canibalización con `kit-tareas-pasteleria`:** ¿confirmas el reparto del §16.2 (la guía NO repite la matriz de vitrina y hace upsell al kit), o prefieres que la guía sea autosuficiente aunque solape?
4. **Convenio de la pastelería-cafetería.** ¿Tienes criterio propio (29 años de alta hostelería) sobre qué convenio se aplica cuando el mismo local vende mostrador y sirve mesas? Es un dato de dinero y no lo he podido resolver con fuente.
5. **Cobertura territorial de los cuadros por CCAA.** ¿Cerramos en las 4 de ejemplo (Madrid, Cataluña, Andalucía, C. Valenciana) o hacemos las 17? Las 17 son ~2 días más de verificación y multiplican el coste de mantenimiento (R-10).
6. **Anexo normativo fechado como pieza separada:** ¿lo montamos así (permite reeditar sin tocar la guía) o va integrado en el cuerpo?
7. **Presupuesto.** Regla de 1 producto/semana y techo del 15 % de cuota. Este bloque normativo es el más pesado de los cuatro productos nuevos hasta la fecha (7 quedan verificaciones pendientes, §18). ¿Se aprueba una **segunda pasada de verificación** antes del guion, o se escribe el guion con lo que hay y se refuta después?

---

## 18. Registro de verificación: lo que NO pude verificar y hay que cerrar antes del guion

Ordenado por riesgo. **Ninguno de estos siete puede entrar en el producto tal cual está.**

| # | Qué falta | Por qué no salió | Cómo cerrarlo |
|---|---|---|---|
| **V-01** | **Fecha de entrada en vigor de la Ley 1/2025** y su régimen sancionador (cuantías) | El BOE devuelve sólo el índice; el metadato «Entrada en vigor» devuelve **02/01/2025**, anterior a la publicación (02/04/2025) → incoherente. Tres fuentes secundarias dan tres fechas | Descargar `https://www.boe.es/buscar/pdf/2025/BOE-A-2025-6597-consolidado.pdf` y extraer las disposiciones finales y los arts. 20-21 con `pypdf` (el mismo método que funcionó con el RD 1021/2022) |
| **V-02** | **Art. 91 de la Ley 37/1992 literal** (10 % / 4 % / hostelería / bebidas azucaradas) | La página consolidada del BOE trunca antes del art. 91; la URL de la sede AEAT da 404 | PDF consolidado de `BOE-A-1992-28740` + `pypdf`, buscando «Artículo 91» |
| **V-03** | **Art. 30 del RD 1086/2020** (comidas preparadas) | No consultado. Es la puerta de la variante cafetería | PDF consolidado de `BOE-A-2020-16345` (verificar el id) |
| **V-04** | **Articulado del RD 496/2010** y confirmación de que NO regula «artesano/artesanal/casero» | El BOE sirvió sólo índice y metadatos | PDF consolidado de `BOE-A-2010-7714` + `grep` de los cuatro términos |
| **V-05** | **RD 1055/2022: ¿una pastelería que envasa es «productor de producto»?** | Leído a nivel B. Es la duda de mayor impacto económico del bloque de envases | PDF consolidado de `BOE-A-2022-22690`, arts. 2.t), 16 y el capítulo de RAP |
| **V-06** | **Venta online a toda España**: ¿rompe algún requisito sanitario o exige RGSEAA? | Hipótesis planteada, no resuelta | Consulta expresa sobre el art. 3 vs. venta a consumidor final + criterio AESAN |
| **V-07** | **Decreto 13/2025 (C. Valenciana)** y **Decreto 85/2024 (Cataluña)** en su boletín | `noticias.juridicas.com` devolvió error de certificado TLS dos veces | Leerlos en DOGV y DOGC directamente |

**Verificaciones menores también pendientes:** RD 919/2006 / RITE para horno de gas (PA-08); Ley 37/2003 del Ruido y ordenanza municipal (PA-42); DB-SUA para accesibilidad de local (PA-40); calendario del RD 193/2023 leído a nivel B; actualización de 27-feb-2026 del RD 308/2019; convenios de Valencia y Sevilla (PA-33); redacción vigente de las tarifas del IAE (PA-38); Reglamento 852/2004 consolidado en EUR-Lex para citar el Cap. XI bis y el Cap. XII literalmente (PA-09, PA-11).

---

## 19. Conteo de cifras (metodología del recuento)

- **Cifras con fuente (URL + fecha de consulta):** 83. Incluye los 13 umbrales de temperatura del art. 4.1, los 3 umbrales del art. 3 (25 %, 500 kg, 50 km), los 6 parámetros del art. 9 (70 °C/2 s, 63 °C/20 s, 8 °C, 24 h) y art. 13 (100 kg, pH 4,5), los 6 importes del SMI, los 11 importes del convenio de Madrid, los 5 tramos del art. 9.4 del RD 1055/2022, los umbrales de gluten (20/100 mg/kg), los del pan (5 %, pH 4,2, 0,2 %, 3 harinas), el 1.300 m², el 0,45 €/kg, los 90 h / 16 domingos / 300 m² de horarios, y las fechas-umbral (2027 Verifactu, 2029/2030 accesibilidad, 28-mar-2027 Madrid).
- **Cifras sin fuente primaria (marcadas como tales y NO utilizables en el producto):** 20. Son las de §11 (inversión, obra, equipamiento, mobiliario, licencias, rentabilidad, tarifa de despacho), la rampa del 10 %/12 %, el capital de 42.071 € del seguro, las tres fechas incompatibles de la Ley 1/2025, el rango sancionador 2.000-500.000 €/60.000 €, y las tablas 2026 de Barcelona.
