// astro-site/src/data/productos-en/tareas/restaurant-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Restaurant Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones). Primer producto EN de la
// línea Tareas. SPEC: scripts/productos-digitales/checklists-kit/SPEC.md (§6 = esta landing).
//   · D2: nombre «Restaurant Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine
//     en bloque): «Restaurant Checklists Kit Pro: Opening, Closing & Cleaning Checklist Templates for Excel».
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (§2.1, dl/restaurant-checklist-templates/).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos. Fórmula de la tienda EN.
//   · Cifras y normas SOLO de SPEC §3 (FDA Food Code 2022, NFPA 96, notas UK). Lo que el ES afirma y el kit
//     no trae, fuera: «48 h» del pre-evento (el xlsx dice «from booking to event day»).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC §6 y §9): la FAQ ES «¿Funcionan con
//     Google Sheets?» no se traduce; pastillas y subtítulo del carrusel (default EN de la plantilla) sin
//     Sheets. Cuando el test pase: pastilla «Google Sheets», subtítulo (data.compatSubtitle) y una FAQ.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual (nombres,
//     negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan.
//   · Imágenes: og-kit-tareas.jpg lleva texto en español («Kit de Tareas Recurrentes», «€14», «Imprimible
//     A4») → fuera; OG = la portada del hero ES (sin texto) hasta tener una OG EN propia (F3-NOTAS).
//     tareas-restaurante-manager.jpg (pizarra «HORARIOS») y -perfiles.jpg (pizarra «Vinos/Tapas») → fuera;
//     entran staff-en-preshift.jpg, staff-en-schedule-board.jpg y manual-manager-briefing.jpg (sin texto,
//     ya publicadas en la tienda EN).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_RESTAURANT_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'restaurant-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_RESTAURANT_CHECKLISTS_KIT',

  seo: {
    title: 'Restaurant Checklists Kit Pro: Opening, Closing & Cleaning Checklist Templates for Excel',
    description:
      '11 Excel checklists for restaurants with 491 tasks already written: opening & closing by area, kitchen stations, manager, side work, cleaning schedule, cash drawer count. One-time $19.',
    keywords:
      'restaurant opening checklist, restaurant closing checklist, restaurant cleaning checklist, restaurant cleaning schedule, kitchen checklist, restaurant checklist template, restaurant manager checklist, side work checklist, bartender opening checklist, restaurant opening and closing checklist, cash drawer count sheet, pre-shift meeting template, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-restaurante-hero.jpg',
  },

  schema: {
    productName: 'Restaurant Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for a casual restaurant with 491 tasks already written: opening and closing by area, whole building, cash drawer, kitchen stations, manager, roles and side work, cleaning schedule, events and holidays.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a restaurant opening checklist?',
        a: 'One list per area, in order: kitchen (temperatures, equipment, mise en place), front of house (tables, service stations, allergen chart, reservations, pre-shift meeting) and bar (drink stock, ice, garnishes, glassware), plus the whole building: alarm, lights, POS, security gate and patio. Each task needs who does it, a due-by time and initials.',
      },
      {
        q: 'What goes on a restaurant closing checklist?',
        a: 'Cleaning and shutdown by area (kitchen, front of house and bar), food labeled, dated and stored, the cash drawer counted against the POS Z report, and the building locked up: POS and HVAC off, security gate and doors closed, alarm set.',
      },
      {
        q: 'How often should a restaurant be deep cleaned?',
        a: 'Daily cleaning belongs in the closing checklists; a deep clean by zone, once a week. Kitchen hoods follow NFPA 96: monthly with solid fuel, quarterly in high-volume kitchens and every six months in moderate-volume ones, and the hood fire-suppression system every six months.',
      },
      {
        q: 'What is side work in a restaurant?',
        a: 'The tasks servers and bartenders do besides serving guests: setting and restocking stations, rolling silverware, refilling condiments, polishing glassware and the cleaning duties of each shift. This kit has a checklist for each role.',
      },
      {
        q: 'Is there a free restaurant checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 491 restaurant tasks already written, a counter that skips N/A tasks, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits in cells you can change: in the UK, use 8 °C and 63 °C and the 14 allergens; your patio is your terrace or beer garden; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Restaurant Checklists Kit Pro',
  },

  images: {
    // hero bg (6): el set del ES sin -manager (pizarra «HORARIOS») ni -perfiles (pizarra «Vinos / Tapas»).
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-restaurante-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-apertura.jpg',
      '/lovable-uploads/ai-gallery/staff-en-preshift.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-sala.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-limpieza.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-eventos.jpg',
    ],
    // strip visible del ContentGrid (6), como el ES: distinto del hero.
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-restaurante-apertura.jpg',
      '/lovable-uploads/ai-gallery/staff-en-schedule-board.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-sala.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-limpieza.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-eventos.jpg',
      '/lovable-uploads/ai-gallery/manual-manager-briefing.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Restaurant Checklists Kit Pro»; Forma B como los kits EN hermanos.
    titlePre: 'Restaurant Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Opening, Closing & Cleaning Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 491 restaurant tasks already written: opening, closing, whole building, cash drawer, kitchen stations, manager, roles, events and holidays. Print it, delegate it to your team, initial it and file it.',
    checkItems: [
      'Opening and closing checklists by area (kitchen, front of house, bar)',
      'Whole-building opening and closing, and a cash drawer count by bill and coin',
      'Tasks by role: head chef, sous chef, FOH manager, server, bartender',
      'Manager checklists: daily, weekly and monthly',
      "Event and holiday checklists (Valentine's Day, Christmas & New Year's Eve)",
      '3 editable master templates + a pre-shift meeting template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS — €14»).
  stickyLabel: 'CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Restaurant Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '491 casual-restaurant tasks already written and sorted by shift, area and role. Adjust them to your restaurant, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Opening & Closing Checklists: Kitchen, FOH & Bar',
        desc: '6 checklists: kitchen, front of house and bar opening + kitchen, front of house and bar closing. Every task with who does it, when and initials. 111 tasks already written in this file alone.',
      },
      {
        icon: 'ChefHat',
        title: 'Kitchen Checklists by Station (Hot Line, Cold Station, Mise en Place)',
        desc: 'Tasks before, during and after service for the hot line and the cold station, plus mise en place by proteins, vegetables and sides, sauces and desserts. Temperatures in °F under the FDA Food Code: 135 °F hot holding, 41 °F cold holding.',
      },
      {
        icon: 'ClipboardList',
        title: 'Restaurant Manager Checklist: Daily, Weekly, Monthly & Shift Handover',
        desc: 'Daily checklist, weekly checklist in blocks (DAY 1-5 + weekend, so no block gets lost if you close on Mondays) and monthly checklist. Plus a shift handover.',
      },
      {
        icon: 'Users',
        title: 'Daily Duties & Side Work Checklists by Role',
        desc: 'Checklists for the head chef, sous chef, FOH manager, server and bartender: the daily duties and side work of each position.',
      },
      {
        icon: 'CalendarDays',
        title: 'Restaurant Cleaning Schedule & Maintenance Checklists',
        desc: 'Weekly deep clean by zone, weekly FIFO check of walk-ins and dry storage, and monthly equipment and safety maintenance. + a Quarterly & Annual sheet for contracted services: pest control, hood cleaning (NFPA 96) and the fire-suppression system, fire extinguishers, gas, refrigeration, backflow, grease trap and used cooking oil, with the service report number and initials.',
      },
      {
        icon: 'PartyPopper',
        title: 'Event & Holiday Checklists',
        desc: "Pre-event checklist (from booking to event day), Valentine's Day, Christmas & New Year's Eve, and patio season opening and closing.",
      },
      {
        icon: 'FileEdit',
        title: 'Blank Restaurant Checklist Template (Editable)',
        desc: '3 master templates already structured (by time of day, by area and by role) with the sections and the area or person in charge set up: you just type your tasks in the green cells.',
      },
      {
        icon: 'Building2',
        title: 'Restaurant Opening & Closing Checklist (Whole Building)',
        desc: 'The checklist for the whole building, not just the kitchen: lights, alarm, POS, security gate, patio. Who does it and the due-by time are filled in for every task.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. Plus a monthly cash log with the over/short by formula.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Pre-Shift Meeting Template (Line-Up Notes)',
        desc: 'Pre-shift meeting template: reservations, specials, 86s, allergens and the team on shift. Print it and post it at the pass.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Restaurant Holiday & Events Calendar (US)',
        desc: "22 key US dates for restaurants, from the Super Bowl to New Year's Eve, with their tasks and recommended lead time, plus free rows for your own.",
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a restaurant consultant since 2010.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'The Usual Tasks, Already Written',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a casual restaurant. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Clock',
        title: 'Organized by Shift and Area',
        desc: 'Opening, service, closing. Kitchen, front of house, bar, patio. Every task at its time and in its place. Your team knows exactly what to do and when.',
      },
      {
        icon: 'Users',
        title: 'Delegation With Initials',
        desc: "Print the checklist and hand it to the person in charge. When they're done, they initial it and you file it. No more \"I didn't know I had to do that.\"",
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists restaurants run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
      },
    ],
    // Pastillas del ES (orden incluido) sin Google Sheets hasta el test real (SPEC §6, §9); «A4» → US Letter.
    compatLabel: 'Compatible with:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Pre-Shift Meeting Template',
        desc: 'The 5-minute meeting that separates good restaurants from great ones. Reservations, specials, allergens, 86s, the team on shift.',
        image: '/lovable-uploads/ai-gallery/staff-en-preshift.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Restaurant Holiday & Events Calendar (US)',
        desc: "22 key dates for US restaurants (Super Bowl, Valentine's Day, Mother's Day, Memorial Day, the Fourth of July, Thanksgiving, holiday parties, New Year's Eve) with tasks and recommended lead time.",
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-eventos.jpg',
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
    ctaLabel: 'YES, I WANT THE CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your restaurant's operations better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): People Also Ask de la SPEC §6 + las del ES adaptadas (tareas ya escritas, firma →
  // iniciales, frente a las apps, varios locales con la licencia de la tienda EN, eventos) + UK/CA/AU, moneda,
  // suscripción y garantía (como los hermanos EN). La de Google Sheets del ES, fuera hasta el test (SPEC §9).
  faqs: [
    {
      q: 'What should be on a restaurant opening checklist?',
      a: 'Think of it as one list per area, done in order. Kitchen: cooler and freezer temperatures (41 °F and 0 °F or below), equipment on, the line set up and mise en place checked. Front of house: lights, tables and the service station set, the allergen chart at hand, reservations reviewed and a pre-shift meeting. Bar: drink stock, ice, garnishes, the coffee machine and glassware. And the building itself: alarm, lights, POS, security gate, patio. Every task needs who does it, a due-by time and initials. The "Opening & Closing Checklists" workbook has the three areas already written, and the "Restaurant Opening & Closing Checklist" covers the whole building.',
    },
    {
      q: 'What goes on a restaurant closing checklist?',
      a: 'Cleaning and shutdown by area (kitchen, front of house and bar), food labeled, dated and stored, equipment off, the cash drawer counted against the POS Z report, and the building locked up: POS and HVAC off, security gate and doors closed, alarm set. In this kit, the closing checklists by area and the whole-building "Restaurant Closing" tab have those tasks already written, and the "Cash Drawer Opening & Closing" workbook works out the over/short for you.',
    },
    {
      q: 'How often should a restaurant be deep cleaned?',
      a: 'Daily cleaning belongs in the closing checklists. On top of that, this kit schedules a deep clean by zone every week (the "Weekly Deep Clean" tab), a weekly FIFO check of walk-ins and dry storage, and monthly equipment maintenance. Contracted services go on the "Quarterly & Annual" tab: kitchen hoods are cleaned on the NFPA 96 schedule (monthly with solid fuel, quarterly in high-volume kitchens, every six months in moderate-volume ones) and the hood fire-suppression system is serviced every six months, alongside pest control, fire extinguishers, the grease trap and the rest.',
    },
    {
      q: 'What is side work in a restaurant?',
      a: 'Side work is everything servers and bartenders do besides serving guests: setting and restocking stations, rolling silverware, refilling condiments, polishing glassware and the cleaning duties of each shift. When it isn\'t written down, it falls on whoever stays last. The "Daily Duties & Side Work Checklists by Role" workbook has one checklist each for the head chef, sous chef, FOH manager, server and bartender.',
    },
    {
      q: 'Is there a free restaurant checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 491 restaurant tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in?',
      a: "Yes. Every checklist comes with the most common tasks of a casual restaurant already written. You'll want to make it yours: adjust tasks to your restaurant, delete the ones that don't apply and add your own. The editable cells are green, and each table ends with 5 free green rows that the counter already includes.",
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for who does it, when (a due-by time on the daily lists, a day on the weekly ones, a frequency on the monthly ones and a lead time on the event lists), ✓ Done and initials. The manager prints the checklist and hands it to the team, and each person checks off and initials their tasks. At the end of the shift, the shift manager checks it and signs at the bottom.',
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: 'Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same task lists in Excel for $19, a one-time payment. No subscription, no internet needed. What it is not: there are no reminders, photos or notifications on your staff\'s phones.',
    },
    {
      q: 'Can I use it for several locations or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for restaurant groups and multi-unit operators. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it include tasks for events and holidays?',
      a: "Yes. There are checklists for private events (from booking to event day), Valentine's Day, Christmas & New Year's Eve, and opening and closing patio season. And the bonus calendar lists 22 key US dates for restaurants, from the Super Bowl to New Year's Eve, with their tasks and recommended lead time.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: 'Yes, with a few edits, all in cells you can change. The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 135 °F hot holding), the 9 major allergens and a cash count in US bills and coins. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, and allergen information covers 14 allergens: edit those task lines, because every task is an editable cell. In Canada and Australia, check your provincial or state food safety rules the same way. Your patio is your terrace or beer garden. For pounds, Canadian or Australian dollars, unprotect the cash count sheet (there is no password) and change the label and value of each bill and coin. The holiday calendar has a UK note (Mothering Sunday, bank holidays, Boxing Day) and free rows for your own dates. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.',
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
    heading: 'Stop Repeating the Same Instructions Every Day',
    subtitle: "9 templates + 3 bonuses (12 files) for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: kitchen, front of house, bar',
      'Whole-building opening and closing, and a cash drawer count with automatic over/short',
      'Kitchen station tasks: hot line, cold station, mise en place',
      'Manager checklists: daily, weekly and monthly',
      'Tasks by role: head chef, sous chef, FOH manager, server, bartender',
      'Weekly deep clean + FIFO + maintenance',
      "Events and holidays: Valentine's Day, Christmas & New Year's Eve, patio season",
      'BONUS: Pre-Shift Meeting Template',
      'BONUS: Restaurant Holiday & Events Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 10 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas
  // Recurrentes, la edición española de este kit: por eso conservan sus nombres, negocios y cifras, y el
  // subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Restaurant owners and managers who already run their operations with Kit de Tareas Recurrentes, the Spanish edition of this kit',
    items: [
      {
        name: 'Alberto Riera',
        role: 'Executive Chef, Restaurante Origen',
        text: "Mise en place used to depend on who was working the station. Since we started printing the opening and station checklists, prep is consistent every day. The cooks know exactly what to do without me having to repeat it.",
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Elena Navarro',
        role: 'Director of Operations, Grupo Tres Tenedores',
        text: 'Running 3 restaurants with different teams was chaos. With these checklists we standardized opening, closing and manager tasks across all three locations. Now everyone follows the same system, and you can see it in the results.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'David Molina',
        role: 'Owner, Gastrobar La Esquina',
        text: 'I opened my first restaurant a year ago and I kept forgetting things: turning on the oven, checking reservations, restocking napkins. With the checklists I cut the slip-ups by 80%. They literally saved my day-to-day operation.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Marta Herrero',
        role: 'Hospitality Consultant',
        text: "Every time I start with a new client, the first thing I do is hand them these checklists. They bring order from day one. It's the most practical thing I've found for organizing a restaurant's tasks.",
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Sergio Blanco',
        role: 'General Manager, Brasserie Central',
        text: 'A new server used to need two weeks to learn the full routine. Now, with the checklists by role, in 2 days they know what to do on every shift. Staff turnover is no longer a drama.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Cristina Pardo',
        role: 'Owner, Café Amanecer',
        text: "I printed the opening checklist and taped it to the kitchen door. The team follows it like a ritual every morning. I no longer have to ask if they've turned on the coffee machine or checked the display case. It's all checked off.",
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Fernando López',
        role: 'Owner, Restaurante Mesa Abierta',
        text: 'The pre-shift meeting template alone is worth the price. Our pre-shift used to be improvised and last 30 seconds. Now we go over the specials, allergens, VIP reservations and goals in 5 minutes. Service goes much better.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Raúl Domínguez',
        role: 'Head Chef, Hotel Litoral',
        text: "I've been in kitchens for 25 years and I always trusted my memory for the daily tasks. When I moved everything to paper checklists, I found I was missing 4-5 things a day. Now I don't forget anything and I sleep better.",
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo Santana',
        role: 'Restaurant Consultant',
        text: "I recommend it to every one of my consulting clients, no exceptions. The opening, closing and manager checklists cover 90% of what any restaurant needs to run in an orderly way. It's a must-have.",
        avatar: '/avatars/chef-avatar-5.jpg',
      },
      {
        name: 'Ignacio Ferrer',
        role: 'F&B Director, Hotel Gran Bahía',
        text: 'The weekly manager checklist is my favorite tool. I keep track of inventory, supplier meetings, cost reviews and team training in a single document. Running 4 F&B outlets has never been so organized.',
        avatar: '/avatars/avatar-1.jpg',
      },
    ],
  },

  pricing: {
    price: '$19',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    // D4: obligatorio en KitTareasPricing; sin «valor total» ni ahorro (FTC).
    bonusTotalLabel: 'Everything included: 9 templates + 3 bonuses',
  },

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
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
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: '/en/digital-products/how-to-open-a-pastry-shop', label: 'How to Open a Pastry Shop' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'restaurant-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
