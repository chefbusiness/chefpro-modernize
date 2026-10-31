// astro-site/src/data/productos-en/tareas/bar-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Bar Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-bar.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de su hermano EN
// restaurant-checklist-templates.ts. SPEC: scripts/productos-digitales/checklists-kit/bar/SPEC.md (delta) + la base.
//   · D2: nombre «Bar Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Bar Checklists Kit Pro: Bar Opening & Closing Checklist Templates for Excel».
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (bar/SPEC §2, dl/bar-checklist-templates/).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos. Fórmula de la tienda EN.
//   · Cifras y normas SOLO de bar/SPEC §3 y de la base (FDA Food Code 2022, Brewers Association, notas UK).
//     Alcohol: horas, last call, happy hour y promociones siempre «check your state's ABC/liquor authority».
//     Lo que el ES afirma y el kit no trae, fuera: Halloween y St. Patrick no son hojas del 06 (están en el
//     calendario), la presión «2,5-3 bar» y el «cóctel gratis» (D-BAR), las 17 fechas del dashboard ES (son 23).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como el hermano EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual (nombres,
//     negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan.
//   · Imágenes: las 7 del ES no llevan texto en español (rótulos en inglés: «PREMIUM SPIRITS», «THE BOTANICAL») →
//     se quedan. og-kit-tareas-bar.jpg sí («Kit de Tareas Recurrentes», «€12», «Imprimible A4») → fuera; OG = la
//     portada del hero ES (sin texto) hasta tener una OG EN propia (F3-NOTAS). Bonus 3 = en-equivalents-guide.jpg.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_BAR_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'bar-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_BAR_CHECKLISTS_KIT',

  seo: {
    title: 'Bar Checklists Kit Pro: Bar Opening & Closing Checklist Templates for Excel',
    description:
      '11 Excel bar checklists with 342 tasks already written: opening & closing, cocktail, draft beer & wine stations, bar manager, bartender duties by role, inventory, cash count. One-time $19.',
    keywords:
      'bar opening checklist, bar closing checklist, bar checklist, bartender checklist, bar cleaning checklist, bar opening and closing checklist template, bartender opening checklist, bar manager checklist, barback duties, bar inventory checklist, beer line cleaning, cash drawer count sheet, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
  },

  schema: {
    productName: 'Bar Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for bars and cocktail bars with 342 tasks already written: bar opening and closing, whole venue, cash drawer, cocktail, draft beer and wine stations, bar manager, duties by role, weekly inventory, cleaning and maintenance, events and holidays.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a bar opening checklist?',
        a: 'Personal hygiene first, then the bar: lights and music, coolers checked, citrus and garnish prep, ice wells filled with a scoop, the speed rail set, juices and syrups, glassware and tools, the espresso machine and the patio. The whole venue gets its own list: alarm, lights, HVAC, POS, restrooms, draft taps and CO₂. Each task needs who does it, a due-by time and initials.',
      },
      {
        q: 'What goes on a bar closing checklist?',
        a: 'Last call, glassware collected, ice wells emptied, garnish, juices and syrups wrapped, labeled and stored, the bar top, sink, beer taps, espresso machine and floor cleaned, open bottles and waste logged, the cash drawer closed, the patio put away and the venue locked up with the alarm set.',
      },
      {
        q: 'How often should beer lines be cleaned?',
        a: 'Every 2 weeks, with an acid clean every 3 months, as the Brewers Association recommends. Kegs are kept at 38 °F and the CO₂ pressure is the one your draft tech or distributor set for your system.',
      },
      {
        q: 'Is there a free bar checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 342 bar tasks already written, a counter that skips N/A tasks, °F temperatures and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'Does it cover liquor laws?',
        a: 'It builds responsible service into the tasks (21+ and ID checks, no service to visibly intoxicated guests, occupancy limit, server training where required). Closing time, last call and happy hour rules vary by state, so those tasks tell you to check your state\'s ABC/liquor authority.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits in cells you can change: in the UK, Challenge 25, your licensing hours and the personal licence holder; in Canada and Australia, the local legal drinking age and server training (RSA in Australia); for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Bar Checklists Kit Pro',
  },

  images: {
    // Las mismas 7 fotos del ES: ninguna lleva texto en español (ver cabecera).
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
    ],
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Bar Checklists Kit Pro»; Forma B como el hermano EN.
    titlePre: 'Bar Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Bar Opening & Closing Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 342 bar tasks already written: opening, closing, whole venue, cash drawer, bar stations, manager, roles, events and holidays. Print it, delegate it to your team, initial it and file it.',
    checkItems: [
      'Bar opening and closing checklists: bar station, coffee machine, patio',
      'Whole-venue opening and closing, and a cash drawer count by bill and coin',
      'Bar stations: cocktails, draft beer, wine by the glass and cellar',
      'Tasks by role: head bartender, bartender, barback, cocktail server',
      "Event checklists: cocktail night, New Year's Eve, happy hour, tastings",
      '3 editable master templates + a bar pre-shift meeting template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS BAR — €12»).
  stickyLabel: 'BAR CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Bar Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '342 bar and cocktail bar tasks already written and sorted by shift, area and role. Adjust them to your bar, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Bar Opening & Closing Checklists: Bar Station, Coffee & Patio',
        desc: 'Bar opening and closing: personal hygiene, bar mise en place, glassware and tools, the espresso machine, the patio and the end-of-night close. Every task with who does it, when and initials. 54 tasks already written in this file alone.',
      },
      {
        icon: 'Wine',
        title: 'Bar Station Checklists: Cocktails, Draft Beer & Wine',
        desc: 'Cocktail station (spirits, batches, syrups, bitters, garnish and ice, always with a scoop or tongs), draft beer station (kegs at 38 °F, CO₂ pressure set by your draft tech) and wine by the glass and cellar, with temperatures in °F.',
      },
      {
        icon: 'ClipboardList',
        title: 'Bar Manager Checklist: Daily, Weekly & Monthly',
        desc: 'Daily checklist (before opening, during service, end of day), weekly checklist with one focus a day (inventory, team, quality, menu, weekend prep) and monthly checklist (pour cost, waste, maintenance, team review).',
      },
      {
        icon: 'Users',
        title: 'Bartender Checklist & Daily Duties by Role (Head Bartender, Bartender, Barback, Server)',
        desc: 'Checklists for the head bartender, bartender, barback and cocktail server: the daily duties of each position, shift after shift.',
      },
      {
        icon: 'CalendarDays',
        title: 'Bar Cleaning Checklist, Inventory & Maintenance Schedule',
        desc: 'Weekly deep clean, monthly maintenance of the draft system, espresso machine and coolers, and a weekly inventory by category (spirits, beer, wine, mixers, consumables) with a shelf-life table for open products. + a Quarterly & Annual sheet for contracted services: pest control, fire extinguishers, draft system service, refrigeration, music licensing (ASCAP, BMI, SESAC, GMR) and your liquor license renewal, with the service report number and initials.',
      },
      {
        icon: 'PartyPopper',
        title: "Bar Event Checklists: Cocktail Night, New Year's Eve, Happy Hour & Tastings",
        desc: "A special cocktail night, New Year's Eve, a weekly happy hour and guided pairings and tastings, with the terms to put in writing when a private tasting is booked.",
      },
      {
        icon: 'FileEdit',
        title: 'Blank Bar Checklist Template (Editable)',
        desc: '3 master templates already structured (by time of day, by area and by role) with the sections and the area or person in charge set up: you just type your tasks in the green cells.',
      },
      {
        icon: 'Building2',
        title: 'Bar Opening & Closing Checklist (Whole Venue)',
        desc: 'The checklist for the whole venue, not just the bar: alarm, lights, HVAC, POS, restrooms, patio, draft taps and CO₂. Who does it and the due-by time are filled in for all 33 tasks.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. Plus a monthly cash log with the over/short by formula.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Bar Pre-Shift Meeting Template (Line-Up Notes)',
        desc: "Bar pre-shift meeting template: cocktail of the day, reservations and private events, VIPs and regulars, active promotions, 86'd items and the team on shift.",
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Bar Holiday & Events Calendar (US)',
        desc: "23 key US dates for bars, from Mardi Gras and St. Patrick's Day to Thanksgiving Eve and New Year's Eve, with their tasks and recommended lead time in editable cells, plus a UK note.",
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
        title: 'Pre-Filled for Bars',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a professional bar. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Wine',
        title: 'The Whole Bar, Cocktails Included',
        desc: "Spirits, batches, syrups, draft beer, wine by the glass, espresso. The tasks generic checklist apps don't cover.",
      },
      {
        icon: 'Users',
        title: 'Duties by Role',
        desc: 'Checklists for the head bartender, bartender, barback and cocktail server. Everyone knows exactly what to do every shift.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists bars run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
      },
    ],
    // Pastillas del hermano EN: sin Google Sheets hasta el test real (SPEC base §6, §9); «A4» → US Letter.
    compatLabel: 'Compatible with:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants, bars and cocktail bars.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Bar Pre-Shift Meeting Template',
        desc: 'The 5-minute meeting that separates good bars from great ones. Cocktail of the day, reservations, VIPs, promotions, the team on shift.',
        image: '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Bar Holiday & Events Calendar (US)',
        desc: "23 key dates for US bars (Mardi Gras, St. Patrick's Day, Cinco de Mayo, the Fourth of July, Halloween, Thanksgiving Eve, New Year's Eve, Negroni Week) with tasks and recommended lead time.",
        image: '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
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
    ctaLabel: 'YES, I WANT THE BAR CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your bar's operations better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de bar/SPEC D5 (bar opening / closing / bartender checklist, limpieza de
  // líneas) + las del ES adaptadas (tareas ya escritas, coctelería, tipos de bar, frente a las apps, varios locales
  // con la licencia de la tienda EN) + alcohol, UK/CA/AU, moneda, suscripción y garantía (como el hermano EN).
  faqs: [
    {
      q: 'What should be on a bar opening checklist?',
      a: 'Start with personal hygiene (clean uniform, cuts covered, hands washed at the bar sink), then set up the bar: lights and music on, the coolers and back bar cooler checked after the night with the reading logged, citrus and garnish prepped, ice wells filled with a scoop, never a glass, enough ice for the shift (65–110 lb), the speed rail stocked, fresh juices and the syrups of the day, glassware polished and the bar tools ready, the espresso machine warmed up and dialed in, and the patio set. The whole venue has its own list: alarm, lights, HVAC, POS, restrooms, draft taps and CO₂. Every task needs who does it, a due-by time and initials. The "Bar Opening & Closing Checklists" workbook has the bar written out, and the "Bar Opening & Closing Checklist (Whole Venue)" covers the building.',
    },
    {
      q: 'What goes on a bar closing checklist?',
      a: "Last call 30 minutes before closing, glassware collected, ice wells emptied and cleaned, citrus, garnish, juices and syrups wrapped, labeled and stored, speed rail bottles capped, and the shaker, jigger and strainers washed. Then the cleaning: bar top, bar sink, beer taps, espresso machine (backflush), grinder, glass washer and the floor behind the bar. Open bottles and the shift's waste (broken glassware, spills, sent-back drinks) get logged, the cash drawer count gets closed and signed, the patio gets put away, and the venue is locked up: POS, lights and HVAC off, alarm set. Closing time and the end of alcohol sales are set by your state and city: check your state's ABC/liquor authority.",
    },
    {
      q: "What's on a bartender checklist?",
      a: "Before service, the bartender sets up their station: garnish cut, syrups of the day, glassware polished, the speed rail stocked. During service, cocktails to spec, draft beer, wine by the glass and coffee, with the station kept clean. At close, the station is cleaned, the mise en place goes into the cooler and the tools are washed and put away. In this kit, the \"Bartender Checklist & Daily Duties by Role\" workbook has one checklist each for the head bartender, bartender, barback and cocktail server, and the cocktail, draft beer and wine stations have their own checklists.",
    },
    {
      q: 'How often should beer lines be cleaned?',
      a: "Every 2 weeks, plus an acid clean every 3 months, as the Brewers Association's Draught Beer Quality Manual recommends. The kit also keeps kegs at 38 °F and leaves the CO₂ pressure to the number your draft tech or distributor set for your system, because it depends on the system and the gas. Line cleaning shows up on the monthly maintenance sheet and on the bar manager's monthly checklist, so someone checks off and initials every cleaning in the period, and the Quarterly & Annual sheet adds the draft system service.",
    },
    {
      q: 'Is there a free bar checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 342 bar tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, temperatures in °F and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a bar?',
      a: "Yes. Every checklist comes with the real tasks of a professional bar already written. You'll want to make it yours: adjust tasks to your bar, delete the ones that don't apply and add your own. The editable cells are green, and each table ends with 5 free green rows that the counter already includes.",
    },
    {
      q: 'Does it include cocktail prep?',
      a: 'Yes. The cocktail station checklist covers spirits, vermouth and bitters stock, batches of your high-volume cocktails, infusions, house syrups, citrus twists, a written allergen list for the cocktail menu, a quality check on every drink and a clean station between drinks. Adjust it to your own recipes.',
    },
    {
      q: 'Does it work for a neighborhood bar, a cocktail bar or a hotel bar?',
      a: 'Yes. The templates scale. A small bar can use the bar station and patio lists. A premium cocktail bar can add the cocktail station, the cellar and the events. A hotel bar can use every area.',
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same task lists in Excel for $19, a one-time payment. No subscription, no internet needed. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it in several bars or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for bar groups. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it cover liquor laws and responsible alcohol service?',
      a: "It builds them into the tasks: 21+ and ID checks, no service to guests who are visibly intoxicated, the occupancy limit posted by the fire marshal, and responsible alcohol service training (TIPS, ServSafe Alcohol or another approved course) where your state requires it. Closing time, last call, happy hour and drink promotions vary by state and city, so those tasks tell you to check your state's ABC/liquor authority, and the Quarterly & Annual sheet reminds you to renew your liquor license. It's an operating tool, not legal advice.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change. The kit is set up for the US: 21+ ID checks, temperatures in °F under the FDA Food Code, draft beer at 38 °F and a cash count in US bills and coins. In the UK, the legal age is 18 and many bars run Challenge 25 (the bar manager's daily checklist already mentions it); every alcohol sale has to be made or authorized by a personal licence holder, and your premises licence sets your licensing hours, so type your own times into the last call and closing tasks. Cold holding is 8 °C and allergen information covers 14 allergens, sulfites included. The events calendar has a UK note: bank holidays, Boxing Day and a Temporary Event Notice if you want to open beyond your licence. In Canada, the legal drinking age is 19 in most provinces and 18 in Alberta, Manitoba and Quebec, and provinces such as Ontario (Smart Serve) and British Columbia (Serving It Right) require server training. In Australia, the legal age is 18 and bar staff need a Responsible Service of Alcohol (RSA) certificate. For pounds, Canadian or Australian dollars, unprotect the cash count sheet (there is no password) and change the label and value of each bill and coin. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
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
    heading: 'Stop Repeating the Same Instructions Every Shift',
    subtitle: "9 templates + 3 bonuses (12 files) for your bar for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: bar station, coffee machine, patio',
      'Whole-venue opening and closing, and a cash drawer count with automatic over/short',
      'Bar stations: spirits, batches, draft beer, wine by the glass',
      'Weekly inventory: spirits, beer, wine, mixers, consumables',
      'Bar manager checklists: daily, weekly and monthly',
      'Tasks by role: head bartender, bartender, barback, cocktail server',
      "Events: cocktail night, New Year's Eve, happy hour, tastings",
      'BONUS: Bar Pre-Shift Meeting Template',
      'BONUS: Bar Holiday & Events Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE BAR CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 10 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas
  // Recurrentes: Bar / Cocktails, la edición española de este kit: por eso conservan sus nombres, negocios y
  // cifras, y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Bartenders, bar managers and bar owners who already run their operations with Kit de Tareas Recurrentes: Bar / Cocktails, the Spanish edition of this kit',
    items: [
      {
        name: 'Álvaro Reyes',
        role: 'Head Bartender, The Alchemist Bar',
        text: 'The bar mise en place checklist changed my life. Every bartender used to set up their own way, and something was always missing in the middle of service. Now everything is ready before we open.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Claudia Martín',
        role: 'Owner, Cocktail Lab BCN',
        text: 'I opened my cocktail bar 8 months ago and the chaos of the first few weeks was brutal. The checklists by area and shift brought order from the day we printed them.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Roberto Vega',
        role: 'General Manager, Grupo Bar Madrid',
        text: 'We have 4 bars, and each manager used to do things differently. With the checklists, we have standardized our operations. Barback onboarding went from 3 weeks to 5 days.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Marina Torres',
        role: 'Bartender, Hotel Arts Barcelona',
        text: "The tasks by role are great. As a bartender, I know exactly what I have to do before, during and after service. There's no excuse for forgetting anything.",
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Ruiz',
        role: 'Head Bartender, Speakeasy Madrid',
        text: 'The weekly inventory by category (spirits, beer, wine, mixers) is exactly what we needed. Our pour cost used to surprise us every month. Now we keep it under control.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Sofía Hernández',
        role: 'Manager, Vermutería El Rincón',
        text: "The beer tap cleaning and espresso machine maintenance checklists have saved us from breakdowns. We didn't have a preventive maintenance routine before.",
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Ignacio López',
        role: 'Barback, Cocktail Bar Negroni',
        text: "As a barback, my checklist tells me exactly what to restock, when and where. I don't have to ask the bartender every 5 minutes. It gives me autonomy.",
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Enrique Campos',
        role: 'Director of Operations, Grupo Nightlife',
        text: "The annual calendar with the key dates (New Year's Eve, Halloween, St. Patrick's Day) helps us plan stock and staff weeks ahead. We used to improvise, and it showed.",
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo García',
        role: 'Bar & Restaurant Consultant',
        text: 'The first thing I do with every new client is hand them these checklists. Bar, cellar, patio, inventory... they cover 95% of what any professional bar needs.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Carlos Navarro',
        role: 'Bartending Instructor, Hospitality School',
        text: "I recommend this kit to all my students. The cocktail, stock control and bar closing tasks are perfectly structured. It's the standard every bar should have.",
        avatar: '/avatars/chef-avatar-3.jpg',
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
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
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
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/mobile-bar-business-plan', label: 'Mobile Bar Business Plan Kit' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'bar-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
