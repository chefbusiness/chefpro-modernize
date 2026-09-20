# -*- coding: utf-8 -*-
"""
Contenido REDACTOR B — Kit de Tareas: Taquería Mexicana (aichef.pro)

Cubre las 12 hojas de checklist de los ficheros 05, 06, 07 y 08 (§3.1 de la
SPEC `02-SPEC-kit-tareas-taqueria.md`), más el 09 (PLANTILLA_SECCIONES),
BONUS-01 (BRIEFING_BLOQUES) y BONUS-02 (CALENDARIO_FILAS).

Columna `cuando` por hoja (regla dura + corrección del coordinador):
- 05 (las dos) y 06 (las 6)         -> hora HH:MM
- 07 Tareas Semanales               -> día de la semana, con tilde
- 07 Tareas Mensuales                -> SOLO {'1º de mes','Quincenal','Mensual','Fin de mes'}
- 08 (las dos)                      -> SIEMPRE con 'antes' / 'víspera' / 'día siguiente' / 'al confirmar'
"""

# --- 05 · 05-tareas-manager.xlsx ------------------------------------------

SEC_TAREAS_DIARIAS_MANAGER = [
    ('ANTES DE APERTURA', [
        ('Revisar la hoja de temperaturas firmada del turno anterior y archivarla',
         'Oficina', 'Encargado', '08:30'),
        ('Medir el rendimiento del trompo (asador vertical) del día: kilos montados y sobrante',
         'Cocina', 'Encargado', '09:00'),
        ('Repasar la previsión de reservas y de grupos del turno',
         'Oficina', 'Encargado', '09:15'),
        ('Comprobar que la barra de salsas está lista antes de abrir',
         'Barra', 'Encargado', '09:30'),
        ('Revisar la previsión de delivery del turno',
         'Oficina', 'Encargado', '09:45'),
    ]),
    ('DURANTE EL SERVICIO', [
        ('Supervisar los tiempos y las incidencias del canal de delivery',
         'Oficina', 'Encargado', '13:00'),
        ('Revisar el escandallo (costeo) del taco al pastor con las ventas del día',
         'Oficina', 'Encargado', '13:30'),
        ('Revisar el escandallo (costeo) de los guisados (cazuelas de relleno) más vendidos',
         'Oficina', 'Encargado', '14:00'),
        ('Registrar la merma del trompo del turno y anotar la causa',
         'Cocina', 'Encargado', '15:00'),
        ('Resolver las incidencias de sala y de mostrador que suban del turno',
         'Sala', 'Encargado', '15:30'),
    ]),
    ('CIERRE DE NEGOCIO', [
        ('Hacer el arqueo y el cuadre de caja y dejar constancia del reparto de propinas',
         'Oficina', 'Encargado', '23:30'),
        ('Cerrar el canal de delivery y revisar el balance del turno',
         'Oficina', 'Encargado', '23:40'),
        ('Responder las reseñas del día',
         'Oficina', 'Encargado', '23:50'),
        ('Revisar la merma de la barra de salsas y anotar el total del turno',
         'Barra', 'Encargado', '23:55'),
        ('Repasar con el equipo las incidencias del turno antes de cerrar',
         'Sala', 'Encargado', '00:00'),
    ]),
]

SEC_TAREAS_SEMANALES_MANAGER = [
    ('COMPRAS E IMPORTACIÓN', [
        ('Lanzar el pedido al importador de chile seco y de masa, con su plazo: ______ días',
         'Almacén', 'Encargado', '10:00'),
        ('Comparar precios de cerdo y de res con al menos dos proveedores',
         'Oficina', 'Encargado', '10:15'),
        ('Revisar el estado de la recepción y la documentación del último pedido de importación',
         'Almacén', 'Encargado', '10:30'),
        ('Hacer inventario de bebida, mezcal y tequila',
         'Almacén', 'Encargado', '10:45'),
    ]),
    ('COSTES', [
        ('Revisar el escandallo (costeo) de los 5 tacos más vendidos de la semana',
         'Oficina', 'Encargado', '11:00'),
        ('Comparar la merma semanal del trompo con la semana anterior',
         'Oficina', 'Encargado', '11:15'),
        ('Revisar el gasto de la barra de salsas frente a la venta de la semana',
         'Oficina', 'Encargado', '11:30'),
    ]),
    ('EQUIPO', [
        ('Planificar los turnos de la semana siguiente',
         'Oficina', 'Encargado', '11:45'),
        ('Cerrar y firmar el registro de jornada (obligatorio; en el soporte que exija la normativa vigente)',
         'Oficina', 'Encargado', '12:00'),
        ('Dar 15 minutos de formación al equipo y anotar el tema tratado',
         'Sala', 'Encargado', '12:15'),
    ]),
]

