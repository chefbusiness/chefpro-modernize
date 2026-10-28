#!/usr/bin/env python3
"""datos_checklist.py — las 80 tareas del checklist de apertura de la Cafetería Móvil para Eventos ES 1.0
(F1-camino §4: 12/16/14/10/14/14). Origen: el checklist del Parrillero ES 2.2 (`parrillero-2_2/datos_checklist.py`, con
lo legal común de los eventos ya verificado: constitución, IAE 677.9, IRPF art. 95.6, Veri*factu, RGPD, ET arts. 1.1,
16 y 34.9, formación acreditada por la empresa, TRLGDCU art. 103.l, LIVA art. 75.Dos, Ley 7/2012 art. 7) y el delta del
research (`F1-research-cafeteria-movil.md` §0-§2) y de la SPEC D10-D11, sólo con lo que el producto afirma:
  · RD 1021/2022 (registro autonómico previa declaración responsable; RGSEAA sólo si se vende a otros negocios;
    art. 13.5.b: nada se prepara en casa, la base tiene fregadero);
  · RD 1086/2020, arts. 2.h, 30.8.d y 30.10 (comida testigo: con salado, sí; bebidas y bollería servida tal cual,
    fuera según nuestra lectura, sin criterio oficial);
  · RD 3/2023, arts. 2.a, 65.3 y 66.b (agua en depósitos móviles); RD 126/2015 (alérgenos; avena = gluten salvo
    certificada; una jarra por leche);
  · Ley 7/2022, arts. 2.aa, 55.2 y 56, y RD 1055/2022, art. 7.6 (vasos, pajitas y agitadores; loza por defecto);
  · RD 199/2010 (venta no sedentaria con autorización municipal) frente a servicio en recinto privado;
  · RGV arts. 25-26 (remolque ≤ 750 kg) y reforma de la furgoneta con informe e ITV; Ape 50 = ciclomotor;
  · SPEC D11 (electricidad: 16 A ≈ 3,7 kW; cafetera ≤ 3,5 kW o toma dedicada; si no, generador o baterías);
  · IAE 677.9 (+ 675 si hay venta directa) como criterio de asesoría; ALEH VI art. 4 (camarero/a, no «barista»).
Lo 🟡 del research va con «compruébalo con tu ayuntamiento / gestor», sin cifra. Sin «carné» en todo el libro salvo el
de conducir B (el gate de ortografía del motor confunde «carne» y «carné»: F2-NOTAS del paellero §5). Cada tarea:
(trámite / acción, responsable, plazo, notas). Pestañas ≤ 31 caracteres. Sesión Claude Code, 28-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — CAFETERÍA MÓVIL PARA EVENTOS'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF y tu '
         'sueldo es el beneficio: compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036/037) y epígrafes del IAE', 'Gestoría', 'Semana 2',
         'Para los eventos contratados, el epígrafe 677.9 («otros servicios de alimentación propios de la '
         'restauración», RDLeg 1175/1990), como el catering; si vendes al público en mercados o ferias, también el '
         '675. Es criterio de asesoría: confírmalo con tu gestoría. Exento de cuota con una cifra de negocio '
         'inferior a 1 millón de euros'),
        ('Alta en la Seguridad Social (administrador o autónomo)', 'Gestoría', 'Semana 2',
         'Consulta la cuota del ejercicio en curso y si te aplica la cuota reducida de inicio de actividad'),
        ('Certificado digital', 'Titular', 'Semana 1',
         'Imprescindible para Hacienda, la Seguridad Social y la declaración responsable sanitaria'),
        ('Cuenta bancaria y tarjeta del negocio', 'Titular', 'Semana 2',
         'Separadas de las personales: por ellas pasan las señales, las facturas de empresas y agencias y los pagos '
         'al tostador'),
        ('Gestoría laboral y fiscal y software de facturación Veri*factu', 'Titular', 'Semanas 2-4',
         'Nóminas de los fijos discontinuos cada mes con llamamientos. El software de facturación tiene que cumplir '
         'el RD 1007/2023 (Veri*factu): confirma la fecha que te aplica antes de contratarlo'),
        ('IVA trimestral (modelo 303) al 10 %', 'Gestoría', 'Cada trimestre',
         'Lo que sirves, en la barra del evento o en la venta directa, va al 10 % (art. 91.Uno.2.2.º de la Ley '
         '37/1992). Los extras con precio propio (personalización, talleres, alquiler de la cafetera sin barista), al '
         '21 %'),
        ('Pagos fraccionados y retenciones de las nóminas (modelos 202 o 130, y 111)', 'Gestoría', 'Cada trimestre',
         'SL: modelo 202; autónomo: modelo 130. Tus facturas a empresas NO llevan retención de IRPF: el epígrafe '
         '677.9 es una actividad empresarial (art. 95.6 del Reglamento del IRPF). El 111 recoge las retenciones de '
         'las nóminas'),
        ('Declaraciones anuales: 390 y 347', 'Gestoría', 'Enero-febrero',
         '390: resumen anual del IVA. 347: clientes o proveedores con más de 3.005,06 € en el año (el tostador y las '
         'agencias habituales suelen pasarlo)'),
        ('RGPD: registro de actividades de tratamiento y cláusulas en presupuestos y contratos', 'Titular',
         'Antes del primer presupuesto',
         'Art. 30 del RGPD y LOPDGDD. Tratas datos de clientes, de invitados (las alergias son datos de salud) y del '
         'personal'),
        ('Web: aviso legal, privacidad, cookies (LSSI) y condiciones de contratación', 'Titular',
         'Antes de publicar la web',
         'Precio final con IVA para particulares. En un servicio con fecha no hay derecho de desistimiento de 14 días '
         'si el contrato se cierra a distancia (art. 103.l del TRLGDCU): tu señal, tus pagos y tu cancelación tienen '
         'que estar escritos y firmados, como en el contrato del kit'),
    ]),
    ('F2 - Vehículo y sanidad', 'FASE 2: VEHÍCULO, BASE, SANIDAD Y PERMISOS (semanas 3-8)', [
        ('Elegir el soporte: barra-carro con furgoneta, Piaggio Ape o remolque', 'Titular', 'Semana 3',
         'El caso del plan es furgoneta + barra-carro: entra en salones y pabellones. El Ape 50 es un ciclomotor (45 '
         'km/h como máximo, sin vías rápidas): para ir lejos, en remolque o furgoneta. Compara las tres '
         'configuraciones del plan de negocio (sección 6)'),
        ('Furgoneta: si fijas mueble, fregadero o depósitos, informe de reforma e ITV', 'Titular / Taller',
         'Antes de equiparla',
         'Fijar mobiliario, fregadero o depósitos es una reforma de vehículo: informe de conformidad e ITV de la '
         'reforma. Una barra-carro que se carga y se descarga no la necesita. Compruébalo con tu estación de ITV'),
        ('Remolque: hasta 750 kg sin matrícula, con tarjeta ITV propia', 'Titular', 'Al comprarlo, si lo usas',
         'Hasta 750 kg no lleva matrícula propia y sí tarjeta ITV (Reglamento General de Vehículos, arts. 25 y 26); '
         'por encima, matrícula, ITV y seguro, y el carné B o el B96 según el peso del conjunto. Desconfía de los '
         'remolques de importación sin homologación europea'),
        ('Almacén base con fregadero y punto de agua', 'Titular', 'Semanas 3-6',
         'Una nave o un garaje con fregadero para lavar loza, jarras y depósitos, almacén seco y frío, y plaza para la '
         'furgoneta. Nada se prepara en casa ni en un trastero sin agua (RD 1021/2022, art. 13.5.b)'),
        ('Declaración responsable e inscripción en el registro sanitario autonómico', 'Titular',
         'Antes del primer evento',
         'En el registro de la comunidad donde tiene su base; el vehículo y la barra forman parte del establecimiento '
         '(RD 1021/2022). Cada comunidad lo tramita a su manera: compruébalo con tu servicio de salud pública'),
        ('RGSEAA: sólo si vendes a otros negocios', 'Titular', 'Solo si aplica',
         'El Registro General Sanitario sólo hace falta si suministras a otros negocios (por ejemplo, café en grano '
         'con tu marca para tiendas); para servir al cliente final, no'),
        ('Plan APPCC itinerante: agua, leche, limpieza y alérgenos', 'Titular', 'Antes del primer evento',
         'Carga del agua, temperaturas de la leche (la de la etiqueta), limpieza de grupos, lanza y jarras, '
         'proveedores, alérgenos y formación, con sus registros'),
        ('Agua de los depósitos: carga en red, depósito alimentario y registro', 'Titular', 'Desde el primer evento',
         'El agua de los depósitos móviles es agua de consumo (RD 3/2023, art. 2.a) y respondes de ella hasta el '
         'punto de uso (arts. 65.3 y 66.b): carga en red pública, depósitos de uso alimentario, limpieza y '
         'desinfección registradas. El agua gris, a un punto autorizado, nunca al terreno de la finca'),
        ('Comida testigo: sólo si sirves salado', 'Titular', 'Antes del primer evento',
         'Si la barra añade sándwiches, tostas o quiches, guarda una ración de 100 g o más de cada uno durante 7 días, '
         'a 4 °C o menos, en todos los eventos, porque son tu actividad principal (RD 1086/2020, arts. 30.8.d y '
         '30.10). Según nuestra lectura, las bebidas y la bollería servida tal cual quedan fuera; no hay criterio '
         'oficial: confírmalo con tu autoridad sanitaria'),
        ('Fichas de alérgenos de cada bebida y de la bollería', 'Titular', 'Antes del primer evento',
         'Leche (también la sin lactosa), soja, frutos de cáscara (almendra, avellana) y avena, que es cereal con '
         'gluten salvo la certificada «sin gluten»; siropes, chai y cacao según su etiqueta. Cartel en la barra o '
         'información oral registrada por escrito (RD 126/2015)'),
        ('Vasos: loza en bodas y empresa; el de un solo uso, con precio aparte', 'Titular', 'Antes del primer evento',
         'El vaso de papel con forro de PE o PLA también es plástico (Ley 7/2022, art. 2.aa): se cobra aparte en el '
         'tique (art. 55.2). Pajitas y agitadores de plástico, prohibidos (art. 56): palillos de madera. En ferias y '
         'festivales manda el sistema de vaso reutilizable del organizador (RD 1055/2022, art. 7.6)'),
        ('Seguro de responsabilidad civil de explotación y de producto', 'Aseguradora', 'Antes del primer evento',
         'Recomendado: de 300.000 a 600.000 €, con daños al recinto y RC de producto. Es lo que suelen pedir fincas, '
         'hoteles y recintos feriales: adjunta el certificado a los presupuestos'),
        ('Seguro de la furgoneta y de los equipos', 'Aseguradora', 'Al comprarla',
         'Declara el uso profesional y la carga (cafetera, generador, depósitos); los equipos que salen a cada '
         'evento, asegurados aparte'),
        ('Electricidad: cafetera de 3,5 kW como máximo o toma dedicada', 'Titular', 'Antes de comprar la cafetera',
         'Una cafetera de dos grupos consume de 2,4 a 4,5 kW y un enchufe de 16 A da unos 3,7 kW: elige una de 3,5 kW '
         'como máximo o pide toma dedicada; si no la hay, generador inverter o baterías. En un stand de feria, la '
         'instalación la contrata el expositor con el recinto'),
        ('Venta en mercados, ferias y vía pública: autorización municipal', 'Titular', '30-60 días antes',
         'Vender al público en la vía pública o en un mercado es venta no sedentaria: autorización municipal por '
         'emplazamiento y modalidad, de duración limitada y expuesta al público (RD 199/2010). En un recinto ferial '
         'o un festival privado, contrato y canon con el organizador. Pide la ordenanza de tu ayuntamiento'),
        ('Evento contratado en recinto privado: permiso del recinto, por escrito', 'Titular', 'Por evento',
         'La barra en una finca, un hotel o una oficina es un servicio, no venta ambulante: el permiso es del '
         'recinto. Pide por escrito la toma eléctrica, el acceso y el aparcamiento del vehículo, y quién responde de '
         'cada permiso (el contrato del kit lo reparte)'),
    ]),
    ('F3 - Equipo y proveedores', 'FASE 3: EQUIPAMIENTO Y PROVEEDORES (semanas 4-8)', [
        ('Cafetera de dos grupos de gama media', 'Titular', 'Mes 1',
         'De 3,5 kW como máximo para que quepa en un enchufe de 16 A; con servicio técnico cerca de tu base'),
        ('Molino de espresso bajo demanda y molino de descafeinado o filtro', 'Titular', 'Mes 1',
         'El invitado español pide descafeinado de máquina: un segundo molino evita mezclar y purgar a cada pedido'),
        ('Barra-carro a medida con depósitos ocultos y ruedas', 'Titular', 'Mes 1',
         'Que pase por una puerta de salón y suba una rampa; con la carpa de 3 × 3 m y la iluminación para la noche'),
        ('Generador inverter o baterías con inversor, y cuadro con protecciones', 'Titular', 'Mes 1',
         'Para las fincas sin toma suficiente. Las baterías son silenciosas para las bodas; el generador, a sotavento '
         'y lejos de los invitados'),
        ('Depósitos alimentarios, bomba, filtro descalcificador y lavamanos', 'Titular', 'Mes 1',
         'Agua limpia y gris por separado; el filtro protege la cafetera y el sabor del café'),
        ('Nevera bajo barra, neveras portátiles, acumuladores y termómetro', 'Titular', 'Mes 1',
         'La leche, a la temperatura de su etiqueta desde la base hasta la barra; la UHT o la ESL «barista» aguanta '
         'mejor el evento'),
        ('Jarras por tipo de leche, tampers y básculas', 'Titular', 'Mes 1',
         'Una jarra por cada leche (entera, sin lactosa, avena, soja) y purga de la lanza entre leches: es la '
         'medida de alérgenos que más se olvida'),
        ('Loza para 150 invitados y cajas de transporte', 'Titular', 'Mes 1-2',
         'Tazas, platos y cucharillas con reposición durante el lavado (tabla de escalado de la calculadora)'),
        ('Tostador de café de especialidad con ficha de cata', 'Titular', 'Mes 1',
         'Pide la ficha del tostador (puntuación SCA de 80 o más) antes de anunciar «café de especialidad»: sin '
         'ficha, no lo escribas. Nada de torrefacto. Pacta precio y entrega por trimestre'),
        ('Leche, bebidas vegetales «barista», cacao, chai y siropes', 'Titular', 'Mes 1',
         'Con su ficha técnica y de alérgenos; la avena, certificada «sin gluten» si la ofreces a celíacos'),
        ('Obrador de bollería y dulces con ficha de alérgenos', 'Titular', 'Mes 1',
         'Se compra hecha y se sirve tal cual: guarda etiquetas y albaranes para la trazabilidad'),
        ('Vasos, tapas, servilletas y palillos de madera', 'Titular', 'Mes 1',
         'Para la venta directa; nada de pajitas ni agitadores de plástico'),
        ('TPV, datáfono y software de presupuestos', 'Titular', 'Mes 1-2',
         'Datáfono para la venta directa y software de facturación Veri*factu'),
        ('Uniformes y menaje de limpieza', 'Titular', 'Mes 1',
         'Delantales, paños por zonas, detergente de grupos y cepillos'),
    ]),
    ('F4 - Personal y formación', 'FASE 4: PERSONAL Y FORMACIÓN (semanas 6-10)', [
        ('Camarero/a de barra (barista) como fijo discontinuo', 'Gestoría', 'Antes del primer evento',
         '«Barista» no es categoría del convenio: se contrata como camarero/a de hostelería (VI Acuerdo Laboral de '
         'ámbito Estatal, art. 4: «instalaciones fijas o móviles»), fijo discontinuo con llamamiento (art. 16 del '
         'Estatuto de los Trabajadores). Nunca con facturas de autónomo: con tu horario y tu dirección es falso '
         'autónomo (art. 1.1)'),
        ('Bolsa de suplencias y de refuerzo para los eventos grandes', 'Titular', 'Antes de la temporada',
         'Una segunda estación pide un tercer barista: tenlo localizado en tu bolsa de fijos discontinuos (tabla de '
         'escalado de la calculadora)'),
        ('Alta en la Seguridad Social antes de cada llamamiento', 'Gestoría', 'Antes de cada evento',
         'El alta va antes de empezar a trabajar, también para un solo día'),
        ('Formación en higiene alimentaria acreditada por la empresa', 'Titular', 'Antes del primer evento',
         'El antiguo título de manipulador de alimentos ya no se exige: la empresa forma y acredita a su personal '
         '(Reglamento (CE) 852/2004, anexo II, cap. XII). Con un módulo de leche, agua y alérgenos'),
        ('Formación de barista: extracción, texturizado y latte art', 'Titular', 'Antes del primer evento',
         'Receta de la casa (gramos, tiempo y rendimiento), calibrado del molino y purga del grupo y de la lanza'),
        ('Formación en alérgenos y en el plan APPCC', 'Titular', 'Antes del primer evento',
         'Cada persona de la barra sabe qué lleva cada bebida y cada dulce, y cómo evitar el contacto cruzado entre '
         'leches'),
        ('Prevención de riesgos laborales: vapor, cargas y conducción', 'Servicio de prevención',
         'Antes del primer evento',
         'Evaluación de riesgos y plan de prevención (Ley 31/1995): quemaduras de vapor, carga de la barra y de los '
         'depósitos, conducción y posturas'),
        ('Registro de jornada', 'Titular', 'Desde el primer día',
         'Obligatorio para todo el personal, también los fijos discontinuos (art. 34.9 del Estatuto de los '
         'Trabajadores)'),
        ('Información de protección de datos al trabajador', 'Gestoría', 'Al contratar',
         'Cláusula informativa en el contrato y en el registro de jornada'),
        ('Fichas de trabajo por formato de evento', 'Titular', 'Antes del primer evento',
         'Bebidas por invitado, baristas, café, leche y vasos de cada formato (boda, empresa, congreso, feria), '
         'sacados de la tabla de escalado de la calculadora'),
    ]),
    ('F5 - Marca y captación', 'FASE 5: MARCA Y CAPTACIÓN (meses 1-3)', [
        ('Nombre, logo e identidad visual', 'Titular', 'Mes 1',
         'Comprueba que el nombre está libre en la OEPM y como dominio'),
        ('Web con formulario de presupuesto y SEO técnico', 'Titular', 'Mes 1-2',
         'Galería, formatos, zona de servicio y formulario con invitados, horas y lugar; datos estructurados y '
         'Search Console'),
        ('Fotos y vídeo profesionales de la barra y del latte art', 'Titular', 'Mes 1-2',
         'Es lo que miran los novios y los planners antes de pedir presupuesto'),
        ('Perfil de empresa en Google y primeras reseñas', 'Titular', 'Mes 1-3',
         'La zona que cubres y los servicios; pide la reseña después de cada evento'),
        ('Instagram y TikTok con servicios reales', 'Titular', 'Mes 1+',
         'La barra montada, el latte art y la cola de invitados funcionan solos en vídeo'),
        ('WhatsApp Business con plantillas', 'Titular', 'Mes 1',
         'Bienvenida, presupuesto, confirmación y recordatorio de alérgenos y de la toma eléctrica'),
        ('Alta en portales de bodas', 'Titular', 'Mes 2',
         'Con fotos y precio «desde» con lo que incluye (horas, invitados, desplazamiento)'),
        ('Wedding planners y fincas: lista y primer contacto', 'Titular', 'Mes 1-3',
         'El café se contrata después que la finca y el catering: llega a los planners y a las fincas de tu zona con '
         'un correo personal y el dossier'),
        ('Agencias de eventos y organizadores de congresos', 'Titular', 'Mes 2-4',
         'Pausas de café, stands de marca y jornadas: es la tipología que sostiene el equilibrio del plan'),
        ('Empresas de la zona: oficinas, presentaciones y Navidad', 'Titular', 'Mes 2-4',
         'Pop-up de café en la oficina, team building y cenas de Navidad; LinkedIn para llegar a recursos humanos y '
         'comunicación'),
        ('Calendario de mercados, ferias y festivales con su canon', 'Titular', 'Mes 2-6',
         'Elige las jornadas de venta directa por su público y su canon (porcentaje o cuota fija, conviértelo a '
         'porcentaje con tu previsión de ventas)'),
        ('Dossier para bodas, empresas y congresos', 'Titular', 'Mes 1-2',
         'Formatos, carta de bebidas, alérgenos, lo que pides al recinto (toma, acceso, agua) y el precio por '
         'invitado de cada tipo de evento'),
        ('Catas para planners, agencias y fincas', 'Titular', 'Mes 2-4',
         'Una barra montada para los que más eventos mueven: es tu mejor dossier'),
        ('Presencia en una feria nupcial', 'Titular', 'Mes 2-6',
         'Con la barra montada y café para los visitantes; recoge contactos con permiso para escribirles'),
    ]),
    ('F6 - Primer evento y 90 días', 'FASE 6: PRIMER EVENTO Y 90 DÍAS', [
        ('Briefing del cliente', 'Titular', '30 días antes',
         'Invitados, horario, formato (barra tras la cena, pausas de congreso, jornada de feria), carta, alergias, '
         'lugar, toma eléctrica, agua y acceso para la furgoneta'),
        ('Visita técnica o fotos del recinto', 'Titular', '21 días antes',
         'Toma de 16 A dedicada o generador, distancia de la furgoneta a la barra, suelo, sombra o cubierta en '
         'exterior, punto de agua y salida del agua gris'),
        ('Presupuesto firmado y señal a cuenta del precio', 'Titular', 'Al reservar la fecha',
         'Sin señal no se bloquea la fecha. Particulares: 30 % a cuenta del precio al firmar y 70 % siete días antes; '
         'empresas: 30 % al confirmar y 70 % a 30 días de la factura. Factura cada pago, también la señal (art. '
         '75.Dos de la Ley 37/1992). En efectivo, sólo pagos por debajo de 1.000 € (Ley 7/2012, art. 7)'),
        ('Contrato firmado con cancelación, plan B de lluvia y fuerza mayor', 'Titular', 'Al reservar la fecha',
         'Modelo del kit: cancelación en cuatro tramos sin huecos (se retiene el 10, 30, 60 o 100 % menos los costes '
         'que te ahorras, y es recíproca), plan B de lluvia (no es fuerza mayor), toma eléctrica y acceso exigidos '
         'por escrito al recinto'),
        ('Carta y alérgenos confirmados por escrito', 'Titular', '7 días antes',
         'Invitados definitivos, bebidas, leches vegetales y qué invitados tienen alergias o intolerancias'),
        ('Cálculo del evento con la calculadora', 'Titular', '7 días antes',
         'Bebidas, baristas, cafeteras, kg de café, litros de leche, vasos o loza, potencia y agua con tus invitados '
         'y tus horas'),
        ('Pedido de café, leche y bollería', 'Titular', '5-7 días antes',
         'Confirma la entrega 48-72 horas antes; la bollería, el día anterior o el mismo día'),
        ('Carga con la lista: cafetera, molinos, depósitos llenos, loza y fichas de alérgenos', 'Ayudante',
         'Día del evento',
         'Agua cargada en red pública y registrada, leche en neveras con acumuladores, generador con combustible'),
        ('Salida con margen y montaje una hora antes', 'Titular', 'Día del evento',
         'Una hora de margen sobre el trayecto, montaje y calibrado del molino con la primera tanda de café'),
        ('Servicio, cola y reposición', 'Titular', 'Día del evento',
         'Jarra por leche, purga entre leches, cartel de alérgenos visible y recuento de bebidas servidas'),
        ('Desmontaje, limpieza y agua gris', 'Ayudante', 'Final del evento',
         'Grupos y lanza limpios, posos y envases recogidos, el agua gris a un punto autorizado; fotos del espacio '
         'antes y después'),
        ('Facturas y vencimientos del evento', 'Titular', 'D+1 / D+2',
         'Particulares: el 70 % ya se cobró siete días antes. Empresas y agencias: factura del 70 % a 30 días; '
         'anota el vencimiento en la previsión de caja'),
        ('Reseña, fotos y agradecimiento al planner', 'Titular', 'D+2',
         'Pide la reseña y el permiso para publicar las fotos; si vino por un planner o una finca, agradéceselo'),
        ('Costes reales frente al presupuesto y cierre trimestral', 'Titular', 'D+7 y cada trimestre',
         'Compara las bebidas, el café y las horas reales de cada evento con la calculadora y ajusta precios'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 16, 14, 10, 14, 14], [len(t) for _, _, t in FASES]
assert sum(len(t) for _, _, t in FASES) == 80
assert all(len(n) <= 31 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
