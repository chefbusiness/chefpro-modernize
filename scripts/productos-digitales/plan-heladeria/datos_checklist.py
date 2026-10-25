#!/usr/bin/env python3
"""datos_checklist.py — las 80 tareas del checklist de apertura de la Heladería Artesanal ES 1.0 (SPEC D14; F1-camino §4:
12/15/15/12/13/13). Producto nuevo: no hay versión anterior; formato del `parrillero-2_2/datos_checklist.py`.
Marco legal: `F1-research-heladeria.md` §1 y la lista de tareas obligadas de §3 (lo marcado 🟡 va como «compruébalo»):
  · RDLeg 1175/1990: epígrafes 644.4 (fabricar y vender helado en el propio local) y 676 (consumo en el local); 414.4
    sólo si se fabrica para otros a escala industrial;
  · Ley 12/2012, arts. 2-4 y anexo: declaración responsable sin licencia previa para el 644.4 hasta 750 m²; la parte de
    hostelería (676) por el régimen municipal; la terraza, siempre con autorización de ocupación de la vía pública;
  · RD 1021/2022: registro autonómico previa declaración responsable; art. 3 (suministro marginal, localizado y
    restringido a otros negocios, con declaración y registro de destinatarios); art. 9 (huevo ≥ 70 °C 2 s u
    ovoproducto; mezcla con huevo, mantecada en 24 h); arts. 4.1 y 5.9 (≤ −18 °C, sin recongelar); art. 11
    («ELABORACIÓN PROPIA»); RD 618/1998, arts. 2.9 y 3 (artesano, denominaciones, 430 g/l); RD 126/2015 (alérgenos);
  · ET arts. 1.1, 16 y 34.9; ALEH VI art. 4 (convenio provincial de hostelería); Ley 31/1995 (PRL).
Orden del proceso (SPEC D11, seguridad): grasas, yemas y emulsionantes ANTES de pasteurizar; después, sólo lo que no
necesita tratamiento. Sin «carné» en todo el libro. Cada tarea: (trámite / acción, responsable, plazo, notas).
Pestañas ≤ 31 caracteres. Sesión Claude Code, 25-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — HELADERÍA ARTESANAL'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Consulta urbanística previa del local', 'Titular / Técnico', 'Antes de firmar el alquiler',
         'Pregunta al ayuntamiento cuatro cosas: si el uso permite elaborar y vender helado con consumo en el local, '
         'qué potencia eléctrica tiene el local, si admite salida de humos (crepes y gofres) y si la calle admite '
         'terraza. Sin humos, el invierno va de chocolate, tartas y turrón helado'),
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF: '
         'compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036/037) en los epígrafes 644.4 y 676 del IAE', 'Gestoría', 'Semana 2',
         'El 644.4 («comercio al por menor de helados») te permite fabricar helado y tartas heladas en el propio '
         'local para venderlos allí; el 676 cubre el consumo en mesas y terraza (RDLeg 1175/1990). Exento de cuota '
         'con una cifra de negocio inferior a 1 millón de euros'),
        ('Valorar el epígrafe 414.4 sólo si vas a fabricar para otros a escala', 'Gestoría', 'Semana 2',
         'El 414.4 es la elaboración industrial de helados. Vender algo a restaurantes de tu zona cabe en el 644.4 '
         'si es marginal (fase 3), pero confírmalo con tu gestoría si el canal crece'),
        ('Alta en la Seguridad Social (administrador o autónomo)', 'Gestoría', 'Semana 2',
         'Consulta la cuota del ejercicio en curso y si te aplica la cuota reducida de inicio de actividad'),
        ('Certificado digital', 'Titular', 'Semana 1',
         'Imprescindible para Hacienda, la Seguridad Social y las declaraciones responsables'),
        ('Cuenta bancaria y tarjeta del negocio', 'Titular', 'Semana 2',
         'Separadas de las personales: por ellas pasan las liquidaciones del datáfono, los pagos a proveedores y '
         'los cobros de los restaurantes'),
        ('Gestoría laboral y fiscal y software de facturación Veri*factu', 'Titular', 'Semanas 2-4',
         'Nóminas de los fijos discontinuos con sus llamamientos. El software de facturación del TPV tiene que '
         'cumplir Veri*factu: consulta con tu gestoría la fecha que te aplica antes de comprar el TPV'),
        ('Presentar el plan al banco y pedir dos ofertas de préstamo', 'Titular', 'Semanas 2-4',
         'Lleva el plan financiero completo, con la tesorería mes a mes. Pide también oferta de leasing o renting de '
         'la maquinaria de frío y de una línea ICO'),
        ('Seguro de responsabilidad civil y multirriesgo', 'Corredor de seguros', 'Antes de la obra',
         'RC de al menos 300.000 € y multirriesgo con avería de maquinaria y deterioro de mercancía en frío'),
        ('Registro de la marca en la OEPM', 'Titular', 'Semanas 2-4',
         'Comprueba antes que el nombre no está registrado en tu clase (productos de heladería y servicios de '
         'hostelería)'),
    ]),
    ('F2 - Local y licencia', 'FASE 2: LOCAL, OBRA, LICENCIA Y TERRAZA (semanas 3-12)', [
        ('Elegir el local: 80-90 m² con obrador de 20-25 m²', 'Titular', 'Semanas 3-6',
         'Calle comercial de barrio o paseo cerca de un parque o colegios, con paso de gente en las tardes de verano '
         'y de fin de semana en invierno'),
        ('Comprobar la potencia: unos 30 kW en trifásica', 'Técnico / Distribuidora', 'Antes de firmar',
         'Vitrinas encendidas las 24 horas, pasteurizador, mantecadora, abatidor, crepera y climatización. Un local '
         'monofásico obliga a una acometida nueva: pregunta plazo y coste a la distribuidora'),
        ('Comprobar desagües, ventilación y salida de humos', 'Técnico', 'Antes de firmar',
         'Desagüe en el obrador, salida de aire para los condensadores de las máquinas y, si quieres crepes y '
         'gofres, la salida de humos que pida la ordenanza'),
        ('Negociar el alquiler: carencia de obra y fianza', 'Titular', 'Antes de firmar',
         'El plan cuenta dos meses de renta antes de abrir y tres de fianza. Pide carencia mientras dura la obra'),
        ('Contrato de arrendamiento con el uso de heladería', 'Titular / Abogado', 'Semana 6',
         'Que el contrato diga «heladería con obrador y consumo en el local» y quién paga la acometida eléctrica'),
        ('Encargar el proyecto técnico y la memoria de la actividad', 'Arquitecto/a o ingeniero/a', 'Semanas 6-8',
         'Distribución del obrador con circuito de sucio a limpio, potencia, ventilación y la terraza'),
        ('Declaración responsable de la actividad comercial (644.4)', 'Técnico / Ayuntamiento', 'Antes de la obra',
         'La venta y fabricación de helado en el propio local, hasta 750 m², va por declaración responsable, sin '
         'licencia previa (Ley 12/2012, arts. 2-4 y anexo). Si la obra no necesita proyecto, tampoco necesita '
         'licencia (art. 3.3)'),
        ('Licencia o declaración municipal de la parte de hostelería (676)', 'Técnico / Ayuntamiento',
         'Antes de la obra',
         'Las mesas y el consumo en el local no están en el anexo de la Ley 12/2012: van por el régimen de tu '
         'ayuntamiento (licencia o declaración responsable, según la ordenanza)'),
        ('Solicitar la autorización de la terraza', 'Titular / Ayuntamiento', 'Con la declaración responsable',
         'Es ocupación de la vía pública y siempre se pide aparte (Ley 12/2012, art. 2.2). Pregunta la tasa de tu '
         'ayuntamiento: la del plan es una cifra de ejemplo'),
        ('Aumento de potencia a trifásica y boletín eléctrico', 'Instalador autorizado', 'Durante la obra',
         'Certificado de la instalación (boletín) para el nuevo contrato de luz'),
        ('Obra del obrador: superficies lavables y suelo antideslizante', 'Constructor', 'Semanas 8-12',
         'Paredes alicatadas, suelo antideslizante, falsos techos lavables, lavamanos de accionamiento no manual y '
         'aseo con vestuario'),
        ('Fontanería, desagües y climatización', 'Instalador', 'Semanas 8-12',
         'Agua caliente y fría en el obrador, desagües sifónicos y climatización de la tienda'),
        ('Instalación de la maquinaria de frío y del pasteurizador', 'Proveedor', 'Semanas 10-12',
         'Prueba en marcha con el técnico: temperaturas de la vitrina, del abatidor y de los armarios'),
        ('Rótulo, escaparate y cartel de horario', 'Rotulista', 'Semanas 10-12',
         'El rótulo puede necesitar su propia autorización municipal. «Artesano» sólo con la calificación (fase 5)'),
        ('Licencia o comunicación de la obra y certificado final', 'Técnico', 'Fin de la obra',
         'Guarda el certificado final y el boletín: te los pedirá la declaración responsable de inicio'),
    ]),
    ('F3 - Obrador y sanidad', 'FASE 3: OBRADOR, EQUIPO Y REGISTRO SANITARIO (semanas 8-14)', [
        ('Comprar el pasteurizador, la mantecadora y el abatidor', 'Titular', 'Semanas 8-10',
         'Pasteurizador de 30 l, mantecadora horizontal de 6-12 l por ciclo y abatidor para cubetas. Pide ficha '
         'técnica, potencia y garantía; la maquinaria de ocasión revisada cuesta bastante menos'),
        ('Comprar los armarios de conservación y la vitrina de 18 cubetas', 'Titular', 'Semanas 8-10',
         'Dos armarios a −20/−25 °C, uno a +2/+4 °C para madurar y una vitrina de 18 cubetas: en una ciudad media, 24 '
         'son merma y consumo'),
        ('Contrato de mantenimiento con un frigorista certificado', 'Titular', 'Antes de abrir',
         'Revisión antes del verano y en el cierre de enero. La carga de gases refrigerantes la hace sólo un técnico '
         'certificado: el personal no la toca'),
        ('Declaración responsable de inicio de la actividad alimentaria', 'Titular / Gestoría', 'Antes de abrir',
         'Va al registro sanitario de tu comunidad autónoma (RD 1021/2022). El RGSEAA sólo aplica si sirves a otros '
         'negocios por encima de lo que permite el art. 3 (tarea siguiente)'),
        ('Declaración del art. 3 del RD 1021/2022 antes del primer pedido a un restaurante', 'Titular',
         'Antes de vender a otro negocio',
         'Vender helado a restaurantes o cafeterías de otra titularidad exige que sea marginal (el 25 % del volumen '
         'del año o 500 kg a la semana como máximo), de tu zona y a nadie inscrito en el RGSEAA, con una declaración '
         'responsable y el registro de destinatarios, cantidades y fechas'),
        ('Plan APPCC con el punto crítico de la pasteurización', 'Consultor / Titular', 'Antes de abrir',
         'Orden de la mezcla: secos con el azúcar, líquidos, y grasas (nata, mantequilla), yemas y emulsionantes al '
         'subir, a 40-50 °C, ANTES de pasteurizar; después 85 °C, enfriado rápido a 4 °C o menos y maduración a 2-4 '
         '°C. Tras pasteurizar sólo entra lo que no necesita tratamiento (pastas puras, variegatos, fruta lavada '
         'de los sorbetes): nunca yema ni nata cruda'),
        ('APPCC: maduración, mantecación, abatimiento y conservación', 'Titular', 'Antes de abrir',
         'La mezcla con huevo se manteca en las 24 horas siguientes (RD 1021/2022, art. 9.3); abatimiento a −18 °C '
         'en el corazón; conservación a −18 °C o menos y sin recongelar (arts. 4.1 y 5.9). La temperatura de la '
         'vitrina la fija tu APPCC, no una norma estatal'),
        ('Huevo: pasteurizado en la mezcla u ovoproducto', 'Titular', 'Antes de abrir',
         'El huevo crudo vale si la mezcla alcanza 70 °C durante 2 segundos (la pasteurización a 85 °C lo cumple); '
         'si no, ovoproducto de un establecimiento autorizado (RD 1021/2022, art. 9)'),
        ('Trazabilidad por lote y registros de temperatura', 'Titular', 'Desde la primera tanda',
         'Lote y fecha de cada tanda, temperaturas de pasteurización y de los armarios, y proveedores de cada '
         'materia prima'),
        ('Fichas técnicas por sabor con sus alérgenos', 'Maestro heladero', 'Antes de abrir',
         'Receta balanceada, rendimiento y alérgenos de cada sabor: frutos de cáscara, cacahuete, leche, huevo, '
         'gluten (galleta, barquillo), soja y sulfitos'),
        ('Cartel e información de alérgenos en el mostrador', 'Titular', 'Antes de abrir',
         'Por escrito en cartel o carta, o de palabra si está registrado por escrito y un cartel dice dónde pedirlo '
         '(RD 126/2015, arts. 4 y 6)'),
        ('Etiqueta completa de las tarrinas preenvasadas', 'Titular', 'Antes de vender tarrinas de autoservicio',
         'Las tarrinas que dejas envasadas en el congelador llevan la etiqueta de los arts. 9 y 10 del Reglamento '
         '(UE) 1169/2011, menos la nutricional (RD 126/2015, art. 5)'),
        ('Carta con las denominaciones del RD 618/1998', 'Maestro heladero', 'Antes de abrir',
         '«Helado crema», «mantecado» (4 % de yema o más), «sorbete» (15 % de fruta o más) o «granizado» sólo si la '
         'receta cumple el art. 3; si no, «helado de…» o «sabor a…». El helado tiene que pesar 430 g por litro o más'),
        ('Protocolo de espátulas y lavaporcionador contra el contacto cruzado', 'Titular', 'Antes de abrir',
         'Una espátula por cubeta y lavaporcionador con agua corriente; para un cliente alérgico, espátula limpia y '
         'cubeta sin empezar'),
        ('Proveedores de leche, nata, fruta, pastas y envases', 'Titular', 'Semanas 10-14',
         'Dos proveedores por materia prima clave (pistacho, cacao, vainilla) y envases sin poliestireno expandido; '
         'cucharillas de madera o compostables'),
    ]),
    ('F4 - Personal y APPCC', 'FASE 4: PERSONAL, APPCC Y FORMACIÓN (semanas 10-14)', [
        ('Copiar la tabla salarial del convenio provincial de hostelería', 'Gestoría', 'Semana 10',
         'Las heladerías están en el convenio provincial de hostelería (VI Acuerdo Laboral de ámbito Estatal para el '
         'sector de Hostelería, art. 4). Pon su salario más bajo en la hoja de Supuestos del plan'),
        ('Contratos fijos discontinuos para la temporada', 'Gestoría', 'Antes de la temporada',
         'Por escrito, con la orden y la forma de llamamiento (art. 16 del Estatuto de los Trabajadores). El eventual '
         'es para lo imprevisible, y una factura de «autónomo» con tu horario es falso autónomo (art. 1.1)'),
        ('Contrato del dependiente/a y encargado/a de todo el año', 'Gestoría', 'Semana 12',
         'Abre y cierra cuando el titular está en el obrador: define sus funciones y su grupo del convenio'),
        ('Calendario de llamamientos de abril a septiembre', 'Titular', 'Febrero',
         'Quién entra en abril, quién en mayo y quién en junio, y cuándo se para cada uno en otoño'),
        ('Registro de jornada', 'Titular', 'Desde el primer contrato',
         'Obligatorio para toda la plantilla (art. 34.9 ET), también para los fijos discontinuos'),
        ('Menores de 18 años: horario sin noche ni horas extra', 'Gestoría', 'Si contratas a menores',
         'No pueden trabajar de noche ni hacer horas extraordinarias (art. 6 ET): confírmalo con tu gestoría si el '
         'horario de verano llega a medianoche'),
        ('Formación de manipuladores de alimentos', 'Titular', 'Antes de abrir',
         'La da y la acredita la empresa (no hay un documento oficial que sacar): higiene, temperaturas, alérgenos '
         'y el orden de la pasteurización'),
        ('Formación técnica del maestro heladero', 'Titular', 'Antes de abrir',
         'Balanceo de mezclas (azúcares, sólidos y grasas), maduración y rendimiento: es inversión, no gasto'),
        ('Plan de prevención de riesgos laborales', 'Servicio de prevención', 'Antes de abrir',
         'Obligatorio (Ley 31/1995): trabajo en frío, cargas, cortes y quemaduras de la crepera; guantes para -20 °C'),
        ('Vigilancia de la salud de la plantilla', 'Servicio de prevención', 'Al contratar',
         'Reconocimientos médicos ofrecidos a cada persona que entra'),
        ('Desinsectación, desratización y desinfección (DDD)', 'Empresa del ROESB', 'Antes de abrir',
         'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
        ('Plan de limpieza del obrador y de la vitrina', 'Titular', 'Antes de abrir',
         'Pasteurizador y mantecadora tras cada uso, cubetas, carapinas y lavaporcionador; con su registro'),
    ]),
    ('F5 - Marca y carta', 'FASE 5: MARCA, CARTA Y CAPTACIÓN (semanas 8-16)', [
        ('Decidir el tipo de heladería y su carta', 'Titular', 'Semana 8',
         'Con obrador propio (este plan), vitrina sin obrador, quiosco o franquicia: cada uno tiene otra inversión '
         'y otra licencia'),
        ('«Artesano» en el rótulo sólo con la calificación de tu comunidad', 'Titular', 'Antes del rótulo',
         'La condición de empresa artesana se acredita con el documento de calificación artesanal (RD 618/1998, art. '
         '2.9), que da cada comunidad. Si no lo tienes, «ELABORACIÓN PROPIA» (RD 1021/2022, art. 11)'),
        ('Carta de 18 sabores en verano y 10-12 en invierno', 'Maestro heladero', 'Semanas 10-14',
         'Clásicos, de temporada y uno o dos de autor; sorbetes sin lácteos para alérgicos y veganos'),
        ('Escandallo de cada sabor y precio de carta', 'Titular', 'Semanas 12-14',
         'Calcula el coste de la bola, de la tarrina de medio litro y de la tarta helada; revísalo cada temporada '
         '(el pistacho, el cacao y la vainilla se mueven)'),
        ('Carta de invierno: crepes, gofres, chocolate y tartas por encargo', 'Maestro heladero', 'Octubre',
         'Crepes y gofres sólo si la ordenanza permite la salida de humos; si no, chocolate a la taza, tartas heladas '
         'y turrón helado de Navidad'),
        ('Identidad, fotos y web con la carta de sabores', 'Diseñador/a', 'Semanas 8-14',
         'Fotos reales del obrador y del helado; la web con los sabores del día y los encargos de tartas'),
        ('Ficha de Google Business y reseñas', 'Titular', 'Antes de abrir',
         'Horario de temporada y de invierno, fotos y respuesta a cada reseña'),
        ('Redes sociales con el sabor del día', 'Titular', 'Desde la obra',
         'La obra, la primera tanda, el sabor nuevo de cada semana y la vuelta de la temporada'),
        ('Canal de encargos de tartas heladas y para eventos', 'Titular', 'Antes de mayo',
         'Comuniones, cumpleaños y Navidad: formulario, plazo de encargo y señal'),
        ('Ofrecer helado a restaurantes de la zona (art. 3)', 'Titular', 'Tras la apertura',
         'Sólo después de la declaración del art. 3 del RD 1021/2022 y dentro de sus límites (fase 3). Cobro a 30 '
         'días'),
        ('Alta en una plataforma de reparto para las tarrinas', 'Titular', 'Junio',
         'Sólo tarrinas de medio litro y de litro en envase isotérmico; la comisión ronda el 30 %'),
        ('Fiesta de apertura con degustación', 'Titular', 'Semana de apertura',
         'Catas de sabores para el barrio, colegios y comercios vecinos'),
        ('Cláusula informativa de protección de datos', 'Titular', 'Antes de abrir',
         'En la web, en la lista de correo y en los encargos: cada canal necesita su información previa'),
    ]),
    ('F6 - Apertura y temporada', 'FASE 6: APERTURA, TEMPORADA Y PRIMEROS 90 DÍAS', [
        ('Abrir en marzo, no en otoño', 'Titular', 'Mes 1',
         'El plan abre en marzo para llegar al primer invierno con la caja del verano: abriendo en octubre, el '
         'fondo se gasta antes del primer julio'),
        ('Pruebas de producción y cata interna', 'Maestro heladero', 'Semana previa',
         'Dos o tres tandas por sabor para ajustar textura, dulzor y rendimiento antes de abrir'),
        ('Comprobar temperaturas y registros del primer día', 'Titular', 'Día 1',
         'Vitrina, armarios, abatidor y la hoja del pasteurizador; corrige cualquier desviación antes de servir'),
        ('Inspección sanitaria: tener el APPCC y los registros a mano', 'Titular', 'Desde el día 1',
         'Fichas de alérgenos, trazabilidad por lote, registros de temperatura y de limpieza, formación y DDD'),
        ('Revisar el seguro de mercancía y de avería antes de julio', 'Corredor de seguros', 'Junio',
         'Comprueba que cubre la mercancía de la vitrina y de los armarios si falla el frío en pleno verano'),
        ('Revisión del frío antes del pico de verano', 'Frigorista', 'Mayo',
         'Limpieza de condensadores y prueba de temperaturas: una avería en agosto es una cubeta perdida por sabor'),
        ('Cuadrante de julio y agosto', 'Titular', 'Junio',
         'En el pico el cuadrante va justo: prevé horas de más del titular o un extra de fin de semana'),
        ('Medir la merma cada semana', 'Titular', 'Semanal',
         'Helado derretido, devuelto o caducado: no se recongela. Si pasa del 5-8 % de la producción, recorta '
         'cubetas'),
        ('Comparar ventas y costes reales con el plan cada mes', 'Titular', 'Mensual',
         'Clientes al día, ticket, mercancía y personal frente a la cuenta de resultados del Excel'),
        ('Seguir la tesorería mes a mes y el saldo mínimo', 'Titular', 'Mensual',
         'Mira cuánta caja del verano llega a noviembre: es la que paga el invierno'),
        ('Plan de invierno: carta reducida y horario', 'Titular', 'Septiembre',
         'Menos sabores, horario de invierno y la carta de crepes, chocolate y tartas por encargo'),
        ('Fin de los llamamientos y vacaciones de enero', 'Gestoría', 'Octubre y enero',
         'Fin de la temporada de cada fijo discontinuo por escrito y tres semanas de cierre en enero'),
        ('Mantenimiento del frío en las semanas de cierre', 'Frigorista', 'Enero',
         'Revisión de vitrinas, armarios y mantecadora con el local cerrado, antes de la siguiente temporada'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 15, 15, 12, 13, 13], [len(t) for _, _, t in FASES]
assert all(len(n) <= 31 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