# --- 06 · 06-tareas-perfiles.xlsx ------------------------------------------

SEC_TAQUERO_DEL_TROMPO = [
    ('MONTAJE Y SONDA', [
        ('Comprobar el cono del trompo (asador vertical) recibido: ≤ −18 °C si congelado, ≤ 4 °C si refrigerado',
         'Cocina', 'Taquero', '10:30'),
        ('Montar el trompo del día: capas, grasa, piña y cebolla, y anotar el peso total',
         'Cocina', 'Taquero', '10:45'),
        ('Sondar la capa exterior antes de cada tanda de corte y anotar la lectura: ____ °C',
         'Cocina', 'Taquero', '13:00'),
        ('Registrar la sonda al inicio y a mitad del servicio, como mínimo',
         'Cocina', 'Taquero', '13:15'),
    ]),
    ('CORTE Y LIMPIEZA', [
        ('Cortar sólo la capa cocinada del trompo; no rebanar hacia el interior todavía crudo',
         'Cocina', 'Taquero', '13:30'),
        ('Pasar a mantenimiento ≥ 63 °C la carne cortada que no se sirve al momento',
         'Cocina', 'Taquero', '14:00'),
        ('Limpiar cuchillo y tabla del trompo antes de tocar producto listo para consumo',
         'Cocina', 'Taquero', '20:00'),
        ('Vaciar, lavar y desinfectar la bandeja de grasas del trompo al cierre',
         'Cocina', 'Taquero', '23:30'),
    ]),
]

SEC_TORTILLERIA = [
    ('NIXTAMAL Y MOLIENDA', [
        ('Pesar el maíz y la cal del nixtamal y anotar la hora de inicio de la cocción',
         'Tortillería', 'Tortillero/a', '06:00'),
        ('Desinfectar el molino de la tortillería (obrador de tortilla de maíz) antes de moler',
         'Tortillería', 'Tortillero/a', '06:30'),
        ('Anotar la hora de molienda y la temperatura de conservación de la masa',
         'Tortillería', 'Tortillero/a', '07:00'),
        ('Anotar la hora límite de la masa definida en tu APPCC (HACCP): ______',
         'Tortillería', 'Tortillero/a', '07:15'),
    ]),
    ('PRENSADO Y COMAL', [
        ('Calibrar la tortilladora al arranque: grosor y peso por pieza',
         'Tortillería', 'Tortillero/a', '09:00'),
        ('Anotar las mermas de tortilla por turno y su causa',
         'Tortillería', 'Tortillero/a', '13:00'),
        ('Comprobar que la tortilla de harina se almacena separada de la de maíz',
         'Tortillería', 'Tortillero/a', '13:15'),
        ('Limpiar a fondo la tortilladora al cierre y dejarla seca',
         'Tortillería', 'Tortillero/a', '23:30'),
    ]),
]

SEC_SALSAS = [
    ('SALSAS Y BARRA', [
        ('Asignar al salsero/a (responsable de salsas) la molienda y el etiquetado de las salsas del día',
         'Barra', 'Salsero/a', '09:00'),
        ('Tostar y moler los chiles del día y anotar la cantidad',
         'Barra', 'Salsero/a', '09:15'),
        ('Elaborar las salsas cocidas y etiquetarlas con fecha y hora de elaboración',
         'Barra', 'Salsero/a', '09:30'),
        ('Montar la barra y comprobar ≤ 4 °C en las salsas crudas',
         'Barra', 'Salsero/a', '10:45'),
    ]),
    ('ALÉRGENOS Y LIMPIEZA', [
        ('Marcar la salsa macha (cacahuete y/o sésamo) en el cartel y separarla físicamente del resto',
         'Barra', 'Salsero/a', '10:50'),
        ('Reponer por tandas en recipiente limpio; nunca rellenar sobre el resto anterior',
         'Barra', 'Salsero/a', '12:00'),
        ('Descartar las salsas crudas al cierre y anotar la merma',
         'Barra', 'Salsero/a', '23:30'),
        ('Limpiar y desinfectar licuadora y molcajete entre salsas distintas',
         'Barra', 'Salsero/a', '23:45'),
    ]),
]

