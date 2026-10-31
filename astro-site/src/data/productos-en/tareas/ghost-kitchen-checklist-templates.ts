// astro-site/src/data/productos-en/tareas/ghost-kitchen-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Ghost Kitchen Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-dark-kitchen.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-, bar-, coffee-shop-, catering-, pizza-shop- y burger-joint-checklist-templates.ts. SPEC:
// scripts/productos-digitales/checklists-kit/ghost/SPEC.md (delta) + la base.
//   · D2: nombre «Ghost Kitchen Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Ghost Kitchen Checklists Kit Pro: Cloud Kitchen Opening & Closing Templates». «dark kitchen» nunca en el copy EN
//     (ghost kitchen 33.100/mes US; cloud kitchen 8.100): solo sobrevive en un nombre propio de testimonio.
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (ghost/SPEC §2,
//     dl/ghost-kitchen-checklist-templates/). La intención genérica «restaurant opening / closing checklist» va en el
//     copy (keywords y las dos primeras FAQ).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos (el ES los «valora en €31»). Fórmula de la tienda EN.
//   · Cifras SOLO de ghost/SPEC (D-GHO, D10, D11, D14, §3) y del censo del ES (ghost/censo_es.json; la EN conserva las
//     filas, D10 solo las reordena): 331 tareas (31 + 24 = 55 en el 01; 33 en el 08 con responsable y hora), inventario
//     diario de 32 artículos (proteínas, bases, frescos, salsas y el packaging de cada marca) con Par y «⚠️ REORDER»,
//     22 fechas + 5 huecos y nota UK; caliente a 135 °F o más hasta el empaquetado y frío a 41 °F o menos, en bolsas
//     separadas (3-501.16); pollo 165 °F, picada 155 °F 17 s, pescado 145 °F 15 s (3-401.11); pescado crudo congelado
//     a −4 °F 7 días, −31 °F + 15 h a −31 °F o + 24 h a −4 °F, o con la declaración del proveedor (3-402.11/12); arroz de sushi (3-502.11(D) /
//     3-501.19); precintos (California AB 3336; el resto, check local rules); 8–12 min por pedido, < 10 min el
//     cocinero, < 12 min de media semanal, aceptar en < 30 s, > 15 min en la noche de partido → pausar la marca menos
//     rentable; food cost por marca 25–30 %; comisiones de las apps según el plan (≈ 15–30 %); NFPA 96 trimestral si hay alto volumen (semestral si moderado).
//   · Lo que el ES afirma y el kit no trae, fuera: «Trail €60-75/mes» y «sin internet» (→ la fórmula de los
//     hermanos), Glovo / Just Eat (→ DoorDash, Uber Eats y Grubhub), «coordinación / comunicación con riders» y
//     «tiempos de espera por plataforma» (el kit trabaja con los repartidores de las apps: estantería de recogida por
//     app, pedido comprobado contra el ticket, timbre y avisos de acceso; sin repartidor propio), el «foco por día»
//     del semanal (todo va el lunes), «calibración de balanzas» (la calibración es de termómetros, trimestral),
//     «checklist pre-evento (48h y día)» y «festivos con menú limitado» (→ las 4 hojas reales del 06), «DDD», «BIE» y
//     «Verifactu» (→ servicios contratados US). En el dashboard ES: «6 checklists» en el 01 (son 2) y «17 fechas»
//     (son 22).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los del ES traducidos tal cual (nombres, negocios y
//     cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan. Tres retirados SOLO
//     en EN por citar una marca o cadena real (ver los comentarios en la lista): «CloudEats» (operador real de cloud
//     kitchens de Filipinas), «GhostBurger» (ghost kitchen real de Washington DC, premio RAMMY 2021) y el de las tres
//     apps europeas (Glovo, Uber Eats y Just Eat). Ninguna frase de los 7 que quedan contradice el kit.
//   · Imágenes: ninguna de las 6 del ES lleva texto en español; fuera solo «tareas-dk-tablets» (cuatro tablets con
//     Glovo, Deliveroo, Uber Eats y Just Eat a toda pantalla, apps que la EN no usa) → «tareas-ghost-tablets-en»,
//     JPG de la imagen YA publicada en el blog EN (blog-assets/en/2026/03/post9-order-tablets.png, ghost-kitchen-
//     technology-stack), mismas medidas que el set. OG ES fuera (og-kit-tareas-dark-kitchen lleva «Kit de Tareas» y
//     «€12») → OG = el hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_GHOST_KITCHEN_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'ghost-kitchen-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GHOST_KITCHEN_CHECKLISTS_KIT',

  seo: {
    title: 'Ghost Kitchen Checklists Kit Pro: Cloud Kitchen Opening & Closing Templates',
    description:
      '11 Excel ghost kitchen checklists with 331 tasks already written: opening & closing, stations, packing, delivery apps, manager, roles, cash count. One-time $19.',
    keywords:
      'ghost kitchen checklist, cloud kitchen checklist, virtual kitchen checklist, delivery-only restaurant checklist, ghost kitchen opening checklist, ghost kitchen closing checklist, restaurant opening checklist, restaurant closing checklist, cloud kitchen cleaning checklist, delivery packing checklist, virtual brands, multi-brand kitchen, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-dk-hero.jpg',
  },

  schema: {
    productName: 'Ghost Kitchen Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for multi-brand ghost kitchens with 331 tasks already written: kitchen opening and closing, hot and cold stations, packing by brand, delivery apps and driver pickup, manager, duties by role, daily inventory, cleaning and maintenance schedule, peak nights and brand launches, whole-site opening and closing, and a cash drawer count.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a ghost kitchen opening checklist?',
        a: 'One list in order: personal hygiene, the hood on before any equipment and the gas checked, the walk-in at 41 °F or below and the freezer at 0 °F or below, the steam table at 135 °F or above, prep for every brand, packaging and tamper-evident seals stocked, the packing station set up, then the order tablets on and every brand live in the delivery apps, with menus, 86s and allergens up to date. Each task needs who does it, a due-by time and initials.',
      },
      {
        q: 'What goes on a ghost kitchen closing checklist?',
        a: 'New orders paused and every brand off in the apps once the last orders are out, prep labeled, dated and refrigerated, the fryer oil handled the way the fryer maker says, the hood off once the equipment has cooled, stations cleaned and sanitized, the day’s orders reconciled against each app’s sales report, packaging counted, and the site locked up last, with the alarm set.',
      },
      {
        q: 'Does it cover DoorDash, Uber Eats and Grubhub?',
        a: 'Yes. The tasks cover the order tablets, turning each brand on and off in every app, accepting orders in under 30 seconds, menus, 86s and allergens in each app listing, prep times, refunds, reviews, sales by brand and app, and the app commissions every month.',
      },
      {
        q: 'Is there a free ghost kitchen checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 331 ghost kitchen tasks already written, a counter that skips N/A tasks, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C, hot holding at 63 °C and information on the 14 allergens before the customer orders and again at delivery; in Canada and Australia, your local holding temperatures and allergen list; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Ghost Kitchen Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid: el set del ES (sin texto en español) salvo las tablets con Glovo y Just Eat,
    // que pasan a la foto de tablets ya publicada en el blog EN (ver cabecera).
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-dk-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-produccion.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-empaquetado.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-expedicion.jpg',
      '/lovable-uploads/ai-gallery/tareas-ghost-tablets-en.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-equipo.jpg',
    ],
    // El ES pinta en el BuyBox y el CTA dos fotos de la línea «restaurante» (quirk de la SPA); la EN usa las suyas.
    whyBg: '/lovable-uploads/ai-gallery/tareas-dk-produccion.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-dk-empaquetado.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-dk-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Ghost Kitchen Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Ghost Kitchen Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Cloud Kitchen Opening & Closing Templates',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 331 ghost kitchen tasks already written: opening and closing, hot and cold stations, packing by brand, delivery apps and driver pickup, manager, roles, cleaning, peak nights and a cash drawer count. Print it, delegate it to your team, initial it and file it.',
    checkItems: [
      'Opening and closing checklists: hot and cold stations, packing and the delivery apps',
      'Delivery apps: every brand on and off in DoorDash, Uber Eats and Grubhub, orders accepted in under 30 seconds, prep times under 12 minutes',
      "Packing by brand: each brand's containers and stickers, hot and cold bagged apart, tamper-evident seals",
      'Food safety for delivery: hot food at 135 °F or above until it is packed, cold at 41 °F or below, raw fish for poke and sushi',
      'Whole-site opening and closing, and a cash drawer count by bill and coin',
      '3 editable master templates + a pre-shift meeting template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS DARK KITCHEN — €12»).
  stickyLabel: 'GHOST KITCHEN CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Ghost Kitchen Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '331 ghost kitchen tasks already written and sorted by shift, station and role. Adjust them to your brands, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Ghost Kitchen Opening & Closing Checklists: Kitchen, Packing & Delivery Apps',
        desc: '2 checklists: opening and closing for a multi-brand production kitchen, with the packing station and the delivery apps. Every task with who does it, a due-by time and initials. 55 tasks already written in this file alone.',
      },
      {
        icon: 'Warehouse',
        title: 'Cloud Kitchen Station Checklists: Hot Station, Cold Station & Packing',
        desc: "The hot station (proteins cooked to temperature and checked with a probe: chicken 165 °F, ground beef 155 °F, fish 145 °F; hot food held at 135 °F or above until it is packed; each order ready in 8–12 minutes), the cold station (bowls and salads, raw fish for poke and sushi only if it was frozen to kill parasites or comes with the supplier's letter, sushi rice, inserts at 41 °F or below) and the packing station (each brand's containers and stickers, hot and cold in separate bags, allergen orders labeled and kept apart, tamper-evident seals, the order checked against the ticket before it goes to the driver).",
      },
      {
        icon: 'ClipboardList',
        title: 'Ghost Kitchen Manager Checklist: Daily, Weekly, Monthly & Shift Handover',
        desc: "Daily (order forecast, brands paused when the kitchen is overloaded, refunds, the team's time-clock records), weekly (sales and ratings by brand and app, average prep time under 12 minutes, each app listing's allergens checked against the real recipe, reviews answered) and monthly (P&L and food cost by brand with a 25–30% target, delivery app commissions, packaging cost per order, which brand to cut or launch), plus a shift handover: open orders, paused brands, items running low, packaging and fryer oil.",
      },
      {
        icon: 'Users',
        title: 'Virtual Kitchen Duties by Role: Cook, Packer, App Manager & Operations Manager',
        desc: 'Checklists for the multi-brand cook, the packer, the app manager (order tablets, brands on and off, orders accepted in under 30 seconds, 86s and refunds) and the operations manager: what each role does at opening, during service and at closing.',
      },
      {
        icon: 'CalendarDays',
        title: 'Cloud Kitchen Cleaning Checklist, Inventory & Maintenance Schedule',
        desc: 'Daily inventory of 32 items (proteins, bases, produce, sauces and the packaging for each brand) with par levels and a REORDER flag, weekly deep clean, weekly FIFO check with a freezer shelf-life table, and monthly maintenance of the equipment, the order tablets, the ticket printer and the Wi-Fi. + a Quarterly & Annual sheet for contracted services: pest control, hood and duct cleaning (NFPA 96), fire extinguishers and hood suppression, gas, refrigeration, used fryer oil and cardboard pickup, thermometer calibration, insurance with products coverage, and the delivery app contracts, commissions and sales tax, with the service report number and initials.',
      },
      {
        icon: 'PartyPopper',
        title: 'Ghost Kitchen Peak Checklists: Friday Rush, Game Night, Brand Launch & Holidays',
        desc: 'The Friday night rush (prep on Thursday, 50% more mise en place, weekend promos in the apps), game night (double stock of the top sellers, extra packaging, an extra cook and packer, and the least profitable brand paused if prep times pass 15 minutes), a new brand launch (8–12 menu items, packaging, app listings with allergens declared before going live, a timed test run, first-week data) and the holiday season, each task with its lead time.',
      },
      {
        icon: 'FileEdit',
        title: 'Blank Ghost Kitchen Checklist Template (Editable)',
        desc: '3 master templates already structured (by time of day, by area and by role) with the sections and the area or person in charge set up: you just type your tasks in the green cells.',
      },
      {
        icon: 'Building2',
        title: 'Delivery-Only Kitchen Opening & Closing Checklist (Whole Site)',
        desc: 'The checklist for the whole site, not just the kitchen: alarm, lights, HVAC, the POS, the order tablets and ticket printers, the driver pickup area and doorbell, the packing station and every brand in the apps, in a safe order: brands go live only once the tablets, printers and prep times are checked, and at close they go off before the alarm and the lock-up. Who does it and the due-by time are filled in for all 33 tasks.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. Plus a monthly cash log with the over/short by formula for every day of the month.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Ghost Kitchen Pre-Shift Meeting Template (Huddle Notes)',
        desc: 'Pre-shift meeting template: the order forecast, the brands live today and their hours, promos by app, 86s, allergens to watch and the team on shift (kitchen, packing and the app manager). Print it and post it in the kitchen.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Ghost Kitchen Holiday & Peak Delivery Days Calendar (US)',
        desc: "22 key US dates for delivery, from Super Bowl Sunday, March Madness and Cinco de Mayo to football season, Thanksgiving, the cold and rainy days that push orders up and New Year's Eve, with the key tasks and recommended lead time for each, a UK note and 5 free rows for your own.",
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
        title: 'Pre-Filled for Ghost Kitchens',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a ghost kitchen running several virtual brands. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Tablet',
        title: 'Delivery Apps and Order Tablets',
        desc: 'Every brand on and off in DoorDash, Uber Eats and Grubhub, orders accepted in under 30 seconds, prep times under 12 minutes, 86s, refunds, reviews and sales by brand and app.',
      },
      {
        icon: 'Package',
        title: 'Multi-Brand Packing and Driver Pickup',
        desc: "Each brand's containers and stickers, hot and cold packed apart, allergen orders labeled, tamper-evident seals, the order checked against the ticket and a driver pickup shelf for each app.",
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists ghost kitchens run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants, ghost kitchens and cloud kitchens.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Ghost Kitchen Pre-Shift Meeting Template',
        desc: 'The 5-minute huddle that separates good ghost kitchens from great ones. The brands live today, promos by app, 86s, allergens and the team on shift.',
        image: '/lovable-uploads/ai-gallery/tareas-dk-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Ghost Kitchen Holiday & Peak Delivery Days Calendar (US)',
        desc: "22 key dates for US delivery (Super Bowl Sunday, Valentine's Day, Lent Fridays and Easter, St. Patrick's Day and March Madness, Cinco de Mayo, Mother's Day and Father's Day, graduation season, July 4, Labor Day and football season, Halloween, Thanksgiving and Black Friday, holiday office parties, New Year's Eve) with the key tasks and the recommended lead time.",
        image: '/lovable-uploads/ai-gallery/tareas-ghost-tablets-en.jpg',
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
    ctaLabel: 'YES, I WANT THE GHOST KITCHEN CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your ghost kitchen better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de ghost/SPEC D5 (ghost / cloud kitchen checklist, y la genérica «restaurant
  // opening / closing checklist» en las dos primeras) + las del ES adaptadas (tareas ya escritas, apps de delivery,
  // empaquetado por marca, repartidores de las apps, frente a las apps, varias cocinas con la licencia de la tienda EN,
  // garantía) + seguridad alimentaria del delivery, limpieza, firma, picos y lanzamientos, UK/CA/AU, moneda y
  // suscripción (como los hermanos EN). La de Latinoamérica del ES → la de UK/CA/AU.
  faqs: [
    {
      q: 'What should be on a ghost kitchen opening checklist?',
      a: "The same as a restaurant opening checklist, built around production and delivery instead of a dining room, one list in order. Personal hygiene first (clean uniform, no jewelry, cuts covered, hands washed, anyone with symptoms stays off food). Then the hood on and the kitchen ventilated before any equipment, a check that the hood really draws, and the gas checked (if you smell gas, don't turn anything on); the griddle, oven, fryer and burners on, and the steam table at 135 °F or above; the walk-in at 41 °F or below and the freezer at 0 °F or below, with the readings logged; prep for every brand (house sauces, cut vegetables and proteins, rice and pasta); each brand's containers, delivery bags, utensils and tamper-evident seals stocked; and the packing station set up. Last, the order tablets on and online, every brand live in the delivery apps, menus and prices up to date, each dish's allergens still listed, the ticket printer working and 86s paused. Every task needs who does it, a due-by time and initials. The \"Ghost Kitchen Opening & Closing Checklists\" workbook has it all written, and the whole-site checklist covers the alarm, lights, POS, driver pickup area and printers.",
    },
    {
      q: 'What goes on a ghost kitchen closing checklist?',
      a: "Like any restaurant closing checklist: cleaning and shutdown by area, food stored and the money counted, plus the delivery apps. Kitchen: prep labeled and dated, sauces in sealed containers and everything covered and refrigerated at 41 °F or below; what you won't use tomorrow frozen the same day in single-use portions; the day's waste logged by brand; the griddle, oven, fryer and burners off, and the fryer oil filtered or changed the way your fryer maker says; the hood off once the griddle, oven and fryer have cooled; the walk-in temperature logged and the gas shut off; stations cleaned and sanitized, floors, trash and a lot of cardboard; the packing station cleaned, every brand off in the apps and the tablets off; the day's orders reconciled against each app's sales report, and cancellations, refunds and complaints noted; tomorrow's orders placed and what you need thawing in the walk-in. The whole-site \"Site Closing\" tab pauses new orders first, checks no driver is still waiting, turns the brands off before the alarm and the lock-up, and the \"Cash Drawer Opening & Closing\" workbook works out the over/short against the POS Z report for you.",
    },
    {
      q: 'Does it cover DoorDash, Uber Eats and Grubhub?',
      a: "Yes. The app manager checklist turns the order tablets on (Wi-Fi and battery checked), turns every brand on in every app, keeps menus and daily promos up to date, 86s what's out of stock, accepts orders in under 30 seconds, watches prep times, handles cancellations, changes and refunds, pauses brands when the kitchen is overloaded and turns everything off at close. The manager checklists add ratings and reviews by brand and app, prep times against a 12-minute target, price checks against the competition in each app, sales by brand and app, and the app commissions every month (they depend on your plan, roughly 15–30%, and some cities, such as New York and San Francisco, cap them).",
    },
    {
      q: 'Does it include packing tasks for each brand?',
      a: "Yes. The packing station and packer checklists cover each brand's containers, bags and stickers, utensils, napkins and extra sauce, the brand sticker and the order ticket on every bag, hot and cold food in separate bags so hot food stays at 135 °F or above and cold food at 41 °F or below until pickup, allergen orders labeled where everyone can see them and kept apart on the pickup shelf, the order checked against the ticket, and a tamper-evident seal on the bag (California requires one on ready-to-eat food that an app's driver picks up; elsewhere, check your city or state rules). The packaging left is counted at close and the daily inventory tracks each brand's containers, bags, stickers and seals.",
    },
    {
      q: 'Does it cover food safety for delivery?',
      a: "Yes, under the FDA Food Code: chicken cooked to 165 °F, ground beef to 155 °F for 17 seconds and fish to 145 °F for 15 seconds, checked with a probe; raw meat kept apart from ready-to-eat food; cooked food cooled from 135 °F to 70 °F in 2 hours and to 41 °F in 4 more, and reheated to 165 °F within 2 hours; date marking for up to 7 days; and thawing in the walk-in. For poke and sushi, raw fish is used only if it was frozen to kill parasites (−4 °F for 7 days, or −31 °F until solid and then 15 hours at −31 °F or 24 hours at −4 °F) or the supplier states it in writing, with the record kept for 90 days and a consumer advisory on the app listing; sushi rice is held at 41 °F or below, under a written time-as-a-public-health-control procedure (marked and thrown out after 4 hours), or acidified with a variance and a HACCP plan from your health department. Sanitizer is checked with test strips.",
    },
    {
      q: 'Does it cover driver pickup?',
      a: 'Yes, for drivers who come from the delivery apps. The tasks cover the driver pickup area (a clear counter, pickup shelves marked by app and good lighting), the pickup signs and each brand\'s hours, the doorbell or intercom and the access instructions you publish in each app, the order number checked when handing it over and the pickup confirmed on the tablet, no driver left waiting at close, and missing drivers or late pickups noted in the shift handover. The kit is written for third-party delivery: there is no checklist for your own drivers.',
    },
    {
      q: 'What should a cloud kitchen cleaning checklist include?',
      a: "Daily cleaning belongs in the closing checklists. On top of that, the kit schedules a weekly deep clean (walk-in interiors, the hood filters, behind and under equipment, cutting boards deep-cleaned and inspected, a fryer boil-out, floors with degreaser, the packaging storeroom organized by brand, the pickup shelves cleaned and damaged packaging pulled), a weekly FIFO check (fresh proteins for 3 days at most, house sauces for 5, cut vegetables for 2) with a freezer shelf-life table, and monthly maintenance of the griddle, the fryer (the oil itself is changed when the TPM tester says), the dish machine, the hood motor and filters and the walk-in gaskets, plus the order tablets, the app updates, the ticket printer and the Wi-Fi, and a visual check of the fire extinguisher and the first aid kit. Contracted services go on the \"Quarterly & Annual\" tab: hood and duct cleaning under NFPA 96 (quarterly for a high-volume kitchen that cooks all day, semiannual if moderate), alongside pest control, fire extinguishers and the hood suppression system, gas, refrigeration, used fryer oil and cardboard and plastic pickup, and thermometer calibration.",
    },
    {
      q: 'Is there a free ghost kitchen checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 331 ghost kitchen tasks already written and sorted by shift, station and role, a counter on every checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a multi-brand ghost kitchen?',
      a: "Yes. Every checklist comes with the real tasks of a ghost kitchen that runs several virtual brands already written. You'll want to make it yours: adjust tasks to your operation, delete the ones that don't apply and add the ones specific to your brands. The editable cells are green, and each checklist ends with 5 free green rows that the counter already includes.",
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for who does it, when (a due-by time on the daily lists, a day on the weekly ones, a frequency on the monthly ones and a lead time on the peak and launch lists), ✓ Done and initials. The shift manager prints the checklist and hands it to the team, and each person checks off and initials their tasks. At the end of the shift, the shift manager checks it and signs at the bottom.',
    },
    {
      q: 'Does it include tasks for peak nights and brand launches?',
      a: "Yes. There are checklists for the Friday night rush (extra ingredients and packaging ordered on Thursday, a bigger team, 50% more mise en place, weekend promos in the apps), game night (double stock of the top sellers, extra packaging, an extra cook and packer, and the least profitable brand paused if prep times pass 15 minutes), a new brand launch and the holiday season. The brand launch checklist runs from two weeks out: a menu of 8–12 items, packaging, the brand's listing in each app with photos, descriptions and prices, allergens declared before the brand goes live, the team trained and a timed test run, then a launch promo and the first week's data. Each kitchen needs its health permit; virtual brands usually run under it, but some cities ask you to report or register them, and you register each brand's trade name (DBA) if your state requires it. And the bonus calendar lists 22 key US delivery dates, from Super Bowl Sunday to New Year's Eve, with their tasks and recommended lead time.",
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it for several ghost kitchens or virtual brands?',
      a: "Yes. One purchase covers one business with all of its kitchens and virtual brands, which makes it a good fit for multi-site operators. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 135 °F hot holding), the 9 major allergens in each app listing and a cash count in US bills and coins. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, and for food sold online the information on the 14 allergens has to be available before the customer orders and again when the food is delivered (the kit's allergen tasks already note the UK's 14). In Canada and Australia, check your provincial or state food safety rules and allergen list and type them into the tasks. Type in the delivery apps you use, and check the tamper-evident seal rules in your area. For pounds, Canadian or Australian dollars, unprotect the cash count sheet and change the label and value of each bill and coin. The holiday calendar has a UK note and free rows for your own dates. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
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
    subtitle: "9 templates + 3 bonuses (12 files) for your ghost kitchen for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: hot and cold stations, packing, delivery apps',
      'Delivery apps: brands on and off in DoorDash, Uber Eats and Grubhub, 86s, prep times, reviews',
      'Multi-brand packing: brand containers, tamper-evident seals, allergen orders labeled',
      'Manager checklists: daily, weekly, monthly + shift handover',
      'Tasks by role: multi-brand cook, packer, app manager, operations manager',
      'Driver pickup: pickup shelves by app, every order checked against the ticket',
      'Whole-site opening and closing + cash drawer count',
      'BONUS: Ghost Kitchen Pre-Shift Meeting Template',
      'BONUS: Ghost Kitchen Holiday & Peak Delivery Days Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE GHOST KITCHEN CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Dark Kitchen, la edición española de este kit: por eso conservan sus nombres, negocios y cifras, y el subtítulo lo
  // dice. Solo se pintan: NO alimentan el JSON-LD. «Dark Kitchen Valencia» es nombre propio (D2 manda en el copy, no en
  // los nombres de negocio). Tres retirados SOLO en EN (ver los comentarios); ninguna frase cambiada.
  testimonials: {
    subtitle:
      'Ghost kitchen operators, cooks and packers who already run their operations with Kit de Tareas Recurrentes: Dark Kitchen, the Spanish edition of this kit',
    items: [
      {
        name: 'Roberto Navarro',
        role: 'Ghost Kitchen Operator, 4 virtual brands',
        text: 'Running 4 brands out of the same kitchen was chaos. Since we printed the checklists by station and by brand, packing mistakes dropped by 85%. Every shift knows exactly what to do.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Elena Morales',
        role: 'Owner, Multi-Brand Ghost Kitchen',
        text: 'I opened my ghost kitchen 6 months ago and kept getting lost with the tablets, the apps and the different packaging for each brand. These checklists got me organized from day one. A must-have.',
        avatar: '/avatars/avatar-2.jpg',
      },
      // Testimonio de «Daniel Ortiz, Encargado de Operaciones, CloudEats» retirado SOLO en EN (18-oct-2026): CloudEats es
      // un operador real de cloud kitchens y marcas virtuales (Filipinas, con cocinas en Vietnam); en la tienda EN se
      // leería como aval de esa empresa. Mismo criterio que Burger Factory y PizzaExpress. Decide John.
      {
        name: 'Carmen Ruiz',
        role: 'Multi-Concept Cook, 3 brands',
        text: 'Cooking for 3 different brands at the same station takes military-level organization. The checklists by role save my shift every day. I know exactly what to prep for each brand.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Marcos Gimenez',
        role: 'Packer / Expediter, FoodFactory BCN',
        text: 'The packing checklist by brand changed my life. Tamper-evident seals, the right labels, different packaging for each brand. Complaints about wrong orders dropped to zero.',
        avatar: '/avatars/avatar-5.jpg',
      },
      // Laura Serrano: el ES cita Glovo, Uber Eats y Just Eat; en EN se cambia SOLO esa frase por «three delivery apps»
      // (regla de John: testimonio que choca con el kit → cambiar solo esa frase).
      {
        name: 'Laura Serrano',
        role: 'Platform Manager, DarkKitchen Madrid',
        text: 'Managing three delivery apps at once without a checklist is impossible. Now I know exactly what to check at opening, during service and at closing. Our prep times dropped to 10 minutes.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Pascual',
        role: 'Director of Operations, Grupo Virtual Foods',
        text: 'We run 3 ghost kitchens and every manager used to do things differently. With the checklists we standardized the operation. Onboarding new staff went from 2 weeks to 3 days.',
        avatar: '/avatars/avatar-7.jpg',
      },
      // Testimonio de «Hugo Martinez, Fundador, GhostBurger + GhostPoke + GhostWok» retirado SOLO en EN (18-oct-2026):
      // Ghostburger es una marca real de EE. UU. (nació como ghost kitchen en Washington DC en 2020, premio RAMMY 2021,
      // hoy con local propio); ante un público US se leería como el fundador de esa marca. Decide John.
      {
        name: 'Pablo Herrero',
        role: 'Executive Chef, Dark Kitchen Valencia',
        text: 'The pre-shift meeting template alone is worth the price. We never used to hold one. Now in 5 minutes we go over the brands that are live, the promos running and the 86s. Service runs perfectly.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Adrián Soto',
        role: 'Ghost Kitchen Consultant',
        text: 'The first thing I do with every new client is hand them these checklists. It puts them in order from day one. Production, packing, delivery apps, drivers... they cover 95% of what any ghost kitchen needs.',
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

  // Saliente extra (no lo llevan los hermanos): el caso de uso EN de las ghost kitchens, que a su vez lista este kit
  // (products-catalog.ts urlByLang.en). Sin guía EN de dark kitchen todavía.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/bar-checklist-templates', label: 'Bar Checklists Kit Pro' },
    { href: '/en/digital-products/coffee-shop-checklist-templates', label: 'Coffee Shop Checklists Kit Pro' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
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
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: '/en/use-cases/concept/dark-kitchen', label: 'AI for Ghost Kitchens' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'ghost-kitchen-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
