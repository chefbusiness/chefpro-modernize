// astro-site/src/data/productos-en/guias/how-to-open-a-pastry-shop.ts
// TIENDA INTERNACIONAL EN — How to Open a Pastry Shop. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/guias/guia-pasteleria-obrador.ts (mismo tipo GuiaData, misma plantilla
// GuiaLandingPage con lang="en", mismo orden de campos). Segunda guía de la tienda EN; patrón = la ficha
// food-cost-menu-engineering-guide.ts (primera guía EN).
// SPEC: scripts/productos-digitales/guia-pasteleria-en/SPEC.md (D1, D2, D17, D18, D19 y §6 SEO).
//   · D1: nombre «How to Open a Pastry Shop» (titlePre + titleGold y schema.productName EXACTOS: ya publicado
//     como «Coming soon» en el hub EN). «Bakery» va como descriptor (title, H1 vía subtitleLine, meta).
//     Slug/productId how-to-open-a-pastry-shop.
//   · D2: $69, pago único. SIN anclas: sin priceOld, descuento, «Total value» ni «Save $».
//   · §6 SEO (F1-research-us.md §15): title y meta EXACTOS de la SPEC; descriptor del H1 en subtitleLine;
//     FAQ con las PAA de §12.3 (sin tasa de fracaso: no hay dato verificado) + «Does it work in the UK, Canada
//     or Australia?» con los hechos de §14. Texas y Florida, nombrados (búsquedas relacionadas por estado), y la
//     ruta «home bakery → storefront» (cottage food → licensed kitchen) contestada en la FAQ.
//   · D17: sin Kit de Tareas (no tiene gemelo EN): «your daily checklists and logs». Registros de temperatura,
//     limpieza y alérgenos de vitrina → HACCP Food Safety Kit Pro; escandallo unitario → Food Cost Kit Pro;
//     plan para el banco → Bakery Business Plan Kit; ya abiertos → Food Cost + Menu Engineering Guide.
//   · Cifras SOLO de los entregables: PDF guía 113 págs. y bonus 39 págs. (PyMuPDF, 17-oct), 20 capítulos + anexo
//     normativo US, 8 xlsx (SPEC §2, pestañas leídas con openpyxl), 30 referencias, 30 trámites en 6 fases,
//     18 comprobaciones de visita con 8 eliminatorias, 9 proveedores, 4 estados de ejemplo. Caso modelado
//     (D6): $165,800 de inversión de apertura y $227,916 con circulante, $14,966 el formato casero, 8,6 % neto
//     en el año de crucero, $4,469 el año 1 frente a $27,836 el año 2 (caps. 1 y 18 de la guía EN).
//   · «2 bonuses» (meta de la SPEC) = business plan modelo + 12 decisiones; la Equivalents Guide es el bonus
//     COMÚN de la tienda EN (D18) y va rotulada aparte, como en el dashboard («International Bonus»).
//   · Sin testimonios (el ES no tiene), sin aggregateRating ni review. La plantilla, fuera del ES, no pinta los
//     avatares con 5 estrellas del hero si no hay testimonios.
//   · Imágenes: las 6 del ES (guia-pasteleria-*.jpg) y su OG, revisadas el 17-oct: ninguna lleva texto.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_HOW_TO_OPEN_A_PASTRY_SHOP (resuelto en el wrapper .astro).
import type { GuiaData } from '../../productos/guias/types';