SEC_PLANCHA_Y_FREIDORA = [
    ('PLANCHA', [
        ('Calibrar la plancha por zonas al arranque y anotar la temperatura de trabajo',
         'Cocina', 'Plancha', '10:45'),
        ('Dorar los tacos y quesadillas a la plancha vigilando que no se quemen',
         'Cocina', 'Plancha', '13:00'),
        ('Rascar y engrasar la plancha entre tandas de servicio',
         'Cocina', 'Plancha', '15:00'),
        ('Rascar y engrasar la plancha en caliente al cierre',
         'Cocina', 'Plancha', '23:40'),
    ]),
    ('FREIDORA Y SEPARACIÓN', [
        ('Comprobar el punto de humo del aceite antes del servicio y anotar la incidencia',
         'Cocina', 'Plancha', '10:50'),
        ('Usar pinzas y cesta distintas para la tortilla de harina y la de maíz',
         'Cocina', 'Plancha', '13:15'),
        ('Filtrar el aceite de la freidora al cierre y anotar la fecha del último cambio',
         'Cocina', 'Plancha', '23:45'),
        ('Registrar las mermas de totopos y tortilla frita por turno',
         'Cocina', 'Plancha', '23:50'),
    ]),
]

SEC_MOSTRADOR_Y_CAJA = [
    ('COMANDA Y ALÉRGENOS', [
        ('Preguntar por alergias e intolerancias antes de cerrar cada comanda',
         'Mostrador', 'Mostrador', '11:30'),
        ('Dar la información de alérgenos por escrito cuando el cliente la pida',
         'Mostrador', 'Mostrador', '11:45'),
        ('Avisar en cocina si un pedido lleva salsa macha (cacahuete y/o sésamo) aparte',
         'Mostrador', 'Mostrador', '12:00'),
        ('Repetir la comanda al cliente antes de cobrar',
         'Mostrador', 'Mostrador', '12:15'),
    ]),
    ('COBRO Y DELIVERY', [
        ('Cobrar y entregar el ticket con el desglose correcto',
         'Mostrador', 'Mostrador', '12:30'),
        ('Gestionar la cola en hora punta y avisar a cocina si se satura',
         'Mostrador', 'Mostrador', '14:00'),
        ('Comprobar que el pedido de delivery sale sellado y con el ticket correcto',
         'Mostrador', 'Mostrador', '20:00'),
        ('Registrar las incidencias de cobro y de delivery del turno',
         'Mostrador', 'Mostrador', '00:05'),
    ]),
]

SEC_REPARTO_Y_DELIVERY = [
    ('PREPARACIÓN Y SELLADO (SI APLICA)', [
        ('Sellar cada pedido de delivery con el precinto de garantía',
         'Delivery', 'Repartidor', '12:00'),
        ('Comprobar que el pedido lleva los cubiertos y las salsas solicitadas',
         'Delivery', 'Repartidor', '12:15'),
        ('Medir la temperatura de salida del pedido caliente antes de entregarlo al repartidor',
         'Delivery', 'Repartidor', '13:00'),
        ('Anotar la hora de salida y la hora estimada de entrega de cada pedido',
         'Delivery', 'Repartidor', '13:10'),
    ]),
    ('TIEMPOS Y TEMPERATURA', [
        ('Registrar el tiempo real de entrega frente al estimado',
         'Delivery', 'Repartidor', '14:00'),
        ('Avisar a mostrador si un pedido supera el tiempo máximo de entrega',
         'Delivery', 'Repartidor', '14:15'),
        ('Registrar cualquier incidencia de reparto: devolución, retraso o reclamación',
         'Delivery', 'Repartidor', '20:00'),
        ('Revisar el estado de las bolsas térmicas y sustituir las dañadas',
         'Delivery', 'Repartidor', '23:30'),
    ]),
]

