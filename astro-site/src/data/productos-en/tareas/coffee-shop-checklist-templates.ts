// astro-site/src/data/productos-en/tareas/coffee-shop-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Coffee Shop Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-cafeteria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-checklist-templates.ts y bar-checklist-templates.ts. SPEC: scripts/productos-digitales/checklists-kit/
// cafe/SPEC.md (delta) + la base.
//   · D2: nombre «Coffee Shop Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Coffee Shop Checklists Kit Pro: Coffee Shop Opening & Closing Checklist Templates for Excel». «cafe» sin tilde.
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (cafe/SPEC §2, dl/coffee-shop-checklist-templates/).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos. Fórmula de la tienda EN.
//   · Cifras y normas SOLO de cafe/SPEC §3 (REGLAS_US de mapas_cafe.py) y de la base: 41 °F (leche, vitrina),
//     date marking 7 días, sin mano desnuda, hielo = alimento, backflush diario y descale según el fabricante,
//     «25–30 s / 25–30 ml (about 1 fl oz)», «9 bar», muelas en lb, alcohol solo con licencia y 21+ con ID.
//   · Lo que el ES afirma y el kit no trae, fuera: «latte art del día» y «temperatura de tazas» en el barista (el
//     latte art está en San Valentín y en la formación del 03), «barista jefe» y «responsable de cocina» (los perfiles
//     son Shift Lead, Barista, Baker, Server y Busser & Runner), el semanal «lun-vie con foco por día» (es un semanal
//     de lunes por bloques), «pre-evento 48 h» y «pop-ups» (las hojas del 06 son Sunday Brunch, Valentine's Day,
//     Holiday Season y Patio Season), las «17 fechas» del dashboard ES (son 22 + 5 filas libres). Cold brew: una celda.
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual (nombres,
//     negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan.
//     Dos frases que el kit contradice, cambiadas (regla de John, 11-oct): Andrés Gallego («48 h antes, día
//     anterior, mañana» → la estructura real del brunch) y Diego Navarro («rotación de vitrinas… todo organizado
//     por día» → lo que trae el semanal del manager, por bloques). «A4» de Patricia Vega → «one sheet».
//   · Imágenes: con texto en español, fuera → sustituidas por fotos EN ya publicadas de la familia coffee shop:
//     tareas-cafeteria-hero («TOMA CAFÉ») → use-case-coffee-shop-hero (pizarra en $), -vitrina (etiquetas y precios
//     en español y en €) → use-case-coffee-shop-pastries (etiquetas en inglés), -inventario («LECHE ENTERA»,
//     «ALMENDRA») → use-case-coffee-shop-bar, og-kit-tareas-cafeteria («Kit de Tareas», «€12») → OG = el hero EN.
//     Se quedan las que no llevan texto en español: barista («THE DAILY GRIND»), brunch, terraza, equipo.
//     Los fondos del ES (cochinillo, gambas, risotto: quirk de la SPA) se sustituyen por fotos de cafetería.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'coffee-shop-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_CHECKLISTS_KIT',

  seo: {
    title: 'Coffee Shop Checklists Kit Pro: Coffee Shop Opening & Closing Checklist Templates for Excel',
    description:
      '11 Excel coffee shop checklists with 500 tasks already written: opening & closing, espresso bar, pastry case, barista duties, manager, cleaning, cash count. One-time $19.',
    keywords:
      'coffee shop opening checklist, coffee shop closing checklist, coffee shop checklist, cafe checklist, barista checklist, cafe cleaning checklist, coffee shop opening and closing checklist template, barista opening checklist, coffee shop manager checklist, espresso machine cleaning checklist, pastry case checklist, cash drawer count sheet, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/use-case-coffee-shop-hero.jpg',
  },

  schema: {
    productName: 'Coffee Shop Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for coffee shops and brunch cafes with 500 tasks already written: opening and closing by area, whole shop, cash drawer, espresso bar, kitchen and pastry case, manager, duties by role, inventory, cleaning and maintenance, Sunday brunch, events and holidays.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a coffee shop opening checklist?',
        a: 'Personal hygiene first, then each area: the kitchen (hood, oven, griddle, cooler readings), the front of house and patio, and the espresso bar: machine warmed up, group heads purged, grinder dialed in with a test shot, milk, beans and syrups stocked, the ice bin filled with a scoop and the pastry case stocked, labeled and at 41 °F or below. The whole shop gets its own list: alarm, lights, HVAC, POS and patio. Each task needs who does it, a due-by time and initials.',
      },
      {
        q: 'What goes on a coffee shop closing checklist?',
        a: 'Backflush the espresso machine group by group, clean the portafilters, steam wand and drip tray, empty the knock box and brush the grinder. Date and store leftover pastries, put open milk back in the fridge at 41 °F or below, wash the milk pitchers, empty the ice bin, close the cash drawer against the POS Z report and lock up with the alarm set.',
      },
      {
        q: 'How often should you backflush and descale an espresso machine?',
        a: 'Backflush every day at close with espresso machine detergent, following the manufacturer\'s instructions. Descale as the manufacturer says (on many commercial machines your espresso tech does it). The kit puts the backflush on the closing checklists, descaling on the monthly maintenance sheet, and the water filter, water hardness and a full tech service on the quarterly and annual sheet.',
      },
      {
        q: 'Is there a free coffee shop checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 500 coffee shop tasks already written, a counter that skips N/A tasks, °F temperatures and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'How do you keep a pastry case food safe?',
        a: 'Keep cream cakes, cheesecake and dairy-filled pastries at 41 °F or below and log the reading, date-mark them for 7 days at most, serve with tongs, bakery tissue or gloves, never bare hands, and label every item with its name, price and allergens (the 9 major allergens in the US).',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits in cells you can change: in the UK, cold holding at 8 °C, hot holding at 63 °C and 14 allergens on your labels; in Canada and Australia, your local holding temperatures and allergen list; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Coffee Shop Checklists Kit Pro',
  },

  images: {
    // Ver cabecera: fuera las 3 fotos del ES con texto en español (hero, vitrina, inventario) y los 3 fondos ajenos.
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-coffee-shop-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-barista.jpg',
      '/lovable-uploads/ai-gallery/use-case-coffee-shop-pastries.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-terraza.jpg',
      '/lovable-uploads/ai-gallery/use-case-coffee-shop-bar.jpg',
    ],
    // Como el ES: el strip de la rejilla empieza en barista y termina en equipo.
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-cafeteria-barista.jpg',
      '/lovable-uploads/ai-gallery/use-case-coffee-shop-pastries.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-terraza.jpg',
      '/lovable-uploads/ai-gallery/use-case-coffee-shop-bar.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-cafeteria-barista.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-coffee-shop-bar.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/use-case-coffee-shop-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Coffee Shop Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Coffee Shop Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Coffee Shop Opening & Closing Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 500 coffee shop and brunch tasks already written: opening, closing, whole shop, cash drawer, espresso bar, pastry case, manager, roles, brunch and events. Print it, delegate it to your team, initial it and file it.',
    checkItems: [
      'Opening and closing checklists by area: kitchen, front of house and patio, espresso bar',
      'Whole-shop opening and closing, and a cash drawer count by bill and coin',
      'Barista tasks: dialing in the grinder, purging, backflushing, milk and syrup stock',
      'Pastry case control and a Sunday brunch checklist',
      'Manager checklists: daily, weekly and monthly, plus a shift handover',
      '3 editable master templates + a pre-shift meeting template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS CAFETERÍA — €12»).
  stickyLabel: 'COFFEE SHOP CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Coffee Shop Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '500 coffee shop and brunch tasks already written and sorted by shift, area and role. Adjust them to your shop, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Coffee Shop Opening & Closing Checklists: Espresso Bar, Kitchen & FOH',
        desc: '6 checklists: kitchen, front of house (patio included) and espresso bar opening, and the same three at closing. Every task with who does it, when and initials. 130 tasks already written in this file alone.',
      },
      {
        icon: 'Coffee',
        title: 'Cafe Kitchen Checklists: Hot Line, Cold Station & Pastry Case',
        desc: 'Hot line (griddle, oven, eggs, pancakes, toast), cold station (bowls, fruit, salads, avocado, with the cooler reading in °F) and the pastry case: the morning bake, a refrigerated case at 41 °F or below for cream cakes and cheesecake, labels with name, price and allergens, tongs or gloves, FIFO rotation and the day\'s waste.',
      },
      {
        icon: 'ClipboardList',
        title: 'Coffee Shop Manager Checklist: Daily, Weekly, Monthly & Shift Handover',
        desc: 'Daily checklist (before opening, during service, admin, at close), a Monday weekly checklist (sales, orders and stock, team, maintenance) and a monthly checklist (P&L, food cost, labor, team, equipment, menu and reviews). Plus a shift handover so nothing gets lost between shifts.',
      },
      {
        icon: 'Users',
        title: 'Barista Checklist & Daily Duties by Role (Shift Lead, Barista, Baker, Server, Busser)',
        desc: 'Checklists for the shift lead, barista, baker, server and busser / runner: what each position does at opening, during service and at close, shift after shift.',
      },
      {
        icon: 'CalendarDays',
        title: 'Cafe Cleaning Checklist, Inventory & Maintenance Schedule',
        desc: 'Weekly deep clean by area, a weekly FIFO check of coolers, bar, pastry case and dry storage, monthly equipment maintenance (espresso machine, grinder, oven, dish machine, HVAC), a daily inventory that flags REORDER when stock drops below your minimum and a weekly inventory by category in US units. + a Quarterly & Annual sheet for contracted services: pest control, fire extinguishers, refrigeration, the espresso tech, water filter and hardness, grinder burrs and thermometer calibration, with the service report number and initials.',
      },
      {
        icon: 'PartyPopper',
        title: "Coffee Shop Event Checklists: Sunday Brunch, Valentine's Day, Holiday Season & Patio",
        desc: "Sunday brunch (Saturday prep, Sunday opening, service and close), Valentine's Day, the holiday season and the start and end of patio season, with allergens written down when each reservation is confirmed.",
      },
      {
        icon: 'FileEdit',
        title: 'Blank Coffee Shop Checklist Template (Editable)',
        desc: '3 master templates already structured (by time of day, by area and by role) with the sections and the area or person in charge set up: you just type your tasks in the green cells.',
      },
      {
        icon: 'Building2',
        title: 'Cafe Opening & Closing Checklist (Whole Shop)',
        desc: 'The checklist for the whole shop, not just the espresso bar: alarm, lights, HVAC, POS, signage, restrooms, patio and the espresso machine up to temperature. Who does it and the due-by time are filled in for all 31 tasks.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. Plus a monthly cash log with the over/short by formula.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Coffee Shop Pre-Shift Meeting Template (Huddle Notes)',
        desc: "Pre-shift huddle template: reservations and groups, specials of the day and 86'd items, allergens and special diets, the team on shift. Print it and pin it up behind the counter.",
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Coffee Shop Holiday & Events Calendar (US)',
        desc: "22 key US dates for coffee shops, from King cake season and Valentine's Day to National Coffee Day, Thanksgiving pie orders and holiday catering, with their tasks and recommended lead time in editable cells, 5 empty rows for your own dates and a UK note.",
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
        title: 'Pre-Filled for Coffee Shops',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a coffee shop and brunch cafe. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Coffee',
        title: 'Barista Tasks Included',
        desc: "Dialing in the grinder, purging the group heads, backflushing, the pastry case, the milk station. The tasks generic checklist apps don't cover.",
      },
      {
        icon: 'Users',
        title: 'Delegate It, Get It Initialed',
        desc: "Print the checklist and hand it to the person in charge. When they're done, they initial it and you file it. No more \"I didn't know I had to do that.\"",
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists coffee shops run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants and coffee shops.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Coffee Shop Pre-Shift Meeting Template',
        desc: 'The 5-minute huddle that separates good coffee shops from great ones. Reservations, specials of the day, allergens, the team on shift.',
        image: '/lovable-uploads/ai-gallery/tareas-cafeteria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Coffee Shop Holiday & Events Calendar (US)',
        desc: "22 key dates for US coffee shops (King cake season, Valentine's Day, Easter, Teacher Appreciation Week, Mother's Day, the Fourth of July, National Coffee Day, Thanksgiving, holiday catering) with tasks and recommended lead time, plus 5 rows for your own dates.",
        image: '/lovable-uploads/ai-gallery/tareas-cafeteria-terraza.jpg',
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
    ctaLabel: 'YES, I WANT THE COFFEE SHOP CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your coffee shop's operations better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de cafe/SPEC D5 (coffee shop / cafe opening, closing, barista, cafe
  // cleaning) + las del ES adaptadas (tareas ya escritas, barista, frente a las apps, varios locales con la licencia
  // de la tienda EN, brunch y eventos) + espresso, vitrina, UK/CA/AU, moneda, suscripción y garantía (como los
  // hermanos EN). La de Google Sheets del ES no va (sin test real, SPEC base §9).
  faqs: [
    {
      q: 'What should be on a coffee shop opening checklist?',
      a: 'Start with personal hygiene (clean uniform, hair tied back, cuts covered, hands washed), then open each area. Kitchen: hood on before anything else, the gas check if you have gas, oven and griddle on, and the overnight cooler readings logged. Front of house and patio: lights and HVAC, tables set, the menu board updated, condiments restocked, the POS and card terminal working. Espresso bar: machine warmed up, group heads purged, the grinder dialed in with a test shot (25–30 s, 25–30 ml, about 1 fl oz), machine pressure checked (9 bar), the steam wand purged, beans, milks, syrups and tea stocked, cold milk pitchers ready, the ice bin filled with a scoop, never a glass, and the batch brew on. Then the pastry case: glass cleaned, stocked with the day\'s bake, labeled with price and allergens, the refrigerated case at 41 °F or below with the reading logged, and tongs or gloves out. The whole shop has its own list: alarm, lights, HVAC, POS, signage and patio. Every task needs who does it, a due-by time and initials.',
    },
    {
      q: 'What goes on a coffee shop closing checklist?',
      a: 'At the espresso bar: backflush each group head with espresso machine detergent, clean the portafilters, purge and wipe the steam wand, clean the drip tray, empty the knock box and turn the machine off; brush out the grinder and close the hopper; clean the blender and the batch brew airpots. Leftover pastries get dated and stored, the refrigerated case is emptied or covered, and open milk goes back into the fridge at 41 °F or below, covered and dated. Note the bean stock and tomorrow\'s orders, sanitize the bar top, wash the milk pitchers, empty the ice bin and sweep. Then the kitchen and front of house close, the patio is brought in, the cash drawer is counted against the POS Z report and the shop is locked up: POS and HVAC off, final safety check, alarm set.',
    },
    {
      q: "What's on a barista checklist?",
      a: 'At opening, the barista turns on and warms up the espresso machine, purges the group heads, dials in the grinder with a test shot, checks the stock of coffee, milks, syrups and tea, gets the cold milk pitchers, the toppings and syrup station, the batch brew and the ice bin ready. During service: drinks to order (espresso, latte, cappuccino) with consistent crema, temperature and texture, the portafilter cleaned between shots, the steam wand purged after every use and stock topped up. At close: backflush, grinder brushed, pitchers and tools washed, coffee stock noted for the order, bar wiped and the machine off. In this kit, the "Barista Checklist & Daily Duties by Role" workbook has one checklist each for the shift lead, barista, baker, server and busser, and the espresso bar has its own opening and closing tabs.',
    },
    {
      q: 'How often should you backflush and descale an espresso machine?',
      a: "Backflush every day at close, group by group, with espresso machine detergent and following the manufacturer's instructions. Descale as the manufacturer says: on many commercial machines your espresso tech does it. In this kit, the backflush is on the espresso bar closing checklist and on the barista's close; descaling, gaskets, boiler pressure and the water filter are on the monthly maintenance sheet; and the Quarterly & Annual sheet adds the filter change, a water hardness test (GH/KH), a full service by your espresso tech and the grinder burrs by pounds ground (as a guide, flat burrs 880–1,320 lb and conical 1,760–2,650 lb; your grinder's maker has the final word).",
    },
    {
      q: 'How do you keep a pastry case food safe?',
      a: 'Keep anything that needs refrigeration (cream cakes, cheesecake, dairy fillings) in a refrigerated case at 41 °F or below and log the reading, as the FDA Food Code requires. Date-mark those items and use them within 7 days, counting the day they were made. Serve with tongs, bakery tissue or gloves, never bare hands. Label every item with its name, price and allergens (the 9 major allergens in the US; for pastries, mostly wheat, eggs, milk, soy, tree nuts, peanuts and sesame). Rotate the oldest product to the front, and log the day\'s waste so tomorrow\'s bake matches what sells. The "Pastry Case" tab of the kitchen workbook has these tasks already written.',
    },
    {
      q: 'Is there a free coffee shop checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 500 coffee shop tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, temperatures in °F and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a coffee shop?',
      a: "Yes. Every checklist comes with the real tasks of a coffee shop and brunch cafe already written. You'll want to make it yours: adjust tasks to your shop, delete the ones that don't apply and add your own. The editable cells are green, and each table ends with 5 free green rows that the counter already includes.",
    },
    {
      q: 'Does it include brunch and events?',
      a: "Yes. There are event checklists for Sunday brunch (Saturday prep, Sunday opening, service and post-brunch close), Valentine's Day, the holiday season and the start and end of patio season, and the calendar bonus adds 22 key US dates with their tasks. Mimosas and bellinis only appear where your license allows alcohol, served to guests 21+ with ID.",
    },
    {
      q: 'Does it work for a small coffee shop or a cafe with a kitchen?',
      a: 'Yes. The templates scale. A small espresso bar can use the espresso bar, front of house and pastry case lists. A cafe with a kitchen adds the hot line, the cold station and the brunch checklist. A group of shops adds the manager checklists and the shift handover.',
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same task lists in Excel for $19, a one-time payment. No subscription, no internet needed. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it in several coffee shops or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for coffee shop chains. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change. The kit is set up for the US: temperatures in °F under the FDA Food Code, the 9 major allergens and a cash count in US bills and coins. In the UK, most people say cafe, cold holding is 8 °C or below and hot holding 63 °C or above, and allergen information covers 14 allergens (the allergen tasks already note the UK's 14); the events calendar has a UK note with Mothering Sunday, bank holidays and Boxing Day. In Canada and Australia, type your province's or state's holding temperatures in °C and its allergen list into the green cells. If you serve mimosas at brunch, you need a licence: the legal age is 18 in the UK and Australia (where staff also need an RSA certificate), and 19 in most Canadian provinces (18 in Alberta, Manitoba and Quebec). For pounds, Canadian or Australian dollars, unprotect the cash count sheet (there is no password) and change the label and value of each bill and coin. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
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
    subtitle: "9 templates + 3 bonuses (12 files) for your coffee shop for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: espresso bar, front of house, patio, kitchen',
      'Whole-shop opening and closing, and a cash drawer count with automatic over/short',
      'Barista tasks: dialing in, cleaning, stock',
      'Pastry case control and a Sunday brunch checklist',
      'Manager checklists: daily, weekly and monthly',
      'Tasks by role: shift lead, barista, baker, server, busser',
      "Events: Sunday brunch, Valentine's Day, holiday season, patio season",
      'BONUS: Coffee Shop Pre-Shift Meeting Template',
      'BONUS: Coffee Shop Holiday & Events Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE COFFEE SHOP CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 10 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas
  // Recurrentes: Cafetería / Brunch, la edición española de este kit: por eso conservan sus nombres, negocios y
  // cifras, y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD. Dos frases cambiadas (ver cabecera).
  testimonials: {
    subtitle:
      'Baristas, managers and coffee shop owners who already run their operations with Kit de Tareas Recurrentes: Cafetería / Brunch, the Spanish edition of this kit',
    items: [
      {
        name: 'Carlos Mendoza',
        role: 'Head Barista, Café Arábica',
        text: 'Every barista used to dial in the grinder their own way. With the barista checklist, everyone now follows the same routine every morning. Our espresso is far more consistent.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Laura Serrano',
        role: 'Manager, La Cafetería del Mercado',
        text: 'Running the opening of a coffee shop with a patio and its own bakery kitchen was chaos. Since we printed the opening checklists by area, the team knows exactly what to do before we open the doors.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Miguel Ángel Ruiz',
        role: 'Owner, Coffee Lab Barcelona',
        text: 'I opened my coffee shop 8 months ago and I kept forgetting everything: purging the group heads, checking the pastry case, restocking the plant-based milks. With these checklists I cut those slip-ups by 90%. They literally saved me.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Pastry Chef and Partner, Dulce Brunch',
        text: 'The pastry case checklist is amazing. FIFO rotation, temperatures, allergen labels... all on one sheet we keep inside the case. Zero waste since then.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Andrés Gallego',
        role: 'General Manager, Brunch & Co.',
        text: 'Sunday brunch was always stressful. With the brunch checklist (Saturday prep, Sunday opening, service), everything runs smoothly now. The team preps the mise en place, decorates and sets up the buffet without me having to repeat a thing.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Sofía Montero',
        role: 'Director of Operations, Grupo Café Central',
        text: 'We have 4 coffee shops, and each manager used to do things differently. With the checklists, we have standardized operations across all 4. Onboarding new staff went from 2 weeks to 3 days.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Reyes',
        role: 'Owner, Tostadores Artesanos',
        text: "The pre-shift meeting template alone is worth the price. We never used to hold one. Now in 5 minutes we go over the specials, allergens, reservations and the team. Service starts much better prepared.",
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Rodrigo Espinosa',
        role: 'Barista and Trainer',
        text: "As a barista trainer, I recommend this kit to all my students. The dialing-in, cleaning and espresso machine maintenance tasks are perfectly structured. It's what every coffee shop should have.",
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Diego Navarro',
        role: 'Pastry Chef, Café Gourmand',
        text: "The manager's weekly checklist is my favorite tool. Supplier orders, date checks, the deep clean and the team meeting, all in one document and organized by section.",
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Pablo Ibáñez',
        role: 'Specialty Coffee Shop Consultant',
        text: 'The first thing I do with every new client is hand them these checklists. They bring order from day one. Opening, closing, barista, pastry case... they cover 95% of what any coffee shop needs.',
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
    { href: '/en/digital-products/bar-checklist-templates', label: 'Bar Checklists Kit Pro' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
    { href: '/en/digital-products/ghost-kitchen-checklist-templates', label: 'Ghost Kitchen Checklists Kit Pro' },
    { href: '/en/digital-products/ice-cream-shop-checklist-templates', label: 'Ice Cream Shop Checklists Kit Pro' },
    { href: '/en/digital-products/chocolate-shop-checklist-templates', label: 'Chocolate Shop Checklists Kit Pro' },
    { href: '/en/digital-products/pastry-shop-checklist-templates', label: 'Pastry Shop Checklists Kit Pro' },
    { href: '/en/digital-products/hotel-checklist-templates', label: 'Hotel Checklists Kit Pro' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/coffee-cart-business-plan', label: 'Coffee Cart Business Plan Kit' },
    { href: '/en/digital-products/how-to-open-a-pastry-shop', label: 'How to Open a Pastry Shop' },
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
    product: 'coffee-shop-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
