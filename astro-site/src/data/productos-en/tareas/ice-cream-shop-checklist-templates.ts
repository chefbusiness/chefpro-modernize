// astro-site/src/data/productos-en/tareas/ice-cream-shop-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Ice Cream Shop Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-heladeria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-, bar-, coffee-shop-, catering-, pizza-shop-, burger-joint- y ghost-kitchen-checklist-templates.ts. SPEC:
// scripts/productos-digitales/checklists-kit/icecream/SPEC.md (delta) + la base.
//   · D2: nombre «Ice Cream Shop Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Ice Cream Shop Checklists Kit Pro: Opening, Closing & Production Templates». Demanda US (SPEC §R): ice cream shop
//     246.000/mes, ice cream parlor y gelato shop 27.100, scoop shop 4.400: las cuatro van en keywords y FAQ.
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (icecream/SPEC §2,
//     dl/ice-cream-shop-checklist-templates/).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos (el ES los «valora en €33»). Fórmula de la tienda EN.
//   · Cifras SOLO de icecream/SPEC (D6, D9-D14, D-ICE, D-UK, §3), de mapas_icecream.py (POR_CELDA, CALENDARIO, ADAPTAR)
//     y del censo del ES (icecream/censo_es.json; la EN tiene paridad estructural): 298 tareas (26 + 17 = 43 en el 01;
//     13 + 14 = 27 en el 02; 38 en el 03; 14 + 14 + 13 = 41 en el 04; 44 en el 05; 36 en el 06; 33 en el 08 con
//     responsable y hora; 23 en el 09; 13 en el briefing), 3 plantillas en blanco de 25 filas, 12 meses con 4 sabores
//     cada uno; 0 °F conservación, 6–10 °F vitrina [fabricante], 36–39 °F maduración y nunca > 41 °F (3-501.16),
//     extracción 16–19 / 10–14 °F [fabricante], cubetas a −4 °F, 10 °F a la llegada del catering, pasteurización
//     185 °F 15 s [criterio del kit] con el programa validado y la licencia estatal por delante, 104–122 °F para grasas,
//     enfriado 135 → 70 °F en 2 h y → 41 °F en 4 h (3-501.14), maduración 4 h mínimo / 8–12 h, vida útil 2–3 meses a
//     0 °F y 3–5 días a 36–39 °F; horas del 08 desde las 10:00 AM (D9: +3 h). Las que salen del ES traducido tal cual
//     (18–24 y 10–14 sabores, 2–3 tandas al día, 2 scoopers, 24–48 h, 4 h / 8–12 h) quedan A CONFIRMAR contra los
//     xlsx EN de la F2 (F3-NOTAS §3). Food cost sin cifra (el ES dice < 28-32 %).
//   · Lo que el ES afirma y el kit no trae, fuera: «software de gestión €40/mes» y «sin internet» (→ la fórmula de los
//     hermanos), el «inventario semanal por categoría (bases, frutas, toppings, envases)» (el kit trae comprobaciones de
//     stock en el 03 y el 05, sin hoja de inventario: «sin inventario con mínimos», SPEC D-ICE), el «foco por día» del
//     semanal del manager, las «fechas clave (Día del Helado, ferias)» en el 06 (están en el calendario, BONUS-02),
//     «mermas de producción» en el checklist del manager (las mermas se anotan al cierre del 01 y se revisan en el
//     mensual del 05), «DDD», «gases fluorados», «legionela», «BIE» y «registro sanitario» (→ servicios contratados
//     US, D11), «Imprimible A4» (→ US Letter) y, en el dashboard ES, «15 fechas clave» (son 12 meses).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 8 del ES traducidos tal cual (nombres, negocios y
//     cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan. Ninguno cita una marca
//     o persona real (SPEC §R). Una frase que el kit contradice, cambiada (regla de John, 11-oct): Ana Belén Ruiz (ver
//     el comentario en la lista).
//   · Imágenes: las 6 del ES llevan texto en español o la marca «Madrid» a la vista (hero: «HELADOS ARTESANALES MADRID
//     2026», «PRECIOS»; vitrina: etiquetas de sabores en español; obrador y equipo: pizarras «SABORES DEL DÍA»; equipo:
//     «TAREAS DIARIAS»; producción: «LA CREMÉ MADRID» y la marca Carpigiani), salvo «tareas-heladeria-servicio»
//     (etiquetas en inglés; solo un «GELATO MADRE · MADRID» pequeño en el delantal), que se queda. El resto, fotos YA
//     publicadas en las páginas de casos de uso EN de heladería y de gelato, sin texto en español: cucurucho
//     («GELATERIA»), vitrina cenital (etiquetas en italiano), mantecadora, mezcla y la reunión de equipo («ARTISANAL
//     GELATO»). OG ES fuera (og-kit-tareas-heladeria lleva texto español y «€12») → OG = el hero EN.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'ice-cream-shop-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT',

  seo: {
    title: 'Ice Cream Shop Checklists Kit Pro: Opening, Closing & Production Templates',
    description:
      '11 Excel ice cream shop checklists with 298 tasks already written: opening & closing, production, roles, cleaning, seasons, catering, cash count. One-time $19.',
    keywords:
      'ice cream shop checklist, ice cream shop opening checklist, ice cream shop closing checklist, ice cream shop cleaning checklist, gelato shop checklist, ice cream parlor checklist, scoop shop checklist, ice cream production checklist, batch freezer, dipping cabinet, dipper well, ice cream catering checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/use-case-heladeria-conos.jpg',
  },

  schema: {
    productName: 'Ice Cream Shop Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for ice cream and gelato shops with 298 tasks already written: opening and closing, production (pasteurizing, aging and batch freezing), manager, duties by role, cleaning and maintenance schedule, peak season, off-season and ice cream catering, whole-shop opening and closing, and a cash drawer count.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on an ice cream shop opening checklist?',
        a: "One list in order: personal hygiene, the hood on before the pasteurizer and the batch freezer, the dipping cabinets switched from overnight storage (0 °F) to service (6–10 °F) with the reading logged, the freezers at 0 °F or below and the aging cooler at 36–39 °F, toppings, sauces and cones stocked, the scoops in a dipper well or one per flavor, the allergen chart checked against today's flavors, then the register and the door. Every task has columns for the area, who does it, a check mark and the time.",
      },
      {
        q: 'What goes on an ice cream shop closing checklist?',
        a: "Pans covered, the dipping cabinets switched back to storage mode (never off with product inside), the day's waste logged by flavor, pans labeled with their use-by date, the scoops, the dipper well and the sauce dispensers cleaned and sanitized, the counter, scale and register area cleaned, the cash counted and sales logged by flavor. The whole-shop checklist then puts the night covers on the cabinets and logs the closing temperatures before the alarm and the lock-up.",
      },
      {
        q: 'Does it cover pasteurizing, aging and batch freezing?',
        a: "Yes. The production workbook covers the mix weighed by recipe card, pasteurizing at 185 °F for 15 seconds (your pasteurizer's validated program and your state license come first), cooling the mix to 41 °F or below and aging it at 36–39 °F, then batch freezing at the draw temperature your batch freezer maker gives, hardening at 0 °F or below, labeling, yield and overrun, with a shelf-life table in °F.",
      },
      {
        q: 'Is there a free ice cream shop checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 298 ice cream shop tasks already written, a counter that skips N/A tasks, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, frozen storage at −18 °C, cold holding at 8 °C and information on the 14 allergens; in Canada and Australia, your local temperatures and allergen list; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Ice Cream Shop Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid: fotos sin texto en español (ver cabecera). El ES repite el hero y la
    // vitrina en el bonus; la EN, el cucurucho y la vitrina cenital.
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-heladeria-conos.jpg',
      '/lovable-uploads/ai-gallery/use-case-heladeria-flavors.jpg',
      '/lovable-uploads/ai-gallery/use-case-heladeria-team.jpg',
      '/lovable-uploads/ai-gallery/use-case-maestro-heladero-mantecadora.jpg',
      '/lovable-uploads/ai-gallery/tareas-heladeria-servicio.jpg',
      '/lovable-uploads/ai-gallery/consultor-heladero-equipo.jpg',
    ],
    // Mismo reparto que el ES (why = obrador, buyBox = producción, cta = hero).
    whyBg: '/lovable-uploads/ai-gallery/use-case-heladeria-team.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-maestro-heladero-mantecadora.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/use-case-heladeria-conos.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Ice Cream Shop Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Ice Cream Shop Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Opening, Closing & Production Templates',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 298 ice cream shop tasks already written: opening and closing, production, manager, roles, cleaning, peak season, ice cream catering and a cash drawer count. Print it, delegate it to your team, check it off and file it.',
    checkItems: [
      'Production: pasteurizing, aging the mix and batch freezing, with temperatures in °F',
      'Counter: dipping cabinets, toppings, sauces, cones, the dipper well and the allergen chart',
      'Roles: ice cream maker, scooper and shift lead',
      'Manager: daily, weekly and monthly checklists, food cost included',
      'Seasons: peak season, off-season, ice cream catering and a seasonal calendar',
      'Whole-shop opening and closing, and a cash drawer count by bill and coin',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS HELADERÍA — €12»).
  stickyLabel: 'ICE CREAM SHOP CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Ice Cream Shop Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '298 ice cream shop tasks already written and sorted by shift, area and role. Adjust them to your shop, print and delegate.',
    templates: [
      {
        icon: 'IceCream',
        title: 'Ice Cream Shop Opening & Closing Checklists: Dipping Cabinets, Toppings & Counter',
        desc: "2 checklists. Opening: personal hygiene and a safe start-up, the dipping cabinets switched from overnight storage to service mode and the freezers and aging cooler checked, with each reading logged, then toppings, sauces, cones, the dipper well and the allergen chart by flavor, the register and the door. Closing: pans covered, the dipping cabinets back to storage mode (never off with product inside), the day's waste logged by flavor, the scoops, dipper well and sauce dispensers cleaned and sanitized, and the cash count. 43 tasks already written in this file alone.",
      },
      {
        icon: 'Beaker',
        title: 'Ice Cream & Gelato Production Checklists: Pasteurizing, Aging & Batch Freezing',
        desc: "Pasteurizing: the mix weighed by recipe card, pasteurized at 185 °F for 15 seconds (or as your pasteurizer's validated program and your state license say), cooled to 41 °F or below and aged at 36–39 °F, with a batch record. Batch freezing: the draw temperature from your batch freezer maker (around 16–19 °F for ice cream, 10–14 °F for sorbet), mix-ins and swirls, each pan labeled with flavor, dates and batch, yield and overrun, hardening at 0 °F or below and the batch freezer taken apart and cleaned. Plus a shelf-life table in °F and a note on state frozen dessert licenses.",
      },
      {
        icon: 'ClipboardList',
        title: 'Ice Cream Shop Manager Checklist: Daily, Weekly & Monthly',
        desc: "Daily (the production plan, key ingredients, yesterday's temperature logs, mixes ready to freeze, sales by flavor, team positions, the team's time records, the dipping cabinet's look and rotation, online reviews), weekly (sales by flavor, food cost against your target, checklist compliance, a team huddle, the weekly order, next week's flavors, packaging and equipment) and monthly (P&L, a full inventory, food cost by flavor family, profit per flavor, schedules, training, preventive maintenance, the seasonal menu and your suppliers).",
      },
      {
        icon: 'Users',
        title: 'Ice Cream Shop Duties by Role: Ice Cream Maker, Scooper & Shift Lead',
        desc: 'Checklists for the ice cream maker (mixes, pasteurizing, batch freezing, mix-ins, filling the dipping cabinet and the batch log), the scooper at the counter (setup, flavors and allergens, samples on single-use tasting spoons, the line at peak times, the register) and the shift lead (team and positions, temperature logs, complaints, breaks, discounts and the cash count sign-off): what each role does at the start of the shift, during service and at closing.',
      },
      {
        icon: 'CalendarDays',
        title: 'Ice Cream Shop Cleaning Checklist & Maintenance Schedule',
        desc: "Weekly deep clean (the dipping cabinets' grates and interiors, sauce and topping dispensers, the batch freezer's parts, condenser filters, aging containers, the ice machine, freezer interiors and FIFO dates), weekly upkeep and stock (a batch freezer test run, a refrigeration check that leaves the refrigerant to the technician, the scales checked with test weights, a quick stock check of key ingredients and packaging, slow sellers pulled from the cabinet) and monthly tasks (thermometers checked, pasteurizer maintenance, freezer door gaskets, a full inventory, food cost against target, waste by flavor, allergen labels). + a Quarterly & Annual sheet for contracted services and paperwork: pest control, hood and duct cleaning (NFPA 96, only if you cook with grease), refrigeration by an EPA 608-certified tech, thermometer calibration, fire extinguishers, gas, backflow testing, your health permit and state frozen dessert license, food handler cards, insurance with food spoilage coverage, and the POS and sales tax, with the service report number in the notes.",
      },
      {
        icon: 'Sun',
        title: 'Ice Cream Shop Seasonal Checklists: Peak Season, Off-Season & Ice Cream Catering',
        desc: 'Peak season (from Memorial Day to Labor Day: a menu of 18–24 flavors with seasonal fruit, summer hires two weeks ahead with the federal hour limits for 14- and 15-year-olds, two or three batch freezer runs a day, the patio, at least 2 scoopers at peak times, pints and quarts to go), the off-season (10–14 flavors, hot chocolate, waffles, crepes and ice cream cakes, deep maintenance and new recipes) and ice cream catering (allergens, headcount, deposit and cancellation terms in writing before you produce, freezer space at 0 °F, insulated carriers and dry ice, product at 10 °F or below on arrival).',
      },
      {
        icon: 'FileEdit',
        title: 'Blank Ice Cream Shop Checklist Template (Editable)',
        desc: '3 blank templates (by area, by shift and by role) with 25 rows each, the columns for area, person in charge, ✓, time and notes, and the counter already set up: you just type your tasks.',
      },
      {
        icon: 'Building2',
        title: 'Ice Cream Parlor Opening & Closing Checklist (Whole Shop)',
        desc: 'The checklist for the whole shop, not just the counter: alarm, lights, HVAC, the POS, special orders, restrooms, the patio, menu boards and flavor signs, and the dipping cabinets at serving temperature, with due-by times for a shop that opens mid-morning. At close, in a safe order: the cabinets get their night covers (they stay on) and the closing temperatures are logged before the register, the safety check and the lock-up. Who does it and the due-by time are filled in for all 33 tasks.',
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. Plus a monthly cash log with the over/short by formula for every day of the month.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Ice Cream Shop Pre-Shift Meeting Template (Huddle Notes)',
        desc: "Pre-shift huddle template: the flavors to make today, mixes ready to freeze, flavors running low in the dipping cabinet, deliveries, the team and positions, special orders and catering, today's promo or new flavor, a sales goal, the flavor to recommend and a reminder on allergens. Print it and post it in production and at the counter.",
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Ice Cream Shop Seasonal Calendar & Flavor Planner (US)',
        desc: "12 months, each with its key US dates and actions, four featured flavors and the season (peak in June, July and August): Valentine's Day, St. Patrick's Day and Opening Day for seasonal shops, Easter, Mother's Day, graduations and Memorial Day, Father's Day, July 4, National Ice Cream Month and National Ice Cream Day (the third Sunday of July), county fairs, Labor Day, Halloween, Thanksgiving pie à la mode and holiday flavors, with a UK note.",
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
        title: 'Pre-Filled for Ice Cream Shops',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a shop that makes its own ice cream and gelato. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'IceCream',
        title: 'Production and Counter Covered',
        desc: "Pasteurizing, aging, batch freezing, the dipping cabinets, the counter and the manager's numbers: the tasks generic checklist apps don't cover for an ice cream shop.",
      },
      {
        icon: 'Users',
        title: 'Role-Specific Checklists',
        desc: 'Checklists for the ice cream maker, the scooper at the counter and the shift lead. Everyone knows exactly what to do.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists ice cream shops run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants, ice cream shops and production kitchens.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Ice Cream Shop Pre-Shift Meeting Template',
        desc: "The 5-minute huddle that makes the difference: the flavors to make today, flavors running low, special orders and catering, today's promo, the flavor to recommend and allergens.",
        image: '/lovable-uploads/ai-gallery/consultor-heladero-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Ice Cream Shop Seasonal Calendar & Flavor Planner (US)',
        desc: "12 months with the key US dates (Valentine's Day, St. Patrick's Day, Easter, Mother's Day, Memorial Day, Father's Day, July 4, National Ice Cream Month and Day, Labor Day, Halloween, Thanksgiving, the holidays), four featured flavors a month, the season and the key action for each.",
        image: '/lovable-uploads/ai-gallery/use-case-heladeria-flavors.jpg',
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
    ctaLabel: 'YES, I WANT THE ICE CREAM SHOP CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your ice cream shop better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de icecream/SPEC D5 (ice cream shop / parlor / gelato / scoop shop checklist)
  // + las del ES adaptadas (tareas ya escritas, producción y servicio, tiendas pequeñas y cadenas, frente a las apps,
  // varias tiendas con la licencia de la tienda EN, garantía) + temperaturas, scoop y alérgenos, licencia estatal de
  // frozen dessert, temporada y catering, limpieza, firma, UK/CA/AU, moneda y suscripción (como los hermanos EN). La de
  // Latinoamérica del ES → la de UK/CA/AU.
  faqs: [
    {
      q: 'What should be on an ice cream shop opening checklist?',
      a: "One list in order. Personal hygiene first (clean uniform and apron, hair restrained, no rings or watches, cuts covered with a waterproof bandage and a glove, hands washed, anyone with symptoms stays off ice cream, fruit and toppings). Then a safe start-up: the hood and ventilation on before the pasteurizer and the batch freezer and, if you have gas for waffles or crepes, a check that it doesn't smell of gas before you light anything. Next, the equipment: the dipping cabinets switched from overnight storage mode (0 °F) to service (6–10 °F), the freezers at 0 °F or below and the aging cooler at 36–39 °F, each reading logged, and the blast freezer working. Then the counter: fruit for toppings washed, nuts and sprinkles in closed containers, the scoops in a running-water dipper well or one per flavor, the allergen chart checked against today's flavors, sauces, cones, cups, spoons and napkins stocked, the cabinet glass cleaned and the pans checked for ice crystals. Last, the POS and the starting bank, the card terminal, the sidewalk sign with today's flavors, the patio and the door. The \"Ice Cream Shop Opening & Closing Checklists\" workbook has all 26 opening tasks written, and the whole-shop checklist covers the alarm, lights, HVAC and restrooms.",
    },
    {
      q: 'What goes on an ice cream shop closing checklist?',
      a: "Product first: every pan covered, the dipping cabinets switched to storage mode at 0 °F (with product inside they are never turned off: one night off can cost you every pan), the day's waste logged by flavor, amount and reason, pans labeled with their updated use-by date and tomorrow's pans checked. Then cleaning: the cabinets' outside surfaces, the sauce dispensers, the scoops and the dipper well, the counter, the scale and the register area cleaned and sanitized, trash, floors and the patio. Last, the paperwork: the cash count, sales by flavor (your top sellers), the shift log, lights and sign off, doors and alarm. The whole-shop \"Shop Closing\" tab runs in a safe order: customers out, the patio and signs in, night covers on the dipping cabinets (they stay on) and the closing temperatures logged, then the POS, trash and a final safety check that never unplugs a freezer or a dipping cabinet, and the alarm and lock-up last. The \"Cash Drawer Opening & Closing\" workbook works out the over/short against the POS Z report for you.",
    },
    {
      q: 'Does it cover pasteurizing, aging and batch freezing?',
      a: "Yes. The production workbook has a sheet for each phase. Pasteurizing: ingredients weighed by recipe card, the dry ingredients blended into the liquids, the mix pasteurized at 185 °F for 15 seconds (your pasteurizer's validated program and your state license minimum come first), fats and emulsifiers added at 104–122 °F on the way down, the mix cooled to 41 °F or below (from 135 °F to 70 °F within 2 hours and to 41 °F within 4 more, as the FDA Food Code asks) and aged at 36–39 °F for at least 4 hours, ideally 8–12, then labeled and logged by batch. Batch freezing: the aging time checked, the draw temperature your batch freezer maker gives (around 16–19 °F for ice cream and 10–14 °F for sorbet), pans pre-chilled at −4 °F, mix-ins and swirls in the last minute, each pan labeled with flavor, production date, use-by date and batch, weighed for yield and overrun, hardened at 0 °F or below and moved to the storage freezer, and the batch freezer taken apart and cleaned. At the bottom there is an editable shelf-life table in °F (for example, ice cream and sorbet in covered pans, 2–3 months at 0 °F; pasteurized mix, 3–5 days at 36–39 °F).",
    },
    {
      q: 'Do I need a license to make my own ice cream?',
      a: "It depends on your state. Pasteurizing your own mix usually takes a state frozen dessert or dairy manufacturer license on top of your health permit, and some states also license freezing a mix you buy already pasteurized, or running a soft serve machine; with a bought, pasteurized mix, the health permit is often enough. The kit flags it in the production workbook and checks both papers on the annual sheet, but it is not legal advice: check with your state's department of agriculture or health before you start.",
    },
    {
      q: 'How does the kit handle scoops, the dipper well and allergens?',
      a: "Between scoops, the scoop sits in a dipper well with running water (FDA Food Code 3-304.12) or you use one scoop per flavor. Running water does not remove allergens, so for an allergy order the kit asks for washed hands, fresh gloves, a clean, sanitized scoop and, where you can, a pan no other scoop has touched. The allergen chart by flavor is checked every morning against the pans in the cabinet and covers the 9 major US allergens (milk, egg, tree nuts such as pistachio, hazelnut and almond, peanuts, wheat in cones and cookies, soy and sesame, plus fish and shellfish). Cones and toppings are never touched with bare hands, samples go out on single-use tasting spoons, and the pints you pack ahead for a grab-and-go freezer carry a label with the major allergens.",
    },
    {
      q: 'What temperatures does an ice cream shop need to log?',
      a: "The kit works with temperatures that never mix: frozen storage at 0 °F or below, the dipping cabinets at 6–10 °F during service (check your cabinet maker's range), the mix aging at 36–39 °F and never above 41 °F, and the draw temperature of your batch freezer. The dipping cabinets go back to storage mode at night instead of being switched off, catering product has to arrive at 10 °F or below, and the readings are logged in °F at opening and at close, with the shift lead checking the cabinets during service. Probe thermometers are checked every month in ice water (32 °F).",
    },
    {
      q: 'Does it include peak season, the off-season and ice cream catering?',
      a: 'Yes. The peak season checklist runs from Memorial Day to Labor Day: a bigger menu with seasonal fruit, summer staff hired two weeks ahead (many are 14 or 15, so it notes the federal limits on their hours and on the equipment they can use, and the work permit some states require), more stock, a capacity check, two or three batch freezer runs a day, the patio, at least 2 scoopers at peak times, social media and pints and quarts to go (sold by weight only on a legal-for-trade scale). The off-season checklist cuts the menu, adds hot chocolate, waffles, crepes and ice cream cakes, and schedules deep maintenance, new recipes and training. The ice cream catering checklist starts before you say yes: allergens and headcount in writing, a price per guest, a deposit before you produce (event ice cream can\'t be resold), cancellation terms and freezer space at 0 °F; then production 24–48 hours ahead, insulated carriers and dry ice, and the product at 10 °F or below on arrival. The bonus calendar adds the 12 months with their US dates, from Valentine\'s Day and National Ice Cream Day to Thanksgiving and the holidays.',
    },
    {
      q: 'What should an ice cream shop cleaning checklist include?',
      a: "Daily cleaning belongs in the closing checklists (scoops, the dipper well, sauce dispensers, the counter and the scale, floors). On top of that, the kit schedules a weekly deep clean (the dipping cabinets' grates and interiors, sauce and topping dispensers, cone and cup trays, the batch freezer's dasher, gasket and cylinder, condenser filters, the production walls and shelves, the aging containers, the ice machine, the freezer interiors and the storage shelves, with the FIFO dates checked), sanitizer checked with test strips, and monthly tasks (thermometers, pasteurizer maintenance, freezer door gaskets and insulation, and a general deep clean of floors, walls and ceilings). Contracted services go on the \"Quarterly & Annual\" tab: pest control by a licensed operator, refrigeration by an EPA 608-certified tech (your staff never touches the refrigerant), thermometer calibration, fire extinguishers, gas, backflow testing for the dipper wells and the ice machine, and hood and duct cleaning under NFPA 96 only if you cook with grease, such as waffles or crepes.",
    },
    {
      q: 'Is there a free ice cream shop checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 298 ice cream shop tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for an ice cream shop?',
      a: "Yes. Every checklist comes with the real tasks of a shop that makes its own ice cream already written: production, dipping cabinets, the counter and the manager. You'll want to make it yours: adjust tasks to your shop, delete the ones that don't apply and add your own. The editable cells are green, and the whole-shop and cash drawer checklists end with 5 free green rows that the counter already includes.",
    },
    {
      q: 'Does it work for a gelato shop, a small scoop shop or a chain?',
      a: 'Yes. The kit is written for shops that make their own ice cream or gelato with a pasteurizer and a batch freezer, and it scales: a small scoop shop can start with opening and closing, production and the whole-shop checklist, and a chain can use every role, area and the full calendar. If you buy your mix already pasteurized, mark the pasteurizing tasks N/A and the counter leaves them out.',
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for the area, who does it, ✓ (a drop-down with ✓, — for not done, or N/A), the time and notes, and a signature line at the bottom. The whole-shop and cash drawer checklists come with who does it and a due-by time already filled in. The shift lead prints the checklist and hands it out, each person checks off their tasks, and at the end of the shift the shift lead checks it and signs.',
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it in several ice cream shops?',
      a: "Yes. One purchase covers one business with all of its shops, which makes it a good fit for ice cream shop chains. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code (0 °F frozen storage, 41 °F cold holding), the 9 major allergens and a cash count in US bills and coins. In the UK, ice cream is stored frozen at −18 °C or below, chilled food such as the aging mix is kept at 8 °C or below, and allergen information covers 14 allergens (the kit's allergen tasks already note the UK's 14). In Canada and Australia, check your provincial or state food safety rules, frozen dessert licensing and allergen list, and type them into the tasks. For pounds, Canadian or Australian dollars, unprotect the cash count sheet and change the label and value of each bill and coin. The seasonal calendar has a UK note (Mothering Sunday, bank holidays and Boxing Day) and room for your own dates. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
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
    subtitle: "9 templates + 3 bonuses (12 files) for your ice cream shop for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: dipping cabinets, toppings, counter, cash',
      'Production: pasteurizing, aging and batch freezing, in °F',
      'Stock checks: key ingredients, cones, cups and packaging',
      'Manager checklists: daily, weekly and monthly',
      'Tasks by role: ice cream maker, scooper, shift lead',
      'Seasons: peak season, off-season and ice cream catering',
      'Whole-shop opening and closing + cash drawer count',
      'BONUS: Ice Cream Shop Pre-Shift Meeting Template',
      'BONUS: Ice Cream Shop Seasonal Calendar & Flavor Planner (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE ICE CREAM SHOP CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Heladería Artesanal, la edición española de este kit: por eso conservan sus nombres, negocios y cifras, y el
  // subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD. Ninguno cita una marca o persona real (SPEC §R).
  testimonials: {
    subtitle:
      'Ice cream makers, shift leads and shop owners who already run their operations with Kit de Tareas Recurrentes: Heladería Artesanal, the Spanish edition of this kit',
    items: [
      {
        name: 'Adrián Molina',
        role: 'Artisan Ice Cream Maker, Gelateria Dolce Vita',
        text: 'The production checklist saved me. I used to forget to log the pasteurizing and aging temperatures. Now everything is on record and our quality control is spotless.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Lucía Torres',
        role: 'Owner, Heladería La Cremería',
        text: 'I opened my ice cream shop a year ago and the chaos of peak season was unbearable. With the checklists by shift and area, the team knows exactly what to do without me watching over them.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Pablo Reyes',
        role: 'Head of Production, Helados Artesanos Reyes',
        text: 'The production checklists are perfectly structured: pasteurizing, batch freezing, filling the pans, labeling. My new ice cream makers learn the process in half the time.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Carmen Ortiz',
        role: 'Counter Lead, Heladería El Polo Norte',
        text: 'The dipping cabinet checklist is great. Toppings, sauces, cones, cleaning the glass... it is all listed. The counter always looks perfect for the customer.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Raúl Ibáñez',
        role: 'Director, Frozen Art ice cream shop chain',
        text: 'We have 6 ice cream shops and every manager did things differently. Now, with standardized checklists, the customer experience is the same in all of them. Onboarding went from 2 weeks to 4 days.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Sofía Delgado',
        role: 'Hospitality Consultant, ice cream shops and production kitchens',
        text: 'The first thing I do with every ice cream shop client is hand them these checklists. Production, dipping cabinets, management, seasons... they cover 95% of what any artisan ice cream shop needs.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Marco Valentini',
        role: 'Master Gelato Maker, Gelateria Valentini',
        text: 'The seasonal calendar is pure gold. The summer menu, the winter menu, key dates, catering prep... I finally have the yearly plan I always wanted.',
        avatar: '/avatars/avatar-7.jpg',
      },
      // Ana Belén Ruiz: el ES dice que el control de «food cost y mermas de producción» lo «incluye el checklist del
      // manager»; el 03 trae el food cost, pero las mermas se anotan al cierre (01) y se revisan en el mensual (05).
      // En EN se cambia SOLO esa frase (regla de John: testimonio que choca con el kit → cambiar solo esa frase).
      {
        name: 'Ana Belén Ruiz',
        role: 'General Manager, Heladería Sabores del Sur',
        text: "The food cost control in the manager checklist, with the waste log at closing, is exactly what we needed. Waste used to catch us by surprise at the end of the month. Now we keep it under control every day.",
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

  // Saliente extra (como el Ghost Kitchen): el caso de uso EN de las heladerías artesanas, que a su vez lista este kit
  // (products-catalog.ts urlByLang.en).
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
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: '/en/use-cases/concept/artisan-ice-cream-shop', label: 'AI for Ice Cream Shops' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'ice-cream-shop-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
