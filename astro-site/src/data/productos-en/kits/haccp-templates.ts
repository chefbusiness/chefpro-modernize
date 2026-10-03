// astro-site/src/data/productos-en/kits/haccp-templates.ts
// TIENDA INTERNACIONAL EN — HACCP Food Safety Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/kits/pack-appcc.ts (mismo tipo, misma plantilla KitExcelLandingPage,
// mismo orden de campos). Patrón = restaurant-inventory-templates.ts (ola 1, producto 2).
// SPEC: scripts/productos-digitales/haccp-kit/SPEC.md (§6 = esta landing).
//   · D2: nombre «HACCP Food Safety Kit Pro»; title SEO y H1 = «HACCP Food Safety Kit Pro: HACCP Plan
//     Template, Food Safety Logs & Checklists for Excel». H1 en Forma B como el ES (titlePost «: » +
//     titleSubtitle en bloque): el texto del H1 es exactamente el de D2.
//   · D5 / §6 grid: 19 tarjetas + 2 bonus con los títulos de los xlsx EN (§2.1), la 12 (plan HACCP)
//     primero por ser la intención principal; el resto en el orden de los ficheros.
//   · D3: $19, pago único. D4: priceOld 29 € → $39; bonos 9 € → $19 y 7 € → $9. Derivados: bonos
//     $28 · total $67 · ahorro $20 · descuento 1 − 19/39 = 51,3 % → «-51%».
//   · D8-D25: cifras y normativa SOLO de SPEC §3 (FDA Food Code 2022 + notas UK). Nada de
//     «aprobado por la FDA», «certificado» ni «obligatorio por ley»: el kit ayuda a llevar los
//     registros, no sustituye al health department ni a un asesor.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual
//     (nombres y negocios de origen), con el subtítulo de la edición española (TIENDA §3.5).
//   · Compatibilidad: las mismas afirmaciones que los kits EN hermanos (Excel, Google Sheets,
//     LibreOffice, Numbers); papel US Letter (D21). Sin protección de hojas (como el ES): no se dice.
//   · Imágenes: SOLO las que no llevan texto en español. De las 6 del ES se queda appcc-limpieza-cocina;
//     appcc-control-temperaturas («Restaurante El Abrazo»), appcc-recepcion-mercancias («Granja Luna»,
//     «Mercado»), appcc-alergenos-carta («Alérgenos e intolerancias»), appcc-registro-plantilla
//     («Restaurante Amura») y appcc-inspector-sanidad (carpeta «Documentos HACCP / Registros
//     sanitarios») se sustituyen por las use-case-task-appcc-* (rótulos en inglés). La OG del ES
//     (og-pack-appcc.jpg) lleva el titular en español: la EN es og-haccp-kit.jpg (Gemini, 1200×630,
//     sin texto legible, como og-food-cost-kit.jpg).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_HACCP_KIT (resuelto en el wrapper .astro).
import type { KitExcelData } from '../../productos/kits/types';