# --- 07 · 07-semanales-mensuales.xlsx --------------------------------------

SEC_TAREAS_SEMANALES = [
    ('LIMPIEZA PROFUNDA', [
        ('Desengrasar a fondo el trompo (asador vertical) y la campana extractora',
         'Cocina', 'Taquero', 'Lunes'),
        ('Afilar los cuchillos de corte y registrar la fecha',
         'Cocina', 'Taquero', 'Lunes'),
        ('Limpiar a fondo el molino y la tortilladora, con desmontaje completo',
         'Tortillería', 'Tortillero/a', 'Martes'),
        ('Limpiar a fondo la freidora y cambiar el aceite',
         'Cocina', 'Plancha', 'Miércoles'),
        ('Desinfectar a fondo la barra de salsas y sus utensilios',
         'Barra', 'Salsero/a', 'Jueves'),
    ]),
    ('INVENTARIO Y ALMACÉN', [
        ('Hacer inventario de chiles secos y revisar el control de plagas del almacén seco',
         'Almacén', 'Encargado', 'Viernes'),
        ('Revisar la caducidad de los productos en cámara y descartar lo caducado',
         'Cámara', 'Encargado', 'Viernes'),
        ('Contar el stock de tortilla comprada y de envases de delivery',
         'Almacén', 'Mostrador', 'Sábado'),
        ('Revisar el inventario de mezcal y tequila de la semana',
         'Almacén', 'Encargado', 'Sábado'),
        ('Comprobar el estado de las bolsas térmicas y del material de reparto',
         'Delivery', 'Repartidor', 'Domingo'),
    ]),
    ('EQUIPO', [
        ('Dar 15 minutos de formación al equipo y anotar el tema tratado',
         'Sala', 'Encargado', 'Lunes'),
        ('Revisar el escandallo (costeo) de los 5 tacos más vendidos de la semana',
         'Oficina', 'Encargado', 'Martes'),
        ('Responder las reseñas acumuladas de la semana',
         'Oficina', 'Encargado', 'Miércoles'),
        ('Repasar con el equipo las incidencias de la semana antes del fin de semana',
         'Sala', 'Todo el equipo', 'Viernes'),
    ]),
]

SEC_TAREAS_MENSUALES = [
    ('INSTALACIONES', [
        ('Revisar la instalación de gas del trompo (asador vertical) y del comal, y archivar el parte',
         'Cocina', 'Encargado', '1º de mes'),
        ('Calibrar las sondas y los termómetros y anotar la desviación medida',
         'Cocina', 'Encargado', 'Quincenal'),
        ('Limpiar los filtros de extracción y registrar la fecha y el responsable',
         'Cocina', 'Encargado', 'Quincenal'),
        ('Revisar el sistema de gas y la campana extractora de la tortillería (obrador de tortilla de maíz)',
         'Tortillería', 'Encargado', 'Mensual'),
    ]),
    ('APPCC Y DOCUMENTACIÓN', [
        ('Revisar el plan APPCC (HACCP) y las fichas de alérgenos',
         'Oficina', 'Encargado', 'Mensual'),
        ('Archivar las hojas de temperaturas del mes y comprobar que están firmadas',
         'Oficina', 'Encargado', '1º de mes'),
        ('Revisar el registro de jornada (obligatorio; en el soporte que exija la normativa vigente) del mes',
         'Oficina', 'Encargado', 'Fin de mes'),
        ('Comprobar que la ficha de alérgenos de las salsas y de los guisados (cazuelas de relleno) está actualizada',
         'Oficina', 'Encargado', 'Mensual'),
    ]),
    ('PROVEEDORES', [
        ('Auditar a los proveedores de importación: plazos, incidencias y documentación',
         'Oficina', 'Encargado', 'Fin de mes'),
        ('Comparar precios de cerdo, de res y de chile seco con el mes anterior',
         'Oficina', 'Encargado', 'Fin de mes'),
        ('Revisar el escandallo (costeo) mensual del taco al pastor y de los guisados',
         'Oficina', 'Encargado', 'Fin de mes'),
        ('Cerrar el inventario mensual de bebida, mezcal y tequila',
         'Almacén', 'Encargado', 'Fin de mes'),
    ]),
]

