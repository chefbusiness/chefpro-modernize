// astro-site/src/data/productos-en/tareas/seafood-restaurant-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Seafood Restaurant Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-marisqueria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// (food-truck-, bakery- y taco-shop-checklist-templates.ts los más cercanos). SPEC: scripts/productos-digitales/
// checklists-kit/seafood/SPEC.md (delta) + F2-NOTAS.md + la del food truck (molde plano) + la base.
//   · D2: nombre «Seafood Restaurant Checklists Kit Pro»; title SEO = H1 (Forma B): «Seafood Restaurant Checklists Kit
//     Pro: Raw Bar, Receiving & Opening Checklist Templates for Excel». DataForSEO US (31-oct): restaurant opening checklist
//     260, raw bar 9.900 (intención local), raw bar setup 30; seafood restaurant checklist / shellfish tag log / seafood
//     receiving log sin volumen → la intención «restaurant opening checklist», «raw bar setup» y «shellfish tags» va en
//     keywords y en las primeras FAQ.
//   · D3/D4: $15 (molde plano), pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine, `value` en los bonos, aggregateRating ni review (el ES los lleva). Sin «el software de
//     gestión cobra €40/mes» (→ la fórmula de los hermanos) ni «por menos de una mariscada».
//   · MOLDE PLANO (F2-NOTAS): una hoja por libro, sin hoja de instrucciones, sin contador, sin N/A que descuente, sin
//     protección, sin línea de versión, sin firma ni iniciales, sin hoja de caja (el cierre de caja es una tarea, 01 B37).
//     NADA de eso se afirma aquí. Sí: desplegable ✓ / — / N/A con la fila en verde en 7 hojas (01-04, 06-08); el 01 trae
//     la HORA de cada tarea (7:00 AM-11:45 PM); el 02 trae una columna «Reading».
//   · Cifras SOLO de los 11 xlsx EN (revision/dump_en.txt, contrastadas el 31-oct): 165 tareas (01 30 = 8 + 8 + 5 de
//     apertura y 9 de cierre; 02 21 = 7 + 7 + 7; 03 17 = 6 + 5 + 6; 04 19 = 7 + 7 + 5; 05 18; 06 25 = 5 × 5; 07 17 = 9 + 8;
//     08 18 = 8 + 6 + 4), 5 CCP, briefing de 13 campos, calendario de 12 meses (temporada, eventos, mantenimiento,
//     formación). °F solo los de los xlsx (−31, −4, 0, 41, 45, 50, 70, 145); °C solo en la FAQ UK (8 / 63 °C).
//   · Lo que el ES afirma y el kit EN no trae, fuera: cifras de temperatura del vivero por especie (→ «per your supplier and
//     the tank maker's spec»), «densidad de carga», lonja y subasta (→ seafood distributor / dock-to-door supplier),
//     Reglamento UE 1379/2013 y zona FAO (→ FDA Seafood List, harvest area / origin), RD 1021/2022, «alérgenos 2 y 14» de
//     la UE (→ pescado y crustáceos de los 9 de EE. UU.; moluscos solo UK), temporadas y vedas de España (→ temporadas US
//     orientativas, «dates vary by state»), percebe, gamba roja, «el origen en la carta es obligatorio por ley» (→ house
//     standard), arqueo como hoja, «formación» y «cierres por vacaciones» del calendario más allá de lo que trae,
//     «Imprimible A4» (→ US Letter), la guía ES↔LatAm (→ Equivalents Guide) y la FAQ de Google Sheets (sin test real).
//   · Testimonios: los 8 del ES traducidos tal cual (nombres, roles y ciudades, sin marcas), con el subtítulo de la
//     edición española (TIENDA §3.5). Solo se pintan. Frases que el kit EN contradice, cambiadas (regla de John, 11-oct):
//     Alejandro Ruiz («densidad de carga» → pH), María López («zona FAO» → harvest area; «cumplir con el reglamento UE»
//     → «stay compliant»), David Torres («lonjas, temporadas de pesca» → «receiving, the seasons»), Ana García
//     («temporadas de pesca en España y vedas», «compras en lonja», «gamba roja» → seasons and closures, orders, the fresh
//     season). Avatares reasignados para que oficio y género cuadren (jefe de cocina → chef-avatar-1; jefa de sala → 6).
//   · Imágenes: de las 6 del ES, abiertas el 31-oct-2026, DOS llevan texto en español legible (el rótulo «VIVERO
//     CENTOLLOS Y BOGAVANTES» y las etiquetas «OSTRAS / PERCEBES / NAVAJAS…» del expositor) y una el bordado «MADRID» en
//     la chaquetilla → fuera. Se quedan hero, mariscos y emplatado; entran el ceviche de la Guía Peruano (crudo, CCP 5) y
//     el corte de pescado del Kit Tareas Sushi Bar (partida de pescado), reutilizados, y UNA imagen nueva sin texto
//     (Nano Banana 2, 31-oct: vivero de langostas americanas y Dungeness con la barra de crudos detrás,
//     ai-gallery/tareas-seafood-en-live-tank.jpg, ≈ $0,07). OG = el hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'seafood-restaurant-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT',

  seo: {
    title: 'Seafood Restaurant Checklists Kit Pro: Raw Bar, Receiving & Opening Checklist Templates for Excel',
    description:
      '11 Excel seafood restaurant checklists with 165 tasks already written: opening & closing, live tank, receiving, shellfish tags, raw bar, HACCP. One-time $15.',
    keywords:
      'seafood restaurant checklist, seafood restaurant opening checklist, seafood restaurant closing checklist, restaurant opening checklist, raw bar checklist, raw bar setup checklist, oyster bar checklist, seafood receiving checklist, seafood receiving log, shellfish tag log, live lobster tank checklist, seafood HACCP checklist, AI Chef Pro',
    // OG = el hero de la ficha (como los hermanos EN): el og-kit-tareas-marisqueria.jpg del ES lleva texto en español y €.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-marisqueria-hero.jpg',
  },

  schema: {
    productName: 'Seafood Restaurant Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for seafood restaurants with 165 tasks already written: opening and closing for the live tank, display, kitchen and dining room, the live tank and seafood receiving, HACCP and traceability with shellfish tags and 5 critical control points, the raw bar and ice display, the manager, duties by role, weekly and monthly upkeep, seafood seasons and events, a pre-shift meeting template and an annual calendar.',
    price: '15.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page. Sin reviews ni aggregateRating (D3).
    faqs: [
      {
        q: 'What should be on a seafood restaurant opening checklist?',
        a: 'The live tank first (water temperature by species, aeration, filters, dead animals removed and logged), then the ice display on drained crushed ice at 41 °F or below, the fresh fish walk-in at 41 °F with the fish on ice, the freezer at 0 °F, sauces and fish stock, thawing done safely, the raw bar with shellfish from NSSP-listed shippers, and the dining room with seafood tools, today\'s catch and prices, and the shellfish allergy notes on the reservations.',
      },
      {
        q: 'How long do you keep shellfish tags?',
        a: 'Under the FDA Food Code (3-203.12), shellstock tags stay on file for 90 days after the container is emptied, and molluscan shellfish must come from shippers on the Interstate Certified Shellfish Shippers List (NSSP). The kit has you check the tags at receiving, keep the lot tag at the raw bar and file them.',
      },
      {
        q: 'What does a raw bar setup checklist include?',
        a: 'Crushed ice on a tray with a drain, no standing water; crustaceans, oysters, clams, mussels and whole fish laid out by family; tags kept for 90 days; price labels; ice replenished every 90 minutes to hold 41 °F; FIFO rotation; oysters shucked to order with the consumer advisory on the menu; and the display pulled, sorted and the tray sanitized at close.',
      },
      {
        q: 'Is there a free seafood restaurant checklist template in Excel or PDF?',
        a: 'Yes, you will find free restaurant checklist templates online. This kit is 11 Excel workbooks with 165 seafood restaurant tasks already written, °F temperatures under the FDA Food Code, shellfish tags and the raw bar covered, and a ✓ / — / N/A drop-down. Print it on US Letter or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C, hot holding at 63 °C and 14 allergens, molluscs included; in Canada and Australia, your local holding temperatures, shellfish rules and allergen list. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Seafood Restaurant Checklists Kit Pro',
  },

  images: {
    // 6 fotos sin texto legible: 3 del ES (hero, mariscos, emplatado), 2 reutilizadas de otras fichas (ceviche, corte de
    // pescado) y la nueva del vivero. Fuera las del ES con texto en español (vivero, expositor) y la del bordado «MADRID».
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-marisqueria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-seafood-en-live-tank.jpg',
      '/lovable-uploads/ai-gallery/tareas-marisqueria-mariscos.jpg',
      '/lovable-uploads/ai-gallery/tareas-marisqueria-emplatado.jpg',
      '/lovable-uploads/ai-gallery/guia-peruano-plato.jpg',
      '/lovable-uploads/ai-gallery/tareas-sushi-bar-corte.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-seafood-en-live-tank.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-marisqueria-emplatado.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-marisqueria-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $15, once',
    // D2: titlePre + titleGold = «Seafood Restaurant Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Seafood Restaurant Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Raw Bar, Receiving & Opening Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) with 165 seafood restaurant tasks already written in Excel: opening and closing, the live tank and receiving, HACCP and traceability with shellfish tags, the raw bar and ice display, the manager, roles, cleaning and seasons. Print it, hand it to your team and check it off.',
    checkItems: [
      'Opening and closing for the live tank, the ice display, the kitchen and the dining room, task by task with times',
      'Live tank and receiving: oxygen, salinity and pH, mortality, the day\'s catch, freshness signs and histamine-forming fish',
      'Shellfish tags kept 90 days, shellfish only from NSSP-listed shippers and a lot log for traceability',
      'Raw bar on drained ice at 41 °F, oysters shucked to order, parasite destruction and the consumer advisory for raw fish',
      'Manager checklists, duties for 5 roles (head chef, fish station, shellfish station, FOH manager, server) and upkeep',
      'Bonuses: a pre-shift meeting template with today\'s catch and a 12-month US calendar of seafood seasons and events',
    ],
    ctaLabel: 'BUY NOW — $15',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS MARISQUERÍA — €14»).
  stickyLabel: 'SEAFOOD RESTAURANT CHECKLISTS KIT PRO — $15',

  grid: {
    countGold: '9',
    headingRest: ' Seafood Restaurant Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '165 seafood restaurant tasks already written and sorted by shift, area and role. Adjust them to your menu and your suppliers, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Seafood Restaurant Opening & Closing Checklist: Live Tank, Display, Kitchen & Dining Room',
        desc: 'Opening for the live tank and the display (8 tasks), the kitchen (8) and the dining room (5): water and aeration checked, dead animals logged, the display on drained ice at 41 °F, walk-ins and freezer, sauces and fish stock, safe thawing, the raw bar, seafood tools and today\'s catch. Closing (9): the display into the walk-in on ice, the tank checked overnight, waste, the fish area sanitized, tomorrow\'s order and the register. 30 tasks, each with a time and who does it.',
      },
      {
        icon: 'Droplets',
        title: 'Live Tank & Seafood Receiving Checklist: Water Quality, Suppliers & Freshness Signs',
        desc: 'Daily live tank checks (water temperature by species per your supplier and the tank maker, dissolved oxygen at 6 mg/L or more, salinity, pH, filter, mortality, feeding), receiving from your seafood distributor or dock-to-door supplier (refrigerated transport, the day\'s catch, shellstock tags and invoices, 41 °F cold and 0 °F frozen, histamine-forming fish rejected if warm, the lot log) and the freshness signs for fish, live crustaceans, bivalves and cephalopods. 21 checks with a column for each reading.',
      },
      {
        icon: 'ShieldCheck',
        title: 'Seafood HACCP & Traceability Checklist: Shellfish Tags, Allergens & Critical Control Points',
        desc: 'Traceability (lot, species with its FDA Seafood List market name, harvest area or origin, dates, receiving and walk-in temperatures, thawing), allergens (crustacean shellfish and fish are major US allergens, molluscs are not; separate prep areas, a written notice, anaphylaxis training) and 5 critical control points: receiving with shellstock per NSSP rules, storage, cooking to 145 °F, the display on drained ice and raw fish with its parasite-destruction record and consumer advisory. 17 checks.',
      },
      {
        icon: 'Snowflake',
        title: 'Raw Bar & Seafood Display Checklist: Ice Display, Service & Close',
        desc: 'Setup (crushed ice on a drained tray, crustaceans, oysters, clams, mussels and razor clams with their tags, cephalopods, whole fish, price labels and garnish), service (ice every 90 minutes to hold 41 °F, FIFO, melt water drained, every piece checked, oysters shucked to order with the lot tag kept and the consumer advisory) and the close (product pulled and sorted, the tray sanitized). 19 tasks.',
      },
      {
        icon: 'Briefcase',
        title: 'Seafood Restaurant Manager Checklist: Purchasing, Market Price, Waste & Food Cost',
        desc: 'The daily order before your distributor\'s cutoff, prices from wholesalers, delivery ratings, inventory and waste, the pre-shift meeting, stations, sales by item, market price items adjusted to today\'s cost, display and tasting checks, schedules, training, invoices, weekly food cost under 32% (the kit\'s target), group bookings and social media. 18 tasks with frequency and priority.',
      },
      {
        icon: 'Users',
        title: 'Seafood Restaurant Duties by Role: Head Chef, Fish & Shellfish Stations, FOH Manager & Server',
        desc: 'Clear tasks for 5 roles: the head chef and seafood buyer, the fish station cook (fillets, fumet, cooking to 145 °F), the shellfish station cook (cooking times, seafood stews, opening bivalves), the FOH manager (today\'s catch, tableside seafood towers, allergens at every table) and the server (seafood tools, finger bowls, wine pairings for guests 21+). 5 tasks each.',
      },
      {
        icon: 'ClipboardList',
        title: 'Seafood Restaurant Weekly & Monthly Checklists: Live Tank, Walk-Ins, Maintenance & Audits',
        desc: 'Weekly: the live tank drained, sanitized and refilled, filters and pump serviced, inventory, waste review, walk-ins deep cleaned, freezer dates, knives sharpened, white wine stock and the display tray. Monthly: a review of your HACCP and traceability records, supplier ratings, the menu by season, refrigeration serviced by an EPA 608-certified tech, training, food cost, prices and pest control by a licensed operator.',
      },
      {
        icon: 'CalendarDays',
        title: 'Seafood Seasons & Events Checklist: US Seasons, Holidays & Regulations',
        desc: 'A seasonal guide for the US (dates vary by state): crawfish, soft-shell crabs, wild salmon, lobster, stone and king crab, bay scallops and oysters; the key sales events (the Feast of the Seven Fishes on Christmas Eve, New Year\'s Eve seafood towers, Valentine\'s Day, Lent Fridays, oyster and seafood festivals, summer patio and raw bar); and the rules: your state\'s seasons, closures and minimum sizes, origin documented to avoid IUU seafood. 18 tasks.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Blank Seafood Restaurant Checklist Template (Editable)',
        desc: 'A blank checklist with the kit\'s columns (area, task, assigned to, frequency, OK and notes) to build lists for your exact concept: oyster bar, fish house, raw bar, with or without a live tank.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Seafood Pre-Shift Meeting Template (Today\'s Catch)',
        desc: 'A pre-shift meeting sheet: today\'s catch (3 fresh fish and 3 live shellfish), specials and the off-menu special, allergens and allergy notes, covers, VIPs and group seafood feasts, and the wine pick of the day (21+ with ID).',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Seafood Restaurant Annual Calendar: Seasons, Events, Maintenance & Training (US)',
        desc: '12 months for a US seafood restaurant: the seafood in season (oysters, crawfish, soft-shell crabs, wild salmon, lobster, blue crab, stone and Dungeness crab), the sales events (Valentine\'s Day, Lent, Mother\'s Day, July 4th, clambakes, Thanksgiving, the Feast of the Seven Fishes), the maintenance and the training for each month.',
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a hospitality consultant since 2010, set up for a US seafood restaurant under the FDA Food Code.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Built for Seafood Restaurants',
        desc: 'Not restaurant templates with the name changed. Checklists for the real operation of a seafood restaurant: the live tank, the ice display, receiving, traceability and the raw bar.',
      },
      {
        icon: 'Droplets',
        title: 'The Live Tank, Every Day',
        desc: 'Water temperature by species, dissolved oxygen, salinity, pH, the filter, mortality and feeding, plus the weekly drain, sanitize and refill. The tank stays healthy and the shellfish reach the plate in good shape.',
      },
      {
        icon: 'ShieldCheck',
        title: 'Shellfish Tags and HACCP',
        desc: 'Shellstock tags kept 90 days, shellfish only from NSSP-listed shippers, a lot log, 5 critical control points and the parasite-destruction record for raw fish. Ready when the health inspector asks.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $15, Once',
        desc: 'The same kind of task lists seafood restaurants run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has advised seafood restaurants, fish houses and raw bars on running their operations professionally: the live tank, the ice display, traceability and the seafood seasons.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Seafood Pre-Shift Meeting Template',
        desc: "Today's catch (3 fresh fish and 3 live shellfish), specials and the off-menu special, the dishes with crustacean shellfish and molluscs, allergy notes, covers, VIPs and group seafood feasts, and the wine pick of the day. The sheet that lines up the kitchen and the dining room before service.",
        image: '/lovable-uploads/ai-gallery/tareas-marisqueria-mariscos.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Seafood Restaurant Annual Calendar (US)',
        desc: '12 months of seafood in season (a guide: dates vary by state), US sales events from Valentine\'s Day and Lent to Thanksgiving and the Feast of the Seven Fishes, and the maintenance and team training for each month.',
        image: '/lovable-uploads/ai-gallery/tareas-seafood-en-live-tank.jpg',
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
    ctaLabel: 'YES, I WANT THE SEAFOOD RESTAURANT CHECKLISTS KIT — $15',
  },

  guarantee: {
    text: "If the checklists don't help you run your seafood restaurant more professionally, from the live tank and receiving to the raw bar and your shellfish tags, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US medida (restaurant opening checklist, raw bar setup, shellfish tags, seafood
  // receiving) arriba + las 7 del ES adaptadas (vivero sin cifras por especie, tipo de local, trazabilidad → FDA Food
  // Code y NSSP, temporadas → guía US orientativa, garantía; Google Sheets fuera hasta el test real; la de Latinoamérica →
  // UK/CA/AU) + crudo, histamina, alérgenos, plantilla gratis, cómo se marca, apps, varios locales, caja, moneda y
  // suscripción.
  faqs: [
    {
      q: 'What should be on a seafood restaurant opening checklist?',
      a: "Everything a restaurant opening checklist has, plus the live product. The live tank and the display first: the water temperature checked by species (per your supplier and the tank maker's spec), aeration and filters, live shellfish condition, dead animals removed and logged, the display set on drained crushed ice (display ice is never used in food), today's seafood laid out by family with price labels, and the display at 41 °F or below. Then the kitchen: the fresh fish walk-in at 41 °F or below with the fish on ice, the live shellfish walk-in and the freezer at 0 °F or below, the sauces (cocktail sauce, mignonette, tartar, remoulade, drawn butter), the fish stock, the sides, the griddle and grill, and the day's thawing done in the walk-in or under cold running water at 70 °F or below. Then the dining room: tables set with seafood tools, bibs, wet wipes and lemons, today's menu with the catch and prices, the raw bar with shellfish from NSSP-listed shippers, and the reservations with shellfish allergy notes. The \"Opening & Closing\" checklist has those 21 opening tasks already written, each with a time and who does it.",
    },
    {
      q: 'What goes on a seafood restaurant closing checklist?',
      a: "The seafood pulled from the display and stored in the walk-in on ice, the live tank checked again (temperature, oxygen and overnight mortality), the fish and shellfish inventory against tomorrow's order, the day's waste logged (it is high-value product), the fish area and cutting boards deep cleaned and sanitized (checked with test strips), the walk-ins checked with the doors closed, the seafood service tools washed and stored, tomorrow's order placed with your seafood distributor or dock-to-door supplier, and the register closed out by fresh item with the cash count, over/short and tips per your written tip pool. The kit has those 9 closing tasks already written.",
    },
    {
      q: 'What does a raw bar setup checklist include?',
      a: 'The "Raw Bar & Display" checklist has 19 tasks in three steps. Setup: crushed ice on a tray with a drain (no standing water), crustaceans (lobster, spiny lobster, crab, langoustines), bivalves (oysters, littlenecks and cherrystones, mussels, razor clams) from NSSP-listed shippers with their tags kept 90 days, cephalopods, the whole fish of the day, price labels and the garnish. Service: ice replenished every 90 minutes to hold 41 °F or below, FIFO rotation, melt water drained, the look and smell of every piece checked, prices updated when a species sells out, and oysters shucked to order with no shell fragments, the lot tag kept and the consumer advisory on the menu for raw or undercooked items. Close: everything pulled and sorted, good product stored on fresh ice, unfit product logged and discarded, and the tray, drain and surface cleaned and sanitized.',
    },
    {
      q: 'How long do you keep shellfish tags?',
      a: 'Under the FDA Food Code (3-203.12), shellstock tags stay on file for 90 days after the container is emptied, and molluscan shellfish must come from shippers on the Interstate Certified Shellfish Shippers List under the National Shellfish Sanitation Program (3-201.15). The kit puts that where it happens: the receiving checklist asks for the tags (harvest area and date, certified shipper number) with every lot, the raw bar keeps the lot tag while the oysters are being shucked, and the opening checklist checks the shippers before the raw bar opens.',
    },
    {
      q: 'What should a seafood receiving checklist cover?',
      a: 'The delivery time with your seafood distributor or dock-to-door supplier and refrigerated transport at 41 °F or below; the day\'s catch checked for species, size and freshness; the paperwork for every lot (shellstock tags, and species, origin and supplier on the invoice for finfish); the receiving check (temperature, appearance, smell, eyes; cold at 41 °F or below, frozen at 0 °F or below and frozen solid; shellstock received per NSSP rules, on ice or shipped at 45 °F air or 50 °F internal or below, then held at 41 °F); a traceability log with lot, supplier, date and weight; and the product in the walk-in right away. The freshness signs are spelled out: bright, convex eyes, red gills, firm flesh, a fresh ocean smell and never ammonia, live crustaceans active, bivalves closed or closing when tapped.',
    },
    {
      q: 'Does it cover the live lobster tank?',
      a: "Yes, every day. Water temperature by species (per your supplier and the tank maker's spec: cold-water lobster runs colder than spiny lobster, so the kit leaves a blank for your figure instead of one that doesn't fit your species), dissolved oxygen (6 mg/L minimum), salinity (30–35 ppt for Atlantic shellfish), pH (7.5–8.5), the mechanical filter, mortality removed and logged, and feeding if needed. Weekly, the tank is drained, sanitized and refilled and the filters and pump are serviced, as the maker and your health department require. A display tank for live molluscan shellfish is a different case: it needs a variance and a HACCP plan from your health department.",
    },
    {
      q: 'Does it cover HACCP and traceability?',
      a: 'Yes. The traceability records cover the lot number, species (with its FDA Seafood List market name and scientific name), harvest area or origin, catch method, date, weight and supplier; receiving and walk-in temperatures twice a day; shelf life (fresh shellfish within 48 hours as a house standard, cooked ready-to-eat seafood date-marked for 7 days at 41 °F); and thawing. The HACCP section lists 5 critical control points: receiving, storage in separate walk-ins, cooking fish and shellfish to 145 °F for 15 seconds, the display on drained ice at 41 °F or below rotated every 2 hours, and raw or undercooked fish with its parasite-destruction record. The monthly checklist reviews the records so they are ready for the health inspection.',
    },
    {
      q: 'Does it cover raw fish, ceviche and crudo?',
      a: 'Yes. Raw or undercooked fish (crudo, ceviche, tartare) needs parasite destruction under the FDA Food Code (3-402.11): frozen and stored at −4 °F or below for 7 days, or frozen at −31 °F or below until solid and stored at −31 °F or below for 15 hours, or frozen at −31 °F or below until solid and stored at −4 °F or below for 24 hours. The kit has you keep that record for 90 days (3-402.12) and the consumer advisory on the menu (3-603.11), and the raw bar checklist repeats the advisory for raw oysters.',
    },
    {
      q: 'Does it cover histamine?',
      a: 'Yes, at receiving. Histamine-forming fish (tuna, mackerel, mahi-mahi, sardines, anchovies) must arrive cold: the checklist has you reject warm product, because cooking does not destroy histamine. Keeping them cold from the delivery truck to the walk-in is the control, so the kit pairs it with the receiving temperatures and the rule that product goes into the walk-in right away.',
    },
    {
      q: 'Which seafood allergens does it cover?',
      a: 'Fish and crustacean shellfish (shrimp, prawns, lobster, crab, langoustines) are among the 9 major US allergens. Molluscs (mussels, clams, oysters, scallops, octopus, squid) are not a major US allergen, so the kit tells your team to answer guests who ask; in the UK they are one of the 14. The checklists also keep crustaceans, molluscs and fish in separate prep areas, put a written allergen notice for each dish where your state has adopted the 2022 FDA Food Code (3-602.12(C)), train the team on severe allergies, and have the FOH manager tell every table about allergens.',
    },
    {
      q: 'Does it work for my kind of seafood restaurant?',
      a: "Yes. It covers seafood restaurants and fish houses, oyster and raw bars, and places with or without a live tank. If you don't have a live tank or a raw bar, delete those tasks or mark them N/A. Every cell can be edited, so adjust tasks, species and times to your menu, and use the blank template for anything extra.",
    },
    {
      q: 'Are the seafood seasons for the US?',
      a: 'Yes, as a guide: dates vary by state and by year, so check your state fish and wildlife agency and NOAA Fisheries. The seasonal checklist covers crawfish (Gulf states, peak in spring), soft-shell crabs, wild salmon runs, lobster, stone crab and king crab, bay scallops, oysters in the cold months and year-round shrimp, farmed oysters and mussels, plus your state\'s closures and minimum sizes and origin documented to avoid IUU seafood. The annual calendar adds the seafood in season month by month.',
    },
    {
      q: 'Is there a free seafood restaurant checklist template in Excel or PDF?',
      a: 'Yes, you will find free restaurant checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 165 seafood restaurant tasks already written and sorted by shift, area and role, the live tank, receiving, shellfish tags and the raw bar covered, °F temperatures under the FDA Food Code, and a ✓ / — / N/A drop-down on the checklists. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'How do you check off the tasks?',
      a: 'Each checklist has columns for the area, the task, who does it, when (a time on the opening and closing list, a frequency, a day or a lead time in the others), OK and notes; the live tank and receiving checklist adds a column for each reading. In 7 of the checklists the OK column has a ✓ / — / N/A drop-down, and the row turns green when you pick ✓; the manager checklist has a status column you fill in yourself. Print the list and hand it to the team, or keep it open on a tablet.',
    },
    {
      q: 'How is it different from checklist apps?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $15, a one-time payment. What it is not: there are no reminders, photos or notifications on your team's phones.",
    },
    {
      q: 'Can I use it for several restaurants or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for seafood restaurant groups. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it include a cash drawer count?',
      a: "The register close-out is part of the day: the closing checklist has you close out by fresh item with the cash count and over/short against the POS Z report, and split tips per your written tip pool policy (managers and supervisors don't keep tips). This kit has no separate cash count sheet by bill and coin; if you want one that works out the starting bank and the over/short for you, the Restaurant Checklists Kit Pro includes it.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change. The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 145 °F cooking), shellfish under the NSSP and the 9 major allergens. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, allergen information covers 14 allergens with molluscs included, and live shellfish come with the labels of an approved dispatch centre instead of NSSP tags: keep them as your local rules require. In Canada and Australia, check your provincial or state food safety and shellfish rules and allergen list and type them into the tasks. The legal drinking age for the wine pairings is 18 in the UK and Australia and 19 in most Canadian provinces. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
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
    heading: 'Your Seafood Restaurant, Organized from the Live Tank to the Raw Bar — in 11 Checklists',
    subtitle:
      '9 templates + 3 bonuses (12 files) for the critical areas of your seafood restaurant: the live tank, receiving, traceability, the raw bar, roles and seasons. For a one-time $15.',
    items: [
      'Opening and closing for the live tank, the display, the kitchen and the dining room',
      'Live tank: oxygen, salinity, pH, filters and mortality, every day',
      'Receiving and traceability: shellstock tags kept 90 days, lot log, histamine-forming fish (FDA Food Code)',
      'Raw bar on drained ice at 41 °F, FIFO and oysters shucked to order',
      'Tasks by role: head chef, fish station, shellfish station, FOH manager, server',
      'US seafood seasons and events, from crawfish to the Feast of the Seven Fishes',
      'BONUS: Seafood Pre-Shift Meeting Template',
      'BONUS: Seafood Restaurant Annual Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE SEAFOOD RESTAURANT CHECKLISTS KIT — $15',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Marisquería con Vivero y APPCC, la edición española de este kit: por eso conservan sus nombres, roles y ciudades, y el
  // subtítulo lo dice. Sin marcas. Solo se pintan: NO alimentan el JSON-LD. Frases cambiadas y avatares (ver cabecera).
  testimonials: {
    subtitle:
      'Head chefs, seafood restaurant owners and consultants who already run their operations with Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC, the Spanish edition of this kit',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Head Chef, seafood restaurant in Madrid',
        text: 'The live tank checklists are really thorough. Temperature, oxygen, salinity, pH… the whole team follows the same standard every morning, and the shellfish reach the plate in top condition.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Owner, Galician seafood restaurant',
        text: 'The HACCP traceability, with the lot log, the harvest area and the shellfish allergens, saved us in two health inspections. A must-have to stay compliant.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director, seafood restaurant group (3 locations)',
        text: 'We rolled it out in all 3 locations. The ice display, FIFO rotation and oyster shucking now follow the same standard. Same standard in Vigo, Madrid and Marbella.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'FOH Manager, seafood restaurant in Madrid',
        text: "The duties by role make it clear who does what. The pre-shift meeting with today's catch, the specials and the VIP tables lines up the kitchen and the dining room in 5 minutes before we open.",
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'David Torres',
        role: 'Hospitality Consultant specializing in fish and seafood',
        text: "For seafood restaurants it's the most complete kit out there. Live tank, display, traceability, receiving, the seasons… it covers every critical point where seafood places tend to slip.",
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Manager, fish restaurant in Barcelona',
        text: 'The calendar with the seafood seasons and closures lets us plan the menu and our orders ahead. No more buying frozen shrimp right in the middle of the fresh season.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Shellfish Cook, Galicia',
        text: "The live tank tasks are really clear: oxygen, salinity, pH, filter cleaning, mortality. I know exactly what to check every shift without having to ask the chef.",
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Executive Chef, premium seafood restaurant, Marbella',
        text: 'Checking the freshness of the fish and the lot traceability are the details that make the professional difference. We built it into our HACCP plan and went from "improvised" to "auditable".',
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
    { href: '/en/digital-products/food-truck-checklist-templates', label: 'Food Truck Checklists Kit Pro' },
    { href: '/en/digital-products/bakery-checklist-templates', label: 'Bakery Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  // La versión de los xlsx (docProps subject «Seafood Restaurant Checklists Kit Pro · v1.1»; el ES es v1.1). Los ficheros
  // no llevan línea de versión dentro (molde plano): esto solo fecha la edición.
  updateNote: 'Version 1.1 · October 2026',

  alreadyBought: {
    product: 'seafood-restaurant-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