// FAQ: la misma lista en el acordeón y en el FAQPage (patrón de la Food Cost EN y de los planes EN).
const FAQS: { q: string; a: string }[] = [
  {
    q: 'How much does it cost to open a bakery?',
    a: "Published bakery startup figures run from about $10,000 to well over $150,000, because they describe different businesses: a home bakery, a counter-only shop, a café with seating or a production kitchen. This guide prices one specific case, line by line: a mid-size pastry shop with its own production kitchen and front counter needs an opening investment of $165,800, and $227,916 with working capital, before the sales tax you pay on equipment. The home-based format starts at $14,966. The Startup Cost Calculator lets you swap in your square footage, your quotes and your format.",
  },
  {
    q: 'How do I start a bakery business from home?',
    a: "Most people start under their state's cottage food law, selling straight to their own customers, and move to a licensed kitchen when they outgrow it. The usual stepping stone between the two is renting time in a licensed commissary or shared kitchen before you sign a lease. Chapter 9 and the \"Cottage Food Route\" sheet take you through the home route in four example states, and chapter 1 compares the eleven bakery formats, from the home kitchen to a shop with its own production kitchen, so you know which one you're really opening.",
  },
  {
    q: 'Do I need a license to sell baked goods from home?',
    a: "It depends on your state's cottage food law. In California it's a registration (Class A) or a permit (Class B) with your county; in Texas, a registration with DSHS only if you sell items that need refrigeration; in New York, a free home processor registration; Florida asks for no license at all. What you can sell is set by your state's list, and by default only shelf-stable baked goods qualify, so a cake with a cream filling usually doesn't (Texas opened that door in September 2025, with registration, labeling and delivery at 41 °F or below). Each state also sets its own sales cap, channel rules and label wording, and the \"Cottage Food Route\" sheet lays them out for the four example states.",
  },
  {
    q: 'What permits do I need to open a bakery?',
    a: "A bakery that sells directly to consumers is a retail food establishment: it doesn't register with the FDA and gets its food permit from the local health department, or from a state agency in some states (New York and Florida license a bakery that sells to go through their agriculture departments). The permit is issued after plan review and the pre-opening inspection, and it runs alongside the building permit, certificate of occupancy and business license from your city or county. FDA registration comes back only if more than half of your food sales by value go to other businesses. The permits checklist puts the 30 steps in six phases, in order.",
  },
  {
    q: 'Is a bakery a profitable business?',
    a: "It can be, but not by much, and not in year one. Third-party estimates (Toast) put the food sector's typical net margin at 3% to 5%, higher for specialty shops. The case modeled in this guide closes its steady-state year at 8.6% net, inside the 8% to 12% band a fourth-generation bakery owner in Spain gives for a business that's doing well, and it earns $4,469 in year one against $27,836 in year two, because you carry the full fixed costs from the first month while sales ramp up. The 3-year financial plan shows you the same picture with your own numbers.",
  },
  {
    q: 'What are the biggest mistakes people make when opening a bakery?',
    a: "Three come up again and again. Signing the lease before you know the space can work: a space where you can't run a hood duct up to the roof, or where zoning or the landlord says no, isn't fixed by a good rent, and chapter 6 is the deal-breaker screen to run before you sign. Sizing the kitchen for an ordinary day: a peak multiplies production by five to ten with the same equipment, so chapter 15 measures each of the year's six peaks against your capacity before it arrives. And pricing from ingredients alone, when in a production kitchen labor weighs more (chapter 12).",
  },
  {
    q: 'Can I start a bakery with no money?',
    a: "Not with no money, but with far less than a storefront. The cottage food route lets you start from your own kitchen: the home-based format in this guide starts at $14,966. Renting time in a licensed commissary kitchen runs about $250 to $750 a month according to WebstaurantStore. And the SBA Microloan program lends $50,000 or less for working capital, inventory, furniture and machinery; chapter 19 explains when an SBA 7(a) loan or a conventional bank loan fits instead.",
  },
  {
    q: 'Is owning a bakery worth it?',
    a: "Only if the schedule works for your life as well as the numbers work for the bank. Getting up at four in the morning is the variable that pushes the most people out of the business, and chapter 14 treats the owner's hours as a decision you design before you open, not something you tough out. The financial plan also puts the owner's pay on its own line, because a bakery that's only profitable when its owner works for free isn't profitable.",
  },
  {
    q: 'What sells the most in a bakery?',
    a: "A handful of items carries most of the register: in one documented pastry shop, a single croissant brings in close to 30% of total sales. Chapter 3 builds a 30-item opening menu in five families and explains the role of each one, and the \"Mix and Average Ticket\" and \"Menu Decision\" sheets cross each item's margin with how much it sells, so you see what to keep, what to reprice and what to drop.",
  },
  {
    q: 'Does it work in the UK, Canada or Australia?',
    a: "Yes, as a method; the legal details are US-based. The business model, recipe costing, capacity planning, staffing math and 3-year plan work the same in any market, and every tool lets you type your own figures. The permits, labor and tax chapters follow US rules (FDA Food Code, FLSA, state sales tax), and the startup cost workbook has a \"VAT-GST & Cash\" sheet for when the tax on your purchases comes back. If you open in the UK, register your food business with your local council at least 28 days before trading, and plan for 14 allergens and full ingredient labels on food you prepack for direct sale; cold bakery items to go are generally zero-rated for VAT, while food eaten on your premises is standard-rated. In Canada, inspection is provincial or municipal and Health Canada lists 11 priority allergens; in Australia, many food businesses need a certified Food Safety Supervisor and prices include 10% GST. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, which maps every term.",
  },
  {
    q: "Isn't all this free on Google?",
    a: "The scattered information is, and that's why it contradicts itself: published startup figures run from about $10,000 to well over $150,000 for what sounds like the same business, and none of them says what it assumes. What isn't on Google is the order in which the decisions get made, and eight Excel tools where you enter YOUR square footage, YOUR city and YOUR menu and get YOUR figure, with the assumption written next to it.",
  },
  {
    q: 'What if my bakery is already open?',
    a: "Then this isn't your product, and we'd rather say so before you pay. For pricing and the menu, the Food Cost + Menu Engineering Guide; for your daily temperature, cleaning and allergen records, the HACCP Food Safety Kit Pro. This guide is written for anyone who hasn't opened yet, and half of its value is in decisions you've already made.",
  },
  {
    q: 'Does it replace an architect or a designer?',
    a: "No, and we say it up front. The plans and specifications for plan review are prepared by your designer, architect or engineer, and the building permit and certificate of occupancy go through your city or county. What the guide does is get you to those meetings knowing what the plan reviewer will ask for (the menu, the expected volume, the layout, the equipment with make and model, the finishes), and keep you from signing a lease before you know whether the space can work.",
  },
  {
    q: 'My city and county are different. Will it still work?',
    a: "It's the first objection any expert raises, and they're right: no guide can carry the code of thousands of US cities and counties, and one that tried would be out of date within months. What this one gives you is the federal and state map with each rule and its section, four example states (California, Texas, New York and Florida) side by side, how to find your own agency in five minutes, and the exact list of what to ask your city, your county and your health department.",
  },
  {
    q: 'Do I also need the HACCP Food Safety Kit Pro, the Food Cost Kit Pro or the Bakery Business Plan Kit?',
    a: "They do different jobs. The HACCP Food Safety Kit Pro has the logs you fill in every day once you're open (temperatures, cleaning, the display-case allergen matrix), and this guide doesn't rebuild them on purpose. The Food Cost Kit Pro costs a single item down to the cent in US units, and it already includes three items from this guide's case: the butter croissant, the raspberry macarons and the 70% dark chocolate cake. The Bakery Business Plan Kit is the plan built on your own numbers to take to the bank; this guide comes with a sample plan already filled in with its case, plus the decisions that come before it.",
  },
  {
    q: 'Which programs do the Excel tools work with?',
    a: "Microsoft Excel, Google Sheets, LibreOffice and Apple Numbers. There are no links between workbooks, every assumption lives in an editable green cell, and the workbooks keep their calculated values saved inside the file, so they also display correctly on a phone and in viewers that don't recalculate.",
  },
  {
    q: 'What happens when the rules change?',
    a: "You pay once and updates are included: you open your dashboard and download the new version at no extra cost. The legal parameters live in editable cells with their source and date, the guide closes with a regulatory appendix updated in October 2026, and a section shows you how to check a rule's current version in one minute. The dates we already know will move are written down too: minimum wages change, California adjusts its cottage food sales caps every year, and Texas changed its cottage food rules on September 1, 2025.",
  },
  {
    q: 'What currency will I pay in?',
    a: 'The price is $69 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The workbooks have no currency symbol: you type amounts in your own currency.',
  },
  {
    q: 'Is it a subscription? Are future updates included?',
    a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we improve a tool or update the guide, you download the new version at no extra cost, and the dashboard shows the change history of every version.',
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the guide doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: GuiaData = {
  slug: 'how-to-open-a-pastry-shop',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_HOW_TO_OPEN_A_PASTRY_SHOP',

  seo: {
    title: 'How to Open a Pastry Shop: US Bakery Guide + 8 Excel Tools',
    description:
      'Open a bakery with its own pastry kitchen: permits by state, cottage food, startup costs, equipment, staff and a 3-year plan. 8 Excel tools + 2 bonuses.',
    keywords:
      'how to open a bakery, how to start a bakery business, opening a bakery, pastry shop business, bakery business, bakery startup costs, how much does it cost to open a bakery, bakery permits, bakery license, cottage food law, cottage food license, home bakery license, bakery equipment list, how to open a pastry shop, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-pasteleria-obrador.jpg',
  },

  showCompatibleApps: true,

  hero: {
    badge: 'For anyone who has NOT opened yet: what to decide before you sign anything',
    titlePre: 'How to Open a ',
    titleGold: 'Pastry Shop',
    subtitleLine:
      'The step-by-step guide to opening a bakery with its own production kitchen in the US: permits, startup costs, equipment, team, peak seasons and your first 90 days',
    description:
      "It doesn't teach you to bake. It tells you what to decide and in what order: whether that space works, how much money you really need, what each agency asks of you, what you have to charge and whether your kitchen can handle the busiest weeks of the year. It isn't a recipe book or a baking course, and it doesn't replace the plans your designer submits for plan review.",
    checkItems: [
      'Complete guide in PDF + editable DOCX: 20 chapters and a dated US regulatory appendix (113 pages)',
      '8 Excel tools with live formulas: kitchen capacity and site visit checklist, startup costs, seasonal peaks, opening menu and recipe costing, 3-year financial plan, permits and licenses, equipment and suppliers, and staff schedule with labor cost',
      'From home bakery to storefront: cottage food, your retail food permit and when wholesale brings in FDA registration, with four example states (California, Texas, New York and Florida)',
      'Every legal point names its agency or code section, checked in October 2026, and every assumption in the Excel tools lives in an editable cell',
      'Bonus 1: the sample business plan, filled in with the full case, in editable DOCX',
      'Bonus 2: 12 opening decisions, solved (39 pages)',
    ],
    ctaLabel: 'BUY THE GUIDE — $69',
    avatarAltPrefix: 'Professional',
  },

  pricing: {
    price: '$69',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    bonusTotalLabel:
      'Included in the price: the guide, the 8 Excel tools, both bonuses and the US · UK · Canada · Australia Equivalents Guide',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-1.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-2.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-3.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-4.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-5.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-pasteleria-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-pasteleria-4.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Chapters + 8 Excel Tools + 2 Bonuses',
    subtitle:
      'Decisions, not theory. Every chapter leans on one of the eight Excel tools in the pack, and its tables come from the cells of those files, not from made-up examples. A dated regulatory appendix closes the guide, so you know what was in force the day it was written and which dates we already know will move. Written by a chef and restaurant consultant who has been guiding openings since 2010.',
    // Títulos = los H2 de la guía EN (scripts/productos-digitales/guia-pasteleria-en/en/how-to-open-a-pastry-shop.md);
    // desc = qué se decide, sin cifras (regla de la ficha ES), sacado del índice de la guía EN.
    chapters: [
      { icon: 'Layers', num: '01', title: 'What Business Are You Opening: the Eleven Formats and Which One Is Yours', desc: 'The eleven bakery formats compared, from the home kitchen to a shop with its own production kitchen, what this pack includes and what is sold separately, the map from problem to chapter to tool, and the US · UK · Canada · Australia glossary.' },
      { icon: 'Users', num: '02', title: 'Your Customer and Your Market: Who Buys Pastry and When', desc: 'What US households spend on bakery products, how little of it reaches the specialty bakery, the competitor that really takes your sales and why a production kitchen should not try to compete on volume.' },
      { icon: 'CakeSlice', num: '03', title: 'The Opening Menu: Thirty Items and Why These', desc: 'How to choose an opening assortment with margin in mind, the role of each of the five families, how a handful of items carries most of the register, and why margin is not shared equally among them.' },
      { icon: 'Banknote', num: '04', title: 'What It Costs to Open: Real Startup Costs, Line by Line', desc: 'Why published figures contradict each other and what each one assumes, the three build-out scenarios, the sales tax line that is a cost in the US and throws off any budget, and the cash cushion as a line item.' },
      { icon: 'Layout', num: '05', title: 'The Space: Square Footage, Zones and the Site Visit Checklist', desc: 'The seven zones and the one-way workflow, the finishes and hand sinks the health department asks for, electrical service for the ovens, the hood\'s airflow, ceiling height and floor load.' },
      { icon: 'DoorOpen', num: '06', title: 'Before You Sign the Lease: the Chapter That Saves You Money', desc: 'The deal-breaker screen for the space, the hood duct to the roof and the landlord\'s written OK, the zoning and plan review questions to settle before you sign, and three doors: new build, taking over a bakery or a franchise.' },
      { icon: 'Snowflake', num: '07', title: 'Inside the Production Kitchen: Cold, Heat and Workflow', desc: 'Why pastry runs on freezing and not on the oven, what the blast chiller and the retarder-proofer do, why a chest freezer is not a blast chiller, and which piece of equipment sets the pace for everything else.' },
      { icon: 'Wrench', num: '08', title: 'Equipment: What to Buy, What to Lease and What Can Wait', desc: 'Price ranges by tier with brand and model, the sales tax that dealer list prices leave out, the ventless setup when you cannot vent, when used equipment pays and the lead times that move your opening date.' },
      { icon: 'ShieldCheck', num: '09', title: 'Permits, Health Department and Licenses: the Complete Path', desc: 'Why a retail bakery does not register with the FDA and when it has to, a central kitchen supplying your own shops, four example states and how to find your agency, and the cottage food route from home, state by state.' },
      { icon: 'ClipboardCheck', num: '10', title: 'Food Safety Plan, Allergens and Training: What to Have Ready on Inspection Day', desc: 'The food safety plan and its certified person in charge, food handler cards and the training log, kitchen allergens versus display-case allergens, and what it really takes to say "gluten-free."' },
      { icon: 'Truck', num: '11', title: 'Suppliers: Ingredients, Packaging and Lead Times', desc: 'The nine verified suppliers by category with their link, how to get three comparable quotes, what packaging weighs on your costs, and how to model butter and cocoa price swings instead of fixing a price that expires.' },
      { icon: 'Calculator', num: '12', title: 'Recipe Costing and Pricing: Why Labor Rules', desc: 'The batch as the costing unit, not the piece. The production kitchen\'s cost per hour charged to each piece, a single margin rule, the price per serving of a custom cake and the numbers that cure the fear of raising prices.' },
      { icon: 'UserCog', num: '13', title: 'Your Team: How Many, Which Roles and What They Cost', desc: 'The wage table by role, federal, state and city minimum wages next to what the market pays, the jump from gross pay to employer cost with payroll taxes, workers\' comp and benefits, and how hard it is to hire.' },
      { icon: 'Clock', num: '14', title: 'Early-Morning Shifts and Wage-and-Hour Law', desc: 'Records of hours worked, the overnight bake shift versus the counter shift and how they overlap at peak, workplace safety and the rules for minors, and the owner\'s hours as a life decision.' },
      { icon: 'CalendarRange', num: '15', title: 'The Six Peaks of the Year', desc: 'How much each campaign multiplies production with the same equipment, how much it weighs on the year, the capacity gap and the extra help it calls for, and how much cash the seasonal stock ties up.' },
      { icon: 'PartyPopper', num: '16', title: 'Custom Orders, First Communions and Graduations as a Business Line', desc: 'Winning orders and proving demand, deposits, the delivery calendar and cancellation risk, and which orders to accept and which to turn down while you still have no track record.' },
      { icon: 'Store', num: '17', title: 'Channels: Counter, Custom Orders, Wholesale and Shipping', desc: 'Cash at the counter versus wholesale invoices on credit terms, when selling to other businesses brings in FDA registration, what selling online and shipping still requires, and which products travel and which do not.' },
      { icon: 'TrendingUp', num: '18', title: 'The Financial Plan and the Cash You Need to Reach Break-Even', desc: 'A three-year P&L with monthly seasonality and a ramp-up, break-even with a single margin rule, the owner\'s pay as a line of its own and the honest profitability of the trade.' },
      { icon: 'Wallet', num: '19', title: 'Financing, Sales Tax, Packaging and Startup Cash', desc: 'Debt service and SBA loans, why sales tax follows how you sell and not what you sell, the packaging rules that change from state to state, what the food waste rules ask of a small shop and the startup cash cushion.' },
      { icon: 'Rocket', num: '20', title: 'Timeline, Opening Day and the First Ninety Days', desc: 'The critical path and your opening date, why you open outside a peak, your hours and sales mix as first-day business decisions, and what to measure in month zero and month three.' },
    ],
  },

  // Sin una sola venta en inglés y sin testimonios en el ES: la plantilla oculta la sección y, fuera del ES,
  // también la prueba social del hero.
  testimonials: {
    titleGold: '',
    subtitle: '',
    items: [],
  },

  why: {
    titlePre: 'Why This ',
    titleGold: 'Guide',
    reasons: [
      { icon: 'Shuffle', title: 'What You Decide Before You Open', desc: "Once you're open, your daily checklists and logs tell you what to do each day. This guide is everything you have to decide before: whether that space works, how much you really need, which permit applies to you and what you have to charge. The daily temperature, cleaning and allergen records are not here on purpose: they live in the HACCP Food Safety Kit Pro, and the guide sends you there by name." },
      { icon: 'FileSpreadsheet', title: 'Three Tools Built for a Production Kitchen', desc: "Kitchen capacity (how many pieces a day the equipment you're about to buy allows), takeover versus new build with the full cost over the years of the lease, and the economics of the six peaks: how much each one weighs on the year, what extra help it calls for and how much cash it ties up." },
      { icon: 'ShieldCheck', title: 'Every Legal Point With Its Source and Date', desc: 'No legal statement stands alone: every rule names its agency or code section, the permits workbook carries the source and link of each legal fact in a cell comment, checked in October 2026, and the regulatory appendix closes with the dates we already know will move. The frame is the US one, federal rules plus four example states, with notes for the UK, Canada and Australia.' },
      { icon: 'AlertTriangle', title: "And What This Guide Doesn't Do", desc: "It doesn't replace the plans and specifications your designer, architect or engineer prepares for plan review, or your city's own code. It doesn't promise that your city will say yes, and it doesn't promise customers. What it does is get you to every meeting knowing what to ask for, what to ask and what it's likely to cost, and keep you from signing a lease too early." },
    ],
  },

  author: {
    bio: 'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010. He has advised on the opening of more than 200 venues, including Michelin-starred restaurants and Repsol Sun winners in Spain and Europe.',
    badge3: '200+ openings',
  },

  bonus: {
    subtitle:
      'On top of the PDF + DOCX guide, you get 8 Excel tools with live formulas, two bonuses (the sample business plan and the 12 opening decisions) and the US · UK · Canada · Australia Equivalents Guide',
    // layout 'single': una rejilla de 3 columnas para las 11 tarjetas (mismo criterio que la ficha ES).
    layout: 'single',
    items: [
      { icon: 'FileSpreadsheet', label: 'TOOL 1', title: 'Kitchen Capacity and Site Visit Checklist', value: 'Included in the pack', desc: "Zones and square feet, capacity by equipment, the bottleneck and a site visit checklist of 18 checks, 8 of them deal-breakers, starting with the hood duct to the roof. Decide whether that space works and how many pieces a day the equipment you're about to buy can handle.", image: '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg' },
      { icon: 'Banknote', label: 'TOOL 2', title: 'Startup Cost Calculator', value: 'Included in the pack', desc: 'Startup costs by block, the format variant, takeover versus new build, sales tax and the cash you need on opening day. Decide how much you really need and whether taking over a bakery beats building new.', image: '/lovable-uploads/ai-gallery/guia-pasteleria-3.jpg' },
      { icon: 'CalendarRange', label: 'TOOL 3', title: 'Seasonal Peaks Planner', value: 'Included in the pack', desc: "The calendar of six peaks, each one's share of the year, peak capacity versus demand, and extra staff and cash. Decide whether your kitchen can handle each campaign and how much money it ties up before you sell it.", image: '/lovable-uploads/ai-gallery/guia-pasteleria-4.jpg' },
      { icon: 'Calculator', label: 'TOOL 4', title: 'Opening Menu and Recipe Costing', value: 'Included in the pack', desc: "Batch costing for 30 items, the production kitchen's labor cost per hour, the egg and TCS decision, mix and average ticket, and the menu decision. Decide what you sell, at what price and at what holding temperature.", image: '/lovable-uploads/ai-gallery/guia-pasteleria-1.jpg' },
      { icon: 'TrendingUp', label: 'TOOL 5', title: '3-Year Financial Plan', value: 'Included in the pack', desc: 'Assumptions, startup investment, 3-year P&L, break-even, scenarios, staff, 12-month cash flow, financing and break-even by channel. Decide whether the business holds up and when it reaches break-even.', image: '/lovable-uploads/ai-gallery/guia-pasteleria-5.jpg' },
      { icon: 'ClipboardCheck', label: 'TOOL 6', title: 'Permits and Licenses Checklist', value: 'Included in the pack', desc: 'Thirty steps in six phases with a progress counter, "Which Permit Do I Need," selling wholesale, the cottage food route, a training log, and a timeline with the critical path. Decide which permits apply to you, in what order and when you open.', image: '/lovable-uploads/ai-gallery/guia-pasteleria-3.jpg' },
      { icon: 'Wrench', label: 'TOOL 7', title: 'Equipment and Suppliers Checklist', value: 'Included in the pack', desc: 'Equipment with a price range, sales tax and lead time; the format variant; nine suppliers verified with their link; and a progress counter. Decide what you buy, from whom, at what negotiated price and with what lead time.', image: '/lovable-uploads/ai-gallery/guia-pasteleria-2.jpg' },
      { icon: 'Users', label: 'TOOL 8', title: 'Staff Schedule and Labor Cost', value: 'Included in the pack', desc: "The wage table and payroll settings, the weekly schedule, hours and cost, and the hiring plan. Decide how many people you need, in which roles, and what they really cost with payroll taxes, workers' comp and benefits included.", image: '/lovable-uploads/ai-gallery/guia-pasteleria-4.jpg' },
      { icon: 'ScrollText', label: 'BONUS 1', title: 'Sample Business Plan for a Pastry Shop', value: 'Included in the pack', desc: "The full case in the format a bank or an SBA lender expects to read: executive summary, market and location, concept and menu, operations plan, three-year financial plan, and risks and scenarios. In editable DOCX, with every figure about the case taken from the pack's Excel tools.", image: '/lovable-uploads/ai-gallery/guia-pasteleria-5.jpg' },
      { icon: 'GraduationCap', label: 'BONUS 2', title: '12 Opening Decisions, Solved', value: 'Included in the pack', desc: 'Twelve real decisions with their context, the options, the criterion, the cell in the pack that settles it and the rule that applies when there is one: a shop with its own kitchen or a separate one, buy the blast chiller or wait, open with twenty items or forty, start legally from home, or sign your first wholesale account. In PDF and editable DOCX (39 pages).', image: '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg' },
      { icon: 'Globe', label: 'INTERNATIONAL BONUS', title: 'US · UK · Canada · Australia Equivalents Guide', value: 'Included in the pack', desc: 'Terms, taxes, food safety, staff rules, alcohol and units for using this guide in the US, UK, Canada and Australia.', image: '/lovable-uploads/ai-gallery/en-equivalents-guide.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE GUIDE — $69',
  },

  guarantee: {
    text: "If the guide doesn't help you decide your space, your numbers and your permits with confidence, we'll refund 100% of your money. No questions, no hassle. You have 30 days to decide.",
  },

  faqs: FAQS,

  cta: {
    heading: 'Decide Before You Sign, Not After',
    subtitle: "The order of the decisions, the tools that run your numbers and the documents you'll be asked for. Everything you need to settle before you open.",
    items: [
      'Complete guide in PDF + DOCX: 20 chapters and a dated US regulatory appendix (113 pages)',
      '8 Excel tools with live formulas and every assumption in an editable cell',
      'Kitchen capacity and site visit checklist: whether that space works and how many pieces a day it can handle',
      'Startup costs by scenario, with taking over a bakery versus building new',
      'Which permit you need in three questions, from cottage food to a retail food permit, with a timeline and critical path',
      '30-item opening menu with labor charged to each piece, and a 3-year financial plan',
      'Bonuses: a filled-in sample business plan and 12 opening decisions, solved (39 pages)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE GUIDE — $69',
  },

  stickyLabel: 'HOW TO OPEN A PASTRY SHOP — $69',

  // D17/D19: enlaces recíprocos con Bakery Business Plan, Food Cost Kit Pro, HACCP Kit y Food Cost Guide (los
  // cuatro enlazan de vuelta a esta guía desde sus propios footerLinks).
  footerLinks: [
    { label: 'aichef.pro', href: '/en' },
    { label: 'Digital Products', href: '/en/digital-products' },
    { label: 'Bakery Business Plan Kit', href: '/en/digital-products/bakery-business-plan' },
    { label: 'Food Cost Kit Pro', href: '/en/digital-products/food-cost-templates' },
    { label: 'HACCP Food Safety Kit Pro', href: '/en/digital-products/haccp-templates' },
    { label: 'Food Cost + Menu Engineering Guide', href: '/en/digital-products/food-cost-menu-engineering-guide' },
    { label: 'Contact', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Version 1.0 · October 2026',

  alreadyBought: {
    product: 'how-to-open-a-pastry-shop',
    label: 'Already bought the guide? Get back into your dashboard',
  },

  schema: {
    productName: 'How to Open a Pastry Shop',
    productDescription:
      'A 20-chapter opening playbook for a pastry shop with its own production kitchen in the US, with a dated regulatory appendix: choosing the space, startup costs, equipment, permits by state and the cottage food route, the opening menu with labor costed in, the team and wage-and-hour rules, the six peaks of the year and a 3-year financial plan. Includes 8 Excel tools with live formulas, a filled-in sample business plan and 12 opening decisions, solved.',
    price: '69.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro/en' },
      { name: 'Digital Products', item: 'https://aichef.pro/en/digital-products' },
      { name: 'How to Open a Pastry Shop', item: 'https://aichef.pro/en/digital-products/how-to-open-a-pastry-shop' },
    ],
  },
};

export default data;