# --- 08 · 08-eventos-estacionales.xlsx -------------------------------------

SEC_TEMPORADAS_Y_PRODUCTO = [
    ('CHILES EN NOGADA (15-JUL A FIN DE SEP)', [
        ('Reservar con el importador la nuez de Castilla y la granada para los chiles en nogada',
         'Almacén', 'Encargado', '1 mes antes'),
        ('Anotar el inicio real de la temporada de chiles en nogada, que depende de la cosecha',
         'Oficina', 'Encargado', 'Al confirmar'),
        ('Revisar la disponibilidad de manzana panochera, pera lechera y durazno criollo',
         'Almacén', 'Encargado', '2 semanas antes'),
    ]),
    ('CHILE SECO POR CAMPAÑA', [
        ('Anotar la campaña y el lote de cada chile seco recibido',
         'Almacén', 'Encargado', 'Al confirmar'),
        ('Comparar precio del chile seco de la campaña con la anterior antes de renovar el pedido',
         'Oficina', 'Encargado', '2 semanas antes'),
        ('Revisar el estado de conservación del chile seco almacenado',
         'Almacén', 'Encargado', 'Al confirmar'),
    ]),
    ('CARNE Y MAÍZ', [
        ('Comprobar el precio del cerdo para pastor frente al de la campaña anterior',
         'Oficina', 'Encargado', '2 semanas antes'),
        ('Revisar el precio y la disponibilidad del maíz para nixtamal antes de renovar el pedido',
         'Almacén', 'Encargado', '2 semanas antes'),
        ('Comparar precios de res con al menos dos proveedores del trimestre',
         'Oficina', 'Encargado', '1 mes antes'),
    ]),
    ('PRODUCTO FRESCO', [
        ('Revisar precio y disponibilidad del aguacate antes de fijar la carta del trimestre',
         'Oficina', 'Encargado', '2 semanas antes'),
        ('Comprobar la disponibilidad de cilantro y limón de temporada con el proveedor',
         'Almacén', 'Encargado', 'Víspera'),
        ('Revisar la disponibilidad de chile fresco de temporada antes de ajustar la carta',
         'Almacén', 'Encargado', 'Víspera'),
    ]),
]

SEC_CALENDARIO_DE_EVENTOS = [
    ('PRIMER TRIMESTRE', [
        ('Día de Reyes (6 de enero): previsión de rosca y de turno reforzado',
         'MX', 'Encargado', '2 semanas antes'),
        ('Candelaria (2 de febrero): producción de tamales y comunicación en redes',
         'MX', 'Encargado', '2 semanas antes'),
        ('Cuaresma y Vigilia: reforzar tacos de pescado y capeados; activar el registro de congelación',
         'Todos', 'Encargado', 'Al confirmar'),
        ('Semana Santa: revisar el aforo y la previsión con el equipo de sala',
         'ES', 'Encargado', '1 semana antes'),
    ]),
    ('SEGUNDO TRIMESTRE', [
        ('Cinco de Mayo (5 de mayo): campaña sobre todo para EE. UU.; en México se celebra en Puebla',
         'US-es', 'Encargado', '1 semana antes'),
        ('Terrazas de verano: revisar el aforo y el horario ampliado',
         'ES', 'Encargado', '2 semanas antes'),
        ('Inicio de verano: comprobar la previsión de reservas y de grupos',
         'ES', 'Encargado', '1 semana antes'),
        ('Verano: revisar la disponibilidad del aguacate y del chile fresco',
         'Todos', 'Encargado', '2 semanas antes'),
    ]),
    ('TERCER TRIMESTRE', [
        ('Grito e Independencia (15 y 16 de septiembre): pico del año fuera de México; pozole y mezcal',
         'US-es', 'Encargado', '2 semanas antes'),
        ('Chiles en Nogada (15 de julio a fin de septiembre): activar la campaña con el importador',
         'MX', 'Encargado', '1 mes antes'),
        ('Temporada alta de verano: revisar la previsión de personal',
         'Todos', 'Encargado', '2 semanas antes'),
    ]),
    ('CUARTO TRIMESTRE', [
        ('Día de Muertos (1 y 2 de noviembre): pan de muerto y calabaza en tacha',
         'MX', 'Encargado', '2 semanas antes'),
        ('Virgen de Guadalupe (12 de diciembre): previsión de servicio y de personal',
         'MX', 'Encargado', '2 semanas antes'),
        ('Posadas (16 a 24 de diciembre) y comidas de empresa: cerrar aforos y menús cerrados',
         'Todos', 'Encargado', '1 mes antes'),
    ]),
]

