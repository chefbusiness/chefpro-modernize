// astro-site/src/data/productos-en/tareas/catering-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Catering Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-catering.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-, bar- y coffee-shop-checklist-templates.ts. SPEC: scripts/productos-digitales/checklists-kit/
// catering/SPEC.md (delta) + la base.
//   · D2: nombre «Catering Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Catering Checklists Kit Pro: Catering Event Checklist Templates for Excel».
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (catering/SPEC §2,
//     dl/catering-checklist-templates/).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos (el ES los «valora en €31»). Fórmula de la tienda EN.
//   · Cifras y normas SOLO de catering/SPEC §3 (REGLAS_US de mapas_catering.py) y de los xlsx EN: 347 tareas (los
//     contadores del kit: 327 en las 9 plantillas + 20 en el briefing, como el ES), 38 en el 01, 33 en el 08 con
//     responsable y hora, 16 por perfil, 25 filas en el registro de cobros, 22 fechas; 41 / 135 °F en carga, trayecto
//     (cada 30 min), buffet y descarga (3-501.16); time as a public health control 4 h / frío 6 h ≤ 70 °F
//     (3-501.19); el chafing mantiene y no recalienta (165 °F, 3-403.11); sobrantes: enfriar (3-501.14) o tirar lo
//     expuesto; parásitos 3-402.11; 9 alérgenos (UK: 14); open bar 21+ con la licencia que pida el estado; service
//     charge ≠ gratuity (Rev. Rul. 2012-18); sales tax = tipo que introduce el comprador (C3 del «Event Billing Log», 0
//     por defecto); 12–15 piezas por persona y 1 camarero por 20 invitados en el cocktail.
//   · Alineada con la ronda 1 de la revisión F2 (xlsx de las 02:50): TPHC = servir DENTRO de las 4 h y descartar lo
//     que quede (B1), sobrantes calientes a enfriar y fríos de vuelta a 41 °F (M2), service charge = ingreso y lo que se
//     paga al equipo, salario (m3), tipo de sales tax a 0 hasta que se introduce (M9).
//   · Lo que el ES afirma y el kit no trae, fuera: «cumple normativa APPCC de transporte» (el kit da los límites del
//     FDA Food Code, no certifica nada), el «certificado ATP» (no existe en EEUU: registro, seguro y permiso del
//     condado si lo pide), «IVA 10/21 %» y «Verifactu» (→ sales tax a tu tipo y ajustes del POS), las «secciones ya
//     puestas» de la plantilla en blanco (trae columnas y filas numeradas), «sin internet» de la comparación con apps.
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual (nombres,
//     negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan.
//     Una frase que el kit contradice, cambiada (regla de John, 11-oct): Roberto Ibáñez («el timing sheet del event
//     manager» → el kit trae el checklist del event manager, con la run sheet como tarea, no una hoja de timing).
//   · Imágenes: las 6 fotos del ES no llevan texto en español (furgoneta «FRESH EVENT CATERING», cajas «CRYSTAL –
//     HANDLE WITH CARE») y ya las publica el Catering Business Plan Kit EN: se quedan. Fuera solo la OG del ES
//     (og-kit-tareas-catering: «Kit de Tareas Recurrentes», «€12», «Imprimible A4») → OG = el hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_CATERING_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'catering-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_CATERING_CHECKLISTS_KIT',

  seo: {
    title: 'Catering Checklists Kit Pro: Catering Event Checklist Templates for Excel',
    description:
      '11 Excel catering checklists with 347 tasks already written: prep, transport, setup & breakdown, event manager, staff roles, deposits & payments. One-time $19.',
    keywords:
      'catering checklist, catering event checklist, catering checklist template, catering setup checklist, catering event planning checklist, off-site catering checklist, catering transport checklist, catering staff checklist, banquet captain checklist, catering breakdown checklist, BEO, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
  },

  schema: {
    productName: 'Catering Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for catering companies with 347 tasks already written: off-site prep and production, transport and delivery, event manager, staff by role, setup and breakdown, weddings, corporate events, cocktail receptions and outdoor events, commissary opening and closing, and deposits, invoicing and payments by event.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a catering checklist?',
        a: 'One list for each phase of the event: advance planning from the BEO (guaranteed count, menu, allergens), off-site production and packing, transport with temperatures logged, setup at the venue, service, breakdown and the post-event wrap-up, plus the money: deposit, invoice and balance. Each task needs who does it, a time and a check mark.',
      },
      {
        q: 'How do you keep catered food safe in transport and on the buffet?',
        a: 'Hold hot food at 135 °F or above and cold food at 41 °F or below when you load, every 30 minutes on the road, on the buffet and when you unload, and log the readings. Chafing dishes hold food, they do not reheat it: reheat to 165 °F first. Food without temperature control falls under time as a public health control (FDA Food Code 3-501.19): mark the time and serve it within 4 hours; whatever is left at 4 hours is discarded.',
      },
      {
        q: 'Is there a free catering checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 347 catering tasks already written, a counter that skips N/A tasks, °F temperatures and an event settlement in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'How does the kit handle sales tax and the service charge?',
        a: 'You type your combined state and local sales tax rate once, and the Event Settlement applies it to the taxable subtotal you enter. What is taxable depends on your state. A mandatory service charge is not a tip: what you pay out of it to staff is wages for the IRS (Rev. Rul. 2012-18). The kit is not tax advice: check with your CPA.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C, hot holding at 63 °C and 14 allergens on your buffet signs; in Canada and Australia, your local holding temperatures and allergen list; type your VAT or GST rate in the tax rate cell and change the cash table to your currency. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Catering Checklists Kit Pro',
  },

  images: {
    // Las del ES (ninguna lleva texto en español; ver cabecera). Solo cambia la OG.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-cocina.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-transporte.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Catering Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Catering Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Catering Event Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) in Excel with 347 catering and event tasks already written: off-site production, transport, commissary opening and closing, deposits and payments by event, setup, service, breakdown and the post-event wrap-up. Print it, delegate it to your team, check it off and file it.',
    checkItems: [
      'Off-site production: mise en place, day-before prep, packing in hotel pans and insulated carriers',
      'Transport and delivery: loading, holding temperatures in °F, load-in at the venue',
      'Commissary opening and closing, and payments by event: deposit, settlement and balance',
      'Venue setup and breakdown: temporary kitchen, room, buffet and stations',
      'Event types: weddings, corporate, cocktail receptions, outdoor',
      '3 editable master templates + a pre-event briefing template',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS CATERING — €12»).
  stickyLabel: 'CATERING CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Catering Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '347 catering and event tasks already written and sorted by event phase, area and role. Adjust them to your operation, print and delegate.',
    templates: [
      {
        icon: 'ChefHat',
        title: 'Catering Prep & Production Checklist (Off-Site Catering)',
        desc: 'Advance planning from the BEO (guaranteed count, menu, allergens), personal hygiene and a safe kitchen start-up, day-before prep, event-day cooking, parasite destruction for fish served raw (ceviche, tartare), pre-plating and packing in hotel pans and insulated carriers, with temperatures checked before loading. 38 tasks already written, plus a freezer shelf-life table at the bottom.',
      },
      {
        icon: 'Truck',
        title: 'Catering Transport & Delivery Checklist: Loading, Holding Temps & Load-In',
        desc: 'Vehicle pre-load (clean, pre-chilled, registration and insurance checked), food loading with the temperature of every hotel pan logged, a reading every 30 minutes on the road (hot 135 °F or above, cold 41 °F or below), time as a public health control when there is no temperature control, and unloading at the venue.',
      },
      {
        icon: 'ClipboardList',
        title: 'Catering Event Manager Checklist + Quarterly & Annual Compliance',
        desc: "Event week, event day (before, during and after service) and the wrap-up with the team, with everyone's time-clock records closed out. + a Quarterly & Annual sheet: commissary pest control, hood cleaning (NFPA 96), fire extinguishers and hood suppression, vehicles, thermometer calibration, gas, used oil, health permit, food handler cards and a Certified Food Protection Manager, insurance and COI, I-9 and W-4, and sales tax settings, each with its frequency and the report number.",
      },
      {
        icon: 'Users',
        title: 'Catering Staff Checklists by Role (Event Chef, Banquet Captain, Server, Bartender)',
        desc: 'Checklists for the event chef, the banquet captain, the server / event runner and the bartender: what each role does before, during and after service, 16 tasks each. Hand the extra staff their tab and they know what to do.',
      },
      {
        icon: 'Tent',
        title: 'Catering Event Setup & Breakdown Checklist (Load-In / Load-Out)',
        desc: 'Temporary kitchen (power, water, a handwashing station, open-flame rules), room setup, buffet and stations with allergen signs and chafing dishes, and a final check before guests arrive. Breakdown: room, kitchen, leftovers cooled by the rule or discarded, waste logged, load-out and a final walk-through.',
      },
      {
        icon: 'PartyPopper',
        title: 'Catering Event Checklists: Weddings, Corporate, Cocktail Receptions & Outdoor',
        desc: 'Weddings with allergies collected in writing and marked on the seating chart, corporate events with coffee breaks and dietary restrictions in writing, cocktail receptions (12–15 pieces per person for 2 hours, an allergen card on every tray, parasite destruction for ceviche and tartare) and outdoor events under time as a public health control. A checklist for each format.',
      },
      {
        icon: 'FileEdit',
        title: 'Catering Checklist Template (Blank & Editable)',
        desc: '3 blank templates (by event phase, by venue area and by role) with the columns and numbered rows already set up: you just type your own tasks.',
      },
      {
        icon: 'Building2',
        title: 'Catering Commissary Opening & Closing Checklist',
        desc: "The checklist for the whole commissary, not just the kitchen: the day's BEOs printed and handed out, a route sheet for each vehicle, insulated carriers loaded with the departure temperature logged, outdoor equipment, and access and load-in times confirmed with each venue. Who does it and when are filled in for all 33 tasks.",
      },
      {
        icon: 'Wallet',
        title: 'Catering Deposits, Invoicing & Payments: Event Settlement & Billing Log',
        desc: 'The money for each event, not a cash drawer: a checklist of what to close before (signed quote, 30–50% deposit collected, billing details, COI) and after (actual vs. guaranteed count, extras, invoice, balance, bank reconciliation). An event settlement with sales tax at your rate, the invoice total, the balance after the deposit and the BALANCE DUE in amber, with a STATUS that switches to OVERDUE once the due date passes. Plus a billing log for 25 events with totals and a count of overdue events.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Catering Pre-Event Briefing Template (Team Huddle)',
        desc: 'The team huddle 30–60 minutes before doors open: event details, menu and allergens, team and roles, VIPs and protocol. One copy for the kitchen and one for the service team.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Catering Busy Season & Events Calendar (US)',
        desc: '22 key US dates for caterers, from Super Bowl Sunday and wedding season to graduation parties, July 4 cookouts, Thanksgiving and holiday parties, with the key tasks and the recommended lead time for each, and a UK note.',
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
        title: 'Pre-Filled for Catering',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a professional catering company. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Truck',
        title: 'From the Commissary to the Venue',
        desc: "It covers the whole chain: production, transport, setup, service and breakdown. The tasks generic checklist apps don't cover.",
      },
      {
        icon: 'Users',
        title: 'Event Roles',
        desc: 'Checklists for the event chef, banquet captain, server and bartender. Every team member knows exactly what to do in each phase.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists catering companies run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has coordinated hundreds of catered events, from intimate weddings to conventions of 500+ guests.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Catering Pre-Event Briefing Template',
        desc: 'The huddle 30–60 minutes before doors open. Event details, menu and allergens, team and roles, VIPs and protocol.',
        image: '/lovable-uploads/ai-gallery/tareas-catering-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Catering Busy Season & Events Calendar (US)',
        desc: "22 key dates for US caterers (Super Bowl Sunday, Valentine's Day, Easter and Passover, wedding season, Mother's Day, graduation parties, July 4 cookouts, fall weddings, Thanksgiving, holiday parties, New Year's Eve) with the key tasks and the recommended lead time.",
        image: '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
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
    ctaLabel: 'YES, I WANT THE CATERING CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your catering operation better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de catering/SPEC D5 (catering checklist, catering event checklist, catering
  // checklist template) + las del ES adaptadas (tareas ya escritas, ciclo completo, bodas/corporativos/cocktails,
  // frente a las apps, varios eventos con la licencia de la tienda EN, garantía) + seguridad alimentaria fuera del
  // local, montaje y desmontaje, la FAQ honesta de impuestos (sales tax y service charge), UK/CA/AU, moneda y
  // suscripción (como los hermanos EN). La de Latinoamérica del ES → la de UK/CA/AU.
  faqs: [
    {
      q: 'What should be on a catering checklist?',
      a: "One list for each phase of the event, so nothing depends on memory. Advance planning: review the BEO (banquet event order) with the guaranteed count, menu and allergens, confirm dietary restrictions with the client, build the shopping list and the production run sheet. Production at the commissary: personal hygiene, a safe kitchen start-up, day-before prep, event-day cooking, pre-plating and packing in labeled hotel pans and insulated carriers. Then transport, setup at the venue, service by role, breakdown and the post-event wrap-up, plus the money: signed quote, deposit, invoice and balance. Each task needs who does it, a time and a check mark, and someone signs off the sheet.",
    },
    {
      q: 'What goes on a catering event checklist for the day of the event?',
      a: "Arrive at the venue at least 3 hours before the event starts. Check access, power, potable water, restrooms, cold storage and the handwashing station; coordinate the unloading; supervise the room setup and check the buffet and stations against the floor plan; hold separate pre-event briefings with the service team (timing, menu, allergens, VIPs) and the kitchen (order of service, temperatures); and do a final check-in with the client. During the event: service timing, plating quality, buffet refills, incidents and the bar. After: an orderly breakdown, the equipment count, incidents, breakage and waste logged, and the team's time-clock records closed out. In this kit, that is the event manager's checklist, and each role has its own.",
    },
    {
      q: 'How do you keep catered food safe in transport and on the buffet?',
      a: "Under the FDA Food Code, hot food stays at 135 °F or above and cold food at 41 °F or below: check and log it before loading, every 30 minutes on the road, at unloading and on the line. Chafing dishes hold food, they don't reheat it: reheat cold food to 165 °F first. Anything traveling or sitting out without temperature control falls under time as a public health control (3-501.19): mark the time it left 41 °F or 135 °F and serve it within 4 hours, trip and service included; whatever is left at 4 hours is discarded, and it can't go back into holding to restart the clock. Cold food can go up to 6 hours only if it starts at 41 °F or below and you check it never passes 70 °F. That needs a written procedure and, depending on your county, notice to the health department. After the event, food that stayed at a safe temperature and never went out to guests is kept: hot food is cooled (135 °F to 70 °F within 2 hours, then to 41 °F within 4 more) and cold food goes straight back to 41 °F or below; anything that sat on the buffet or was held under time as a public health control is discarded.",
    },
    {
      q: 'What should a catering setup and breakdown checklist include?',
      a: "Setup: the temporary kitchen placed per the floor plan with power and water, a handwashing station if the site has no sink, open flame only if the venue and the fire marshal allow it, and a temporary food establishment permit if you cook at a public event and your county or city requires one. Then the room (tables, linens, place settings, centerpieces, lighting and sound), the buffet and stations with chafing dishes and a sign on each dish with its name and major allergens, and a final check: sample table, room temperature, restrooms and emergency exits. Breakdown: linens sorted, glassware racked, flatware counted against inventory, equipment off and chafing fuel snuffed, leftovers handled by the cooling rule, the kitchen area left as you found it, a final walk-through and the departure time logged.",
    },
    {
      q: 'Is there a free catering checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 347 catering tasks already written and sorted by event phase, area and role, a counter on every checklist that skips the tasks you mark N/A, temperatures in °F and an event settlement in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for catering and events?',
      a: "Yes. Every checklist comes with the real tasks of a professional catering company already written. You'll want to make it yours: adjust tasks to your operation, delete the ones that don't apply and add your own. The editable cells are green, and the commissary and payment checklists end with 5 free green rows that the counter already includes.",
    },
    {
      q: 'Does it cover the whole event cycle, not just service?',
      a: "Yes. It covers off-site production at your commissary, transport and delivery, setup at the venue, service by role, breakdown and load-out, and the post-event wrap-up. On top of that, the commissary has its own opening and closing checklist, and each event's money (deposit, settlement, invoice and balance) has its own workbook.",
    },
    {
      q: 'Does it work for weddings, corporate events and cocktail receptions?',
      a: 'Yes. The general checklists (production, transport, setup, roles) work for any event, and there are specific checklists for each format: weddings (guaranteed count, seating chart with allergies, cake cutting, open bar, late-night snack), corporate events (agenda, AV, coffee breaks, dietary restrictions in writing), cocktail receptions (12–15 pieces per person for 2 hours, 1 server per 20 guests for passed trays, an allergen card on every tray) and outdoor events (weather checks, a rain plan, generator, tent, food safety in the heat).',
    },
    {
      q: 'How does the kit handle deposits, sales tax and the service charge?',
      a: "The deposits, invoicing and payments workbook tracks each event's money: the deposit (usually 30–50%, per your contract), the invoice total, the balance after the deposit and the balance due, with a status that turns OVERDUE once the due date passes. For sales tax, you type your combined state and local rate once (the cell starts at 0) and split each event's pre-tax amount between a taxable and a non-taxable subtotal; the sheet applies the rate only to the taxable part and warns you if the two don't add up. What is taxable is up to your state: in many states food, drinks, rentals and the mandatory service charge. A mandatory service charge is not a tip: it is your revenue, and whatever part of it you pay to staff is wages for the IRS, not tips (Rev. Rul. 2012-18), while a gratuity is the client's choice and goes on a separate line. A tax-exempt client needs their exemption certificate on file. The kit organizes the numbers; it is not tax advice, so check with your CPA or your state's department of revenue.",
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment, with no limit on events. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it for several events at once, or with my clients?',
      a: "Yes. One purchase covers one business with all of its events and locations, so you can run the checklists for every event you manage, several a week if you need to. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F under the FDA Food Code, the 9 major allergens, sales tax and dollars. In the UK, where off-site catering is usually called event catering, cold holding is 8 °C or below and hot holding 63 °C or above, and allergen information covers 14 allergens (the buffet signs and tray cards already note the UK's 14); the events calendar has a UK note for bank holidays and Boxing Day. In Canada and Australia, type your province's or state's holding temperatures in °C and its allergen list into the tasks. On the payments sheet, type your VAT, GST or HST rate in the tax rate cell (what is taxable is for your accountant to say), and change the bills and coins of the optional cash table to your currency. If you serve alcohol, you need the licence your event requires; the legal age is 18 in the UK and Australia (where staff also need an RSA certificate), and 19 in most Canadian provinces (18 in Alberta, Manitoba and Quebec). Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and alcohol side by side.",
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
    heading: 'Stop Improvising at Every Event',
    subtitle: "9 templates + 3 bonuses (12 files) for your catering business for less than one hour of a consultant's time.",
    items: [
      'Off-site production: planning, mise en place, packing',
      'Transport: holding temperatures, loading, unloading at the venue',
      'Payments by event: deposits, settlement with sales tax and overdue balances',
      'Setup: temporary kitchen, room, buffet, action stations',
      'Event manager tasks: event week + event day',
      'Tasks by role: event chef, banquet captain, server, bartender',
      'Event types: weddings, corporate, cocktail receptions, outdoor',
      'BONUS: Catering Pre-Event Briefing Template',
      'BONUS: Catering Busy Season & Events Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE CATERING CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los 10 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas
  // Recurrentes: Catering / Eventos, la edición española de este kit: por eso conservan sus nombres, negocios y
  // cifras, y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD. Una frase cambiada (ver cabecera);
  // «APPCC» de Ana Belén Torres = HACCP.
  testimonials: {
    subtitle:
      'Event managers, catering chefs and coordinators who already run their operations with Kit de Tareas Recurrentes: Catering / Eventos, the Spanish edition of this kit',
    items: [
      {
        name: 'Manuel Domínguez',
        role: 'Director, Catering Elegance Madrid',
        text: 'Every event used to be organized chaos. The production and transport checklists cut our slip-ups by 90%. Now the extra staff know exactly what to do without asking.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Javier Montero',
        role: 'Executive Chef, Grupo Banquetes del Sur',
        text: 'The off-site production checklist is pure gold. Mise en place, packing, temperature control... all on one sheet. My cooks print it and follow it step by step.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Laura Sánchez',
        role: 'Event Manager, Bodas con Alma',
        text: 'I do 3-4 weddings a week in high season. The checklists by event type save me hours of prep. The wedding one covers everything from the cocktail hour to the late-night snack.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Roberto Ibáñez',
        role: 'General Manager, Catering Corporativo BCN',
        text: "Coffee breaks and corporate events take military precision. The event manager's checklist and the tasks by role have made our operation truly professional.",
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Ana Belén Torres',
        role: 'Logistics Coordinator, Grupo Eventos Premium',
        text: "The transport and cold chain checklist is exactly what we needed to meet our HACCP requirements. We don't improvise with temperatures anymore.",
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Diana Fernández',
        role: "Maître d', Hotel Palace Catering",
        text: 'The tasks by role for event servers are great for temporary staff. We hand them the printed sheet and they know what to do before, during and after service.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Carmen Ruiz',
        role: 'Owner, Catering a Domicilio Valencia',
        text: 'The venue setup and breakdown checklist saved my life. We always used to leave something behind. Now we do the final walk-through with the list and it never fails.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Sergio Navarro',
        role: 'Director of Operations, Catering 360',
        text: 'The busy season calendar is amazing for planning extra staff. We know exactly when we need more people and can plan months ahead.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Isabel García',
        role: 'Event and Catering Consultant',
        text: "I recommend this kit to all my catering clients. Production, transport, setup, service... they cover the full cycle. It's the standard every event company should have.",
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Francisco López',
        role: 'Instructor, Escuela de Hostelería y Eventos',
        text: 'My catering students use these checklists as a reference. The tasks are perfectly structured by event phase. First-class training material.',
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
    { href: '/en/digital-products/catering-business-plan', label: 'Catering Business Plan Kit' },
    { href: '/en/digital-products/bbq-catering-business-plan', label: 'BBQ Catering Business Plan Kit' },
    { href: '/en/digital-products/paella-catering-business-plan', label: 'Paella Catering Business Plan Kit' },
    { href: '/en/digital-products/pizza-shop-business-plan', label: 'Pizza Shop Business Plan Kit' },
    { href: '/en/digital-products/ice-cream-shop-business-plan', label: 'Ice Cream Shop Business Plan Kit' },
    { href: '/en/digital-products/wedding-venue-business-plan', label: 'Wedding Venue Business Plan Kit' },
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
    product: 'catering-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
