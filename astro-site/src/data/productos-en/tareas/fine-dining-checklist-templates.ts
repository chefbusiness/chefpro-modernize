// astro-site/src/data/productos-en/tareas/fine-dining-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Fine Dining Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-restaurante-creativo.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN del
// mismo molde v2.0 híbrido (hotel- y taco-shop-checklist-templates.ts). SPEC: scripts/productos-digitales/checklists-kit/
// finedining/SPEC.md (delta) + F2-NOTAS.md + la base.
//   · D2: nombre «Fine Dining Checklists Kit Pro»; title SEO = H1 (Forma B): «Fine Dining Checklists Kit Pro: Tasting Menu,
//     Brigade & Chef's Table Checklist Templates for Excel». DataForSEO US (31-oct): fine dining restaurant 135.000, chef's
//     table 33.100, tasting menu 8.100, kitchen brigade 2.900, fine dining steps of service 210 → FAQ de apertura, cierre,
//     pasos del servicio, mise en place del menú degustación, brigada y chef's table arriba.
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld, discountBadge,
//     bonusSaveLine, `value` en los bonos, aggregateRating ni review (el ES los lleva: 4,9 de 8 reseñas, -69 %, «ahorra
//     €27», «valorados en €33»). Sin «el software de gestión cobra €40/mes» (→ la fórmula de los hermanos).
//   · MOLDE v2.0 (F2-NOTAS): SÍ hoja «Instructions» en cada libro, contador «Tasks done: X of Y» que no cuenta las N/A,
//     desplegable ✓ / — / N/A, línea de firma «Signed off by», línea de versión y firma de autor; 10 y 11 protegidos SIN
//     contraseña, con responsable y hora límite precargados, columna de iniciales y 5 filas verdes libres; caja en dólares
//     (11). En 01-09 y los bonus, «Assigned to» y «Time» van vacíos (se rellenan), no precargados.
//   · Cifras SOLO de los 13 xlsx EN (revision/dump_en.txt, contrastadas el 31-oct): 13 libros, 49 hojas (13 de
//     instrucciones), 477 tareas escritas (01 55 = 33 + 22 · 02 63 · 03 50 · 04 60 · 05 63 · 06 32 · 07 44 · 08 34 · 10 33 =
//     18 + 15 · 11 23 = 11 + 12 · B01 20) + 9 filas de ejemplo en N/A en el 09 (no se cuentan, como el ES: 477), calendario
//     de 12 meses. °F solo los de los xlsx (−31, −4, 0, 32, 41, 70, 100, 135, 145); °C solo en la FAQ UK (8 / 63 °C).
//   · Lo que el ES afirma y el kit EN no trae, fuera: «€40/mes», commis y stagiaire como perfiles (el 04 EN: executive
//     chef, sous chef, hot line, garde manger, pastry chef, sommelier, maître d' y server), «costes I+D» y «registro
//     fotográfico» como tales (→ coste por ración y fotos por iteración), congelación de anisakis UE (→ FDA Food Code
//     3-402.11), «BIE», «DDD», «Verifactu» (→ los servicios contratados US), «registro de jornada 4 años» (→ FLSA), guías
//     españolas (Repsol: fuera; Michelin Guide «in the cities it covers», 50 Best, OAD, James Beard), fechas españolas
//     (Reyes, comuniones, Día del Padre de marzo), «rangos de sala» del briefing (no están en el B01), «Imprimible A4»
//     (→ US Letter), la guía ES↔LatAm (→ Equivalents Guide) y Google Sheets (sin test real, SPEC base §6 y §9).
//   · Testimonios: los 8 del ES traducidos tal cual (nombres, roles, sin marcas), con el subtítulo de la edición española
//     (TIENDA §3.5). Solo se pintan. Frases que el kit EN contradice, cambiadas (regla de John, 11-oct): Lucía Navarro
//     («rangos de sala» → storytelling: el B01 no los trae) y Javier Ortega («guías, premios y jornadas temáticas» → special
//     menus and food festivals: el calendario EN no trae guías ni premios). Avatares reasignados para que oficio y género
//     cuadren y, sin las estrellas Michelin de los roles ES (no verificables fuera de España), los roles van genéricos
//     (chef ejecutivo → chef-avatar-1; jefa de sala → 6; sous chef → 4; consultora → 2; pastelero → chef-avatar-3;
//     chef propietario → 8; director de operaciones → 1).
//   · Imágenes: de las 6 del ES, abiertas el 31-oct-2026, la de I+D (`-id`) lleva el logo legible de una marca real de
//     circuladores → fuera; el bordado del hero es un nombre inventado. Entra UNA nueva sin texto (Nano Banana 2, 31-oct:
//     el pase de un menú degustación, ai-gallery/tareas-fine-dining-en-pass.jpg, ≈ $0,07). OG = el hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'fine-dining-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT',

  seo: {
    title: "Fine Dining Checklists Kit Pro: Tasting Menu, Brigade & Chef's Table Checklist Templates for Excel",
    description:
      "13 Excel files with 477 fine dining tasks already written: tasting menu mise en place, brigade, sommelier, chef's table, R&D, cash drawer. One-time $19.",
    keywords:
      "fine dining checklist, fine dining restaurant checklist, fine dining opening checklist, fine dining closing checklist, fine dining steps of service, tasting menu checklist, tasting menu mise en place, kitchen brigade duties, chef's table checklist, sommelier checklist, wine pairing checklist, restaurant opening checklist, restaurant closing checklist, AI Chef Pro",
    // OG = el hero de la ficha (como los hermanos EN): el og-kit-tareas-restaurante-creativo.jpg del ES lleva texto en español y €.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-restaurante-creativo-hero.jpg',
  },

  schema: {
    productName: 'Fine Dining Checklists Kit Pro',
    productDescription:
      "11 templates + 3 bonuses (14 files): Excel checklists for fine dining restaurants with 477 tasks already written: AM opening and PM closing with modernist equipment, tasting menu mise en place by lead time and a plating bible, menu development and R&D, kitchen brigade duties by role, weekly, monthly, quarterly and annual tasks, sommelier and wine pairing, chef's table and special events, food photography, social media and press, blank templates, whole-restaurant opening and closing, a cash drawer count in US dollars, a pre-shift meeting template and an annual calendar.",
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page. Sin reviews ni aggregateRating (D3).
    faqs: [
      {
        q: 'What should be on a fine dining opening checklist?',
        a: 'Personal hygiene and a safe start-up first (hood on, then the gas check), then the modernist equipment (immersion circulators, dehydrator, ferments with their pH, dry-aging cabinets and walk-ins that ran overnight at 41 °F or below and 0 °F or below, Pacojet, siphons), the bases and the stations for each course with the plating bible visible, and the dining room: climate, lighting, music, tables, pairing glasses and the pre-shift meetings with allergens on today\'s reservations.',
      },
      {
        q: 'What are the steps of service in fine dining?',
        a: 'A pre-shift meeting with the menu, allergens and VIPs; the storytelling of each course prepared; table timing coordinated with the kitchen; each course received from the pass and explained to the guest; allergens verified at each table before every course; plates cleared in coordination with the kitchen; bread, water and extras between courses; guest feedback relayed to the maître d\'; and a personalized farewell at each table.',
      },
      {
        q: 'How do you organize mise en place for a tasting menu?',
        a: "By lead time: long-lead prep (24–72 hours: stocks, ferments, marinades, long sous vide), mid-lead (6–12 hours: sous vide, infusions, gels, ice cream bases) and same-day (2–4 hours: foams, hot sauces, cuts), with microgreens, flowers and crisps at minute zero. A plating bible checks each course against its reference photo, weight and position.",
      },
      {
        q: 'Is there a free fine dining checklist template in Excel?',
        a: 'Yes, you will find free restaurant checklist templates online. This kit is 13 Excel files with 477 fine dining tasks already written, a counter on each checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C, hot holding at 63 °C and 14 allergens; in Canada and Australia, your local holding temperatures and allergen list. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Fine Dining Checklists Kit Pro',
  },

  images: {
    // 5 fotos del ES sin texto legible ni marcas reales + la nueva del pase. Fuera la de I+D (logo de una marca real).
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-emplatado.jpg',
      '/lovable-uploads/ai-gallery/tareas-fine-dining-en-pass.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-sumiller.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-chefstable.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-emplatado.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Fine Dining Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Fine Dining Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: "Tasting Menu, Brigade & Chef's Table Checklist Templates for Excel",
    description:
      "11 templates + 3 bonuses (14 files) with 477 fine dining tasks already written in Excel: opening and closing with modernist equipment, tasting menu mise en place and the plating bible, R&D, the kitchen brigade, sommelier and pairing, chef's table and events, the whole restaurant and the cash drawer. Print it, delegate it to your team, sign it off and file it.",
    checkItems: [
      'Tasting menu mise en place by lead time (24–72 hr, 6–12 hr, same day) and a plating bible course by course',
      'Kitchen brigade duties: executive chef, sous chef, hot line, garde manger, pastry chef, sommelier, maître d\' and servers',
      'Menu development and R&D: test sessions with 3 iterations, recipe documentation and a technique library',
      "Sommelier and wine pairing course by course, a non-alcoholic pairing and the wine cellar; chef's table, pop-ups and wine dinners",
      'Raw fish, sous vide and allergens under the FDA Food Code: parasite destruction, the consumer advisory, the 9 major allergens',
      'Whole-restaurant opening and closing, and a cash drawer count by bill and coin with automatic over/short',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS RESTAURANTE CREATIVO — €12»).
  stickyLabel: 'FINE DINING CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '11',
    headingRest: ' Fine Dining Checklist Templates + 3 Bonuses (14 files)',
    subtitle:
      '477 fine dining tasks already written and sorted by shift, station and role. Adjust them to your restaurant, print and delegate.',
    templates: [
      {
        icon: 'ChefHat',
        title: 'Fine Dining Opening & Closing Checklist: Kitchen, Modernist Equipment & Dining Room',
        desc: 'AM opening (33 tasks): personal hygiene and a safe start-up (hood first, then the gas check), immersion circulators, the dehydrator, ferments with their pH, dry-aging cabinets and walk-ins that ran overnight, bases and stations for each course, and the dining room with its pre-shift meeting. PM closing (22): logs, cleaning of siphons and specialty equipment, the register, covers, waste, tomorrow\'s allergens and the brigade\'s time records. 55 tasks in this file alone.',
      },
      {
        icon: 'Beaker',
        title: 'Tasting Menu Mise en Place Checklist: Long, Mid & Same-Day Prep + Plating Bible',
        desc: 'Prep by lead time: long-lead (24–72 hours: stocks, glaces, ferments, marinades, long sous vide), mid-lead (6–12 hours: sous vide egg at 145 °F, gels, spherification, ice cream bases) and same-day (2–4 hours: foams, sauces, cuts, tartares with parasite destruction for raw fish, microgreens washed). Plus a plating bible for 9 courses: reference photo, weight, position and tools.',
      },
      {
        icon: 'FlaskConical',
        title: 'Menu Development & R&D Checklist: Test Sessions & Recipe Documentation',
        desc: 'A fixed weekly R&D session, the new dish sheet (concept, technique, cost per portion, execution time, plating difficulty, the 9 major allergens), a test protocol with 3 iterations, the final recipe sheet (weights to 0.01 g, photos, food cost, target margin), operational feasibility for a 40-cover service, 4 seasonal menu changes and a technique library.',
      },
      {
        icon: 'Users',
        title: 'Kitchen Brigade Duties by Role: Executive Chef, Sous Chef, Chefs de Partie, Pastry, Sommelier & Maître',
        desc: "Daily tasks for the executive chef (final pass, plating supervision), the sous chef, the chef de partie on the hot line and in garde manger (crudo and ceviche only with fish frozen for parasite destruction), the creative pastry chef, the sommelier, and the maître d' and tasting menu servers. 60 tasks in 7 sheets.",
      },
      {
        icon: 'CalendarDays',
        title: 'Fine Dining Weekly, Monthly, Quarterly & Annual Checklists',
        desc: 'Weekly inventory of premium products, ferments and dry aging, modernist equipment maintenance and a freezer shelf-life table at 0 °F; monthly menu rotation, deep cleaning, food cost, beverage cost and FLSA time records; and a Quarterly & Annual sheet for contracted services: licensed pest control, hood cleaning (NFPA 96), gas, refrigeration by an EPA 608 tech, probe calibration at 32 °F, extinguishers, fire alarm and emergency lighting, insurance, permits and the POS.',
      },
      {
        icon: 'Wine',
        title: 'Sommelier & Wine Pairing Checklist: Tasting Menu Pairing & Wine Cellar',
        desc: 'Pairing designed course by course (wine or drink, glass, temperature, pour), a non-alcoholic pairing, signature cocktails only under your license and for guests 21+ with ID, and the wine cellar: inventory, FIFO, temperature and humidity, receipts and outflows, tasting sheets for storytelling, winery and distributor relationships, and beverage cost per cover.',
      },
      {
        icon: 'Sparkles',
        title: "Chef's Table & Special Events Checklist: Pop-Ups & Wine Dinners",
        desc: "The chef's table (prep and service, with the chef's storytelling and live plating), pop-ups and cooking demos, pairing dinners with a guest winery, and private dinners: allergens, guest count, price, deposit and cancellation confirmed in writing when you book, cross-checked at the pass on the night, and a mandatory service charge billed as business revenue, not a tip.",
      },
      {
        icon: 'Camera',
        title: 'Food Photography, Social Media & Press Checklist (Storytelling & Guides)',
        desc: 'A photo session for every new dish (overhead, 45° and detail shots), photography standards, a weekly social media editorial calendar and behind-the-scenes content, the narrative of each dish, review and press management, and material for the guides: the Michelin Guide in the cities it covers, the 50 Best lists, OAD and the James Beard Awards.',
      },
      {
        icon: 'FileEdit',
        title: 'Blank Fine Dining Checklist Templates (Editable)',
        desc: '3 blank templates already structured, by time block, by station and by profile, each with 3 example rows marked N/A so they don\'t count: write your own tasks over them or in the free rows.',
      },
      {
        icon: 'Building2',
        title: 'Restaurant Opening & Closing Checklist (Whole Building)',
        desc: 'The whole restaurant, not just the kitchen: alarm, lights, HVAC, security gate, POS, reservations, restrooms, patio, the wine list and the dining room pre-shift at opening; the last guests, decorations, windows, the final safety check, gate, alarm and lock-up at close. 33 tasks with who does it and a due-by time already filled in.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing the cash drawer with a count by US bill and coin, the starting bank deducted automatically and the over/short against your POS Z report (sales + tax, excluding tips). Plus a monthly cash log, one row per day, with the over/short calculated for you.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Fine Dining Pre-Shift Meeting Template',
        desc: "The meeting before every service: the tasting menu of the day and its changes, allergens and restrictions by table, VIPs, press and guides, today's chef's table or private dinner, the pairing and the storytelling of each course, and the dishes in testing. 20 points to check off.",
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Fine Dining Annual Calendar: Menu Changes, Key Dates & Seasons (US)',
        desc: "12 months with the 4 seasonal menu changes, the key US dates (Valentine's Day, Easter and Passover, Mother's Day, graduations, Thanksgiving, the holiday parties and New Year's Eve), the star ingredients of each month and the expected demand.",
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a hospitality consultant since 2010, set up for a US fine dining restaurant under the FDA Food Code.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Built for Fine Dining',
        desc: "Not restaurant templates with the name changed. Checklists for the real operation of a tasting menu restaurant: R&D, mise en place by lead time, the plating bible, the wine cellar and the chef's table.",
      },
      {
        icon: 'FlaskConical',
        title: 'Modernist Kitchen, Safely',
        desc: 'Immersion circulators, ferments, dry aging, siphons and raw fish, with the FDA Food Code where it applies: parasite destruction and the consumer advisory, a HACCP plan or variance for sous vide stored in the bag, and the 9 major allergens.',
      },
      {
        icon: 'Users',
        title: 'Every Role in the Brigade',
        desc: "Daily tasks for the executive chef, sous chef, chefs de partie, pastry chef, sommelier, maître d' and servers. Everyone knows exactly what to do before and during service.",
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same kind of task lists fine dining restaurants run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for creative and chef-driven restaurants.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 11 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Fine Dining Pre-Shift Meeting Template',
        desc: "The meeting before every service, reviewed by the executive chef and the maître d': the tasting menu of the day, allergens by table, VIPs and press, the chef's table, the pairing and the storytelling of each course, and the dishes in testing.",
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Fine Dining Annual Calendar (US)',
        desc: '12 months of menu changes, key US dates, star ingredients by season and expected demand, from the winter menu and Valentine\'s Day to wild mushroom season, Thanksgiving and New Year\'s Eve.',
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-chefstable.jpg',
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
    ctaLabel: 'YES, I WANT THE FINE DINING CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your fine dining restaurant more professionally, from the mise en place and the brigade to the dining room and the wine cellar, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US medida (apertura y cierre, steps of service, mise en place del menú degustación,
  // brigada, chef's table) arriba + las 7 del ES adaptadas (ya rellenadas, I+D, sumiller, fine dining o bistró, apps,
  // garantía; la de Latinoamérica → UK/CA/AU) + crudo, sous vide, foto y guías, trimestral y anual, caja, service charge,
  // plantilla gratis, firma, varios locales, moneda y suscripción.
  faqs: [
    {
      q: 'What should be on a fine dining opening checklist?',
      a: "Four blocks, in order. Personal hygiene and a safe start-up: clean uniform, no jewelry, cuts covered, hands washed with water at 100 °F or above, nobody sick handling food, the hood on before anything else, the gas check, and torch cartridges and N2O chargers away from heat. Modernist equipment: immersion circulators on only after the hood and gas, the dehydrator, ferments with their pH logged, the dry-aging cabinets and walk-ins checked to confirm they ran all night (41 °F or below and 0 °F or below, readings logged), the Pacojet and the siphons. Bases and mise en place: stocks and glaces, infused oils, hydrocolloids, sous vide in progress, a station for each course and the plating bible visible at every pass. Dining room: climate, lighting, music, tables, pairing glasses, the kitchen and dining room pre-shift meetings with allergens on today's reservations, and the floor plan. The \"AM Opening\" checklist has those 33 tasks already written.",
    },
    {
      q: 'What goes on a fine dining closing checklist?',
      a: "Logs first: walk-in, freezer and dry-aging temperatures, the pH of overnight ferments, the time left on long sous vide cooks, and every prep labeled with its use-by date (7 days maximum at 41 °F). Then cleaning: siphons, nozzles and chargers, plating tweezers and squeeze bottles, the Pacojet, torches and smokers, and the circulators and dehydrator turned off unless a cook is running overnight. Then the administration: the register closed out and the day's sales logged, covers served, incidents, the chef's feedback on the dishes, the day's waste (it corrects plate cost and tomorrow's order), tomorrow's reservations and allergens, the brigade's time records validated (FLSA), and the alarm and lock-up. The \"PM Closing\" checklist has those 22 tasks already written.",
    },
    {
      q: 'What are the steps of service in fine dining?',
      a: "The \"Maître & Dining Room\" checklist puts them in order. Before service, the maître d' prepares the narrative of each course, coordinates table timing and the course sequence with the kitchen and manages VIPs. During service, the tasting menu servers receive each course from the kitchen and serve it, explain it to the guest, verify allergens at each table before every course, clear plates in coordination with the kitchen, serve bread, water and extras between courses and relay guest feedback to the maître d', who handles allergens, complaints and requests and gives a personalized farewell at each table. The pre-shift meeting bonus lines it all up before the doors open.",
    },
    {
      q: 'How do you organize mise en place for a tasting menu?',
      a: "By lead time, so nothing is left to the last hour. Long-lead prep (24–72 hours): brown veal stock, dashi, glaces, consommé, lacto-ferments with their pH, koji, long marinades and long sous vide cooks. Mid-lead (6–12 hours): sous vide egg at 145 °F, vegetables, infusions, gels, spherification baths and ice cream and sorbet bases. Same-day (2–4 hours): foams, hot sauces, airs, vinaigrettes, protein and fish cuts to the gram, tartares cut no more than 2 hours before the pass, and the microgreens and flowers washed. Then the plating bible checks each course (from the snack to the petit fours) against its reference photo, weight and position, with the tools ready at the station. The instructions show you how to adapt it to a 7- to 15-course menu.",
    },
    {
      q: 'Which kitchen brigade roles does it cover?',
      a: "Seven sheets of daily tasks: the executive chef (menu of the day, premium suppliers, food cost, plating supervision and the final pass), the sous chef (mise en place of every station, brigade management, temperatures, labeling, restocking), the chef de partie on the hot line (stocks, sauces, proteins, sous vide during service), the chef de partie in garde manger (salads, crudo, ceviches and tartares, cold courses), the creative pastry chef (pre-desserts, desserts, petit fours, ice creams, sweet ferments), the sommelier (the day's pairing, the alternative pairing, cellar stock) and the maître d' with the tasting menu servers. 60 tasks in total.",
    },
    {
      q: "How do you run a chef's table?",
      a: "The \"Chef's Table\" checklist covers it in two steps. Prep: the final guest count and the allergens already confirmed in writing at booking reviewed with the kitchen, a special menu, the storytelling of each course, a visible station set up for interaction, special tableware and the pairing coordinated with the sommelier. Service: the chef's introduction, live plating with the technique explained, course timing adapted to the table, extra bites or off-menu surprises, photos with the guests' permission and a personalized farewell from the chef. The same file covers pop-ups, cooking demos, pairing dinners with a guest winery and private dinners.",
    },
    {
      q: 'Does it cover R&D and menu development?',
      a: 'Yes, a whole file. R&D sessions on a fixed weekly day, with ingredients set aside from service stock and a goal for each session; a new dish sheet (concept, inspiration, ingredients, technique, cost per portion, execution time, plating difficulty and the 9 major allergens); a test protocol with 3 iterations, each photographed and with team feedback, ending with a service timing test and the executive chef\'s approval; the final recipe sheet (weights to 0.01 g for hydrocolloids, temperatures and times, photos, actual food cost, target margin); operational feasibility for a 40-cover service; 4 seasonal menu changes; and a library of tested and discarded techniques.',
    },
    {
      q: 'Does it cover raw fish, crudo and ceviche?',
      a: 'Yes. Any fish served raw or undercooked (tartare, ceviche, crudo, cured or cold-smoked) needs parasite destruction under the FDA Food Code (3-402.11): frozen at −4 °F or below for 7 days, or at −31 °F until solid and held 15 hours, or at −31 °F until solid and then 24 hours at −4 °F. The kit has you require the supplier\'s letter or freeze it yourself, log the lot, keep the record 90 days (3-402.12) and print the consumer advisory on the menu (3-603.11). Citrus acid does not replace freezing: it only changes the texture.',
    },
    {
      q: 'Does it cover sous vide?',
      a: 'Yes. Cook to the time and temperature of your validated recipe; if you chill and store the food in the bag (reduced oxygen packaging), you need a HACCP plan or a health department variance (FDA Food Code 3-502.11 / 3-502.12), and you chill it from 135 °F to 70 °F within 2 hours and to 41 °F within 4 more (3-501.14). The sous vide egg runs at 145 °F (or per your recipe), with the consumer advisory if served undercooked. The Quarterly & Annual sheet checks that your health permit covers sous vide, curing, dry aging and reduced oxygen packaging.',
    },
    {
      q: 'Does it include sommelier and wine cellar tasks?',
      a: "Yes, a whole file for the sommelier: the pairing designed course by course (wine or drink, glass, temperature and pour, about 60–80 ml per course), a non-alcoholic pairing for every course, signature cocktails served only under your license and to guests 21+ with ID, and the wine cellar: monthly inventory, minimum stock for each pairing label, FIFO, temperature and humidity, receipts and outflows, tasting sheets with notes for the dining room's storytelling, winery and distributor relationships, weekly team training and beverage cost per cover.",
    },
    {
      q: 'Does it cover food photography, social media and the guides?',
      a: "Yes. A photo session for every new dish before it goes on the menu (overhead, 45° and detail shots, consistent editing), a weekly editorial calendar for Instagram and TikTok with behind-the-scenes content, the narrative of each dish and the restaurant's story, reviews on Google, Tripadvisor, Yelp and OpenTable answered within 24–48 hours, press management, and material for the Michelin Guide (in the cities it covers), The World's 50 Best and North America's 50 Best, OAD and the James Beard Awards.",
    },
    {
      q: 'Does it cover inspections and contracted services?',
      a: "Yes. The Quarterly & Annual sheet lists what you contract and what an inspector asks for in writing: licensed pest control, hood and duct cleaning by a certified contractor (NFPA 96), your HACCP plan where a variance requires one, food handler cards and a certified food protection manager, your health permit, gas lines, refrigeration and dry-aging cabinets serviced by an EPA 608-certified tech, scale calibration, probes calibrated at 32 °F, used oil pickup, extinguishers and the hood suppression system, the fire alarm and emergency lighting, insurance, FLSA time records and Form I-9, the POS and sales tax, and permit renewals. Each one has a notes cell for the service report number and the next date.",
    },
    {
      q: 'Does it include a cash drawer count?',
      a: 'Yes. A cash drawer workbook with an opening sheet, a closing sheet and a monthly log. You count by US bill and coin, and the sheet works out the total cash, deducts the starting bank and calculates the total collected and the over/short against your POS Z report (sales + tax, excluding tips), which turns amber when the drawer does not balance. The monthly log gives one row per day, so you see at a glance which days did not balance.',
    },
    {
      q: 'Is a mandatory service charge the same as a tip?',
      a: "No, and the kit says so where it matters. For private dinners and events, the special dinners checklist has you confirm in writing what the price includes, and it notes that a mandatory service charge is business revenue, not a tip (IRS Rev. Rul. 2012-18), so you tell the guest in writing. Tips are kept out of sales in the cash count.",
    },
    {
      q: 'Is it only for fine dining, or does it work for a creative bistro?',
      a: 'Both. A restaurant with a 12-course tasting menu can use every file; a creative bistro with a short menu can start with opening and closing, the brigade and the weekly and monthly tasks, and mark the rest N/A. The blank templates let you build anything else your concept needs.',
    },
    {
      q: 'Is there a free fine dining checklist template in Excel or PDF?',
      a: 'Yes, you will find free restaurant checklist templates online, and a blank one is fine to get started. This kit is something else: 13 Excel files with 477 fine dining tasks already written and sorted by shift, station and role, a counter on every checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a fine dining restaurant?',
      a: "Yes. Every checklist comes with the real tasks of a fine dining restaurant already written: 477 in total. You'll want to make it yours: adjust tasks to your restaurant, delete the ones that don't apply and add your own. The whole-restaurant and cash drawer files end with 5 free green rows that the counter already includes, and the blank templates have their own free rows.",
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for the area, who does it, ✓ (a drop-down with ✓, — for not done, or N/A), the time and notes, a counter ("Tasks done: X of Y") and a signature line at the bottom ("Signed off by"). The whole-restaurant and cash drawer files add a column for initials and come with who does it and a due-by time already filled in. The person in charge of the shift prints the checklist and hands it out, each person checks off their tasks, and at the end of the shift the checklist is checked and signed.',
    },
    {
      q: 'How is it different from checklist apps?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your team's phones.",
    },
    {
      q: 'Can I use it for several restaurants or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for restaurant groups. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 145 °F for the sous vide egg), the 9 major allergens, US contracted services and a cash count in US bills and coins. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, and allergen information covers 14 allergens (the kit's allergen tasks already note the UK's 14). In Canada and Australia, check your provincial or state food safety rules and allergen list and type them into the tasks, and swap the denominations in the cash count for your own. For the wine pairing, the legal drinking age is 18 in the UK and Australia and 19 in most Canadian provinces (18 in Alberta, Manitoba and Quebec). Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $19 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you.',
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
    heading: 'Stop Repeating the Same Instructions Every Service — 14 Files for Your Fine Dining Restaurant',
    subtitle:
      "11 templates + 3 bonuses (14 files) for the critical areas of a fine dining restaurant: the tasting menu, the brigade, R&D, the wine cellar, the chef's table, the whole building and the cash drawer. For a one-time $19.",
    items: [
      'Opening and closing for the kitchen, modernist equipment and the dining room',
      'Whole-restaurant opening and closing, and a cash drawer count with automatic over/short',
      'Tasting menu mise en place by lead time and a plating bible course by course',
      'Menu development and R&D: test sessions, recipe sheets and food cost',
      "Kitchen brigade duties: executive chef, sous chef, chefs de partie, pastry chef, sommelier, maître d'",
      'Weekly, monthly, quarterly and annual tasks: premium inventory, maintenance and contracted services',
      'Sommelier and wine pairing: course by course, non-alcoholic pairing and the wine cellar',
      "Chef's table and events: pop-ups, cooking demos, wine dinners and private dinners",
      'Food photography, social media, press and the guides',
      'BONUS: Fine Dining Pre-Shift Meeting Template',
      'BONUS: Fine Dining Annual Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE FINE DINING CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Restaurante Creativo / De Autor, la edición española de este kit: por eso conservan sus nombres y roles, y el subtítulo
  // lo dice. Sin marcas. Solo se pintan: NO alimentan el JSON-LD. Dos frases cambiadas y avatares (ver cabecera).
  testimonials: {
    subtitle:
      'Executive chefs, sous chefs, sommeliers and restaurant managers who already run their operations with Kit de Tareas Recurrentes: Restaurante Creativo / De Autor, the Spanish edition of this kit',
    items: [
      {
        name: 'Alberto Riera',
        role: 'Executive Chef, tasting menu restaurant',
        text: 'The tasting menu mise en place checklist changed my life. Every course documented with timing, temperatures and who is responsible. My sous chef doesn\'t need to ask me anything anymore: it\'s all in the template.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Marina Delgado',
        role: 'Sous Chef, fine dining restaurant',
        text: 'The R&D template is incredible. Recipe sheets, concept tests, tasting feedback… at last I have a system to document all the research we do in the kitchen.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Fernando Casas',
        role: 'Sommelier, fine dining restaurant',
        text: "Finally a checklist that understands a sommelier's work: the wine cellar, pairing by course, serving temperatures, team tastings. Generic tools don't cover even 20% of this.",
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Lucía Navarro',
        role: 'Dining Room Manager, chef-driven restaurant',
        text: 'We use the pre-shift meeting before every service. VIPs, allergies, menu changes, the storytelling of each course… in 5 minutes the whole team is aligned. A must for fine dining.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Carlos Iniesta',
        role: 'Chef-Owner, 2 creative restaurants',
        text: 'I have two creative restaurants, and each sous chef did things their own way. With standardized checklists, the quality is the same in both. Onboarding stagiaires went from 2 weeks to 4 days.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Restaurant Consultant, fine dining',
        text: 'The first thing I do with every creative restaurant client is hand them these checklists. R&D, the tasting menu, the sommelier, events… they cover 95% of what any chef-driven restaurant needs.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Diego Morales',
        role: 'Creative Pastry Chef',
        text: 'The R&D section lets me document every new dessert trial with its costs, times and feedback. I used to lose great ideas because I never wrote them down. Now I have a complete history.',
        avatar: '/avatars/chef-avatar-3.jpg',
      },
      {
        name: 'Javier Ortega',
        role: 'Director of Operations, restaurant group',
        text: 'We run 4 creative restaurants. The annual calendar of events and menus lets us plan seasonal changes, special menus and food festivals months ahead. Pure gold.',
        avatar: '/avatars/avatar-1.jpg',
      },
    ],
  },

  pricing: {
    price: '$19',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    // D4: obligatorio en KitTareasPricing; sin «valor total» ni ahorro (FTC).
    bonusTotalLabel: 'Everything included: 11 templates + 3 bonuses',
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
    { href: '/en/digital-products/seafood-restaurant-checklist-templates', label: 'Seafood Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'fine-dining-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
