// astro-site/src/data/productos-en/tareas/burger-joint-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Burger Joint Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-hamburgueseria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-, bar-, coffee-shop-, catering- y pizza-shop-checklist-templates.ts. SPEC: scripts/productos-digitales/
// checklists-kit/burger/SPEC.md (delta) + la base.
//   · D2: nombre «Burger Joint Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Burger Joint Checklists Kit Pro: Burger Restaurant Opening & Closing Checklist Templates for Excel».
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (burger/SPEC §2,
//     dl/burger-joint-checklist-templates/). «burger joint» y «burger shop» tienen volumen US; las variantes de
//     checklist, no: la intención genérica «restaurant opening / closing checklist» va en el copy (keywords y las dos
//     primeras FAQ). «restaurant» SÍ vale en este kit («burger restaurant»).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos (el ES los «valora en €31»). Fórmula de la tienda EN.
//   · Cifras SOLO de burger/SPEC (D-BUR, D10, D11, D14, §3) y del censo del ES (burger/censo_es.json, misma estructura
//     en la EN): 346 tareas (30+14+18+10 = 72 en el 01; 31 en el 08 con responsable y hora), inventario diario de 28
//     productos con Par y «⚠️ REORDER», 22 fechas + 5 huecos y nota UK; plancha 400–450 °F, aceite 350–355 °F,
//     carne picada a 155 °F durante 17 s con sonda (3-401.11(A)(2)), pollo a 165 °F, bola de smash 3–3.5 oz prensada
//     30–45 s, patatas 3–4 min y aros 2–3 min, make line y toppings a 41 °F con date marking de 7 días, salsas caseras
//     5 días, carne picada fresca 3 días, ticket times < 12 min, food cost 28–32 %; NFPA 96 trimestral (alto volumen o
//     charbroil) o semestral; aceite usado a un recycler; 9 alérgenos (UK: 14, la mostaza incluida).
//   · Lo que el ES afirma y el kit no trae, fuera: «Trail €60-75/mes» y «sin internet» (→ la fórmula de los
//     hermanos), «gestión de riders» (el kit no tiene repartidor propio: delivery con apps de terceros), «etiquetado»
//     del delivery, «control de tiempos por grosor» y la guía «rare a well done» (la EN: 155 °F con sonda; poco hecha
//     solo a petición con el aviso al consumidor y nunca en el menú infantil), «presión» del smash, el «foco por día»
//     del semanal (todo va el lunes), «noche de burger especial», «festivos con menú limitado», «DDD», «BIE» y
//     «Verifactu» (→ servicios contratados US). En el dashboard ES: «6 checklists» en el 01 (son 4) y «17 fechas»
//     (son 22).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual (nombres,
//     negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan. Uno
//     retirado SOLO en EN: «Grupo Burger Factory» (Burger Factory es una cadena real de Canadá; ver el comentario en
//     la lista); «The Burger Lab» (homónimos sueltos, sin cadena conocida en US/UK/CA/AU) y «BurgerExpress» (una
//     cadena británica de los 80 cerrada en 1993) se quedan. Dos frases que el kit contradice, cambiadas (regla de
//     John, 11-oct): Sergio Ramos (retirado después en EN, 18-oct: homónimo del futbolista)
//     («guía para cada grosor: rare, medium rare, medium, well done» → cada patty comprobado con sonda, que el kit sí
//     trae) y Diego Castillo («etiquetado» → el palillo con bandera en las burgers altas, que el kit sí trae).
//   · Imágenes: las 7 del ES no llevan texto en español (menús y bolsas en inglés) y se quedan; fuera solo la OG ES
//     (og-kit-tareas-hamburgueseria: «Kit de Tareas Recurrentes», «€12», «Google Sheets», «Imprimible A4») → OG = el
//     hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_BURGER_JOINT_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'burger-joint-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_BURGER_JOINT_CHECKLISTS_KIT',

  seo: {
    title: 'Burger Joint Checklists Kit Pro: Burger Restaurant Opening & Closing Checklist Templates for Excel',
    description:
      '11 Excel burger joint checklists with 346 tasks already written: opening & closing, grill, make line, fryer, manager, roles, cleaning, cash count. One-time $19.',
    keywords:
      'burger joint checklist, burger restaurant checklist, burger shop opening checklist, burger restaurant closing checklist, burger shop closing checklist, restaurant opening checklist, restaurant closing checklist, burger kitchen cleaning checklist, grill station checklist, flat top griddle cleaning checklist, fryer oil checklist, burger restaurant manager checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
  },

  schema: {
    productName: 'Burger Joint Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for burger joints with 346 tasks already written: opening and closing for the kitchen and front of house, the grill station, make line and fry station, manager, duties by role, delivery and takeout, daily inventory, cleaning and maintenance schedule, events and busy nights, whole-restaurant opening and closing, and a cash drawer count.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a burger joint opening checklist?',
        a: 'One list per area, in order: kitchen (hood on before any equipment, gas check, griddle preheated to about 400–450 °F, fryers on with the oil at 350–355 °F, walk-in at 41 °F or below and freezer at 0 °F or below, buns, toppings, sauces and cheese prepped, the make line set up), front of house (tables, menu board, POS and card terminal, starting bank) and delivery (apps on, burger boxes and bags stocked). Each task needs who does it, a due-by time and initials.',
      },
      {
        q: 'What goes on a burger restaurant closing checklist?',
        a: 'Raw ground beef, toppings and sauces covered, dated and refrigerated; the griddle scraped and degreased and the fryer oil filtered or changed as the fryer maker says, with the hood still running; the make line, spatulas and smash press cleaned; floors, trash and cardboard; delivery apps off; the cash drawer counted against the POS Z report; and the restaurant locked up last, with the alarm set.',
      },
      {
        q: 'Does it cover the grill, smash burgers and doneness?',
        a: 'Yes. The grill station tasks cover griddle start-up and cleaning, smash burgers (a 3–3.5 oz ball pressed on the hot griddle), melting the cheese and toasting the buns, and doneness checked with a probe thermometer: ground beef to 155 °F for 17 seconds under the FDA Food Code, undercooked only on request with a consumer advisory on the menu.',
      },
      {
        q: 'Is there a free burger restaurant checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 346 burger joint tasks already written, a counter that skips N/A tasks, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C, hot holding at 63 °C and 14 allergens (mustard included); in Canada and Australia, your local holding temperatures and allergen list; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Burger Joint Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid (6): el set del ES tal cual (sin texto en español).
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-plancha.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-montaje.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-freidora.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-delivery.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-mesa.jpg',
    ],
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-plancha.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-montaje.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-freidora.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-delivery.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-burger-montaje.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-burger-plancha.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Burger Joint Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Burger Joint Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Burger Restaurant Opening & Closing Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 346 burger joint tasks already written: opening and closing, the grill and smash burgers, make line, fry station, delivery and takeout, manager, roles, cleaning, events and a cash drawer count. Print it, delegate it to your team, initial it and file it.',
    checkItems: [
      'Opening and closing checklists: grill, fryers, make line, front of house and takeout',
      'Grill control: griddle at 400–450 °F, smash burgers, ground beef checked to 155 °F with a probe',
      'Fry station: oil at 350–355 °F, TPM oil test, filtering, fry times for fries and onion rings',
      'Delivery and takeout: burger boxes and bags, delivery apps and delivery times',
      'Whole-restaurant opening and closing, and a cash drawer count by bill and coin',
      '3 editable master templates + a pre-shift meeting template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS HAMBURGUESERÍA — €12»).
  stickyLabel: 'BURGER JOINT CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Burger Joint Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '346 burger joint tasks already written and sorted by shift, area and role. Adjust them to your restaurant, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Burger Joint Opening & Closing Checklists: Kitchen, FOH & Takeout',
        desc: '4 checklists: kitchen opening, front of house opening, kitchen closing and front of house closing, with delivery and takeout. Every task with who does it, a due-by time and initials. 72 tasks already written in this file alone.',
      },
      {
        icon: 'Flame',
        title: 'Burger Kitchen Station Checklists: Grill, Make Line & Fry Station',
        desc: 'The grill station (griddle preheated to 400–450 °F, smash burgers from a 3–3.5 oz ball, ground beef checked with a probe to 155 °F, cheese melted under a dome, buns toasted, raw-meat tools kept apart), the make line (inserts at 41 °F or below, sauces in squeeze bottles, burgers built to the ticket and wrapped and boxed for takeout and delivery) and the fry station (oil at 350–355 °F, TPM oil test, fries and onion rings in batches, chicken to 165 °F), before, during and after service.',
      },
      {
        icon: 'ClipboardList',
        title: 'Burger Restaurant Manager Checklist: Daily, Weekly, Monthly & Shift Handover',
        desc: "Daily, weekly and monthly checklists (ticket times under 12 minutes, food cost target of 28–32%, delivery app commissions, the team's time-clock records), plus a shift handover: open tickets, pending delivery orders, patties and buns left, fryer oil condition and 86s.",
      },
      {
        icon: 'Users',
        title: 'Burger Shop Duties by Role: Grill Cook, Line Cook, Fry Cook, Shift Manager & Server',
        desc: 'Checklists for the grill cook, the line cook, the fry cook, the shift manager and the server: what each role does at opening, during service and at closing.',
      },
      {
        icon: 'CalendarDays',
        title: 'Burger Restaurant Cleaning Checklist, Inventory & Maintenance Schedule',
        desc: 'Daily inventory of 28 products with par levels and a REORDER flag, weekly deep clean by zone, weekly FIFO check with a freezer shelf-life table, and monthly griddle, fryer, hood and equipment maintenance. + a Quarterly & Annual sheet for contracted services: pest control, hood and duct cleaning (NFPA 96), fire extinguishers and hood suppression, gas, refrigeration (make line included), used fryer oil pickup, water, insurance, the POS and sales tax, and thermometer calibration, with the service report number and initials.',
      },
      {
        icon: 'PartyPopper',
        title: 'Burger Joint Event Checklists: Game Night, Burger Week, Holidays & Patio',
        desc: 'Game night (more patties, double the delivery packaging, burger boxes set up ahead, extra staff), Burger Week with 3–5 limited-edition burgers, the holiday season with group bookings, and patio season opening and closing, each task with its lead time.',
      },
      {
        icon: 'FileEdit',
        title: 'Blank Burger Shop Checklist Template (Editable)',
        desc: '3 master templates already structured (by time of day, by area and by role) with the sections and the area or person in charge set up: you just type your tasks in the green cells.',
      },
      {
        icon: 'Building2',
        title: 'Burger Restaurant Opening & Closing Checklist (Whole Building)',
        desc: 'The checklist for the whole restaurant, not just the kitchen: alarm, lights, HVAC, POS, patio, the griddles and fryers, and a final safety check, with the griddles cleaned and the fryer oil filtered before the hood goes off, and the alarm and lock-up last. Who does it and the due-by time are filled in for all 31 tasks.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. Plus a monthly cash log with the over/short by formula for every day of the month.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Burger Joint Pre-Shift Meeting Template (Huddle Notes)',
        desc: 'Pre-shift meeting template: reservations and covers, specials and 86s, allergens and dietary requests, the team on shift and notes. Print it and post it in the kitchen.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Burger Joint Holiday & Busy Days Calendar (US)',
        desc: "22 key US dates for burger joints, from Super Bowl Sunday, March Madness and National Burger Month (May 28 is National Hamburger Day) to National Cheeseburger Day, Halloween, Thanksgiving and New Year's Eve, with the key tasks and recommended lead time for each, a UK note and 5 free rows for your own.",
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
        title: 'Pre-Filled for Burger Joints',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a burger joint. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Flame',
        title: 'Grill Control and Doneness',
        desc: "Griddle start-up at 400–450 °F, smash burgers, ground beef checked with a probe thermometer to 155 °F, and the fryer oil checked with a TPM tester. The tasks generic checklist apps don't cover.",
      },
      {
        icon: 'Users',
        title: 'Delivery and Takeout',
        desc: "Checklists for delivery apps, burger boxes and bags (so the burger doesn't fall apart), delivery times, takeout and packaging stock.",
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists burger joints run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants and burger joints.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Burger Joint Pre-Shift Meeting Template',
        desc: 'The 5-minute huddle that separates good burger joints from great ones. Reservations, specials and 86s, allergens, the team on shift.',
        image: '/lovable-uploads/ai-gallery/tareas-burger-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Burger Joint Holiday & Busy Days Calendar (US)',
        desc: "22 key dates for US burger joints (Super Bowl Sunday, Valentine's Day, Lent Fridays, St. Patrick's Day and March Madness, National Burger Month, graduation season, Mother's Day and Father's Day, July 4, Labor Day and football season, National Cheeseburger Day, Halloween, Thanksgiving and Black Friday, holiday office orders, New Year's Eve) with the key tasks and the recommended lead time.",
        image: '/lovable-uploads/ai-gallery/tareas-burger-mesa.jpg',
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
    ctaLabel: 'YES, I WANT THE BURGER JOINT CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your burger joint better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de burger/SPEC D5 (burger joint / burger restaurant checklist, y la genérica
  // «restaurant opening / closing checklist» en las dos primeras) + las del ES adaptadas (tareas ya escritas, plancha
  // y smash con el punto de la carne según la FDA, freidora y aceite, delivery con apps de terceros, frente a las apps,
  // varios locales con la licencia de la tienda EN, garantía) + make line, limpieza, firma, eventos, UK/CA/AU, moneda
  // y suscripción (como los hermanos EN). La de Latinoamérica del ES → la de UK/CA/AU.
  faqs: [
    {
      q: 'What should be on a burger joint opening checklist?',
      a: "The same as a restaurant opening checklist, built around the grill, the fryers and the make line, one list per area and in order. Kitchen: personal hygiene first; then the hood on and the kitchen ventilated before any equipment, a check that the hood really draws, and the gas checked (if you smell gas, don't turn anything on); the flat-top griddle preheated to about 400–450 °F, the fryers on with the oil level checked and the oil at 350–355 °F for fries, and the bun toaster on; the walk-in at 41 °F or below and the freezer at 0 °F or below, with the readings logged; raw ground beef kept at 41 °F or below until it hits the griddle (never left out to temper); buns, toppings, house sauces, cheese and bacon prepped; fries, onion rings and coleslaw; and the make line set up in order. Front of house: lights and A/C, tables, the menu board (burger of the day and combos), the POS and card terminal and the starting bank. Delivery: tablets and delivery apps on, burger boxes, bags, napkins and fry containers stocked, and menus and 86s updated in the apps. Every task needs who does it, a due-by time and initials. The \"Burger Joint Opening & Closing Checklists\" workbook has the kitchen and front of house already written, and the whole-restaurant checklist covers the alarm, lights, POS, griddles and fryers.",
    },
    {
      q: 'What goes on a burger restaurant closing checklist?',
      a: "Like any restaurant closing checklist: cleaning and shutdown by area, food stored and the money counted, with the grill and the fryers as the extra steps. Kitchen: leftover raw ground beef covered, dated and stored below ready-to-eat food and above any raw chicken; cut toppings and house sauces covered, dated and at 41 °F or below; leftover buns bagged; the griddle scraped and degreased; the fryers off and the oil filtered or changed the way your fryer maker says; the hood turned off last, once the griddle and the fryers have cooled; the make line, trays, spatulas and smash press cleaned; floors, trash, cardboard and used oil; tomorrow's patties made if you prep them ahead; the day's waste logged; and the beef for tomorrow thawing in the walk-in. Front of house: tables and floors, condiments refilled, the delivery tablets off and the packaging counted, the register reconciled, the restrooms cleaned, and the lights, HVAC, alarm and lock-up last. In this kit, the closing checklists by area and the whole-restaurant \"Restaurant Closing\" tab have those tasks already written, and the \"Cash Drawer Opening & Closing\" workbook works out the over/short against the POS Z report for you.",
    },
    {
      q: 'Does it cover the grill, smash burgers and doneness?',
      a: "Yes. The grill station tasks cover the flat-top griddle preheated to 400–450 °F and scraped between batches, the smash press and spatulas ready, raw-meat boards, tongs and spatulas kept apart from the ones for buns and toppings, smash burgers (a 3–3.5 oz ball pressed on the hot griddle for 30–45 seconds), cheese melted under a dome, buns toasted cut side down, and a deep clean with a scraper and degreaser at close. Doneness is checked with a probe thermometer: ground beef to 155 °F for 17 seconds in the center under the FDA Food Code, rare or medium only when the guest asks for it and your menu carries the consumer advisory, and never for the kids' menu. Chicken goes to 165 °F.",
    },
    {
      q: 'Does it include fryer and oil tasks?',
      a: "Yes. The fry station checklist covers the oil level and quality before service (with a TPM oil tester), the oil at 350–355 °F, fries cooked in batches without overloading the basket (3–4 minutes for fries, 2–3 for onion rings), seasoning as they come out, nuggets and tenders cooked to 165 °F, and the fryers turned off at close. The oil is filtered every night the way your fryer maker says and changed when the TPM tester says, the manager tests it every week, the fryers get a monthly boil-out, and the quarterly sheet checks the used fryer oil pickups by a licensed recycler.",
    },
    {
      q: 'Does it include delivery and takeout tasks?',
      a: "Yes. The delivery tablets and third-party apps (DoorDash, Uber Eats, Grubhub) go on at opening and off at closing, menus and 86s are updated in the apps, and burger boxes, bags, napkins and fry containers are stocked. The line cook wraps and boxes every takeout and delivery order, with a frill pick in the tall burgers so they don't fall apart, and the packaging left is counted at close. The manager checklists cover delivery times and packaging, app reviews every week and app commissions every month, and game nights get double the delivery packaging with the boxes set up ahead. The kit is written for third-party delivery: there is no checklist for your own drivers.",
    },
    {
      q: 'Does it cover the make line and toppings?',
      a: "Yes. The make line is set up before service: lettuce, tomato, onion and pickles in the inserts (the produce washed first), sauces in squeeze bottles, cheese sliced, buns checked and extras such as a fried egg or crispy onions ready. During service, burgers are built to the ticket in order (bun, sauce, patty, cheese, toppings, top bun) and the inserts are restocked as they run low; at close, everything is covered and refrigerated and the waste is logged. The inserts are held at 41 °F or below, cut toppings and coleslaw are date-marked for up to 7 days, house sauces are kept for 5, and a fried egg with a runny yolk needs the consumer advisory on your menu.",
    },
    {
      q: 'What should a burger restaurant cleaning checklist include?',
      a: "Daily cleaning belongs in the closing checklists. On top of that, the kit schedules a weekly deep clean by zone (the flat-top griddle deep cleaned, grease trough and splash guards included, and re-seasoned, the inside of the fryers with the baskets out, walk-in interiors, the hood filters, behind and under equipment, windows, floors with degreaser and restrooms), a weekly FIFO check (fresh ground beef for 3 days at most, opened cheese, house sauces, buns and packaging) with a freezer shelf-life table, and monthly maintenance of the griddle surface and thermostat, a fryer boil-out, the dish machine, the hood motor and filters, and a visual check of the fire extinguisher, the first aid kit and the emergency exits. Contracted services go on the \"Quarterly & Annual\" tab: hood and duct cleaning under NFPA 96 (quarterly for a high-volume or charbroil kitchen, semiannual if moderate), alongside pest control, fire extinguishers and the hood suppression system, gas, refrigeration, used fryer oil and thermometer calibration.",
    },
    {
      q: 'Is there a free burger restaurant checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 346 burger joint tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a burger joint?',
      a: "Yes. Every checklist comes with the real tasks of a burger joint already written. You'll want to make it yours: adjust tasks to your restaurant, delete the ones that don't apply and add your own. The editable cells are green, and each checklist ends with 5 free green rows that the counter already includes.",
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for who does it, when (a due-by time on the daily lists, a day on the weekly ones, a frequency on the monthly ones and a lead time on the event lists), ✓ Done and initials. The shift manager prints the checklist and hands it to the team, and each person checks off and initials their tasks. At the end of the shift, the shift manager checks it and signs at the bottom.',
    },
    {
      q: 'Does it include tasks for game nights, holidays and events?',
      a: "Yes. There are checklists for game night (more beef, buns, cheese and fries ordered ahead, double the delivery packaging, burger boxes set up ahead and extra staff), Burger Week (3–5 limited-edition burgers, premium ingredients ordered and the team trained on the new recipes), the holiday season (group bookings with allergens in writing, a deposit and a cancellation policy) and opening and closing patio season. And the bonus calendar lists 22 key US dates for burger joints, from Super Bowl Sunday and National Burger Month to New Year's Eve, with their tasks and recommended lead time.",
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it for several burger joints or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for multi-unit burger operators. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 135 °F hot holding, ground beef cooked to 155 °F), the 9 major allergens and a cash count in US bills and coins. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, and allergen information covers 14 allergens, mustard among them, which is not one of the US 9 (the kit's allergen tasks already note the UK's 14). In Canada and Australia, check your provincial or state food safety rules and allergen list and type them into the tasks. Your patio is your terrace or beer garden, and you can type in the delivery apps you use. For pounds, Canadian or Australian dollars, unprotect the cash count sheet and change the label and value of each bill and coin. If you serve beer, you need the licence your area requires; the legal age is 18 in the UK and Australia, and 19 in most Canadian provinces (18 in Alberta, Manitoba and Quebec). The holiday calendar has a UK note and free rows for your own dates. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
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
    subtitle: "9 templates + 3 bonuses (12 files) for your burger joint for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: grill, fryers, make line, front of house, takeout',
      'Grill cook tasks: smash burgers, doneness checked with a probe, the griddle',
      'Fry station: TPM oil test, filtering, oil temperature',
      'Manager checklists: daily, weekly, monthly + shift handover',
      'Tasks by role: grill cook, line cook, fry cook, shift manager, server',
      'Delivery and takeout: burger boxes, bags, delivery apps, delivery times',
      'Whole-restaurant opening and closing + cash drawer count',
      'BONUS: Burger Joint Pre-Shift Meeting Template',
      'BONUS: Burger Joint Holiday & Busy Days Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE BURGER JOINT CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 10 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas
  // Recurrentes: Hamburguesería, la edición española de este kit: por eso conservan sus nombres, negocios y cifras, y
  // el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD. Dos frases cambiadas y uno retirado (ver cabecera).
  testimonials: {
    subtitle:
      'Grill cooks, shift managers and burger joint owners who already run their operations with Kit de Tareas Recurrentes: Hamburguesería, the Spanish edition of this kit',
    items: [
      {
        name: 'Carlos Méndez',
        role: 'Grill Cook / Grill Master, Smash & Co.',
        text: 'The grill and griddle checklist changed my shift. Every grill cook used to clean and heat up the griddle their own way. Now we all follow the same routine and the smash burgers come out perfect every time.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Marta Iglesias',
        role: 'Shift Manager, The Burger Lab',
        text: 'Opening a burger joint with delivery and a dining room was chaos. Since we printed the checklists by area, the team knows exactly what to do. Slip-ups dropped by 90%.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Rubén Torres',
        role: 'Owner, La Brasería Burger',
        text: 'I opened my burger joint 4 months ago and kept forgetting everything: heating up the griddle on time, filtering the fryer, prepping the toppings. These checklists got me organized from day one.',
        avatar: '/avatars/avatar-3.jpg',
      },
      // Testimonio de «Patricia Vega, …, Grupo Burger Factory» retirado SOLO en EN (18-oct-2026): Burger Factory es una
      // cadena real de hamburgueserías de Canadá (~40 locales, y alguno en EE. UU.) y, ante un público CA/US, se leería
      // como aval de esa marca. Mismo criterio que PizzaExpress en la pizzería. Decide John.
      {
        name: 'Alejandro Fuentes',
        role: 'Line Cook, Stack Burger',
        text: 'The burger make line is where it helped us most. Every ingredient in its place, sauces refilled, buns toasted on time. We used to improvise and orders went out slow. Now everything flows.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Laura Navarro',
        role: 'Fry Cook and Shift Manager, Crispy Burger Bar',
        text: 'The fryer checklist is great. Oil quality testing, daily filtering, temperature control for fries and onion rings. We used to forget to filter and the oil lasted half as long.',
        avatar: '/avatars/avatar-6.jpg',
      },
      // «Sergio Ramos, Grill Cook, Grill House BCN» retirado SOLO en EN (18-oct-2026, decisión delegada por John): es el
      // nombre de un futbolista muy conocido en EE. UU. (Liga MX incluida) y se leería como testimonio falso o aval de famoso.
      {
        name: 'Diego Castillo',
        role: 'Delivery Manager, BurgerExpress',
        text: "The delivery packaging checklist changed our business. The right packaging so the burger doesn't fall apart, delivery times, a frill pick in the tall ones. Returned orders dropped from 15 a month to 2.",
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo Herrera',
        role: 'Grill Chef, Street Smash',
        text: 'The pre-shift meeting template alone is worth the price. We never used to hold one. Now in 5 minutes we go over reservations, the burger of the day and allergens. Service runs much better.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Andrés Molina',
        role: 'Burger Restaurant Consultant',
        text: 'The first thing I do with every new client is hand them these checklists. It puts them in order from day one. Griddle, fryer, make line, delivery... they cover 95% of what any burger joint needs.',
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
    { href: '/en/digital-products/coffee-shop-checklist-templates', label: 'Coffee Shop Checklists Kit Pro' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
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
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'burger-joint-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
