# Glosario de jerga hostelera ES → EN (US) — documento vivo

> Nace el 13-oct-2026 (sesión Claude Code) por instrucción de John: «la clave está en dar con cómo se usa o se maneja la
> jerga profesional en el inglés con respecto al español». Lo consulta **todo** trabajo en inglés: productos (F1, SPEC,
> redactores, revisión), landings, hub y blog. Cada producto nuevo añade aquí sus términos (el research de su F1 lleva
> una sección «Jerga profesional» con fuente).

## Reglas

1. **Tres capas a la vez**: (1) producto (nombre, slug, ficheros, pestañas, rótulos) · (2) contenido de los entregables ·
   (3) SEO de la landing (title, H1, meta, H2, FAQ en la redacción del comprador, alt, keywords).
2. **Los nombres comerciales, de producto y de marca ya publicados NO se cambian** (Gastro Pro Prompts, «Kit Pro», AI
   Chef Pro, los nombres de los agentes…). La keyword US va como descriptor: en title y H1, el nombre primero y la
   keyword detrás de los dos puntos. Si un nombre ES da en inglés un **calco** que el profesional US no usa, se
   **propone a John caso a caso** con el dato que lo sostiene; el nombre de un producto EN se decide al nacer.
3. **US por defecto** (el mercado de la tienda EN). Los términos UK solo en las notas UK de los entregables.
4. **El volumen no basta**: confirmar la intención con la SERP (p. ej., «kitchen cleaning checklist» es limpieza
   doméstica). Medir con `scripts/dataforseo.py … --pais 2840 --idioma en`.
5. **Estado** de cada fila: **firme** (lo dijo John o está medido y aplicado) · **propuesto** (pendiente de John) ·
   **por verificar** (uso común del sector, sin medir; verificar antes de usarlo en un nombre o en un title).

## Cocina, sala y oficio

| ES | ✗ Calco que NO se usa | ✓ US | Estado y fuente |
|---|---|---|---|
| cocina creativa | creative kitchen | **creative cuisine**; en alta cocina, **avant-garde cuisine** | firme: John, 13-oct. El agente EN se llama «Avant-garde Cuisine» (`agentes-en.json`) |
| obrador (pastelería, panadería, chocolatería) | workshop | según el oficio: **pastry kitchen** · **production bakery / wholesale bakery** · **chocolatier / chocolate kitchen**; central de varias unidades = **commissary kitchen** | propuesto (auditoría 13-oct) |
| dark kitchen | — | **ghost kitchen** (33.100/mes frente a 1.900) | firme (medido); los nombres de producto publicados siguen como están |
| showcooking | showcooking | **live cooking** / **in-home dining** (chef privado) | propuesto |
| gastrobar | gastrobar | **gastropub** | propuesto |
| hotel completo | full hotel | **full-service hotel** | propuesto |
| asador / horno Josper | Josper grill | **steakhouse** · **charcoal grill** (Josper es una marca) | propuesto |
| tareas recurrentes (kit de tareas) | recurring tasks | **opening, closing & cleaning checklists** · **side work** | firme: producto EN «Restaurant Checklists Kit Pro» (F1 17-oct, `checklists-kit/SPEC.md` D2; DataForSEO US: restaurant opening checklist 260, restaurant cleaning checklist 260, kitchen checklist 210) |
| escandallo | escandallo / recipe scaling | **recipe costing** · **plate cost**; en bar dry hire, **cost per guest** | firme (Food Cost Kit, mobile bar §9) |
| semáforo (indicador) | traffic light | **color-coded status** / **status flag** | por verificar (auditoría 13-oct, capa 2) |
| materias primas (en el P&L) | raw materials | **food & beverage costs** / **COGS** | por verificar (auditoría 13-oct, capa 2) |
| primer plato / segundo | starter / main (UK) | **appetizer / entrée** | por verificar (auditoría, pestañas del Food Cost) |
| margen bruto % (UK «GP %») | GP % | **food cost %** / **gross margin %** | por verificar |

## Gestión y legal

