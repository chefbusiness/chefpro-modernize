// astro-site/src/data/productos-en/tareas/hotel-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Hotel Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-hotel.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-, bar-, coffee-shop-, catering-, pizza-shop-, burger-joint-, ghost-kitchen-, ice-cream-shop-,
// chocolate-shop- y pastry-shop-checklist-templates.ts. SPEC: scripts/productos-digitales/checklists-kit/hotel/SPEC.md
// (delta) + la base.
//   · D2: nombre «Hotel Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Hotel Checklists Kit Pro: Housekeeping, Front Desk, F&B & Maintenance». Demanda US (SPEC §R): hotel housekeeping /
//     room cleaning / cleaning checklist 260 (una serie), maintenance 70, front desk 30, night audit 20; turndown service
//     4.400 y BEO 9.900 son informativas: van en títulos de plantilla y FAQ, no en el H1.
//   · D5: títulos de las 17 plantillas y los 2 bonus = los de los xlsx EN (hotel/SPEC §2, dl/hotel-checklist-templates/).
//   · D3/D4: $29, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld, discountBadge,
//     bonusSaveLine, `value` en los bonos, aggregateRating ni review (el ES los lleva: 4,9 de 8 reseñas, -81 %, «valorados
//     en €33»). Fórmula de la tienda EN.
//   · Cifras SOLO de hotel/SPEC, F1-inventario-es.md (censo, paridad estructural comprobada contra revision/dump_en.txt)
//     y los xlsx EN: 19 libros, 74 hojas, 636 tareas (64 en el 01, 35 en el 02, 28 en el 03, 39 en el 04, 38 en el 05, 34
//     en el 06, 48 en el 07, 23 en el 08, 52 en el 09, 28 en el 10, 28 en el 11, 17 en el 12, 69 en el 13, 28 en el 14,
//     28 en el 15, 33 en el 18 con responsable y hora, 23 en el 19 y 21 en el briefing), 24 fechas en el calendario.
//   · Fuera lo que el ES afirma y el kit EN no trae: «Trail €60-75/mes», -81 %, «ahorra €76,50», «valorados en €33»,
//     «Imprimible A4» (→ US Letter), «sin internet», «53 hojas» y «11 departamentos» (→ 19 ficheros, 74 hojas), DDD, BIE,
//     OCA de baja tensión y legionela del RD 487/2022 (→ FDA Food Code, OSHA, NFPA, ASHRAE 188, MAHC 2024), anisakis (→
//     3-402.11), Día del Padre, comuniones y puentes (→ calendario US), «20 fechas» del dashboard ES (son 24) y las
//     «tareas por perfil» y los «perfiles» de dos testimonios (el hotel no trae libro de perfiles).
//   · Google Sheets: sin pastilla hasta que el test real lo confirme (SPEC base §6, §9).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'hotel-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT',

  seo: {
    title: 'Hotel Checklists Kit Pro: Housekeeping, Front Desk, F&B & Maintenance',
    description:
      '19 Excel hotel checklist files with 636 tasks already written: housekeeping, front desk, night audit, F&B, pool, maintenance, spa. One-time $29.',
    keywords:
      'hotel housekeeping checklist, hotel room cleaning checklist, hotel maintenance checklist, hotel preventive maintenance checklist, hotel front desk checklist, night audit checklist, hotel checklist template, hotel checklist excel, housekeeping checklist template, turndown service checklist, banquet event order checklist, hotel pool checklist, AI Chef Pro',
    // OG = el hero de la ficha (como los hermanos EN): el og-kit-tareas-hotel.jpg del ES lleva texto en español y €.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg',
  },

  schema: {
    productName: 'Hotel Checklists Kit Pro',
    productDescription:
      '17 templates + 2 bonuses (19 Excel files, 74 sheets) with 636 hotel tasks already written: F&B outlets (buffets, restaurant, bars, in-room dining, banquets), front desk and night audit, concierge, housekeeping, public areas, pool, patio, preventive maintenance, back office, spa, daily opening and closing rounds and a cash drawer count.',
    price: '29.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN). Sin reviews ni
    // aggregateRating (D3).
    faqs: [
      {
        q: 'What should be on a hotel housekeeping checklist?',
        a: 'Separate lists by type of clean: checkout rooms, stayover rooms, turndown service, deep cleaning and linen control. Each has its own steps, from knocking and announcing yourself and stripping the bed (checking the seams for bed bugs) to disinfecting the bathroom with an EPA-registered product, remaking the bed, checking that everything works and reporting damage. The kit includes all five, already written.',
      },
      {
        q: 'What are the steps of the night audit?',
        a: "The night audit shift checklist covers running the audit in the PMS to close the accounting day, verifying that restaurant, spa and minibar charges posted, running the occupancy, ADR, RevPAR and revenue reports, processing no-shows per policy, preparing tomorrow's arrivals and departures, a security round of the lobby and public areas and the shift log for the morning team.",
      },
      {
        q: 'What is a hotel preventive maintenance checklist?',
        a: 'A schedule of the checks that keep the building running before something breaks. The kit has daily rounds (boilers and hot water, electrical panels, the generator, HVAC, pumps), weekly and monthly lists, HVAC, plumbing and electrical sheets, and a Quarterly & Annual sheet for contracted services such as pest control, hood cleaning, extinguishers and water management, each with its frequency.',
      },
      {
        q: 'Is there a free hotel checklist template in Excel?',
        a: 'Yes, you will find free housekeeping and maintenance templates online. This kit is 19 Excel files with 636 hotel tasks already written for every department, a counter on each checklist that skips the tasks you mark N/A, temperatures in °F under the FDA Food Code and a cash count in US dollars. Print it on US Letter or save any sheet as a PDF.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C or below, information on the 14 allergens and your own pool, hot water and fire safety rules in place of the US codes cited; in Canada and Australia, your local food safety, pool and fire rules; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Hotel Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid: las 6 fotos del ES, abiertas una a una el 27-oct-2026 (sin texto en español, sin
    // logos ni marcas: los rótulos del buffet están en inglés). El og-kit-tareas-hotel.jpg del ES SÍ lleva texto en español.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-buffet.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-roomservice.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-cocina.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-banquete.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-equipo.jpg',
    ],
    // Mismo reparto que el ES.
    whyBg: '/lovable-uploads/ai-gallery/tareas-hotel-buffet.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-hotel-roomservice.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $29, once',
    // D2: titlePre + titleGold = «Hotel Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Hotel Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Housekeeping, Front Desk, F&B & Maintenance',
    description:
      '17 templates + 2 bonuses (19 Excel files) with 636 hotel tasks already written for the whole property: F&B outlets, front desk and night audit, housekeeping, pool, patio, maintenance, back office, spa and more. Print it, delegate it to your team, sign it off and file it.',
    checkItems: [
      'F&B: breakfast and lunch/dinner buffets, the restaurant, bars and grab-and-go, in-room dining and banquets',
      'Front desk: AM, PM and night audit shifts, plus the check-in and check-out procedure',
      'Housekeeping: checkout and stayover cleaning, turndown service, deep cleaning and linen control',
      'Pool, patio, public areas and spa, with logs built on the CDC Model Aquatic Health Code',
      'Maintenance: daily, weekly and monthly rounds, a Quarterly & Annual sheet (pest control, hood cleaning, extinguishers, gas, Legionella water management) and HVAC, plumbing and electrical',
      'Daily opening and closing rounds, and a cash drawer count by bill and coin with automatic over/short',
    ],
    ctaLabel: 'BUY NOW — $29',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS HOTEL COMPLETO — €18,50»).
  stickyLabel: 'HOTEL CHECKLISTS KIT PRO — $29',

  grid: {
    countGold: '17',
    headingRest: ' Hotel Checklist Templates + 2 Bonuses (19 Excel files)',
    subtitle:
      '636 hotel tasks already written and sorted by department, shift and area. Each template comes pre-filled: just adjust it, print it and delegate.',
    templates: [
      {
        icon: 'Sunrise',
        title: 'Hotel Breakfast Buffet Checklists: Setup, Service & Closing',
        desc: 'Personal hygiene and a safe kitchen start-up, setup, restocking, show cooking, parasite destruction for raw or marinated fish (FDA Food Code 3-402.11), the buffet sneeze guard and waste. 64 tasks already written in this file alone.',
      },
      {
        icon: 'UtensilsCrossed',
        title: 'Hotel Lunch & Dinner Buffet Checklists',
        desc: 'Station setup, show cooking, restocking and temperatures at 41 °F and 135 °F. A lunch list and a dinner list.',
      },
      {
        icon: 'ClipboardList',
        title: 'Hotel Restaurant Opening & Closing Checklists (À la Carte)',
        desc: 'Opening: reservations and allergies, table setup, pre-shift meeting. Closing: register, resetting, restocking, kitchen debrief. 2 checklists.',
      },
      {
        icon: 'ConciergeBell',
        title: 'Hotel Bar & Outlet Checklists: Pool Bar, Lobby Bar & Grab-and-Go',
        desc: 'Pool bar, lobby bar and lounge, and snack bar and grab-and-go. Each outlet has its own checklist, with 21+ checks on alcohol and no glass in the pool area.',
      },
      {
        icon: 'ConciergeBell',
        title: 'In-Room Dining (Room Service) & Minibar Checklists',
        desc: 'Full in-room dining (order, delivery, pickup) plus the minibar: restocking, the PMS, expiration dates.',
      },
      {
        icon: 'PartyPopper',
        title: 'Hotel Banquet & Event Checklist: From BEO to Breakdown',
        desc: 'Weddings, conferences and galas. What to settle at booking (allergies in writing, guaranteed count, price per person), the BEO, room setup, AV, vendor timing and breakdown.',
      },
      {
        icon: 'Building2',
        title: 'Hotel Front Desk Checklists: AM, PM & Night Audit Shifts, Check-In & Check-Out',
        desc: 'Morning, afternoon and night audit shifts, plus the step-by-step check-in and check-out procedure. 4 checklists.',
      },
      {
        icon: 'Users',
        title: 'Concierge & Guest Experience Checklists',
        desc: 'Concierge (transfers, tours, special requests) plus guest experience (VIPs, reviews, CRM, loyalty).',
      },
      {
        icon: 'Bed',
        title: 'Hotel Housekeeping Checklists: Checkout & Stayover Room Cleaning, Turndown, Deep Cleaning & Linen',
        desc: 'Checkout and stayover cleaning, turndown service, deep cleaning and linen control with a par level. Bed bug checks when stripping the bed, do-not-disturb welfare checks and EPA-registered disinfectants with their contact time. 5 checklists.',
      },
      {
        icon: 'Building2',
        title: 'Hotel Public Area Cleaning Checklists: Lobby, Corridors & Elevators, Restrooms & Parking',
        desc: 'Lobby, corridors and elevators, public restrooms and parking. 4 cleaning and control checklists.',
      },
      {
        icon: 'Waves',
        title: 'Hotel Pool Checklists: Daily Opening & Closing, Weekly Maintenance & Towel Service',
        desc: 'Daily opening and closing with free chlorine and pH readings logged (MAHC 2024; your state code comes first), weekly maintenance (filters, chemicals, drain covers) and towel service.',
      },
      {
        icon: 'Sun',
        title: 'Hotel Patio & Terrace Checklists: Seasonal Setup & Daily Service',
        desc: 'Seasonal setup plus daily service: furniture, umbrellas, cleaning and menu.',
      },
      {
        icon: 'Wrench',
        title: 'Hotel Preventive Maintenance Checklists: Daily Rounds to Annual, HVAC, Plumbing & Electrical',
        desc: 'Daily, weekly and monthly rounds, plus HVAC, plumbing and electrical. A Quarterly & Annual sheet for contracted services: pest control, kitchen hood cleaning (NFPA 96), extinguishers, gas, Legionella water management, elevators and boilers, each with its frequency. 7 technical checklists.',
      },
      {
        icon: 'BarChart3',
        title: 'Hotel Back-Office Checklists: Revenue Management, Reservations, Accounting & HR',
        desc: 'Revenue management, reservations, the daily accounting close and HR operations, time records under the FLSA included. 4 checklists.',
      },
      {
        icon: 'Sparkles',
        title: 'Hotel Spa & Wellness Checklists: Opening, Closing, Treatment Rooms & Locker Rooms',
        desc: 'Opening and closing, treatment rooms between guests and locker rooms. The hot tub keeps its filtration and disinfection running overnight. 4 checklists.',
      },
      {
        icon: 'Building2',
        title: 'Hotel Daily Opening & Closing Rounds: F&B Outlets & Public Areas',
        desc: 'The checklist for the outlets and public areas that open and close every day (the hotel itself never closes): lights, alarm, POS, pending check-outs, and the lock-up last. Who does it and due-by times are preloaded on every task.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing the drawer with a count by US bill and coin, the starting bank and an automatic over/short against the POS Z report. Includes a monthly log with over/short by formula across 31 days.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Hotel Daily F&B Briefing Template (Stand-Up Notes)',
        desc: 'Daily stand-up template: occupancy, VIPs, the menu of the day, the team and open issues.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Hotel F&B Calendar: 24 Key Dates & Seasons (US)',
        desc: '24 key dates for hotel F&B in the US: seasons, holidays (Valentine\'s Day, Mother\'s Day, Memorial Day, Thanksgiving, New Year\'s Eve), wedding season and conferences, with the recommended lead time.',
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a hospitality consultant since 2010.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Filled for Hotels',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a professional hotel department. Just adjust it and add what is specific to your property.",
      },
      {
        icon: 'Building',
        title: 'Every Department Covered',
        desc: 'F&B, front desk, housekeeping, pool, patio, maintenance, back office, spa. The day-to-day operation that generic systems leave out.',
      },
      {
        icon: 'Users',
        title: '636 Tasks Already Written',
        desc: 'Every department with real tasks, from the executive chef to HVAC maintenance. Ready for onboarding on day one.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $29, Once',
        desc: 'The same kind of task lists that hotels run on paid apps, in Excel and for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed F&B operations for 4- and 5-star hotels in Spain and Latin America.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 17 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Hotel Daily F&B Briefing Template',
        desc: 'The daily stand-up of the F&B department: occupancy, VIPs, the menu of the day, the team, allergens and open issues.',
        image: '/lovable-uploads/ai-gallery/tareas-hotel-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Hotel F&B Calendar: 24 Key Dates & Seasons (US)',
        desc: '24 key dates for hotel F&B in the US: high and low seasons, holidays (Valentine\'s Day, Mother\'s Day, Memorial Day, Thanksgiving), wedding season and conferences, with the recommended preparation lead time. It includes a UK note.',
        image: '/lovable-uploads/ai-gallery/tareas-hotel-banquete.jpg',
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
    ctaLabel: 'YES, I WANT THE HOTEL CHECKLISTS KIT — $29',
  },

  guarantee: {
    text: "If the checklists don't help you run your hotel's operations better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de hotel/SPEC §6 y §R (hotel housekeeping checklist; cleaning a guest room; how
  // often rooms are cleaned; bed bugs; night audit steps; preventive maintenance; free template in Excel) + las del ES
  // adaptadas (tareas ya escritas, departamentos, 3 a 5 estrellas → economy a luxury, frente a las apps, varios hoteles con
  // la licencia de la tienda EN, garantía) + F&B y seguridad alimentaria, piscina y spa, caja, firma, UK/CA/AU, moneda y
  // suscripción (como los hermanos EN). La de Latinoamérica del ES → la de UK/CA/AU.
  faqs: [
    {
      q: 'What should be on a hotel housekeeping checklist?',
      a: 'Separate lists for each type of clean, because a checkout room, a stayover room and a turndown are not the same job. The kit has five housekeeping checklists: checkout room cleaning, stayover room cleaning, turndown service, deep cleaning and linen control. Each one is already written, from knocking and announcing yourself, stripping the bed and checking for left-behind items to cleaning and then disinfecting the bathroom, remaking the bed, checking that the lights, A/C, TV and phone work, and reporting damage. Linen control counts soiled and clean linen against the laundry count sheet and checks a par of 3 sets per bed.',
    },
    {
      q: 'What is the proper procedure for cleaning a hotel guest room?',
      a: "In order: knock and announce yourself, strip the bed (checking the mattress seams and box spring for bed bugs) and look for left-behind items, empty the wastebaskets, remove used bathroom amenities and towels, clean and then disinfect the bathroom with an EPA-registered product for its label contact time, clean the furniture, put out new amenities, make the bed, vacuum or mop the whole floor and finish by checking that everything works. That is the checkout room checklist; the stayover one skips the full linen change and respects the Do Not Disturb sign with a welfare check per your hotel or brand policy. Needles, blood or fluids are handled only with gloves and a bloodborne pathogens kit (OSHA 1910.1030).",
    },
    {
      q: 'How often are hotel rooms cleaned?',
      a: "It depends on your brand standard, so the kit gives you one checklist per type of clean and you set the frequency: a checkout clean after each departure, a stayover clean on the days the guest stays (unless they decline it), a turndown service in the evening if you offer it, and a deep cleaning on a schedule you choose (moving furniture, A/C vents, curtains, steam-sanitizing the mattress, windows and drains). The Do Not Disturb sign is respected, with a welfare check per your policy.",
    },
    {
      q: 'How do hotels prevent bed bugs, and does the kit cover it?',
      a: "Partly, and it says so. Room attendants check the mattress seams and box spring when stripping the bed and tell their supervisor if they see anything; the Quarterly & Annual maintenance sheet lists monthly pest control by a licensed company with a rotating sample of guest rooms for bed bugs and a signed service report on file. The kit is a checklist, not a pest management program: treatment itself is for your licensed operator.",
    },
    {
      q: 'What are the steps of the night audit?',
      a: "The night audit shift checklist covers running the night audit in the PMS to close the accounting day, verifying that restaurant, spa and minibar charges posted correctly, generating the occupancy, ADR, RevPAR and revenue-by-department reports, processing no-shows per policy, preparing tomorrow's departures and arrivals, staffing the night front desk, a visual security round of the lobby and public areas, checking access doors and cameras, and writing the shift log for the morning team. The AM and PM shifts and the check-in and check-out procedure each have their own checklist.",
    },
    {
      q: 'What is a hotel preventive maintenance checklist, and what does the kit include?',
      a: "It is the schedule of checks that keep the building running before something breaks. The kit has daily rounds (boilers and domestic hot water at 140 °F or above in the storage tank, electrical panels, the emergency generator, HVAC, pumps, a visual round of public areas), weekly and monthly lists, and separate HVAC, plumbing and electrical sheets. A Quarterly & Annual sheet lists the contracted services, each with its frequency: pest control, kitchen hood and duct cleaning at the NFPA 96 frequency, thermometer calibration, water management for Legionella (ASHRAE 188), sprinklers and fire alarm, extinguishers, gas, electrical, elevators and boilers (your state inspector sets the rules), evacuation drills on every shift, insurance and permits. Your local code governs the exact intervals.",
    },
    {
      q: 'Is there a free hotel checklist template in Excel or PDF?',
      a: 'Yes, you will find free housekeeping and maintenance templates online, and a single one is fine to get started. This kit is something else: 19 Excel files with 636 hotel tasks already written and sorted by department, shift and area, a counter on every checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Does it cover the hotel restaurant, buffets, banquets and in-room dining?',
      a: "Yes, F&B is half of the kit. Breakfast buffet and lunch and dinner buffet checklists (stations, restocking, show cooking, temperatures), restaurant opening and closing, the pool bar, lobby bar and snack bar, in-room dining with the minibar, and banquets and events from the BEO to breakdown. Food safety follows the FDA Food Code: 41 °F cold and 135 °F hot, the buffet sneeze guard, a clean plate on every trip, a watched buffet, the 9 major allergens and alcohol served to guests 21 and over.",
    },
    {
      q: 'Does it cover the pool and the spa?',
      a: "Yes. The pool workbook has opening and closing with free chlorine and pH readings logged before opening and during the day, weekly maintenance (filters, chemicals, drain covers, the pool log kept for 3 years) and towel service; the spa workbook covers opening and closing, treatment rooms and locker rooms, with the hot tub kept at 104 °F or below and its sign posted. The pool and spa figures follow the CDC Model Aquatic Health Code (2024), which is a model code: your state or county code comes first. At closing, the hot tub's filtration and disinfection stay on overnight; only the jets and the air blower are switched off.",
    },
    {
      q: 'Does it include a cash drawer count?',
      a: 'Yes. A cash drawer workbook with an opening sheet, a closing sheet and a monthly log. You count by US bill and coin, and the sheet works out the cash counted, the starting bank deducted, the total collected and the over/short against your POS Z report, which turns amber when the drawer does not balance. The monthly log gives one row per day, so you see at a glance which days did not balance.',
    },
    {
      q: 'Does it work for a small hotel, a midscale property or a resort?',
      a: 'Yes. The checklists scale from economy to luxury. A small property can start with breakfast, housekeeping, the front desk and maintenance; a resort or full-service hotel can use all 17 templates. If you have no pool, spa or banquet space, you can mark those tasks N/A, or just skip the file. The instructions in each file suggest adjusting the stations to the category of your hotel (economy, midscale, upscale or luxury).',
    },
    {
      q: 'Are the tasks already filled in for a hotel?',
      a: "Yes. Every checklist comes with the real tasks of a professional hotel department already written: 636 in total. You'll want to make it yours: adjust tasks to your property, delete the ones that don't apply and add your own. The editable cells are green, and the opening and closing rounds and the cash drawer files end with 5 free green rows that the counter already includes.",
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for the area, who does it, ✓ (a drop-down with ✓, — for not done, or N/A) and notes, and a signature line at the bottom ("Signed off by"). The opening and closing rounds and the cash drawer files come with who does it and a due-by time already filled in. The manager on duty prints the checklist and hands it out, each person checks off their tasks, and at the end of the shift the manager on duty checks it and signs.',
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $29, a one-time payment, for the whole hotel. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it in several hotels?',
      a: "Yes. One purchase covers one business with all of its properties, which makes it a good fit for hotel groups. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 135 °F hot holding), the 9 major allergens, US codes cited for the pool, fire safety and hot water, and a cash count in US bills and coins. In the UK, chilled food is kept at 8 °C or below and allergen information covers 14 allergens (the kit's allergen tasks already note the UK's 14); check your pool against the PWTAG guidance, your hot water against HSE L8 (60 °C stored, 50 °C at the outlets), your fire precautions against the Regulatory Reform (Fire Safety) Order 2005 and your allergen labels against the Food Information Regulations 2014. In Canada and Australia, check your provincial or state rules and type them into the tasks. For pounds, Canadian or Australian dollars, unprotect the cash count sheet and change the label and value of each bill and coin. The F&B calendar has a UK note (bank holidays, Mothering Sunday and Boxing Day) and room for your own dates. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $29 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you.',
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
    heading: 'Standardize the Operations of Your Whole Hotel',
    subtitle: "17 templates + 2 bonuses (19 Excel files) with 636 hotel tasks already written, for less than one hour of a consultant's time.",
    items: [
      'F&B: buffets, restaurant, bars, in-room dining and banquets',
      'Front desk: AM, PM and night audit shifts, check-in and check-out',
      'Housekeeping: checkout, stayover, turndown, deep cleaning and linen',
      'Pool, patio and public areas (lobby, corridors, restrooms, parking)',
      'Maintenance: daily, weekly, monthly, quarterly and annual, plus HVAC, plumbing and electrical',
      'Back office: revenue management, reservations, accounting and HR',
      'Spa and wellness: opening, closing, treatment rooms and locker rooms',
      'Daily opening and closing rounds + cash drawer count by bill and coin',
      'BONUS: Hotel Daily F&B Briefing Template',
      'BONUS: Hotel F&B Calendar: 24 Key Dates & Seasons (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE HOTEL CHECKLISTS KIT — $29',
  },

  // Testimonios: traducción fiel de los del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes: Hotel
  // Completo, la edición española de este kit: por eso conservan sus nombres y cifras, y el subtítulo lo dice. Solo se
  // pintan: NO alimentan el JSON-LD. SIN MARCAS NI HOTELES REALES (hotel/SPEC D-HOT, como los hermanos): el ES cita
  // «Hotel Palace», «Meliá», «W Barcelona», «Ritz-Carlton», «Four Seasons», «NH», «Hoteles Ibéricos» y «Hospitality
  // Experts» → rol + tipo de hotel (+ ciudad cuando el ES la daba). Frases cambiadas SOLO donde chocaban con el kit (regla
  // de John, 11-oct: testimonio que contradice el kit → cambiar solo esa frase): Miguel Ángel Torres hablaba de «tareas por
  // perfil para camarero» y Carlos Navarro de «las tareas de F&B manager y los perfiles»: el hotel no trae libro de perfiles
  // (SPEC §2); Daniela Hernández se presentaba como Revenue Manager y hablaba como F&B manager de grupo (rol = lo que dice).
  testimonials: {
    subtitle:
      'F&B managers, executive chefs and hotel directors who already run their operations with Kit de Tareas Recurrentes: Hotel Completo, the Spanish edition of this kit',
    items: [
      {
        name: 'Pablo Moreno',
        role: 'F&B Manager, luxury city hotel, Madrid',
        text: 'The breakfast buffet checklist eliminated the missed steps in the setup. Before, every shift set up differently. Now the standard is the same at 6:30 in the morning as at 10.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Ricardo Castillo',
        role: 'Executive Chef, beach resort, Costa del Sol',
        text: 'I manage 4 outlets and 120 buffet covers. The checklists for each outlet let me delegate with confidence. Temporary staff know exactly what to do from day one.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Elena Vargas',
        role: 'Banquet Director, lifestyle hotel, Barcelona',
        text: 'The banquet checklists cover weddings, conferences and gala dinners with the level of detail we need. The BEO checklist is exactly what was missing from our operation.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Miguel Ángel Torres',
        role: "Maître d', luxury hotel",
        text: 'The restaurant, banquet and in-room dining checklists are perfect for onboarding new servers. Service protocol, room charges, the pre-shift briefing... it is all covered.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Ana Belén Ruiz',
        role: 'Head of In-Room Dining, luxury resort hotel',
        text: 'We rolled out the in-room dining checklist and delivery times improved by 30%. The room service protocol is exactly the standard we needed.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Daniela Hernández',
        role: 'Group F&B Manager, hotel chain',
        text: 'As a group F&B manager, these checklists let me standardize operations across 6 hotels. The daily briefing is now mandatory in all of our properties.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Santiago Delgado',
        role: 'Executive Housekeeper, boutique hotel',
        text: 'The minibar checklist organized my restocking rounds. Before, we lost stock and the charges were not billed. Now everything is on record.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Javier Martín',
        role: 'Director of Operations, independent hotel group',
        text: 'The annual hotel F&B calendar is brilliant. Seasons, holidays, conferences... it lets us plan temporary staff and purchasing months ahead.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Isabel Fernández',
        role: 'Hospitality Consultant, hotel F&B',
        text: 'I recommend this kit to all my hotel clients. Breakfast, in-room dining, banquets... they cover 95% of the F&B operation of any upscale or luxury hotel.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Carlos Navarro',
        role: 'Professor, Hospitality Management School',
        text: 'My students in the hotel management master’s program use these checklists as a reference. The F&B, housekeeping and front desk checklists are perfectly structured.',
        avatar: '/avatars/chef-avatar-3.jpg',
      },
    ],
  },

  pricing: {
    price: '$29',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    // D4: obligatorio en KitTareasPricing; sin «valor total» ni ahorro (FTC).
    bonusTotalLabel: 'Everything included: 17 templates + 2 bonuses',
  },

  // Pie: los 9 hermanos EN de checklists, los 5 kits EN y el eBook (no hay caso de uso EN de hotel que enlazar: sin saliente extra).
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
    { href: '/en/digital-products/taco-shop-checklist-templates', label: 'Taco Shop Checklists Kit Pro' },
    { href: '/en/digital-products/food-truck-checklist-templates', label: 'Food Truck Checklists Kit Pro' },
    { href: '/en/digital-products/bakery-checklist-templates', label: 'Bakery Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'hotel-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
