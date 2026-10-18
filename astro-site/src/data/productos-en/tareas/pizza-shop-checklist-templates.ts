// astro-site/src/data/productos-en/tareas/pizza-shop-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Pizza Shop Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-pizzeria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-, bar-, coffee-shop- y catering-checklist-templates.ts. SPEC: scripts/productos-digitales/checklists-kit/
// pizza/SPEC.md (delta) + la base.
//   · D2: nombre «Pizza Shop Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Pizza Shop Checklists Kit Pro: Pizzeria Opening & Closing Checklist Templates for Excel».
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (pizza/SPEC §2,
//     dl/pizza-shop-checklist-templates/). Sin volumen US medido en «pizza shop / pizzeria checklist»: la intención
//     genérica «restaurant opening / closing checklist» va en el copy (keywords y las dos primeras FAQ), nunca en los
//     xlsx (G2 la veta).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos (el ES los «valora en €31»). Fórmula de la tienda EN.
//   · Cifras SOLO de pizza/SPEC (D-PIZ, D11, D14, §3), comprobadas contra los 11 xlsx EN de la F2 (b4e89b17):
//     373 tareas (76 en el 01, 31 en el 08 con responsable y hora, 32 productos en el inventario diario), 5 filas verdes libres al pie
//     de cada checklist, 22 fechas + 5 huecos; 750–840 °F (napolitana) y 570 °F (romana), 60–90 s / 3–5 min de
//     cocción, make line y masa en frío a 41 °F o menos, bolsa de reparto caliente ≥ 135 °F y frío aparte ≤ 41 °F,
//     objetivo de entrega < 30 min, food cost objetivo 28–32 %; ceniza en frío a un contenedor metálico con tapa y
//     extracción de combustible sólido inspeccionada cada mes (NFPA 96); 9 alérgenos (UK: 14).
//   · Lo que el ES afirma y el kit no trae, fuera: la comparación «Trail €60-75/mes» y «sin internet» (→ la fórmula
//     de los hermanos), «fermentación lenta 24-72 h», «temperatura de masa madre» y «banco de masas» (FAQ), el
//     «etiquetado» del delivery, «amasadora y cámara de fermentación» del mantenimiento, el «foco por día» del
//     semanal del manager (todas sus tareas van el lunes), «DDD», «BIE» y «Verifactu» (→ servicios contratados US).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual (nombres,
//     negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan.
//     Una frase que el kit contradice, cambiada (regla de John, 11-oct): Carmen Ruiz («etiquetado para
//     repartidores» → cada pedido comprobado contra la comanda: el kit no trae etiquetas, sí esa comprobación).
//   · Imágenes: fuera tareas-pizzeria-delivery.jpg (cajas «A DOMICILIO», «HORNO DE LEÑA», Glovo, bandera española) y
//     la OG ES (og-kit-tareas-pizzeria: «Kit de Tareas Recurrentes», «€12», «Imprimible A4») → OG = el hero.
//     Entran use-case-pizzeria-toppings.jpg y use-case-pizzero-team.jpg (sin texto, ya publicadas en los casos de
//     uso EN). Se quedan las otras 6 del ES (sin texto en español; -equipo lleva una pizarra en inglés).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'pizza-shop-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_CHECKLISTS_KIT',

  seo: {
    title: 'Pizza Shop Checklists Kit Pro: Pizzeria Opening & Closing Checklist Templates for Excel',
    description:
      '11 Excel pizza shop checklists with 373 tasks already written: opening & closing, pizza oven, make line, delivery, manager, roles, cleaning, cash count. One-time $19.',
    keywords:
      'pizza shop checklist, pizzeria checklist, pizza shop opening checklist, pizzeria closing checklist, pizza shop closing checklist, restaurant opening checklist, restaurant closing checklist, pizza kitchen cleaning checklist, pizza oven checklist, pizza make line checklist, pizza delivery driver checklist, pizzeria manager checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
  },

  schema: {
    productName: 'Pizza Shop Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for pizza shops with 373 tasks already written: opening and closing for the kitchen and front of house, the pizza oven station, make line and apps & pasta, manager, duties by role, delivery and takeout, daily inventory, cleaning and maintenance schedule, events and busy nights, whole-shop opening and closing, and a cash drawer count.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a pizza shop opening checklist?',
        a: 'One list per area, in order: kitchen (hood on before the oven, gas check, oven preheated and its temperature checked, walk-in at 41 °F or below and freezer at 0 °F or below, dough balls out to temper, sauce, cheese and toppings, the make line set up), front of house (tables, POS and card terminal, starting bank, patio) and delivery (apps on, pizza boxes and bags stocked). Each task needs who does it, a due-by time and initials.',
      },
      {
        q: 'What goes on a pizzeria closing checklist?',
        a: 'Dough balls, sauce, mozzarella and toppings covered, dated and refrigerated; the oven left to cool down (never doused with water) and ash removed only once cold; the make line, dough table and floors cleaned; tomorrow’s dough made; delivery apps off; the cash drawer counted against the POS Z report; and the shop locked up last, with the alarm set.',
      },
      {
        q: 'Does it work for wood-fired, deck and gas ovens?',
        a: 'Yes. The oven tasks cover wood-fired ovens (fire, wood, ash and chimney) and deck or gas ovens (preheating, brushing the oven deck, burners and gas valves). Mark N/A what does not apply to your oven.',
      },
      {
        q: 'Is there a free pizza shop checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 373 pizza shop tasks already written, a counter that skips N/A tasks, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C, hot holding at 63 °C and 14 allergens; in Canada and Australia, your local holding temperatures and allergen list; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Pizza Shop Checklists Kit Pro',
  },

  images: {
    // hero bg (6): el set del ES sin -delivery (texto en español) → use-case-pizzeria-toppings.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-linea.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/use-case-pizzeria-toppings.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-mesa.jpg',
    ],
    // strip visible del ContentGrid (6), como el ES: -delivery → use-case-pizzero-team.
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-linea.jpg',
      '/lovable-uploads/ai-gallery/use-case-pizzero-team.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-pizzeria-masa.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-pizzeria-horno.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Pizza Shop Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Pizza Shop Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Pizzeria Opening & Closing Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 373 pizza shop tasks already written: opening and closing, pizza oven and dough, make line, delivery and takeout, manager, roles, cleaning, events and a cash drawer count. Print it, delegate it to your team, initial it and file it.',
    checkItems: [
      'Opening and closing checklists: kitchen, front of house, patio and delivery',
      'Wood-fired or deck oven control: 750–840 °F, start-up, cleaning, wood and ash',
      'Pizza maker tasks: dough, hand stretching, 60–90 second bakes',
      'Delivery and takeout: pizza boxes, insulated bags, drivers and order checks',
      'Whole-shop opening and closing, and a cash drawer count by bill and coin',
      '3 editable master templates + a pre-shift meeting template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS PIZZERÍA — €12»).
  stickyLabel: 'PIZZA SHOP CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Pizza Shop Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '373 pizza shop tasks already written and sorted by shift, area and role. Adjust them to your shop, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Pizza Shop Opening & Closing Checklists: Kitchen, FOH & Delivery',
        desc: '4 checklists: kitchen opening, front of house opening, kitchen closing and front of house closing, with the patio, delivery and takeout. Every task with who does it, a due-by time and initials. 76 tasks already written in this file alone.',
      },
      {
        icon: 'Flame',
        title: 'Pizza Kitchen Station Checklists: Pizza Oven, Make Line, Apps & Pasta',
        desc: 'The pizza oven station (oven temperature in °F, 750–840 °F for Neapolitan and 570 °F for Roman-style, bake times, turning the pizza, managing the fire), the make line (inserts set in order, refilled before they run low, covered and refrigerated at close) and apps & pasta, before, during and after service.',
      },
      {
        icon: 'ClipboardList',
        title: 'Pizzeria Manager Checklist: Daily, Weekly, Monthly & Shift Handover',
        desc: "Daily, weekly and monthly checklists (food cost target of 28–32%, delivery app commissions, the team's time-clock records), plus a shift handover: open orders, pending deliveries, 86s, dough count and oven temperature.",
      },
      {
        icon: 'Users',
        title: 'Pizza Shop Duties by Role: Pizza Maker, Line Cook, Shift Manager, Server & Driver',
        desc: 'Checklists for the pizza maker, the line cook, the shift manager, the server and the delivery driver: what each role does before, during and after service.',
      },
      {
        icon: 'CalendarDays',
        title: 'Pizzeria Cleaning Checklist, Inventory & Maintenance Schedule',
        desc: 'Daily inventory of 32 products with par levels and a REORDER flag, weekly deep clean by zone, weekly FIFO check with a freezer shelf-life table, and monthly oven, hood and equipment maintenance. + a Quarterly & Annual sheet for contracted services: pest control, hood, duct and chimney cleaning (NFPA 96), a wood-fired oven check, fire extinguishers and hood suppression, gas, refrigeration (make line included), used cooking oil and insurance, with the service report number and initials.',
      },
      {
        icon: 'PartyPopper',
        title: "Pizza Shop Event Checklists: Game Night, Valentine's Day, Holidays & Patio",
        desc: "Game night and the Super Bowl delivery rush (extra dough, extra drivers, boxes folded ahead), Valentine's Day, the holiday season with group bookings, and patio season opening and closing, each task with its lead time.",
      },
      {
        icon: 'FileEdit',
        title: 'Blank Pizza Shop Checklist Template (Editable)',
        desc: '3 master templates already structured (by time of day, by area and by role) with the sections and the area or person in charge set up: you just type your tasks in the green cells.',
      },
      {
        icon: 'Building2',
        title: 'Pizzeria Opening & Closing Checklist (Whole Shop)',
        desc: 'The checklist for the whole shop, not just the kitchen: alarm, lights, HVAC, POS, patio, the wood-fired oven preheat and cool-down, and a final safety check. Who does it and the due-by time are filled in for all 31 tasks.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. Plus a monthly cash log with the over/short by formula for every day of the month.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Pizza Shop Pre-Shift Meeting Template (Huddle Notes)',
        desc: 'Pre-shift meeting template: reservations and covers, specials and 86s, allergens and dietary requests, the team on shift and notes. Print it and post it in the kitchen.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Pizza Shop Holiday & Busy Days Calendar (US)',
        desc: "22 key US dates for pizza shops, from Super Bowl Sunday and March Madness to Halloween, Thanksgiving Eve and New Year's Eve, with the key tasks and recommended lead time for each, a UK note and 5 free rows for your own.",
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
        title: 'Pre-Filled for Pizza Shops',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a pizza shop. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Flame',
        title: 'Oven and Dough Control',
        desc: "Oven start-up, 750–840 °F for Neapolitan, brushing the oven deck, cold-fermented dough, hand stretching, 60–90 second bakes. The tasks generic checklist apps don't cover.",
      },
      {
        icon: 'Users',
        title: 'Delivery and Takeout',
        desc: 'Checklists for delivery drivers, delivery times, pizza boxes and insulated bags, takeout and third-party delivery apps.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists pizza shops run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants and pizzerias.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Pizza Shop Pre-Shift Meeting Template',
        desc: 'The 5-minute huddle that separates good pizza shops from great ones. Reservations, specials and 86s, allergens, the team on shift.',
        image: '/lovable-uploads/ai-gallery/tareas-pizzeria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Pizza Shop Holiday & Busy Days Calendar (US)',
        desc: "22 key dates for US pizza shops (Super Bowl Sunday, Valentine's Day, St. Patrick's Day and March Madness, Lent Fridays, graduation season, the NBA and NHL playoffs, July 4, football season, Halloween, Thanksgiving Eve, holiday office orders, New Year's Eve) with the key tasks and the recommended lead time.",
        image: '/lovable-uploads/ai-gallery/tareas-pizzeria-mesa.jpg',
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
    ctaLabel: 'YES, I WANT THE PIZZA SHOP CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your pizza shop better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de pizza/SPEC D5 (pizza shop / pizzeria checklist, y la genérica
  // «restaurant opening / closing checklist» en las dos primeras) + las del ES adaptadas (tareas ya escritas, horno de
  // leña / de piso, delivery, masa, frente a las apps, varios locales con la licencia de la tienda EN, garantía) +
  // limpieza, firma, eventos, UK/CA/AU, moneda y suscripción (como los hermanos EN). La de Latinoamérica del ES → la de
  // UK/CA/AU.
  faqs: [
    {
      q: 'What should be on a pizza shop opening checklist?',
      a: "The same as a restaurant opening checklist, built around the oven and the make line, one list per area and in order. Kitchen: personal hygiene first; then the hood on and the kitchen ventilated before you light the oven, the flue checked and the gas checked (if you smell gas, don't light anything); the oven preheated and its temperature checked; the walk-in at 41 °F or below and the freezer at 0 °F or below, with the readings logged; dough balls out of the walk-in to temper; sauce, cheese and toppings prepped; and the make line set up in order: dough, sauce, cheese, toppings. Front of house: lights and HVAC, tables, the specials board, the POS and card terminal, the starting bank and the patio. Delivery: tablets and delivery apps on, pizza boxes, bags and napkins stocked, menus updated in the apps. Every task needs who does it, a due-by time and initials. The \"Pizza Shop Opening & Closing Checklists\" workbook has the kitchen and front of house already written, and the whole-shop checklist covers the alarm, lights, POS and oven preheat.",
    },
    {
      q: 'What goes on a pizzeria closing checklist?',
      a: "Like any restaurant closing checklist: cleaning and shutdown by area, food stored and the money counted, with the oven as the extra step. Kitchen: leftover dough balls, sauce, mozzarella and toppings covered, dated and refrigerated; the oven left to cool down on its own (never doused with water) and the ash removed only once it's cold (at close or first thing the next morning), into a metal container with a lid; the make line, dough table, peel and cutter cleaned; floors, trash and cardboard; tomorrow's dough made; the day's waste logged; and what you need for tomorrow thawing in the walk-in. Front of house: tables, the patio, the delivery tablets off and the pizza boxes counted for tomorrow, the drawer cashed up, the restrooms cleaned, and the lights, HVAC, alarm and lock-up last. In this kit, the closing checklists by area and the whole-shop \"Pizza Shop Closing\" tab have those tasks already written, and the \"Cash Drawer Opening & Closing\" workbook works out the over/short against the POS Z report for you.",
    },
    {
      q: 'Does it work for wood-fired, deck and gas ovens?',
      a: "Yes. The oven tasks cover wood-fired ovens (lighting it, managing the fire and the wood, the chimney, ash removal once cold) and deck or gas ovens (preheating, brushing the oven deck, the burners and the gas valves), with temperatures in °F: 750–840 °F for Neapolitan and 570 °F for Roman-style, and bake times of 60–90 seconds and 3–5 minutes. Preheat and cool-down follow your oven's manufacturer (the kit gives 45–60 minutes of preheat as a guide). If your oven is different (a conveyor, for example), mark N/A what doesn't apply and add your own lines.",
    },
    {
      q: 'Does it include delivery and takeout tasks?',
      a: "Yes. The delivery tablets and third-party apps (DoorDash, Uber Eats, Grubhub) go on at opening and off at closing, menus are updated in the apps, and pizza boxes, bags and napkins are stocked. The delivery driver has a checklist of their own: the vehicle and the insulated bag checked before the shift, every order checked against the ticket, the pizza carried level, delivered within your target time (the kit sets under 30 minutes), hot food at 135 °F or above in the bag and cold items kept apart at 41 °F or below, cash handed in to the shift manager and delivery issues reported. The manager checklists cover delivery times, app fees and reviews, and the quarterly sheet reminds you to review hired and non-owned auto insurance if drivers deliver in their own cars.",
    },
    {
      q: 'Does it cover the dough and the make line?',
      a: "Yes. The pizza maker's tasks follow the dough from the walk-in to the oven: dough balls tempered before service, fermentation, texture and bubbles checked, hand stretching (no rolling pin for Neapolitan), turning the pizza in the oven and checking the leopard spotting, and tomorrow's dough made at closing to cold-ferment at 41 °F or below in covered, dated dough boxes. The make line is set up in order (dough, sauce, cheese, toppings), held at 41 °F or below, refilled before the inserts run low and covered and refrigerated at close, and opened mozzarella is date-marked.",
    },
    {
      q: 'What should a pizzeria cleaning checklist include?',
      a: "Daily cleaning belongs in the closing checklists. On top of that, the kit schedules a weekly deep clean by zone (the oven deck and the outside of the oven, the chimney if it's wood-fired, the oven gaskets, walk-in interiors, the hood, behind and under equipment, cutting boards, shelves, windows, floors, restrooms and the patio), a weekly FIFO check with a freezer shelf-life table, and monthly maintenance of the oven, its thermometer, the dish machine and the hood filters. Contracted services go on the \"Quarterly & Annual\" tab: under NFPA 96, a hood system that serves a wood-fired or other solid-fuel oven is inspected monthly and cleaned whenever buildup is found, alongside pest control, fire extinguishers and the hood suppression system, gas, refrigeration and used cooking oil.",
    },
    {
      q: 'Is there a free pizza shop checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 373 pizza shop tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a pizza shop?',
      a: "Yes. Every checklist comes with the real tasks of a pizza shop already written. You'll want to make it yours: adjust tasks to your shop, delete the ones that don't apply and add your own. The editable cells are green, and each checklist ends with 5 free green rows that the counter already includes.",
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for who does it, when (a due-by time on the daily lists, a day on the weekly ones, a frequency on the monthly ones and a lead time on the event lists), ✓ Done and initials. The shift manager prints the checklist and hands it to the team, and each person checks off and initials their tasks. At the end of the shift, the shift manager checks it and signs at the bottom.',
    },
    {
      q: 'Does it include tasks for game nights, holidays and events?',
      a: "Yes. There are checklists for game night and the Super Bowl delivery rush (extra dough, extra drivers, boxes folded ahead), Valentine's Day, the holiday season (group bookings with allergens in writing, a deposit and a cancellation policy) and opening and closing patio season. And the bonus calendar lists 22 key US dates for pizza shops, from Super Bowl Sunday to New Year's Eve, with their tasks and recommended lead time.",
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it for several pizza shops or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for multi-unit pizza operators. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 135 °F hot holding, in the delivery bag too), the 9 major allergens and a cash count in US bills and coins. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, and allergen information covers 14 allergens (the kit's allergen tasks already note the UK's 14). In Canada and Australia, check your provincial or state food safety rules and allergen list and type them into the tasks. Your patio is your terrace or beer garden, and you can type in the delivery apps you use. For pounds, Canadian or Australian dollars, unprotect the cash count sheet and change the label and value of each bill and coin. If you serve beer or wine, you need the licence your area requires; the legal age is 18 in the UK and Australia, and 19 in most Canadian provinces (18 in Alberta, Manitoba and Quebec). The holiday calendar has a UK note and free rows for your own dates. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
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
    subtitle: "9 templates + 3 bonuses (12 files) for your pizza shop for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: oven, make line, front of house, delivery',
      'Pizza maker tasks: dough, hand stretching, 60–90 second bakes',
      'Oven control: 750–840 °F, cleaning, wood and ash',
      'Manager checklists: daily, weekly, monthly + shift handover',
      'Tasks by role: pizza maker, line cook, shift manager, server, delivery driver',
      'Delivery and takeout: pizza boxes, insulated bags, drivers, delivery apps',
      'Whole-shop opening and closing + cash drawer count',
      'BONUS: Pizza Shop Pre-Shift Meeting Template',
      'BONUS: Pizza Shop Holiday & Busy Days Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PIZZA SHOP CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 10 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas
  // Recurrentes: Pizzería, la edición española de este kit: por eso conservan sus nombres, negocios y cifras, y el
  // subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD. Una frase cambiada (ver cabecera).
  testimonials: {
    subtitle:
      'Pizza makers, shift managers and pizzeria owners who already run their operations with Kit de Tareas Recurrentes: Pizzería, the Spanish edition of this kit',
    items: [
      {
        name: 'Marco Ferrara',
        role: 'Master Pizza Maker, Forno Napoli',
        text: 'The wood-fired oven checklist saved me. Every pizza maker used to fire up the oven their own way and the temperature was all over the place. Now we all follow the same routine and the leopard spotting comes out perfect on every pizza.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Elena Campos',
        role: 'Shift Manager, Pizza & Brasa',
        text: 'Opening a pizzeria with delivery and a dining room was chaos. Since we printed the checklists by area, the team knows exactly what to do before we open. Slip-ups dropped by 90%.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Alberto Moreno',
        role: 'Owner, La Masa Madre Pizzería',
        text: 'I opened my pizzeria 6 months ago and kept forgetting everything: firing up the oven on time, taking the dough out of the walk-in, setting up the toppings. These checklists got me organized from day one.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Lucía Hernández',
        role: 'Operations Manager, Grupo Pizzería Roma',
        text: 'We have 3 pizzerias and every manager used to do things differently. With the checklists we have standardized how we operate. Onboarding new staff went from 2 weeks to 3 days.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Daniel Ortiz',
        role: 'Pizza Maker and Trainer',
        text: 'As a pizza-making trainer, I recommend this kit to all my students. The tasks for fermentation, hand stretching and bake control are perfectly structured. Every pizzeria should have it.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Carmen Ruiz',
        role: 'Director, Pizzería Artesana BCN',
        text: 'The delivery checklists changed our business. Delivery times, the right packaging, every order checked against the ticket. Complaints about wrong orders dropped from 12 a month to 1 or 2.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Domínguez',
        role: 'Line Cook, Il Forno',
        text: 'The pizza make line is where it helped us most. Every ingredient in its place, refilled on time, cleaned after every shift. We used to improvise; now everything flows.',
        avatar: '/avatars/avatar-7.jpg',
      },
      // Testimonio de «Roberto Sánchez, …, PizzaExpress» retirado SOLO en EN (18-oct-2026): PizzaExpress es una
      // cadena real del Reino Unido y, ante un público UK/US, se leería como aval de esa marca. Decide John.
      {
        name: 'Pablo García',
        role: 'Pizza Chef, Napoli Street Food',
        text: 'The pre-shift meeting template alone is worth the price. We never used to hold one. Now in 5 minutes we go over reservations, the pizza of the day and allergens. Service runs much better.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Sergio Navarro',
        role: 'Pizzeria Consultant',
        text: 'The first thing I do with every new client is hand them these checklists. It puts them in order from day one. Oven, dough, make line, delivery... they cover 95% of what any pizzeria needs.',
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
    product: 'pizza-shop-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
