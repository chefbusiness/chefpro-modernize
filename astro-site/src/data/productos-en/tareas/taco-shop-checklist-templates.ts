// astro-site/src/data/productos-en/tareas/taco-shop-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Taco Shop Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-taqueria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// (pizza-shop- y hotel-checklist-templates.ts los más cercanos). SPEC: scripts/productos-digitales/checklists-kit/taco/
// SPEC.md (delta) + la base.
//   · D2: nombre «Taco Shop Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Taco Shop Checklists Kit Pro: Taqueria Opening & Closing Checklist Templates for Excel». «taqueria» sin tilde;
//     nunca «Tex-Mex» ni «authentic» (research US §9). Jerga = la del hermano LIVE Taco Shop Business Plan Kit (trompo,
//     taquero, salsa bar, comal, flat-top griddle, Mexican food distributor).
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (taco/SPEC §2, dl/taco-shop-checklist-templates/).
//     Las colas «taco shop / taqueria checklist» no tienen volumen US medido: la intención genérica «restaurant opening /
//     closing checklist» va en keywords y en las dos primeras FAQ, nunca en los xlsx.
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld, discountBadge,
//     bonusSaveLine, `value` en los bonos, aggregateRating ni review (el ES los lleva: 4,9 de 8 reseñas, -80 %, «ahorra
//     €55», «valorados en €49»). Fórmula de la tienda EN.
//   · Cifras SOLO de taco/SPEC y del censo (taco/censo_es.json, paridad estructural 1:1 con los xlsx EN): 11 libros, 36
//     hojas, 298 tareas (50 en el 01: 28 de apertura y 22 de cierre; 36 en el 02; 48 en el 03; 39 en el 04; 25 en el 05;
//     48 en el 06, 8 por puesto; 26 en el 07; 26 en el 08), 5 filas verdes libres al pie de cada checklist, 27 filas en el
//     calendario anual + 5 libres y nota UK. °F solo de GRADOS_F_SPEC (0, 32, 41, 70, 135, 145, 155, 165); °C solo en la
//     FAQ UK (8 / 63 °C).
//   · Lo que el ES afirma y el kit EN no trae, fuera: «el software de gestión cobra €40/mes» (→ la fórmula de los hermanos),
//     RD 1021/2022 y sus 63 / 74 / 4 / −18 °C (→ FDA Food Code en °F), «los 65 °C que ya no aplican», los 14 alérgenos de
//     la UE (→ los 9 de EE. UU.; UK 14), «estándar Sanidad» (→ food safety), «Imprimible A4» (→ US Letter), «campañas
//     españolas de terraza y Navidad» (→ fechas US: Super Bowl, Cinco de Mayo, Memorial Day, Thanksgiving), «importador»
//     (→ Mexican food distributor), «formación del equipo» del calendario anual (el B02 no la trae: va en el 05 y el 07),
//     «stock de tortilla» del briefing (el B01 trae 86s y la tortilla de harina sí/no) y la guía ES↔LatAm (→ Equivalents
//     Guide).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Testimonios: los 8 del ES traducidos tal cual (nombres, roles y ciudades de origen, sin marcas), con el subtítulo de
//     la edición española (TIENDA §3.5). Solo se pintan. Una frase que el kit EN contradice, cambiada (regla de John,
//     11-oct): Carmen Ibáñez («las campañas españolas» y «chiles en nogada en otoño» → «the busy days» y «chiles en nogada
//     season»: el calendario EN es de fechas US y la temporada va del 15 de julio a finales de septiembre). Avatares
//     reasignados para que el género y el oficio cuadren con el nombre y el rol (en el ES, Guadalupe lleva un avatar de hombre).
//   · Imágenes: las 6 del ES, abiertas una a una el 31-oct-2026 (sin texto legible, sin logos ni marcas). Fuera la OG ES
//     (og-kit-tareas-taqueria.jpg: «Kit de Tareas Recurrentes», €) → OG = el hero, como los hermanos EN.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'taco-shop-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_CHECKLISTS_KIT',

  seo: {
    title: 'Taco Shop Checklists Kit Pro: Taqueria Opening & Closing Checklist Templates for Excel',
    description:
      '11 Excel taco shop checklists with 298 tasks already written: opening & closing, trompo, salsa bar, allergens, nixtamal, tortillas, manager, roles. One-time $19.',
    keywords:
      'taco shop checklist, taqueria checklist, taco shop opening checklist, taco shop closing checklist, taqueria opening checklist, taqueria closing checklist, restaurant opening checklist, restaurant closing checklist, taco shop cleaning checklist, salsa bar checklist, al pastor trompo checklist, taqueria manager checklist, taco shop food safety checklist, AI Chef Pro',
    // OG = el hero de la ficha (como los hermanos EN): el og-kit-tareas-taqueria.jpg del ES lleva texto en español y €.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-taqueria-hero.jpg',
  },

  schema: {
    productName: 'Taco Shop Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for taco shops with 298 tasks already written: opening and closing, the trompo, griddle and comal, temperature logs and receiving, the salsa bar and allergens, nixtamal, masa, tortillas and guisados, the manager, duties by role, weekly and monthly cleaning and upkeep, events and seasonal ingredients, a pre-shift meeting template and an annual calendar.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN). Sin reviews ni
    // aggregateRating (D3).
    faqs: [
      {
        q: 'What should be on a taco shop opening checklist?',
        a: 'One list per area, in order: temperatures (walk-in coolers at 41 °F or below, the freezer at 0 °F or below, the salsa bar display holding 41 °F or below, the probe calibrated), the trompo lit and the cone checked as received before you stack it, the griddle and comal calibrated, raw salsas on the cold salsa bar with the allergen sign flagging the salsa macha, guisados in the steam table at 135 °F or above, and the POS, starting bank and delivery apps. Each task needs who does it, a due-by time and initials.',
      },
      {
        q: 'What goes on a taqueria closing checklist?',
        a: 'The trompo off and the leftover meat logged as cooled or tossed (reused only if your health department allows it), the drip tray, griddle, comal and fryer cleaned, the day\'s raw salsas and salsa macha tossed and logged, guisados cooled or tossed, the salsa bar, blender and molcajete cleaned and sanitized, the cash count and tip split, the delivery apps off, the temperature log signed, and the lock-up last.',
      },
      {
        q: 'What temperature does al pastor need on the trompo?',
        a: 'The FDA Food Code minimum for pork like the layers on a trompo is 145 °F for 15 seconds, and that is what the kit uses for the outer layer you carve, or your county\'s figure if it is stricter (some ask for 155 °F). The leftover cone and the maximum time on the broiler are set by your county, so the kit leaves a blank for them.',
      },
      {
        q: 'Is there a free taco shop checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 298 taco shop tasks already written, a counter that skips N/A tasks and °F temperatures under the FDA Food Code. Print it on US Letter or save it as a PDF from Excel.',
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
    breadcrumbName: 'Taco Shop Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid: las 6 fotos del ES (sin texto legible, sin logos ni marcas). Mismo reparto que el ES.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-taqueria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-trompo.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-tortilleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-salsas.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-equipo.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-tacos.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-taqueria-trompo.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-taqueria-tacos.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-taqueria-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Taco Shop Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Taco Shop Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Taqueria Opening & Closing Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) with 298 taco shop tasks already written in Excel: opening and closing, the trompo, griddle and comal, food safety with the salsa bar and allergens, nixtamal, tortillas and guisados, manager, roles, cleaning and events. Print it, delegate it to your team, initial it and file it.',
    checkItems: [
      'Opening and closing checklists: trompo, griddle and comal, salsa bar, tortillas, guisados, counter and delivery',
      "Trompo for al pastor: cone check, stacking, a probe at 145 °F (or your county's figure), carving and yield in tacos per pound",
      'Nixtamal and tortillas: corn mill, masa, tortilla machine calibration and waste from your own tortilleria',
      'Salsa bar and allergens: salsa macha (peanuts and/or sesame) kept apart, corn tortillas apart from flour',
      'Annual calendar: Three Kings Day, Super Bowl Sunday, Cinco de Mayo, chiles en nogada, Day of the Dead and the posadas',
      'Manager checklists, duties for 6 roles, a blank template and a pre-shift meeting template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS TAQUERÍA MEXICANA — €14»).
  stickyLabel: 'TACO SHOP CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Taco Shop Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '298 taco shop tasks already written and sorted by shift, area and role. Adjust them to your taqueria, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Taco Shop Opening & Closing Checklists: Trompo, Salsa Bar, Tortillas & Counter',
        desc: 'Opening (28 tasks) and closing (22): walk-in and freezer temperatures, the trompo lit and the cone checked before it is stacked, the cold salsa bar, guisados in the steam table, the POS and delivery apps; at close, where the leftover trompo meat goes, the cash count and tip split, and the lock-up last. 50 tasks already written in this file alone.',
      },
      {
        icon: 'Flame',
        title: 'Trompo, Griddle & Comal Checklists: Al Pastor Marinade, Stacking & Carving',
        desc: "Marinade and stacking of the trompo for al pastor (if you have one): weight, batch, stacking time and time limit, the outer layer probed at 145 °F or above (or your county's figure if stricter) at the start and middle of service, and the yield in tacos per pound. Carving, griddle and comal without cross-contact: separate boards for raw and cooked meat, flour and corn tortillas apart.",
      },
      {
        icon: 'ShieldCheck',
        title: 'Taco Shop Food Safety Checklists: Temperature Logs, Salsa Bar & Allergens',
        desc: 'Temperature logs twice per shift (walk-ins and salsa bar at 41 °F or below, freezer at 0 °F or below, guisados at 135 °F or above), receiving and traceability, reheating to 165 °F, raw fish for aguachiles; the self-serve salsa bar with the time each salsa goes on and gets tossed; and the 9 major allergens, starting with the salsa macha (peanuts and/or sesame) and corn vs. flour tortillas.',
      },
      {
        icon: 'Wheat',
        title: 'Nixtamal, Masa, Tortilla & Guisados Checklists',
        desc: "The tortilleria's early shift: nixtamal cooking and milling (if you make your own), masa held as a TCS food, tortilla machine calibration and waste, purchased tortillas checked at receiving, and the guisados (stews in hotel pans) in the steam table with rotation, reheating and leftovers.",
      },
      {
        icon: 'Briefcase',
        title: 'Taqueria Manager Checklist: Daily & Weekly',
        desc: 'The order to your Mexican food distributor for dried chiles and masa with its lead time, pork and beef prices from at least two suppliers, beverage, mezcal and tequila inventory (only with a license), taco costing of your best sellers, trompo waste, the tip split and the time-clock records.',
      },
      {
        icon: 'Users',
        title: 'Taco Shop Duties by Role: Taquero, Tortilla Maker, Salsa Prep, Griddle, Counter & Driver',
        desc: 'Clear tasks for 6 roles: the taquero on the trompo, the tortilla maker, the salsa prep cook, the griddle and fryer, the counter and register, and the delivery driver. 8 tasks each, no overlaps.',
      },
      {
        icon: 'ClipboardList',
        title: 'Taco Shop Weekly & Monthly Checklists: Deep Cleaning, Inventory & Maintenance',
        desc: 'Weekly deep clean of the corn mill, tortilla machine, fryer and salsa bar, the trompo and hood filters degreased, dried chile inventory and pest checks, and team training; monthly gas checks, thermometer calibration, HACCP and allergen reviews, the time-clock file and an audit of your Mexican food distributors.',
      },
      {
        icon: 'CalendarDays',
        title: 'Taco Shop Event & Seasonal Checklists: Holidays, Busy Days & Seasonal Ingredients',
        desc: 'An event calendar by quarter (Three Kings Day, Candelaria, Lent Fridays, Holy Week and Easter, Cinco de Mayo, patio season, Memorial Day, Mexican Independence Day, Day of the Dead, Our Lady of Guadalupe, the posadas and holiday parties) and seasonal ingredients: chiles en nogada, dried chiles by harvest, pork and corn, avocado and fresh chiles.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Blank Taco Shop Checklist Template (Editable)',
        desc: "A blank checklist with the kit's structure (3 sections you name, 15 numbered rows plus 5 free ones, area, who does it, due-by time, ✓ Done, initials and the counter) to build checklists for your exact concept, with or without a trompo, with or without your own tortilleria.",
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Taco Shop Pre-Shift Meeting Template (Huddle Notes)',
        desc: 'A 5-minute pre-shift meeting: the trompo of the day, the guisados and salsas with their heat level, the allergen notice (salsa macha, mole, flour tortillas), 86s and the dining area and delivery forecast.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Taco Shop Annual Calendar: Holidays, Busy Days & Upkeep (US)',
        desc: '27 dates and yearly tasks for a US taco shop, from Three Kings Day and Super Bowl Sunday to Cinco de Mayo, chiles en nogada, Day of the Dead and the posadas, plus gas, hood, pest control and thermometer upkeep, with the lead time for each, a UK note and 5 free rows for your own.',
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a hospitality consultant since 2010, set up for a US taco shop under the FDA Food Code.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Built for Taco Shops',
        desc: 'Not restaurant templates with the name changed. Checklists for the real operation of a taqueria: the trompo, the tortilleria and the self-serve salsa bar.',
      },
      {
        icon: 'Flame',
        title: 'Al Pastor on the Trompo, Under Control',
        desc: "Marinade, stacking, the probe and the time limit for the stacked cone, with the FDA Food Code minimum for the layer you carve: 145 °F, or your county's figure if it's stricter (some ask for 155 °F).",
      },
      {
        icon: 'Thermometer',
        title: 'Salsa Bar and Allergens',
        desc: 'The riskiest point in a taqueria, with the time each salsa goes on and gets tossed, held at 41 °F or below, and the 9 major allergens, starting with the salsa macha (peanuts and/or sesame).',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same kind of task lists taquerias run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has advised taquerias and Mexican restaurants on running their operations professionally, especially the trompo for al pastor and food safety at the salsa bar.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Taco Shop Pre-Shift Meeting Template',
        desc: 'A 5-minute pre-shift meeting: the trompo of the day, the guisados and salsas, the allergen notice starting with the salsa macha, 86s and the dining area and delivery forecast. The sheet that lines up the team every shift.',
        image: '/lovable-uploads/ai-gallery/tareas-taqueria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Taco Shop Annual Calendar (US)',
        desc: "12 months of key dates for a US taco shop: Mexican holidays (Three Kings Day, Candelaria, chiles en nogada season, Mexican Independence Day, Day of the Dead, Our Lady of Guadalupe, the posadas), US busy days (Super Bowl Sunday, Lent Fridays, Cinco de Mayo, Memorial Day, Thanksgiving, New Year's Eve) and equipment upkeep, with the recommended lead time.",
        image: '/lovable-uploads/ai-gallery/tareas-taqueria-trompo.jpg',
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
    ctaLabel: 'YES, I WANT THE TACO SHOP CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your taqueria more professionally and stay on top of food safety, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US (taco shop / taqueria checklist, y la genérica «restaurant opening / closing
  // checklist» en las dos primeras) + las 7 del ES adaptadas (temperaturas → FDA Food Code en °F, sin trompo, tacos por
  // trompo, cómo se lleva una taquería con el kit, garantía; Google Sheets fuera hasta el test real; la de Latinoamérica →
  // UK/CA/AU) + trompo, salsa bar, nixtamal, limpieza, plantilla gratis, firma, eventos, apps, varios locales, caja,
  // moneda y suscripción (como los hermanos EN).
  faqs: [
    {
      q: 'What should be on a taco shop opening checklist?',
      a: "The same as a restaurant opening checklist, built around the trompo, the salsa bar and the tortillas, one list per area and in order. Temperatures first: the walk-in coolers at 41 °F or below and the freezer at 0 °F or below, with the readings logged, the salsa bar display holding 41 °F or below, the shift's probe calibrated and the hood running. Then the trompo (light it and check every burner; if you smell gas, light nothing and call from outside), the cone checked as received before you stack it, the griddle and comal calibrated by zone and the fryer oil checked. Salsas and garnishes: raw salsas on the cold salsa bar, the allergen sign flagging the salsa macha and a utensil of its own for every salsa. Tortillas and guisados: the guisados in the steam table at 135 °F or above, the first batch of corn tortillas calibrated, corn and flour stock checked separately. Counter and delivery: the POS and starting bank, the delivery apps on with the menu current, and the pre-shift meeting. The \"Taco Shop Opening\" tab has those 28 tasks already written, each with who does it, a due-by time and initials.",
    },
    {
      q: 'What goes on a taqueria closing checklist?',
      a: "Like any restaurant closing checklist: shutdown and cleaning by area, food stored or tossed, and the money counted. The trompo goes off and the leftover meat comes off it with a note of where it went: cooled or tossed, reused only if your health department allows it, and if kept, cooled from 135 °F to 70 °F within 2 hours and to 41 °F within 4 more, covered and date-marked. The drip tray is washed and sanitized, the griddle scraped and oiled while hot, the comal cleaned and the fryer oil filtered. The day's raw salsas and leftover salsa macha are tossed and logged, guisados cooled if they qualify or tossed, and corn and flour tortillas stored apart. Then the salsa bar is cleaned and sanitized (checked with a test strip), the blender and molcajete washed, rinsed and sanitized, the trash and floors done, the cash count with any over/short, tips split per your written tip pool policy, the delivery apps off, the temperature log signed and filed, and the lights, alarm and lock-up last. The \"Taco Shop Closing\" tab has those 22 tasks already written.",
    },
    {
      q: 'Does it include the food safety temperatures and logs?',
      a: 'Yes. The "Temp Logs & Receiving" checklist has you log temperatures twice per shift under the FDA Food Code: walk-in coolers at 41 °F or below, the freezer at 0 °F or below, the guisados steam table at 135 °F or above and the cold salsa bar at 41 °F or below, with the probe calibrated at the start of the shift. It also covers receiving (temperature, packaging, use-by date and invoice number for every delivery, out-of-range deliveries rejected and logged, the lot and supplier of the al pastor meat, the masa or tortillas and the dried chiles), and reheating to 165 °F for 15 seconds within 2 hours; the closing and guisados checklists cool what you keep from 135 °F to 70 °F within 2 hours and to 41 °F within 4 more, with 7-day date marking. Every reading has a blank for the °F you measured, and the shift manager signs the sheet.',
    },
    {
      q: 'What temperature does al pastor need on the trompo?',
      a: "The FDA Food Code minimum for pork like the layers on a trompo is 145 °F for 15 seconds, and that is the figure the kit uses for the outer layer you carve, or your county's if it is stricter (some ask for 155 °F). The leftover cone and the maximum time on the broiler are also set by your county or health department, so the kit leaves a blank for your local rule instead of making one up. The trompo checklists have you check the cone as received (0 °F or below frozen, 41 °F or below refrigerated), probe the outer layer before each carving batch and at the start and middle of service, carve only the cooked layer, move carved meat that isn't served right away to 135 °F or above, and log where the leftover meat goes at close.",
    },
    {
      q: 'Does it work if my taqueria has no trompo?',
      a: "Yes. The trompo sections are marked \"if applicable\": if you don't stack a cone, mark those tasks N/A. They come out of the total, so the percentage stays honest, and you use the rest of the workbook for the griddle and comal. The kit covers the tortilleria, the salsa bar and the rest of the operation just the same, and the nixtamal tasks work the same way if you buy your masa or tortillas.",
    },
    {
      q: 'How many tacos do you get from a trompo?',
      a: 'It depends on how thin you carve, your tortilla and your real waste: there is no single figure that works for every taqueria. The kit gives you the tasks to measure your own: pounds stacked and left over at close, the yield in tacos per pound, fat and trim waste, the number of cones used per shift and the day\'s yield against the week\'s average, so you decide with your own numbers instead of a generic one. If you are still planning the shop, the Taco Shop Business Plan Kit has a taco cost and trompo yield calculator.',
    },
    {
      q: 'Does it cover the salsa bar and allergens?',
      a: 'Yes, it\'s the riskiest point in a taqueria. The "Salsa Bar" checklist has you measure the pico de gallo, guacamole and raw salsas at 41 °F or below (or use time as a public health control with a written procedure and toss them at 4 hours), note when each salsa goes on the salsa bar and when it gets tossed, give every salsa its own spoon or tongs, restock in small batches in a clean container (never on top of the previous batch) and check the temperature midway through service. The "Allergens & Cross-Contact" checklist covers the 9 major allergens: the salsa macha (peanuts and/or sesame) flagged and kept apart with its own utensil, flour tortillas (wheat) kept apart from corn with a separate fryer basket and tongs, the moles and the dairy checked against the allergen sheet, the blender and molcajete washed, rinsed and sanitized, and a written allergen notice for unpackaged food.',
    },
    {
      q: 'Does it cover nixtamal, masa and tortillas?',
      a: 'Yes. If you make your own, the "Nixtamal & Masa Milling" checklist follows the corn from cooking with food-grade lime and resting to grinding, with the corn mill cleaned and sanitized before and after (sanitizer checked with a test strip), the masa held at 41 °F or below or under time as a public health control with a written procedure (masa is a TCS food), and the yield logged in pounds of corn, pounds of masa and number of tortillas. The "Tortillas & Comal" checklist calibrates the tortilla machine at startup, keeps corn and flour apart, logs production and waste and, if you buy them, checks purchased tortillas at receiving: supplier, lot, temperature and use-by date.',
    },
    {
      q: 'How do you run a taco shop with this kit?',
      a: 'With 11 workbooks that cover opening and closing, the trompo, griddle and comal, food safety with the salsa bar and allergens, nixtamal, tortillas and guisados, the manager\'s daily and weekly tasks, duties for 6 roles (taquero, tortilla maker, salsa prep cook, griddle and fryer, counter and register, delivery driver), weekly and monthly upkeep, events and seasons, and an annual calendar: the sheets that carry out, shift by shift, what an operations manual only describes.',
    },
    {
      q: 'What should a taco shop cleaning checklist include?',
      a: 'Daily cleaning goes in the closing checklist. On top of that, the kit schedules a weekly deep clean (the trompo and the hood filters degreased, the carving knives sharpened, the corn mill and tortilla machine fully taken apart, the fryer cleaned and its oil changed, the salsa bar and its utensils sanitized) and monthly upkeep: a visual gas check of the trompo, griddle and comal by your staff, with the installation inspected by a licensed professional as often as local code requires; probes calibrated at the ice point (32 °F); the hood filters cleaned by your team while a certified contractor cleans the ducts and the full hood (NFPA 96); and pest control by a licensed operator.',
    },
    {
      q: 'Is there a free taco shop checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 298 taco shop tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, and °F temperatures under the FDA Food Code. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a taco shop?',
      a: "Yes. Every checklist comes with the real tasks of a taqueria already written. You'll want to make it yours: adjust tasks to your shop, delete the ones that don't apply and add your own. The editable cells are green, and each checklist ends with 5 free green rows that the counter already includes.",
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for the area, who does it, when (a due-by time on the daily lists, a day or frequency on the weekly and monthly ones and a lead time on the event lists), ✓ Done and initials. The shift manager prints the checklist and hands it to the team, and each person checks off and initials their tasks. At the end of the shift, the shift manager checks it and signs at the bottom.',
    },
    {
      q: 'Does it include Cinco de Mayo, Day of the Dead and other busy days?',
      a: "Yes. The event calendar works by quarter: Three Kings Day, Candelaria, Lent Fridays (with the parasite-destruction record for raw fish), Holy Week and Easter, Cinco de Mayo (one of the biggest days of the year for a US taco shop), patio season and Memorial Day weekend, Mexican Independence Day, Day of the Dead, Our Lady of Guadalupe, and the posadas with the holiday parties. The bonus annual calendar adds Super Bowl Sunday, Thanksgiving and New Year's Eve, with the key tasks and the lead time for each. Margaritas, mezcal, tequila or beer only if you hold the license, 21+ with ID.",
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it for several taquerias or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for multi-unit taco shop operators. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it include a cash drawer count?',
      a: 'The cash count is part of the day: the closing checklist and the manager\'s daily list have you do the cash count and note any over/short, and split the tips per your written tip pool policy (managers and supervisors don\'t keep tips). This kit has no separate cash count sheet by bill and coin; if you want one that works out the starting bank and the over/short against your POS Z report, the Restaurant Checklists Kit Pro includes it.',
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 135 °F hot holding, in the delivery bag too) and the 9 major allergens. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, and allergen information covers 14 allergens (the kit's allergen tasks already note the UK's 14). In Canada and Australia, check your provincial or state food safety rules and allergen list and type them into the tasks. Your patio is your terrace or beer garden, and you can type in the delivery apps you use. If you serve beer, mezcal or tequila, you need the licence your area requires; the legal age is 18 in the UK and Australia, and 19 in most Canadian provinces (18 in Alberta, Manitoba and Quebec). The annual calendar has a UK note (Mothering Sunday, bank holidays and Boxing Day) and free rows for your own dates. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
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
    heading: 'Your Taqueria, Organized Shift by Shift — in 11 Checklists',
    subtitle:
      '9 templates + 3 bonuses (12 files) for the critical areas of your taqueria: trompo, nixtamal and tortillas, salsa bar, allergens and roles. For less than a taco bar for 10 people.',
    items: [
      'Opening and closing for the trompo, the salsa bar and the tortilleria',
      'Trompo for al pastor: marinade, stacking, probe and yield in tacos per pound',
      'Food safety and receiving: hot holding at 135 °F or above, reheating to 165 °F for 15 seconds within 2 hours (FDA Food Code)',
      'Self-serve salsa bar with the time each salsa goes on and gets tossed, and the 9 major allergens',
      'Tasks by role: taquero, tortilla maker, salsa prep cook, griddle and fryer, counter and register, delivery driver',
      'Annual calendar: Mexican holidays and US busy days',
      'BONUS: Taco Shop Pre-Shift Meeting Template',
      'BONUS: Taco Shop Annual Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE TACO SHOP CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Taquería Mexicana, la edición española de este kit: por eso conservan sus nombres, roles y ciudades, y el subtítulo lo
  // dice. Sin marcas. Solo se pintan: NO alimentan el JSON-LD. Una frase cambiada y avatares reasignados (ver cabecera).
  testimonials: {
    subtitle:
      'Taqueros, taqueria owners and consultants who already run their operations with Kit de Tareas Recurrentes: Taquería Mexicana, the Spanish edition of this kit',
    items: [
      {
        name: 'Roberto Salinas',
        role: 'Trompo Taquero, taqueria in Madrid',
        text: 'The trompo checklist, with the probe at the start and middle of service, finally put our al pastor in order. Every taquero used to do it their own way; now the whole team follows the same standard.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Patricia Domínguez',
        role: 'Taqueria Owner, Valencia',
        text: 'The salsa bar sheet, with the time each salsa goes on and gets tossed, saved us in two health inspections. Everything is documented by shift. A must-have.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Miguel Ángel Torres',
        role: 'Director, taqueria group (3 locations)',
        text: 'We rolled out the checklists in all 3 locations. The nixtamal, the tortilleria and the trompo stacking now follow the same standard in all three. Customers get the same quality wherever they go.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Sofía Ramírez',
        role: 'Counter Lead, taqueria in Bilbao',
        text: "The tasks by role make it clear who does what: taquero, tortilla maker, salsas, counter. The pre-shift meeting with the day's trompo, guisados and salsas and the key allergens is great for lining up the team in 5 minutes.",
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Molina',
        role: 'Hospitality Consultant specializing in Mexican food',
        text: "For taquerias it's the most complete kit out there. Trompo, nixtamal, salsa bar, allergens, roles, a holiday calendar… it covers every critical point where shops tend to slip.",
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Carmen Ibáñez',
        role: 'Taqueria Manager, Seville',
        text: 'The calendar with the Mexican holidays and the busy days lets us plan the menu ahead: chiles en nogada season, Day of the Dead, the posadas… no more improvising.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Guadalupe Reyes',
        role: 'Tortilla Maker in Training',
        text: 'The tortilleria tasks are really clear: grinding, calibrating, waste, cleaning the mill. I know exactly what to do at every moment without the manager having to direct me.',
        avatar: '/lovable-uploads/avatars-nicho/avatar-tortillera.jpg',
      },
      {
        name: 'Fernando Ochoa',
        role: 'Executive Chef, Mexican kitchen, Marbella',
        text: 'Controlling the time limit on the stacked cone and the salsa bar traceability are the details that make the professional difference. We built it into our HACCP plan and went from improvised to auditable.',
        avatar: '/avatars/avatar-8.jpg',
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
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
    { href: '/en/digital-products/ghost-kitchen-checklist-templates', label: 'Ghost Kitchen Checklists Kit Pro' },
    { href: '/en/digital-products/ice-cream-shop-checklist-templates', label: 'Ice Cream Shop Checklists Kit Pro' },
    { href: '/en/digital-products/chocolate-shop-checklist-templates', label: 'Chocolate Shop Checklists Kit Pro' },
    { href: '/en/digital-products/pastry-shop-checklist-templates', label: 'Pastry Shop Checklists Kit Pro' },
    { href: '/en/digital-products/hotel-checklist-templates', label: 'Hotel Checklists Kit Pro' },
    { href: '/en/digital-products/food-truck-checklist-templates', label: 'Food Truck Checklists Kit Pro' },
    { href: '/en/digital-products/bakery-checklist-templates', label: 'Bakery Checklists Kit Pro' },
    { href: '/en/digital-products/seafood-restaurant-checklist-templates', label: 'Seafood Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/fine-dining-checklist-templates', label: 'Fine Dining Checklists Kit Pro' },
    { href: '/en/digital-products/taco-shop-business-plan', label: 'Taco Shop Business Plan Kit' },
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
    product: 'taco-shop-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