# --- Diccionario expuesto: clave = nombre EXACTO de la hoja ---------------

SEC = {
    'Tareas Diarias Manager': SEC_TAREAS_DIARIAS_MANAGER,
    'Tareas Semanales Manager': SEC_TAREAS_SEMANALES_MANAGER,
    'Taquero del Trompo': SEC_TAQUERO_DEL_TROMPO,
    'Tortillería': SEC_TORTILLERIA,
    'Salsas': SEC_SALSAS,
    'Plancha y Freidora': SEC_PLANCHA_Y_FREIDORA,
    'Mostrador y Caja': SEC_MOSTRADOR_Y_CAJA,
    'Reparto y Delivery': SEC_REPARTO_Y_DELIVERY,
    'Tareas Semanales': SEC_TAREAS_SEMANALES,
    'Tareas Mensuales': SEC_TAREAS_MENSUALES,
    'Temporadas y Producto': SEC_TEMPORADAS_Y_PRODUCTO,
    'Calendario de Eventos': SEC_CALENDARIO_DE_EVENTOS,
}

# --- 09 · 09-plantilla-personalizable.xlsx ---------------------------------

PLANTILLA_SECCIONES = [
    'SECCIÓN 1 (PERSONALIZAR)',
    'SECCIÓN 2 (PERSONALIZAR)',
    'SECCIÓN 3 (PERSONALIZAR)',
]

# --- BONUS-01 · BONUS-01-briefing-servicio.xlsx ----------------------------

BRIEFING_BLOQUES = [
    ('TROMPO DEL DÍA (SI APLICA)', [
        'Peso montado (kg):',
        'Hora de montaje:',
        'Hora límite definida en tu APPCC (HACCP):',
        'Previsión de cortes:',
    ]),
    ('GUISADOS DEL DÍA', [
        'Guisado 1 (cazuela de relleno) — hora de entrada / hora límite:',
        'Guisado 2 — hora de entrada / hora límite:',
        'Guisado 3 — hora de entrada / hora límite:',
        'Guisado 4 — hora de entrada / hora límite:',
    ]),
    ('SALSAS DEL DÍA', [
        'Salsa 1 (picante: suave / medio / alto):',
        'Salsa 2 (picante: suave / medio / alto):',
        'Salsa 3 (picante: suave / medio / alto):',
        'Salsa 4 (picante: suave / medio / alto):',
        'Salsa 5 (picante: suave / medio / alto):',
    ]),
    ('AVISO DE ALÉRGENOS', [
        'Salsa macha en barra (cacahuete y/o sésamo) — sí/no:',
        'Mole del día (frutos de cáscara) — sí/no:',
        'Tortilla de harina disponible (gluten) — sí/no:',
    ]),
    ('ROTURAS Y «86»', [
        'Sin (producto 1):',
        'Sin (producto 2):',
        'Sin (producto 3):',
        'Sin (producto 4):',
        'Sin (producto 5):',
    ]),
    ('SALA Y DELIVERY', [
        'Reservas:',
        'Grupos:',
        'Previsión de delivery:',
        'Personal del turno:',
    ]),
]

# --- BONUS-02 · BONUS-02-calendario-anual.xlsx -----------------------------