| ES | ✗ | ✓ US | Estado y fuente |
|---|---|---|---|
| cuadrante de turnos | staff rota (UK) | **employee schedule** · **work schedule** (5.400/mes frente a 10) | firme (PR #126) |
| inventario / recuento | stock take (UK) | **inventory count** · **inventory spreadsheet** · **par sheet** | firme (PR #126) |
| registros APPCC | food safety logs (50/mes) | **temperature logs** · **HACCP plan template** | firme (PR #126) |
| autónomo | freelancer | **sole proprietor** · **single-member LLC** | firme (business plans EN) |
| bartender/camarero freelance | freelance | **W-2 event staff**; 1099 = riesgo de mala clasificación (FLSA, CA AB5) | firme (catering y mobile bar EN) |
| licencia de actividad | activity license | **business license** (ciudad/condado) + **sales tax permit** | firme (mobile bar §9) |
| IVA | VAT | **sales tax** (VAT solo en la nota UK) | firme |
| señal / fianza | — | **deposit** | firme (mobile bar §9) |
| convenio colectivo | collective agreement | no hay equivalente general en US: **FLSA + leyes estatales** | firme (PR #126, testimonios) |
| cuota patronal de Seguridad Social | social security contribution | **payroll taxes** (FICA, FUTA/SUTA) | firme (Staff Kit EN) |

## Checklists de cocina, sala y caja (Restaurant Checklists Kit Pro, F1 17-oct-2026; detalle en `checklists-kit/F1-inventario-es.md` §4)

| ES | ✗ Calco que NO se usa | ✓ US | Estado y fuente |
|---|---|---|---|
| partida (de cocina) · jefe/chef de partida | section · section chef | **station** · **lead line cook** (en alta cocina, *chef de partie*) | por verificar (uso común; la jerga del kit EN la fija `mapas.GLOSARIO`) |
| cocinero · auxiliar de cocina · personal de limpieza | cook assistant · cleaning staff | **line cook** · **prep cook** · **porter** (dishwasher si friega) | por verificar |
| encargado (de turno) | manager in charge | **shift manager** · **MOD** (manager on duty); el responsable sanitario del turno = **person in charge (PIC)**, FDA Food Code 2-101.11 | PIC firme (Food Code); resto por verificar |
| tareas de apoyo del camarero | support tasks | **side work** (590/mes, a la baja; *side work checklist* 30) | firme (DataForSEO 17-oct) |
| briefing de servicio | briefing | **pre-shift meeting** · **line-up** | por verificar |
| comanda · pase | command · pass | **ticket** · **the pass** / **expo** | por verificar |
| baño maría · plancha · cámara | bain-marie · plancha · chamber | **steam table** · **flat-top (griddle)** · **walk-in cooler / walk-in freezer** | por verificar |
| terraza · licencia de terraza | terrace · terrace license | **patio** · **outdoor dining / sidewalk café permit** (ciudad) | por verificar |
| etiquetar y fechar | label and date | **date marking** (7 días a 41 °F, día 1 = preparación) | firme: FDA Food Code 2022 §3-501.17 |
| mermas | shrinkage (eso es robo/pérdida de inventario) | **waste** · **waste log** | por verificar |
| arqueo · fondo de caja · cajón | arching · cash fund | **cash count / cashing out** · **starting bank** (UK **float**) · **cash drawer** (UK **till**) | por verificar |
| TPV · datáfono · lectura Z | TPV · dataphone · Z reading | **POS** · **card terminal** · **Z report** (X report a mitad de turno) | por verificar |
| cerrar el lote de tarjetas | close the lot | **batch out / settle** the card terminal | por verificar |
| descuadre · medios de pago | mismatch · payment means | **over/short** · **tenders** | por verificar |
| vales · invitaciones | vouchers · invitations | **gift cards** · **comps** (descuento, no medio de pago) | por verificar |
| firma (en cada tarea del checklist) | signature | **initials** (la firma va al pie: «Verified by / Signature») | por verificar |
| hora límite · responsable (columna) | limit hour · responsible | **due by** · **assigned to** | por verificar |
| gestor de aceite usado · separador de grasas | authorized manager · grease separator | **used cooking oil recycler** (renderer) · **grease trap / interceptor** (ordenanza **FOG** local) | por verificar |
| DDD (control de plagas) | DDD | **pest control** por **licensed operator (PCO)** | por verificar |
| extintores + BIE · limpieza de campana | fire hose cabinet | **fire extinguishers** + **hood fire suppression system** (cada 6 meses, NFPA 96) · **hood cleaning** (NFPA 96) | firme: NFPA 96 / OSHA 1910.157 (SPEC §3) |
| frigorista | refrigerist | **refrigeration tech** (certificado **EPA 608**) | firme: 40 CFR 82 Subpart F |
| registro de jornada | workday register | **time-clock records / punches** (FLSA: 2 años; nóminas 3) | firme: 29 CFR 516.5-516.6 |
| Nochevieja · cotillón · uvas | New Year's night · cotillion | **New Year's Eve (NYE)** · **party favors** · (no hay uvas: **champagne toast**) | por verificar |
| menú del día | menu of the day | **lunch specials** | por verificar |
| UK (solo notas) | — | float · till · rota · takeaway · EHO · 8 °C / 63 °C · 14 allergens · Mothering Sunday · bank holidays · Boxing Day | por verificar (UK 8/63 °C: Food Safety and Hygiene (England) Regs 2013) |

## Bar y eventos (detalle y fuentes: `business-plans-en-5/F1-research-us-delta.md` §9)

coctelería para eventos → **mobile bar** (negocio) · barra móvil (mueble) → **portable bar** · el cliente pone el alcohol
→ **dry hire** (glosa SEGÚN QUIÉN LEE: para el cliente del bar, «you supply the alcohol»; en los entregables y la landing, que los lee el OPERADOR, «your client buys the alcohol; you bring the bar, the bartenders and everything else». Lo cazó la revisión final del Mobile Bar, 13-oct; «BYOB» solo como aclaración) · cóctel de autor → **signature cocktails**
(nunca «author cocktails») · experiencias temáticas → **specialty bars / themed bars** · barra de pago → **cash bar** ·
jefe de barra → **lead bartender** · ayudante → **barback** · certificado del seguro → **COI / additional insured** ·
requisitos de la sala → **venue requirements** · temporada alta de bodas → **peak wedding season**.

## Equivalencias por país (US · UK · CA · AU)

> 13-oct-2026 (sesión Claude Code, PR #126). Decisión de John: la tienda EN escribe en inglés US, y UK (2.º mercado en
> Search Console), Canadá y Australia se cubren **solo con una FAQ por landing** («Does it work in the UK, Canada or
> Australia?»), sin entregables nuevos. Esta tabla recoge lo que usan esas 12 FAQ. Las cifras provinciales o estatales
> no se publican; ante la duda, «check with your local council / province / state». «Firme» = fuente oficial abierta
> (URL); «por verificar» = uso común o dato citado en nuestros xlsx, sin abrir la fuente.

| Concepto | US (por defecto) | UK | Canadá | Australia | Estado y fuente |
|---|---|---|---|---|---|
| Impuesto sobre ventas | **sales tax** estatal + local, fuera del precio de carta | **VAT** 20 % estándar (5 % reducido; 0 % la mayoría de comida fría para llevar), dentro del precio | **GST** 5 % federal + **HST** o **PST** según provincia, fuera del precio | **GST** 10 %, dentro del precio | firme: gov.uk/vat-rates · canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html · business.gov.au/registrations/register-for-taxes/register-for-goods-and-services-tax-gst |
| Impuesto soportado | no recuperable (reventa exenta con *resale certificate*) | **VAT reclaim** si estás *VAT-registered* | **input tax credits** (GST/HST) | **GST credits** | por verificar (UK citado en los xlsx) |
| Número fiscal del negocio | **EIN** | **VAT number** | **business number (BN)** | **ABN** | por verificar |
| Inspección sanitaria | local/state **health department** (FDA Food Code adoptado) | **EHO** del council; FHRS 0-5 (FHIS en Escocia); marco FSA | **public health inspector** provincial o municipal (la CFIA es federal) | council + autoridad estatal; **FSANZ Food Standards Code** | por verificar (UK citado en los xlsx) |
| Responsable de seguridad alimentaria | **Certified Food Protection Manager** (p. ej. ServSafe) | sin certificado legal; **Level 2** habitual | certificación de *food handler* según provincia | **Food Safety Supervisor** certificado (Standard 3.2.2A, desde dic-2023, categorías 1 y 2) | AU firme: foodstandards.gov.au/business/food-safety/food-safety-supervisor · resto por verificar |
| Alérgenos | **9 major allergens** (FALCPA + FASTER) | **14 allergens** (FIR 2014) | **11 priority allergens** (Health Canada) | lista de FSANZ (PEAL) | CA firme: canada.ca/en/health-canada/services/food-allergies-intolerances/food-allergies.html · resto por verificar |
| Temperaturas | **°F** (41 °F frío, 135 °F caliente) | °C (por debajo de 8 °C frío, 63 °C o más caliente) | °C | °C | por verificar (UK citado en el xlsx HACCP) |
| Licencia de alcohol | **liquor license** (estado/ciudad) | **premises licence** + **personal licence** (Licensing Act 2003, Inglaterra y Gales) | **liquor licence** provincial | **liquor licence** estatal | UK firme: gov.uk/personal-licence-to-sell-alcohol · resto por verificar |
| Formación para servir alcohol | **TIPS** / ServSafe Alcohol (según estado) | titular de *personal licence* (APLH Level 2) | **Smart Serve** (Ontario) · **Serving It Right** (BC) | **RSA** | UK firme (misma URL) · CA/AU por verificar |
| Alcohol en un evento | *special/temporary event permit* | **Temporary Event Notice (TEN)** | permiso de evento provincial | permiso estatal | por verificar |
| Jornada y horas extra | **FLSA**: más de 40 h/semana a 1,5× (+ diarias en California) | **Working Time Regulations**: media de 48 h en 17 semanas, 11 h de descanso; sin recargo legal de horas extra | **ESA** provinciales: umbral semanal y/o diario | **Fair Work** + NES + **Award** (penalty rates de fin de semana y festivos) | UK 48 h firme: gov.uk/maximum-weekly-working-hours · resto por verificar |
| Vacaciones | sin mínimo federal (**PTO** de empresa) | 5,6 semanas (**holiday**) | según provincia (**vacation**) | 4 semanas (**annual leave**, NES) | por verificar (UK citado en el xlsx del Staff Kit) |
| Cargas sociales del empleador | **payroll taxes** (FICA, FUTA/SUTA) + workers' comp | **employer National Insurance** + pensión | **CPP** + **EI** | **superannuation** + workers' compensation | por verificar |
| Salario mínimo | federal + estatal/local | National Minimum Wage / National Living Wage | provincial | national minimum wage + Award | por verificar |
| Cuadrante de turnos | **schedule** | **rota** | schedule | **roster** | por verificar |
| Entrante | **appetizer** | **starter** | appetizer | **entrée** (¡trampa!) | por verificar |
| Plato principal | **entrée** / main | **main** | main / entrée | **main** | por verificar |
| Margen de cocina | food cost % | **GP %** (sobre el precio sin VAT) | food cost % | food cost % / GP | por verificar (UK citado en el xlsx de Food Cost) |
| Para llevar | **to go** / takeout | **takeaway** | takeout | **takeaway** | por verificar |
| Medidas | US customary (oz, fl oz, lb, qt, gal; pinta de 473 ml) | métrico en cocina; **imperial pint** (568 ml) para cerveza; botella de 70 cl | métrico | métrico | por verificar (UK citado en el xlsx de Food Cost) |
| Distancias | **miles** | miles | **km** | **km** | por verificar |
| Venta ambulante | permiso de *mobile food unit* (ciudad/condado) | **street trading licence** o *consent* de cada council | licencia municipal de vendedor | permiso del council | por verificar (UK citado en el xlsx del Food Truck) |
| Alta del negocio de comida | **food establishment permit** + *plan review* | registro en el council **28 días antes** (gratis) | permiso de salud municipal o provincial | registro o notificación en el council | por verificar (UK citado en los planes EN) |
