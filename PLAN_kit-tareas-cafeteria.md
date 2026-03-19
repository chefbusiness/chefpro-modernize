# Kit de Tareas Recurrentes: Cafetería / Brunch — Product Plan

## Product Definition
- **Name**: Kit de Tareas Recurrentes: Cafetería / Brunch
- **Slug**: `kit-tareas-cafeteria`
- **Format**: kit (Excel templates)
- **Price**: €12 (launch) / ~~€39~~ (strikethrough) → -69%
- **Audience**: Dueños, encargados y baristas de cafeterías, brunch spots, coffee shops
- **Problem**: Una cafetería tiene tareas muy distintas a un restaurante: máquina de espresso, vitrina de pastelería, preparación de brunch, terraza de mañana. Sin checklists adaptados, se olvidan tareas críticas (purgar grupo, rotar vitrina, preparar toppings).
- **Tagline**: "Todas las tareas de tu cafetería, organizadas por turno, área y perfil — listas para imprimir"
- **Base**: Adaptación de Restaurante Casual con tareas específicas de cafetería/brunch

## Deliverables (9 archivos Excel)

### 01-apertura-cierre.xlsx (6 pestañas)
- **Apertura Cocina** — encender horno, plancha; mise en place brunch; montar bowls/toppings
- **Apertura Sala/Terraza** — montar mesas café, pizarra menú, terraza (sombrillas, macetas)
- **Apertura Barra Café** — purgar grupo espresso, calibrar molienda, stock leches, toppings
- **Cierre Cocina** — limpiar plancha, guardar prep brunch, FIFO ingredientes frescos
- **Cierre Sala/Terraza** — recoger terraza, limpiar mesas, cuadrar caja
- **Cierre Barra Café** — backflush máquina, limpiar molinillo, stock leches mañana

### 02-partidas-cocina.xlsx (3 pestañas)
- **Calientes** — plancha (tostadas, huevos, pancakes), horno (quiches, croissants)
- **Fríos** — açaí bowls, ensaladas, smashed avocado, overnight oats
- **Pastelería / Vitrina** — reponer vitrina, etiquetar alérgenos, rotar producto, temp vitrina

### 03-tareas-manager.xlsx (4 pestañas)
- **Diario Manager** — revisar reservas brunch, check stock café/leches, briefing equipo
- **Semanal Manager** — pedido café/leche, inventario pastelería, revisión RRSS, limpieza profunda
- **Mensual Manager** — P&L, evaluar personal, mantenimiento máquina espresso, carta estacional
- **Handover Turno** — checklist traspaso turno mañana/tarde

### 04-tareas-perfiles.xlsx (5 pestañas)
- **Encargado/a** — supervisión apertura, caja, gestión equipo, cierre
- **Barista** — calibrar espresso, latte art prep, stock leches vegetales, limpieza máquina
- **Pastelero/a** — producción matutina, vitrina, alérgenos, stock masa/bollería
- **Camarero/a** — montar mesas, tomar comandas, servicio brunch, recoger
- **Auxiliar / Runner** — office, reposición servilletas/cubiertos, apoyo barra/sala

### 05-tareas-semanales-mensuales.xlsx (5 pestañas)
- **Inventario Diario Partida** — stock inmediato para trabajar hoy: café en grano (kg), leches por tipo (L), cacao, siropes, bollería vitrina, pan, mantequilla, huevos, aguacate, fruta fresca. Lo hace el barista/cocinero al inicio del turno.
- **Inventario Semanal Almacén** — conteo completo por rubro: café (variedades/orígenes), lácteos, panadería, pastelería, frescos, secos, bebidas, packaging (vasos take-away, tapas, bolsas, servilletas). Lo hace el encargado/manager.
- **Limpieza Semanal** — campana, vitrina interior, cámaras, cristales, suelos, baños
- **FIFO Semanal** — cámaras, pastelería, lácteos, fruta, pan
- **Mantenimiento Mensual** — máquina espresso (descalcificar), molinillo, horno, lavavajillas

### 06-eventos-festivos.xlsx (4 pestañas)
- **Brunch Dominical Especial** — prep extra, carta ampliada, decoración, refuerzo personal
- **San Valentín** — desayuno especial parejas, decoración, menú brunch temático
- **Navidad** — carta navideña, stock panettone/turrón, decoración, horarios especiales
- **Temporada Terraza** — montaje primavera, sombrillas, plantas, carta terraza

### 07-plantilla-personalizable.xlsx (3 pestañas) — REUSAR de base
### BONUS-01-briefing-servicio.xlsx — REUSAR de base
### BONUS-02-calendario-anual-tareas.xlsx — REUSAR de base

## Technical Setup
- Stripe: "Kit de Tareas Recurrentes: Cafetería / Brunch — AI Chef Pro" — €12
- Routes: /kit-tareas-cafeteria, /kit-tareas-cafeteria-access, /kit-tareas-cafeteria-library
- Env vars: VITE_STRIPE_PAYMENT_LINK_TAREAS_CAFETERIA, KIT_TAREAS_CAFETERIA_URLS
- JWT storage key: 'kit-tareas-cafeteria-jwt'

## SEO Keywords
Primary: "checklist cafetería", "tareas apertura cafetería", "checklist barista"
Secondary: "tareas brunch restaurante", "checklist cierre cafetería", "lista tareas coffee shop"
Long-tail: "plantilla excel tareas cafetería", "checklist apertura cierre cafetería brunch"
