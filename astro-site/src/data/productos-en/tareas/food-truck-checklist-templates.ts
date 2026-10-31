// astro-site/src/data/productos-en/tareas/food-truck-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Food Truck Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-food-truck.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// (taco-shop-checklist-templates.ts el más cercano). SPEC: scripts/productos-digitales/checklists-kit/foodtruck/SPEC.md
// (delta) + F2-NOTAS.md («lo que la F3 tiene que saber») + la base.
//   · D2: nombre «Food Truck Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Food Truck Checklists Kit Pro: Inspection, Setup & Teardown Checklist Templates for Excel». DataForSEO US (31-oct):
//     food truck inspection checklist 170, health inspection checklist 110, food truck checklist 50, fire inspection
//     checklist 40; PAA «pre-trip inspection» → las FAQ de inspección sanitaria, de bomberos y pre-trip van arriba.
//     Jerga = la del hermano LIVE Food Truck Business Plan Kit (commissary, mobile vending license, window staff…).
//   · D3/D4: $15 (los tres kits de MOLDE PLANO: food truck, panadería, marisquería), pago único. SIN precio tachado ni
//     anclas (FTC 16 CFR 233.1, PR #117): sin priceOld, discountBadge, bonusSaveLine, `value` en los bonos,
//     aggregateRating ni review (el ES los lleva: 4,9 de 8 reseñas, -69 %, «ahorra €27», «valorados en €53»).
//   · MOLDE PLANO (F2-NOTAS): una hoja por libro, sin hoja de instrucciones, sin contador de tareas, sin N/A que descuente,
//     sin protección (todo editable), sin línea de versión, sin firma ni iniciales, sin hoja de caja. NADA de eso se
//     afirma aquí. Sí: columna OK con desplegable ✓ / — / N/A y la fila en verde al marcar ✓ en 7 hojas (01-04, 06-08;
//     el 05 lleva «Status» libre y el 09 va sin desplegable); el 01 trae la DURACIÓN de cada tarea (no hora límite).
//   · Cifras SOLO de los 11 xlsx EN (revision/dump_en.txt, contrastadas el 31-oct): 141 tareas (01 23 = 5 + 6 + 4 + 8;
//     02 18; 03 18; 04 18; 05 15; 06 20 = 4 × 5; 07 16 = 8 + 8; 08 13 = 7 + 6), briefing pre-evento de 15 campos en 4
//     bloques, calendario de 12 meses (eventos, menú sugerido, mantenimiento, marketing). °F solo los de los xlsx (0, 41,
//     70, 100, 135, 145, 155, 165); °C solo en la FAQ UK (8 / 63 °C).
//   · Lo que el ES afirma y el kit EN no trae, fuera: vitrina y arqueo como hoja (SPEC §5), «potencia» y «protocolo de
//     emergencia» del generador, «reporting semanal con KPIs», «reservas privadas», ITV (→ DMV y la inspección del estado
//     solo donde la exige), «licencias de actividad / certificados de manipulador» españoles (→ mobile vending license,
//     health permit, food handler cards, CFPM), «APPCC obligatorio» (→ FDA Food Code), «fiestas patronales» (→ county
//     fairs), «Imprimible A4» (→ US Letter), la Guía de Equivalencias ES↔LatAm (→ Equivalents Guide) y la FAQ de Google
//     Sheets (sin test real, SPEC base §6 y §9).
//   · Testimonios: los 8 del ES traducidos tal cual (nombres, roles y ciudades, sin marcas), con el subtítulo de la
//     edición española (TIENDA §3.5). Solo se pintan. Ninguna frase contradice el kit EN («gas» → propane, que es lo que
//     trae). Avatares del ES: género y oficio ya cuadran (2, 4 y 6 son mujeres).
//   · Imágenes: las 6 del ES, abiertas el 31-oct-2026: rótulos en inglés de marcas inventadas (sin marcas reales), sin
//     texto en español → se quedan, con el reparto del ES. Fuera la OG ES (og-kit-tareas-food-truck.jpg: «Kit de Tareas»,
//     €) → OG = el hero, como los hermanos EN.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'food-truck-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT',

  seo: {
    title: 'Food Truck Checklists Kit Pro: Inspection, Setup & Teardown Checklist Templates for Excel',
    description:
      '11 Excel food truck checklists with 141 tasks already written: health inspection prep, pre-trip, setup & teardown, propane, permits, events. One-time $15.',
    keywords:
      'food truck checklist, food truck inspection checklist, food truck health inspection checklist, food truck fire inspection checklist, food truck pre-trip inspection checklist, food truck setup checklist, food truck teardown checklist, food truck opening checklist, food truck closing checklist, food truck daily checklist, food truck permits checklist, food truck commissary, AI Chef Pro',
    // OG = el hero de la ficha (como los hermanos EN): el og-kit-tareas-food-truck.jpg del ES lleva texto en español y €.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg',
  },

  schema: {
    productName: 'Food Truck Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for food trucks with 141 tasks already written: setup and teardown, the pre-trip and vehicle check (generator, propane, fresh and wastewater tanks), food safety and health inspection prep under the FDA Food Code, permits, events and locations, the manager, duties by role, weekly and monthly cleaning and maintenance, events and seasons, a pre-event briefing and an annual calendar.',
    price: '15.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN). Sin reviews ni
    // aggregateRating (D3).
    faqs: [
      {
        q: 'What is on a food truck health inspection checklist?',
        a: 'Cold food at 41 °F or below in transit and on arrival, frozen at 0 °F or below, cooking temperatures (poultry 165 °F, ground meats 155 °F, fish and whole-muscle meats 145 °F), hot holding at 135 °F or above, a stocked handwashing sink with hot water at 100 °F or above, no bare-hand contact with ready-to-eat food, sanitizer checked with test strips, the 9 major allergens, and the paperwork in the truck: health permit, temperature and commissary logs, food handler cards and a Certified Food Protection Manager.',
      },
      {
        q: 'What should a food truck fire inspection checklist cover?',
        a: 'Propane cylinders secured upright with the valves closed in transit, the system per NFPA 58 and your fire marshal, a soapy-water leak test at every connection after each cylinder swap, an ABC extinguisher plus a Class K for the fryer with monthly checks and an annual service tag, the hood suppression system serviced every 6 months, the clearance your event asks for, and the generator outside the truck, away from the window.',
      },
      {
        q: 'What is a food truck pre-trip inspection?',
        a: 'The check you run before the truck rolls: fuel, tire pressure, lights, turn signals and brakes, registration and commercial auto insurance current, kitchen equipment secured, extinguishers tagged, the generator test-started, propane cylinders strapped in with the valves closed, the fresh water tank full and the wastewater tank empty. The kit\'s pre-trip and vehicle checklist has 18 of those checks already written.',
      },
      {
        q: 'Is there a free food truck checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online, often from county health departments and fire marshals. This kit is 11 Excel workbooks with 141 food truck tasks already written, °F temperatures under the FDA Food Code and a ✓ / — / N/A drop-down. Print it on US Letter or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, register with your council at least 28 days before you trade, get a street trading licence, and use 8 °C cold holding, 63 °C hot holding and 14 allergens; in Canada and Australia, your local permits, holding temperatures and allergen list. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Food Truck Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid: las 6 fotos del ES (rótulos en inglés de marcas inventadas, sin marcas reales).
    // Mismo reparto que el ES.
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-line.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-prep.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-counter.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-food-truck-counter.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $15, once',
    // D2: titlePre + titleGold = «Food Truck Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Food Truck Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Inspection, Setup & Teardown Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) with 141 food truck tasks already written in Excel: setup and teardown, the pre-trip and vehicle check, health inspection prep under the FDA Food Code, permits and events, the manager, roles, cleaning and seasons. Print it, hand it to your crew and check it off.',
    checkItems: [
      'Setup and teardown: parking and leveling, the generator, propane, the kitchen, the window and the cash close-out',
      'Pre-trip and vehicle: fuel, tires, lights, registration, extinguishers, generator, propane leak test and water tanks',
      'Health inspection prep in °F: cold at 41 °F, cooking at 165 / 155 / 145 °F, hot holding at 135 °F, handwashing and allergens',
      'Permits and events: mobile vending license, health permit, commissary agreement, insurance and a COI, temporary event permits',
      'Manager checklists, duties for 4 roles (chef, prep cook, window staff, driver / tech) and weekly and monthly upkeep',
      'Bonuses: a pre-event briefing and a 12-month US calendar of events, menus, maintenance and marketing',
    ],
    ctaLabel: 'BUY NOW — $15',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS FOOD TRUCK — €12»).
  stickyLabel: 'FOOD TRUCK CHECKLISTS KIT PRO — $15',

  grid: {
    countGold: '9',
    headingRest: ' Food Truck Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '141 food truck tasks already written and sorted by phase, area and role. Adjust them to your truck and your menu, print and delegate.',
    templates: [
      {
        icon: 'Truck',
        title: 'Food Truck Setup & Teardown Checklist: Arrival, Kitchen, Service & Closing',
        desc: 'Setup on arrival (5 tasks), in the kitchen (6) and at the window (4), and teardown (8): parking and leveling only where vending is legal, the generator outside and away from the window, propane pressure checked, cold equipment at 41 °F or below, the POS and starting bank, the fresh and wastewater tanks; at close, leftovers cooled and date-marked, the cash close-out and the truck secured for the road. 23 tasks, each with who does it and how long it takes.',
      },
      {
        icon: 'Wrench',
        title: 'Food Truck Pre-Trip & Vehicle Checklist: Generator, Propane, Water & Waste',
        desc: 'The pre-trip check: fuel, tires, lights and brakes, DMV registration and commercial auto insurance (a CDL only at 26,001 lb GVWR or more), equipment secured and extinguishers tagged (ABC plus Class K); the generator test-started and serviced, propane cylinders secured with a soapy-water leak test after every swap, potable water from an approved source and wastewater dumped only at the commissary. 18 checks.',
      },
      {
        icon: 'ShieldCheck',
        title: 'Food Truck Food Safety & Health Inspection Prep Checklist (FDA Food Code)',
        desc: 'Temperatures before loading, in transit and on arrival (41 °F or below, frozen at 0 °F or below), cooking (poultry 165 °F, ground meats 155 °F, fish and whole-muscle meats 145 °F), hot holding at 135 °F or time as a public health control, thawing, the handwashing sink at 100 °F, no bare-hand contact, test strips, the 9 major allergens and the paperwork the inspector asks to see. 18 checks.',
      },
      {
        icon: 'MapPin',
        title: 'Food Truck Permits, Events & Locations Checklist',
        desc: 'Permits and licenses (mobile vending license, mobile food unit health permit and commissary agreement, general liability and commercial auto insurance, business license, seller\'s permit and EIN, sales tax by vending location), the pre-event tasks (location, power, stock, event menu, temporary event permit, COI, fire marshal) and 6 event types, from truck parks and night markets to weddings. 18 tasks with lead times.',
      },
      {
        icon: 'Users',
        title: 'Food Truck Manager Checklist: Route, Inventory, Food Cost & Marketing',
        desc: 'The weekly route within each city\'s vending rules, event bookings and permits, orders from the event calendar, waste and leftovers, sales by spot or event, weekly food cost against a 28–35% benchmark, pricing, ROI per event, the daily cash reconciliation and a written tip pool, social media, reviews, new organizers and loyalty. 15 tasks with frequency and priority.',
      },
      {
        icon: 'UserCog',
        title: 'Food Truck Duties by Role: Chef, Prep Cook, Window Staff & Driver',
        desc: 'Clear tasks for 4 roles: the food truck chef (prep at the commissary or in the truck, never in a home kitchen), the prep cook (mise en place, assembly line, fryer), the window staff (orders, payment, allergen questions, the waiting area) and the driver / tech (driving, leveling, the generator and the water tanks). 5 tasks each.',
      },
      {
        icon: 'ClipboardList',
        title: 'Food Truck Weekly & Monthly Checklists: Deep Cleaning, Maintenance & Inventory',
        desc: 'Weekly: a deep clean inside the truck, the hood filters (hood and ducts by a certified contractor, NFPA 96), full inventory, fryer oil, a propane leak test and the water tanks and pump. Monthly: generator service, brakes, tires and lights, a review of your logs, food cost, the menu, every permit and license current, packaging and crew training.',
      },
      {
        icon: 'PartyPopper',
        title: 'Food Truck Event & Seasonal Checklists: Festivals, Fairs, Markets & Weddings',
        desc: 'The year from the spring rallies to the Memorial Day–Labor Day peak, fall markets and winter indoor events, plus the key sales events: food truck festivals and rallies, farmers and night markets, county and state fairs, wedding season (May–October), Black Friday and New Year\'s Eve. 13 tasks with lead times.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Blank Food Truck Checklist Template (Editable)',
        desc: 'A blank checklist with the kit\'s columns (area, task, assigned to, frequency, OK and notes) to build lists for your exact truck and menu: tacos, burgers, coffee, desserts or anything else.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Food Truck Pre-Event Briefing Template',
        desc: '15 fields to fill in before each event: the event (name, location, schedule, expected crowd), logistics (power, water, parking, vendor fee), menu and stock (event menu, estimated stock, packaging, allergens) and the crew (staff, meet-up time, vehicle).',
      },
      {
        icon: 'CalendarDays',
        title: 'BONUS: Food Truck Annual Calendar: Events, Menu, Maintenance & Marketing (US)',
        desc: '12 months for a US food truck, from Super Bowl Sunday, Mardi Gras and St. Patrick\'s Day to Cinco de Mayo, graduations, July 4th, county and state fairs, Labor Day, Halloween, Thanksgiving and the holiday markets, each with a suggested menu, the truck\'s maintenance and that month\'s marketing.',
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a hospitality consultant since 2010, set up for a US food truck under the FDA Food Code.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Built for Food Trucks',
        desc: 'Not restaurant templates with the name changed. Checklists for the real operation of a truck: parking and leveling, the generator, propane, the fresh and wastewater tanks, the window and the drive back to the commissary.',
      },
      {
        icon: 'ShieldCheck',
        title: 'Ready for the Health Inspector',
        desc: 'Temperatures in °F under the FDA Food Code, the handwashing sink, sanitizer test strips, the 9 major allergens and the paperwork the inspector asks to see in the truck: health permit, logs, commissary agreement and food handler cards.',
      },
      {
        icon: 'Flame',
        title: 'Propane, Generator and Fire Safety',
        desc: 'Cylinders secured with the valves closed in transit, a soapy-water leak test after every swap, ABC and Class K extinguishers tagged, the hood suppression system every 6 months and the generator outside the truck, away from the window.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $15, Once',
        desc: 'The same kind of task lists food trucks run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
      },
    ],
    // Pastillas de los hermanos EN: sin Google Sheets hasta el test real (SPEC base §6, §9); «A4» → US Letter.
    compatLabel: 'Compatible with:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has advised food trucks, street food operators and mobile event kitchens on running their operations professionally: setup and teardown, food safety on the road, permits by event and a yearly calendar of events and seasons.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Calendar',
        label: 'BONUS 1',
        title: 'Food Truck Pre-Event Briefing Template',
        desc: 'The event, location, schedule and expected crowd; power, water, parking and the vendor fee; the event menu, estimated stock, packaging and allergens; and the crew, meet-up time and vehicle. One sheet so event day goes without surprises.',
        image: '/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg',
      },
      {
        icon: 'CalendarDays',
        label: 'BONUS 2',
        title: 'Food Truck Annual Calendar (US)',
        desc: "12 months of event types, a suggested menu, the truck's maintenance and the marketing for each month, from Super Bowl Sunday and Cinco de Mayo to county fairs, Labor Day, Thanksgiving and the holiday markets.",
        image: '/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg',
      },
      {
        icon: 'Globe',
        label: 'BONUS 3',
        title: 'US · UK · Canada · Australia Equivalents Guide',
        desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.',
        image: '/lovable-uploads/ai-gallery/en-equivalents-guide.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE FOOD TRUCK CHECKLISTS KIT — $15',
  },

  guarantee: {
    text: "If the checklists don't help you run your food truck more professionally, from setup and the pre-trip check to the health inspection and your permits, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US medida (food truck inspection / health inspection / fire inspection checklist,
  // PAA «pre-trip inspection») arriba + las 7 del ES adaptadas (permisos, seguridad alimentaria móvil, generador, tipos
  // de evento, garantía; Google Sheets fuera hasta el test real; la de Latinoamérica → UK/CA/AU) + setup, teardown,
  // commissary y tanques, limpieza, plantilla gratis, cómo se marca, apps, varios trucks, caja, moneda y suscripción.
  faqs: [
    {
      q: 'What is on a food truck health inspection checklist?',
      a: 'The same things the inspector checks, in the order you can prove them. Temperatures: the cooler at 41 °F or below before loading, logged in transit and checked again on arrival (cold 41 °F or below, frozen 0 °F or below), cooking temperatures probed (poultry 165 °F; ground beef and other ground meats 155 °F for 17 seconds; fish and whole-muscle pork or beef 145 °F for 15 seconds), hot food held at 135 °F or above or under time as a public health control with a written procedure, and thawing never at room temperature. Handling: a handwashing sink with hot water at 100 °F or above, soap and paper towels (hand sanitizer only after washing), no bare-hand contact with ready-to-eat food, sanitizer checked with test strips, raw and cooked foods apart and color-coded cutting boards. Allergens and paperwork: an allergen chart at the window with the 9 major allergens, a crew trained to answer allergy questions, the health permit posted, temperature and commissary logs in the truck, food handler cards for the crew and a Certified Food Protection Manager in charge. The "Food Safety & Inspection" checklist has those 18 checks already written, with a blank for each °F reading.',
    },
    {
      q: 'What should a food truck fire inspection checklist cover?',
      a: 'Propane first: cylinders secured upright with the valves closed in transit, the system per NFPA 58 and your fire marshal\'s inspection, and a soapy-water leak test at every connection after each cylinder swap (never a flame). Then the extinguishers, an ABC plus a Class K for the fryer, accessible and tagged, with a monthly visual check and an annual service tag; the hood suppression system every 6 months (NFPA 96) and the hood and ducts cleaned by a certified contractor; and the generator outside the truck, away from the window, air intakes and people because of carbon monoxide, refueled only when it is off and cool. Many events also ask for a fire marshal inspection and at least 10 ft of clearance from buildings, other vehicles and combustibles; the permits checklist reminds you to confirm both. If you smell gas, the setup checklist says it plainly: light nothing, close the cylinder, get out and call 911 from outside.',
    },
    {
      q: 'What is a food truck pre-trip inspection?',
      a: 'The check you run before the truck rolls, so nothing fails on the road or at the event. The "Vehicle & Mobile Ops" checklist covers it in 18 checks: enough fuel for the round trip, tire pressure for the extra weight, lights, turn signals and brakes, registration with your state DMV and commercial auto insurance current (a vehicle safety inspection only where your state requires one, and a CDL only if the truck is 26,001 lb GVWR or more), kitchen equipment secured, extinguishers tagged; the generator fueled and test-started, extension cords in good shape; propane cylinders for the shift, secured and leak-tested; the fresh water tank filled from an approved source and the wastewater tank empty, the water pump working, and trash bags and the used-oil container on board.',
    },
    {
      q: 'What should be on a food truck setup checklist?',
      a: 'One list in the order you actually work, like a restaurant opening checklist built for a truck. On arrival: park and level the truck only in a legal vending spot (or with the owner\'s written permission on private property), set the generator outside and away from the window, check propane pressure and cylinders, put out the awning and signage, and set up the service counter. In the kitchen: the griddle, fryer and oven on with the hood and fire suppression working first, cold equipment at 41 °F or below with the reading logged, mise en place, stock, sauces and packaging. At the window: the menu posted, the POS, card reader and starting bank, the waiting area, and the water checked (fresh tank full, wastewater tank empty, hot water at the handwashing sink). The "Setup & Teardown" checklist has those 15 setup tasks already written, each with who does it and how long it takes.',
    },
    {
      q: 'What goes on a food truck teardown checklist?',
      a: 'Like any closing checklist, in the order that keeps you safe on the road: cooking equipment off and propane valves closed; leftovers cooled from 135 °F to 70 °F within 2 hours and to 41 °F within 4 more, covered, date-marked and refrigerated at the commissary; the griddle, fryer and work surfaces cleaned and sanitized (checked with test strips); the water and waste tanks emptied, wastewater only at the commissary or an approved servicing area; the awning and signage packed; the cash drawer closed out with the cash count and over/short against the POS Z report and tips split per your written tip pool; the generator shut down; and the truck secured for the road with the propane cylinders strapped in. The kit has those 8 teardown tasks already written.',
    },
    {
      q: 'Does it cover the commissary and the water tanks?',
      a: 'Yes, they run through the whole kit. Prep happens at the commissary or in the truck, never in a home kitchen. The fresh water tank is filled at the commissary with potable water from an approved source and a food-grade hose used for nothing else; the wastewater tank must be at least 15% larger than the fresh tank and is dumped only at the commissary or an approved servicing area, never in the street or down a storm drain; and the weekly list has you clean and sanitize the fresh water tank, pump and hose as your health department requires. The inspection checklist keeps your commissary log or commissary agreement in the truck, and the monthly list checks it is current.',
    },
    {
      q: 'Does it cover the generator?',
      a: 'Yes. Before each trip, the fuel level (gasoline, diesel or propane, per the unit; refuel only with it off and cool), a test start and the extension cords; at the event, the generator outside the truck, away from the window, air intakes and people (carbon monoxide), where the organizer and fire marshal allow, with cords routed so no one trips; at teardown, shut down or power disconnected; and monthly maintenance (oil, filter, spark plugs per the manufacturer\'s service hours). The driver / tech duties include running it, and the annual calendar has the generator check in February and a full-load check in July.',
    },
    {
      q: 'Does it include permits and licenses?',
      a: 'Yes, US-style. The "Permits & Events" checklist lists the mobile vending license from your city or county (one per truck, non-transferable), the mobile food unit health permit (plan review and inspection) with your commissary agreement, general liability insurance (events often ask for $1M per occurrence and a certificate of insurance naming them), commercial auto insurance, a business license, your state seller\'s permit and a free EIN from the IRS, and a POS that collects sales tax by vending location. Before each event it has you confirm the temporary food event permit if your health department requires one and the organizer\'s requirements. The monthly list checks that every permit, license, the fire marshal inspection, DMV registration and insurance are current. Rules vary by city and county, so the kit tells you what to check, not your local fees.',
    },
    {
      q: 'Does it work for different types of events?',
      a: 'Yes. The permits checklist covers 6 event types (food truck parks, farmers markets and night markets; music festivals, county fairs and street fairs; corporate events and private catering; weddings and celebrations; races and sporting events; and a regular daily spot where your city allows it), with the pre-event tasks for each: location, access and setup time, power, expected sales, an event menu and the permits. The pre-event briefing bonus puts it all on one sheet, and the seasonal checklist and annual calendar plan the festivals, fairs, wedding season and holiday markets ahead.',
    },
    {
      q: 'What should a food truck cleaning checklist include?',
      a: 'Daily cleaning goes in the teardown: the griddle, fryer and work surfaces cleaned and sanitized, and the tanks emptied. On top of that, the kit schedules a weekly deep clean inside the truck, the hood and filters degreased by the crew (with the hood and ducts cleaned by a certified contractor as often as NFPA 96 requires), the fryer oil changed and used oil sent to a licensed recycler, and the fresh water tank, pump and hose cleaned and sanitized; and monthly upkeep: generator service, brakes, tires and lights, a review of your temperature, cleaning and commissary logs, and packaging restocked.',
    },
    {
      q: 'Is there a free food truck checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and many county health departments and fire marshals publish the checklist they inspect with. That is a good place to start. This kit is something else: 11 Excel workbooks with 141 food truck tasks already written and sorted by phase, area and role, from the pre-trip check to the teardown, °F temperatures under the FDA Food Code, and a ✓ / — / N/A drop-down on the checklists. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a food truck?',
      a: "Yes. Every checklist comes with the real tasks of a food truck already written. You'll want to make it yours: every cell can be edited, so adjust tasks to your truck and your menu, delete the ones that don't apply and add your own. The blank template has the same columns for anything extra.",
    },
    {
      q: 'How do you check off the tasks?',
      a: 'Each checklist has columns for the phase or area, the task, who does it, when (how long it takes in the setup and teardown list, a frequency, a day or a lead time in the others), OK and notes. In 7 of the checklists the OK column has a ✓ / — / N/A drop-down, and the row turns green when you pick ✓; the manager checklist has a status column you fill in yourself. Print the list and hand it to the crew, or keep it open on a tablet in the truck.',
    },
    {
      q: 'How is it different from checklist apps?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $15, a one-time payment. What it is not: there are no reminders, photos or notifications on your crew's phones.",
    },
    {
      q: 'Can I use it for several trucks or with my clients?',
      a: "Yes. One purchase covers one business with all of its trucks, which makes it a good fit for fleets. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it include a cash drawer count?',
      a: 'The cash close-out is part of the day: the teardown checklist and the manager\'s daily reconciliation have you count the cash, note any over/short against the POS Z report and split tips per your written tip pool policy (managers and supervisors don\'t keep tips). This kit has no separate cash count sheet by bill and coin; if you want one that works out the starting bank and the over/short for you, the Restaurant Checklists Kit Pro includes it.',
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change. The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 135 °F hot holding), the 9 major allergens and US permits. In the UK, register your food business with your local council at least 28 days before you start trading, ask the council for a street trading licence, expect a food hygiene rating (0 to 5 in England, Wales and Northern Ireland), keep cold food at 8 °C or below and hot food at 63 °C or above, and give allergen information for 14 allergens. In Canada and Australia, check your provincial or state food safety rules, mobile vending permits and allergen list, and type them into the tasks. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $15 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you.',
    },
    {
      q: 'Is it a subscription? Are future updates included?',
      a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we add new templates or improvements, you get them at no extra cost — just download the files again.',
    },
    {
      q: 'Is there a money-back guarantee?',
      a: "Yes. A full 30-day guarantee. If you're not happy, we'll refund 100% with no questions asked.",
    },
  ],

  cta: {
    heading: 'Your Food Truck, Organized from Pre-Trip to Teardown — in 11 Checklists',
    subtitle:
      '9 templates + 3 bonuses (12 files) for the critical areas of your truck: setup and teardown, the vehicle, propane and water, food safety, permits, events and roles. For a one-time $15.',
    items: [
      'Setup and teardown at every vending spot, with who does it and how long it takes',
      'Pre-trip and vehicle: generator, propane leak test, fresh and wastewater tanks',
      'Health inspection prep: cold at 41 °F, hot holding at 135 °F, cooking at 165 / 155 / 145 °F (FDA Food Code)',
      'Permits, licenses, insurance and the pre-event checks for 6 event types',
      'Tasks by role: chef, prep cook, window staff, driver / tech',
      'Seasons and key events: festivals, fairs, markets and wedding season',
      'BONUS: Food Truck Pre-Event Briefing Template',
      'BONUS: Food Truck Annual Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE FOOD TRUCK CHECKLISTS KIT — $15',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Food Truck, la edición española de este kit: por eso conservan sus nombres, roles y ciudades, y el subtítulo lo dice.
  // Sin marcas. Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Food truck owners, mobile kitchen chefs and street food consultants who already run their operations with Kit de Tareas Recurrentes: Food Truck, the Spanish edition of this kit',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Food Truck Owner, Madrid',
        text: 'The setup and teardown checklists are essential. Generator, propane, kitchen… the whole crew follows the same routine at every event, and we set up in half the time.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Food Truck Chef, Barcelona',
        text: 'The mobile food safety checklist saved us at our last inspection. Temperatures, cold chain, paperwork… all up to date and ready to show. Zero stress at big events.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director, food truck fleet (3 trucks)',
        text: 'We rolled it out on 3 trucks. Mobile operations and the vehicle and generator checks are now the same across the whole fleet. No more mix-ups.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Manager, gourmet food truck',
        text: 'The duties by role make it clear who does what: chef, prep cook, window staff, driver. The pre-event briefing saves us time and mistakes at every new location.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Street Food Consultant',
        text: "For food trucks it's the most complete kit out there. Setup, teardown, mobile food safety, permits, events… it covers every critical point without gaps.",
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Event Food Truck Operator',
        text: "Keeping track of the permits and licenses for each event keeps us out of legal trouble. Every location has its own requirements, and here it's all planned before we head out.",
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Food Truck Driver and Tech',
        text: 'The vehicle and generator tasks are really detailed. Maintenance, power, propane, water… I know exactly what to check before every trip.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Executive Chef, premium street food',
        text: 'The annual calendar with events by season and a suggested menu helps us plan festivals, weddings and food markets all year round, with no gaps.',
        avatar: '/avatars/avatar-8.jpg',
      },
    ],
  },

  pricing: {
    price: '$15',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    // D4: obligatorio en KitTareasPricing; sin «valor total» ni ahorro (FTC).
    bonusTotalLabel: 'Everything included: 9 templates + 3 bonuses',
  },

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/bar-checklist-templates', label: 'Bar Checklists Kit Pro' },
    { href: '/en/digital-products/coffee-shop-checklist-templates', label: 'Coffee Shop Checklists Kit Pro' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
    { href: '/en/digital-products/ghost-kitchen-checklist-templates', label: 'Ghost Kitchen Checklists Kit Pro' },
    { href: '/en/digital-products/ice-cream-shop-checklist-templates', label: 'Ice Cream Shop Checklists Kit Pro' },
    { href: '/en/digital-products/chocolate-shop-checklist-templates', label: 'Chocolate Shop Checklists Kit Pro' },
    { href: '/en/digital-products/pastry-shop-checklist-templates', label: 'Pastry Shop Checklists Kit Pro' },
    { href: '/en/digital-products/hotel-checklist-templates', label: 'Hotel Checklists Kit Pro' },
    { href: '/en/digital-products/taco-shop-checklist-templates', label: 'Taco Shop Checklists Kit Pro' },
    { href: '/en/digital-products/bakery-checklist-templates', label: 'Bakery Checklists Kit Pro' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  // La versión de los xlsx (docProps subject «Food Truck Checklists Kit Pro · v1.1»; el ES es v1.1). Los ficheros no
  // llevan línea de versión dentro (molde plano): esto solo fecha la edición.
  updateNote: 'Version 1.1 · October 2026',

  alreadyBought: {
    product: 'food-truck-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