CALENDARIO_FILAS = [
    ('Enero', '6 Ene — Día de Reyes',
     'Previsión de rosca y turno reforzado en la fecha', '2 semanas'),
    ('Enero', 'Cierre de vacaciones del equipo',
     'Revisar el calendario de vacaciones y el turno de cierre por descanso', '1 mes'),
    ('Febrero', '2 Feb — Candelaria',
     'Producción de tamales; comunicarlo en Google Business Profile y en redes', '2 semanas'),
    ('Febrero', 'Revisión de instalación de gas',
     'Revisar la instalación de gas del trompo (asador vertical) y del comal, y archivar el parte', '1 mes'),
    ('Marzo-Abril', 'Cuaresma y Vigilia (variable)',
     'Reforzar tacos de pescado y capeados; activar el registro de congelación de crudos', '2 semanas'),
    ('Marzo', 'Calibración de sondas',
     'Calibrar las sondas y los termómetros y anotar la desviación medida', '2 semanas'),
    ('Marzo', 'Revisión de escandallo de temporada',
     'Revisar el escandallo (costeo) de los tacos más vendidos antes de la primavera', '2 semanas'),
    ('Abril', 'Limpieza a fondo del molino',
     'Desmontar y limpiar a fondo el molino y la tortilladora antes del verano', '2 semanas'),
    ('Mayo', '5 Mayo — Cinco de Mayo (EE. UU.; Puebla, México)',
     'Campaña sobre todo para EE. UU.; en México se celebra en Puebla', '1 semana'),
    ('Mayo', 'Previsión de terrazas de verano',
     'Ampliar horario y revisar el aforo autorizado antes del verano', '2 semanas'),
    ('Junio', 'Inicio de terrazas de verano',
     'Reforzar personal de sala y de delivery para el verano', '1 semana'),
    ('Junio', 'Revisión de reseñas',
     'Revisar y responder las reseñas acumuladas antes de la temporada alta', '1 semana'),
    ('Junio', 'Auditoría de proveedores de importación',
     'Auditar plazos, incidencias y documentación del importador de chile seco y masa', '1 mes'),
    ('Julio-Septiembre', '15 Jul a fin de Sep — Chiles en Nogada',
     'Reservar con el importador la nuez de Castilla y la granada; depende de la cosecha', '1 mes'),
    ('Julio', 'Revisión de precio del aguacate',
     'Revisar precio y disponibilidad del aguacate antes de fijar la carta del trimestre', '2 semanas'),
    ('Agosto', 'Pico de Chiles en Nogada',
     'Mes de mayor disponibilidad; reforzar producción y comunicarlo en redes', '1 semana'),
    ('Agosto', 'Revisión de control de plagas',
     'Revisar el control de plagas del almacén seco en el mes de más calor', '2 semanas'),
    ('Septiembre', '15-16 Sep — Grito e Independencia',
     'Pico del año fuera de México; reforzar pozole y mezcal', '2 semanas'),
    ('Septiembre', 'Revisión del plan APPCC',
     'Revisar el plan APPCC (HACCP) y las fichas de alérgenos antes del otoño', '1 mes'),
    ('Octubre', 'Previsión de Día de Muertos',
     'Encargar pan de muerto y calabaza con antelación al proveedor', '1 mes'),
    ('Octubre', 'Limpieza de filtros de extracción',
     'Limpiar los filtros de extracción y registrar la fecha y el responsable', '2 semanas'),
    ('Noviembre', '1-2 Nov — Día de Muertos',
     'Producción de pan de muerto y calabaza en tacha', '2 semanas'),
    ('Noviembre', 'Previsión de comidas de empresa',
     'Cerrar menús y aforos para las comidas de empresa de diciembre', '1 mes'),
    ('Noviembre', 'Inventario de mezcal y tequila',
     'Hacer inventario de bebida, mezcal y tequila antes de la campaña de diciembre', '2 semanas'),
    ('Diciembre', '12 Dic — Virgen de Guadalupe',
     'Previsión de servicio y de personal reforzado', '2 semanas'),
    ('Diciembre', '16-24 Dic — Posadas y comidas de empresa',
     'Cerrar aforos y menús cerrados', '1 mes'),
    ('Diciembre', 'Navidad y Nochevieja',
     'Reforzar turnos de cierre y la previsión de delivery de fin de año', '2 semanas'),
]