const data: KitExcelData = {
  slug: 'haccp-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_HACCP_KIT',

  seo: {
    title: 'HACCP Food Safety Kit Pro: HACCP Plan Template, Food Safety Logs & Checklists for Excel',
    description:
      '21 HACCP & food safety templates for Excel: HACCP plan, temperature and cooling logs, cleaning schedule, allergen matrix. FDA Food Code limits in °F. One-time $19.',
    keywords:
      'haccp plan template, haccp template, food safety logs, food safety templates, food temperature log template, cooling log template, cleaning schedule template, allergen matrix template, health inspection checklist, food safety checklist for restaurants, haccp excel template, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-haccp-kit.jpg',
  },

  schema: {
    productName: 'HACCP Food Safety Kit Pro',
    productDescription:
      '19 HACCP and food safety templates for Excel plus 2 bonuses: HACCP plan with hazard analysis, temperature, receiving, cooking and cooling logs, cleaning schedule, allergen matrix and a health inspection self-checklist, with FDA Food Code 2022 limits in °F.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los kits EN hermanos).
    faqs: [
      {
        q: 'Do I need technical knowledge to use the templates?',
        a: 'No. The HACCP plan, the hazard analysis and the checklists come fully built; the logs include 2-3 sample rows marked "(sample)" that show how to fill them in and that you delete before you start.',
      },
      {
        q: 'Will these templates help me pass a health inspection?',
        a: 'They give you the records a health inspector usually asks to see, with the FDA Food Code 2022 limits in °F. Your state or local health department adopts the Food Code with its own amendments, so check its version. They are not a certification.',
      },
      {
        q: 'Does it work in Google Sheets?',
        a: 'Yes. You can import the .xlsx files straight into Google Sheets and the formulas carry over. They also work with LibreOffice Calc and Apple Numbers.',
      },
      {
        q: 'Can I customize the templates for my restaurant?',
        a: 'Completely. Add cleaning areas, coolers and freezers, menu items to the allergen matrix or hazards to the HACCP plan. Editable cells are marked in green.',
      },
      {
        q: 'Are updates included if the rules change?',
        a: 'Yes. You get lifetime access to the online dashboard, and when we update the templates you download the new version at no extra cost.',
      },
      {
        q: 'What kind of business is it for?',
        a: 'Any foodservice business: restaurants, bars, cafés, hotels, caterers, bakeries, food trucks and institutional kitchens.',
      },
      {
        q: 'Can I write my own HACCP plan?',
        a: 'Yes. The FDA Food Code asks for a written HACCP plan only in specific cases (§8-201.13), such as processes that need a variance or reduced-oxygen packaging. The HACCP Plan Template comes pre-filled with 21 typical hazards for you to adapt.',
      },
      {
        q: 'What is the format for a HACCP plan?',
        a: 'A table by process step: hazard, risk level, whether it is a critical control point, critical limit, where it is recorded, monitoring, corrective action and verification. That is the layout of the Hazard Analysis tab.',
      },
      {
        q: 'What are the 7 steps of a HACCP plan?',
        a: 'The 7 HACCP principles: hazard analysis, critical control points, critical limits, monitoring, corrective actions, verification, and record-keeping. The HACCP Plan Template shows where each one lives in the kit.',
      },
      {
        q: 'What are the 5 documents that go in the HACCP manual?',
        a: 'Usually the HACCP plan, the hazard analysis, the prerequisite programs, the monitoring and corrective action records, and the verification records. The kit has a template for each.',
      },
      {
        q: 'Does it work in the UK?',
        a: 'Yes. The instructions add UK notes where the rules differ (hot holding at 63 °C, cooling below 8 °C within 90 minutes, 48 hours off work after symptoms stop), and the allergen matrix keeps all 14 UK allergens.',
      },
      {
        q: 'What currency will I pay in?',
        a: 'The price is $19 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency and converts it for you.',
      },
    ],
    breadcrumbName: 'HACCP Food Safety Kit Pro',
  },

  images: {
    // hero bg (6) — sin texto en español (ver cabecera); gridGallery omitido: cae en `gallery`, como en el ES
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-task-appcc-fridge.jpg',
      '/lovable-uploads/ai-gallery/appcc-limpieza-cocina.jpeg',
      '/lovable-uploads/ai-gallery/use-case-task-appcc-thermometer.jpg',
      '/lovable-uploads/ai-gallery/use-case-task-appcc-cleaning.jpg',
      '/lovable-uploads/ai-gallery/use-case-task-appcc-team.jpg',
      '/lovable-uploads/ai-gallery/use-case-task-appcc-hero.jpg',
    ],
    // Fondos de platos sin texto: los MISMOS del ES.
    whyBg: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg',
  },

  hero: {
    badgeTone: 'gold',
    // SPEC §6: sin las multas españolas del ES.
    badge: 'FDA Food Code 2022 limits in °F, ready for your next health inspection',
    // D2: titlePre + titleGold = «HACCP Food Safety Kit Pro»; Forma B como el ES.
    titlePre: 'HACCP Food Safety ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    titleSubtitle: 'HACCP Plan Template, Food Safety Logs & Checklists for Excel',
    description:
      '19 professional food safety templates + 2 bonuses: temperatures, cooking, cooling, parasite destruction, cleaning, traceability, allergens, a HACCP plan and more. The records a health inspector expects to see, ready to use in your restaurant.',
    checkItems: [
      '19 templates with an automatic color traffic light on the measurement logs; plans, checklists and posters ready to print',
      'Allergen matrix with the US Big 9 and all 14 UK allergens',
      'Pre-filled HACCP plan: 21 hazards across 7 process steps',
      '25-point health inspection self-checklist',
      'Temperature logs in °F with automatic OK/ALERT',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  compatApps: {
    titleHtml: 'Works with <span class="text-[#FFD700]">Excel</span>, Google Sheets and LibreOffice',
    subtitleHtml:
      'Download, customize and print. Works with Excel, Google Sheets, LibreOffice and Apple Numbers: all 21 files are .xlsx and print on US Letter straight from the sheet',
  },

  grid: {
    countGold: '19',
    headingRest: ' HACCP & Food Safety Templates',
    subtitle:
      'The 12 measurement logs calculate their own status with an automatic color traffic light; the plans, checklists and posters come fully built and ready to print on US Letter.',
    // fourCols omitido → grid-cols-2 md:grid-cols-3, como el ES. SPEC §6: 19 tarjetas + 2 bonus con
    // los títulos de §2.1, la 12 primero (intención principal: «haccp plan template»).
    templates: [
      { icon: 'ShieldCheck', title: 'HACCP Plan Template: Hazard Analysis & CCPs', desc: 'The core of the system, pre-filled with 21 typical hazards across 7 process steps, from receiving to service. Probability × severity gives the risk level on its own, and each hazard is classified as CCP, OPRP or not significant following a written rule, with its critical limit, monitoring, corrective action, verification and the log that records it.' },
      { icon: 'Thermometer', title: 'Food Temperature Log: Coolers, Freezers & Hot Holding', desc: 'A weekly log, twice a day, for walk-in coolers, freezers, display cases and hot holding. Status switches between OK and ALERT on its own against the FDA Food Code limits: 41 °F or below cold, 0 °F or below frozen, 135 °F or above hot.' },
      { icon: 'Thermometer', title: 'Receiving Temperature Log', desc: 'The temperature of every delivery against the receiving limit of its product family: 41 °F, 45 °F for shell eggs, milk and live shellfish, and frozen food received frozen. Status says OK or REJECT, and it never defaults to OK when a reading is missing.' },
      { icon: 'SprayCan', title: 'Master Cleaning & Sanitizing Schedule', desc: 'A master plan with 32 pre-filled areas (kitchen, dining room, restrooms, storeroom, locker room and outdoors: patio, dumpsters and trash room) plus a chemicals tab with EPA Reg. No. and SDS. It sets what gets cleaned, when, how, with what and by whom.' },
      { icon: 'SprayCan', title: 'Daily Cleaning Checklist (AM/PM)', desc: 'A daily checklist by shift, AM and PM, with sign-off and initials, ready to print and post in the kitchen.' },
      { icon: 'ClipboardCheck', title: 'Receiving Checklist for Deliveries', desc: 'Checks temperature, dates (at least 2/3 of the shelf life left), labeling, packaging and appearance on every delivery, with a color traffic light.' },
      { icon: 'Truck', title: 'Food Traceability Log (Lots In & Out)', desc: 'Lot, vendor and dates for everything that comes in, plus a Traceability Out tab that follows each lot to the dish and service where it ended up: one step back, one step forward, in minutes.' },
      { icon: 'Bug', title: 'Pest Control Log & Bait Station Map', desc: 'Every visit from your licensed pest control operator: treatment, products with their EPA Reg. No., areas, re-entry interval and reports, plus a bait station map tab.' },
      { icon: 'AlertTriangle', title: 'Menu Allergen Matrix (US Big 9 & UK 14)', desc: 'Every dish on your menu × 14 allergen columns with Y/T/N drop-downs (contains, traces, does not contain). The US Big 9 are marked in the header, and each row checks that the specific tree nut, fish and crustacean shellfish are named, as FALCPA requires.' },
      { icon: 'Droplets', title: 'Fryer Oil Log (TPM Tests & Disposal)', desc: 'Total polar materials tests with WATCH from 20% and CHANGE at 25%, the kit\'s change point (there is no federal limit in the US), or when the fryer went above 375 °F. Plus a used oil pickup log for your recycler\'s receipts.' },
      { icon: 'Droplets', title: 'Water Quality Log (Chlorine & Private Supply)', desc: 'Free chlorine readings against the 0.2-4.0 mg/L range, water appearance and lab results, with notes for private wells and the ice machine as a sample point.' },
      { icon: 'ClipboardCheck', title: 'Corrective Action Log', desc: 'Every incident with its cause, the action taken, what happened to the product (discarded, returned, reworked or released) and verification. That is HACCP principle 5, and the first thing an inspector asks about.' },
      { icon: 'UserCheck', title: 'Employee Hygiene & Health Checklist', desc: 'Printable rules for the locker room: clothing, 20-second handwashing, no bare-hand contact with ready-to-eat food, jewelry, the Big 6 reportable illnesses and when a sick employee stays home (24 hours after symptoms end; 48 hours in the UK).' },
      { icon: 'AlertTriangle', title: 'Allergen Chart & Allergic Reaction Protocol', desc: 'A printable chart of the allergens for the kitchen and the dining room, and a reaction protocol in order of urgency: call 911 (999 in the UK) and use the epinephrine auto-injector first; keep the dish and the label after.' },
      { icon: 'ShieldCheck', title: 'Health Inspection Self-Checklist', desc: '25 points a health inspector looks at, each with its FDA Food Code category (Priority, Priority foundation or Core). Score yourself before the inspection: an automatic summary counts Priority violations, unanswered points and your compliance rate.' },
      { icon: 'Flame', title: 'Cooking & Reheating Temperature Log', desc: 'Final internal temperature for 5 processes with their Food Code limit (165, 155, 145 and 135 °F, and reheating to 165 °F within 2 hours), with OK or REPEAT on its own.' },
      { icon: 'Snowflake', title: 'Cooling & Thawing Log (2-Stage Cooling)', desc: 'Two-stage cooling, from 135 to 70 °F within 2 hours and to 41 °F within 6 hours in total, plus thawing in the walk-in at 41 °F or below with a time limit you set (24 hours by default).' },
      { icon: 'Fish', title: 'Parasite Destruction Log (Fish Served Raw)', desc: 'For fish served raw or undercooked: −4 °F or below for 168 hours (7 days) or −31 °F for 15 hours, with the hours editable (24 in the UK).' },
      { icon: 'Thermometer', title: 'Thermometer Calibration Log', desc: 'A monthly ice-point (32 °F) or boiling-point check of every probe, with the boiling point corrected for your altitude in feet and a ±2 °F tolerance.' },
      { icon: 'GraduationCap', title: 'BONUS: Food Safety Training Log', desc: 'Your team\'s food safety training on record: Certified Food Protection Manager, food handler training, HACCP and allergen awareness, with renewal dates that flag themselves.' },
      { icon: 'AlertTriangle', title: 'BONUS: Food Recall & Foodborne Illness Response Plan', desc: 'A printable 7-step poster for a recall or a suspected foodborne illness, with emergency contacts for the US and the UK.' },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're records designed by a chef who has worked in kitchens since the age of 17 and has been a restaurant consultant since 2010.",
    reasons: [
      // SPEC §6: «Not a free template, a system» en lugar del «Obligatorio por ley» español.
      { icon: 'ShieldAlert', title: 'Not a Free Template: a System', desc: 'Free templates give you one sheet. This kit gives you 21 that work together: every alert in a log points you to the Corrective Action Log, every critical limit traces back to the HACCP plan, and every hazard in the plan names the log that monitors it.' },
      { icon: 'ClipboardCheck', title: 'Ready to Use', desc: "Don't start from scratch. The HACCP plan, the hazard analysis, the allergen chart and the inspection checklist come fully built and ready to adapt (32 cleaning areas, 21 HACCP hazards, receiving limits by product family, 14 allergens); the logs include 2-3 sample rows marked \"(sample)\" that show how to fill them in and delete in a second." },
      { icon: 'Calculator', title: 'Automatic Formulas and Alerts', desc: 'The temperature logs switch between OK and ALERT on their own, in °F, against the FDA Food Code 2022 limits. The fryer oil log says WATCH from 20% total polar materials and CHANGE at 25%, the kit\'s change point, or when the fryer went above 375 °F.' },
      { icon: 'RefreshCw', title: 'Pay Once, Yours Forever', desc: 'No subscription. Lifetime access to the dashboard with every template, and updates included when the rules change.' },
    ],
    compatLabel: 'Compatible with any spreadsheet software:',
    // Mismas pastillas y orden que el ES; «A4» → US Letter (D21).
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010. He has designed food safety and cost-control systems for hundreds of restaurants.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle:
      'Besides the 19 templates, you get these extra resources — worth $28',
    items: [
      {
        icon: 'GraduationCap',
        label: 'BONUS 1',
        title: 'Food Safety Training Log',
        value: '$19',
        desc: "A template to record all of your team's food safety training: Certified Food Protection Manager, food handler training, HACCP, allergen awareness and first aid, with renewal dates that flag themselves. A health inspector can ask for it at any time.",
        image: '/lovable-uploads/ai-gallery/use-case-task-appcc-team.jpg',
      },
      {
        icon: 'AlertTriangle',
        label: 'BONUS 2',
        title: 'Food Recall & Foodborne Illness Response Plan',
        value: '$9',
        desc: 'A printable poster with the 7 steps to follow in a recall or a suspected foodborne illness, plus emergency contacts for the US and the UK. Identify → Isolate → Notify → Document → Communicate → Verify → Record.',
        image: '/lovable-uploads/ai-gallery/use-case-task-appcc-fridge.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE HACCP KIT — $19',
  },

  guarantee: {
    // headingPre por defecto = ui.guaranteeHeadingPreDefault («Satisfaction Guarantee »).
    text:
      "If the templates don't help you face your next health inspection with more peace of mind, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): las 6 del ES adaptadas (sin «obligatorio por ley» ni normativa española) +
  // People Also Ask de la SPEC §6 + moneda (patrón de los kits EN hermanos).
  faqs: [
    {
      q: 'Do I need technical knowledge to use the templates?',
      a: 'No. The HACCP plan, the hazard analysis, the allergen chart and the inspection checklist come fully built; the logs include 2-3 sample rows marked "(sample)" so you can see how they are filled in, and you delete them before you start. You only add the details of your business: the dishes on your menu for the allergen matrix, your coolers and freezers, your cleaning areas. The status and the color traffic light of the measurement logs are calculated automatically.',
    },
    {
      q: 'Will these templates help me pass a health inspection?',
      a: 'They give you the records a health inspector usually asks to see — temperatures, cooking, cooling, cleaning, receiving, traceability, allergens, pest control, fryer oil, water and a written HACCP plan — with the FDA Food Code 2022 limits in °F. Your state or local health department adopts the Food Code with its own amendments, so check its version and adjust the templates where it differs. They are not a certification, and they do not replace your health department or a food safety consultant.',
    },
    {
      q: 'Does it work in Google Sheets?',
      a: 'Yes. You can import the .xlsx files straight into Google Sheets and the formulas carry over. They also work with LibreOffice Calc and Apple Numbers. Every printable sheet is set up for US Letter paper.',
    },
    {
      q: 'Can I customize the templates for my restaurant?',
      a: 'Completely. Add cleaning areas, coolers and freezers, dishes to the allergen matrix or hazards to the HACCP plan. Editable cells are marked in green, and the formulas and alerts adjust on their own.',
    },
    {
      q: 'Are updates included if the rules change?',
      a: 'Yes. You get lifetime access to the online dashboard. When we update the templates — for example, after a new edition of the FDA Food Code — you download the new version at no extra cost.',
    },
    {
      q: 'What kind of business is it for?',
      a: 'Any foodservice business: restaurants, bars, cafés, hotels, caterers, bakeries, food trucks and institutional kitchens. Every food business has to control temperatures, cleaning and allergens, and this kit keeps all of those records in one place.',
    },
    {
      q: 'Can I write my own HACCP plan?',
      a: 'Yes. The FDA Food Code asks a retail food establishment for a written HACCP plan only in specific cases (§8-201.13), such as processes that need a variance or reduced-oxygen packaging, or when your health department requires one; for everything else, the FDA recommends a voluntary HACCP-based approach in its "Managing Food Safety" guide. The HACCP Plan Template comes pre-filled with 21 typical hazards across 7 process steps, from receiving to service, each with the log of the kit that monitors it: adapt it to your menu and your processes.',
    },
    {
      q: 'What is the format for a HACCP plan?',
      a: 'Usually a table by process step: the hazard (biological, chemical or physical), its risk level, whether it is a critical control point, the critical limit, where it is recorded, how it is monitored and by whom, the corrective action and the verification. That is exactly the layout of the Hazard Analysis tab, where each hazard is classified as CCP, OPRP or not significant.',
    },
    {
      q: 'What are the 7 steps of a HACCP plan?',
      a: 'They are the 7 HACCP principles: 1) conduct a hazard analysis, 2) determine the critical control points, 3) set critical limits, 4) set up monitoring, 5) set corrective actions, 6) set up verification and 7) keep records and documentation. The HACCP Plan Template shows where each one lives: the columns of the hazard analysis, the logs of the kit and the Corrective Action Log.',
    },
    {
      q: 'What are the 5 documents that go in the HACCP manual?',
      a: 'There is no single official list, but a HACCP manual usually holds five kinds of documents: the HACCP plan, the hazard analysis, the prerequisite programs (cleaning, pest control, receiving, training, allergens), the monitoring and corrective action records, and the verification records (thermometer calibration, self-inspections). This kit gives you a template for each of them.',
    },
    {
      q: 'Does it work in the UK?',
      a: 'Yes. The limits follow the FDA Food Code in °F, and the instructions add a UK note where the rules differ: hot holding at 63 °C or above, cooling below 8 °C within 90 minutes (FSA Safer Food Better Business), 48 hours off work after symptoms stop, and the Food Hygiene Rating Scheme in the inspection checklist. The allergen matrix and the allergen chart keep all 14 UK allergens. In the UK, every food business needs procedures based on HACCP principles, and you can use this kit alongside Safer Food Better Business.',
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $19 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you.',
    },
  ],

  cta: {
    heading: "Don't Wait for the Health Inspector",
    subtitle:
      '19 professional templates for less than a single visit from a food safety consultant.',
    // D4: los valores de los bonos repiten los de bonus.items.
    items: [
      '12 Excel logs with calculated status and an automatic traffic light + 9 plans, checklists and posters ready to print',
      'Allergen matrix with the US Big 9 and all 14 UK allergens',
      'HACCP plan pre-filled with 21 hazards',
      'Master cleaning schedule with 32 areas, inside and out',
      '25-point health inspection self-checklist',
      'BONUS: Food Safety Training Log ($19)',
      'BONUS: Food Recall & Foodborne Illness Response Plan ($9)',
      '30-day money-back guarantee',
    ],
    ctaLabel: 'YES, I WANT THE HACCP KIT — $19',
  },

  // Testimonios: traducción fiel de los 10 del ES (decisión de John, 25-sep-2026). Son del Pack
  // Plantillas APPCC, la edición española de este kit: por eso conservan sus nombres y negocios, y el
  // subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD. Los nombres propios con tilde, eñe o
  // « del » están exentos en tienda-gate.py (EXENTOS), como los del piloto.
  testimonials: {
    subtitle:
      'Restaurant and hotel operators who already keep their food safety records up to date with Pack Plantillas APPCC, the Spanish edition of this kit',
    items: [
      { name: 'Carlos Mendoza', role: 'Executive Chef, Restaurante Brasa Viva', text: 'We passed a health inspection with flying colors thanks to these templates. The inspector said it was one of the most complete sets of records he had ever seen. Before, I made do with loose sheets of paper.', avatar: '/avatars/chef-avatar-1.jpg' },
      { name: 'Laura Castillo', role: 'Director of Operations, Grupo Hotelero Azul', text: 'We have 6 hotels and needed to standardize HACCP across all of them. With this pack, every kitchen follows the same system. The internal audit went from 3 days to half a day per property.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Marcos Ibáñez', role: 'Owner, Bar Txoko', text: 'The health inspection used to keep me up at night. Since I started using the templates, everything is up to date: temperatures, cleaning, traceability. Now when the inspector comes, I open the binder without a worry.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Patricia Roldán', role: 'Food Safety Consultant', text: "I use this pack with all my consulting clients. It saves me hours of work because the templates already have the right fields. I just add the name of the business and that's it.", avatar: '/avatars/avatar-4.jpg' },
      { name: 'Javier Esteban', role: 'Director, Catering Eventos del Sur', text: 'In catering, HACCP paperwork is required for every event. With the traceability log and the allergen sheets, I put together all the documentation in 15 minutes per event.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana Belén Torres', role: 'Owner, Cafetería El Trigal', text: "The allergen matrix saved me. I had a customer with celiac disease and my allergens weren't properly documented. Now every dish on the menu has its sheet with the 14 allergens marked.", avatar: '/avatars/avatar-6.jpg' },
      { name: 'Roberto Salazar', role: 'Owner, Trattoria Don Roberto', text: 'I got a surprise inspection and, thanks to the pack, I had six months of spotless records. The inspector told me I had saved myself a real scare.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Miguel Ángel Prieto', role: 'Head Chef, Hotel Montaña', text: "I've been in kitchens for 20 years and always used notebooks to write down temperatures. Moving to Excel with automatic alerts changed everything. If a temperature goes up, I see it in red right away.", avatar: '/avatars/avatar-8.jpg' },
      { name: 'Daniel Ortega', role: 'Restaurant Consultant', text: 'I recommend this pack to all my clients, no exceptions. It is the fastest way to get food safety in order at any business. I have recommended it to more than 40 of them.', avatar: '/avatars/chef-avatar-5.jpg' },
      { name: 'Ignacio Vargas', role: 'Purchasing Director, Hotel Costa Sereno', text: 'The receiving temperature logs let us reject out-of-range product with real data. Since we started using them, incidents with suppliers have dropped a lot.', avatar: '/avatars/avatar-1.jpg' },
    ],
  },

  pricing: {
    priceOld: '$39',
    price: '$19',
    discountBadge: '-51%',
    heroNote: 'Special launch price. Going up soon',
    buyBoxNote: 'Special launch price — 51% off',
    bonusTotalLabel: 'Total value of the complete kit: $67 — 19 templates ($39) + 2 bonuses ($28)',
    bonusSaveLine: 'Save $20 TODAY!',
  },

  stickyLabel: 'HACCP FOOD SAFETY KIT PRO — $19',
  // stickyVariant omitido → default 'v2', como el ES.

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'haccp-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
