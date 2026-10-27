// astro-site/src/data/productos-en/planes/catering-business-plan.ts
// TIENDA INTERNACIONAL EN — Catering Business Plan Kit. DUPLICADO de food-truck-business-plan.ts (gemelo estructural:
// mismo tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos) con el copy
// del catering. Edición inglesa del ES astro-site/src/data/productos/planes/plan-catering-tematico-eventos.ts (hreflang
// recíproco), cuyo contenido NO se traduce: el EN es otro concepto (SPEC D69).
// SPEC: scripts/productos-digitales/business-plans-en-4/SPEC-delta.md (D66-D80) + las heredadas business-plans-en-3
//   (D48-D65), business-plans-en-2 (D30-D47) y business-plans-en/SPEC.md (D1-D29), que mandan en lo demás.
//   · D66/D66b: slug `catering-business-plan`, nombre «Catering Business Plan Kit», H1 Forma B `Catering ` + oro
//     `Business Plan` + «Template for an Event Catering Company: …»; title y keywords de D66b. Keyword principal
//     «catering business plan» (880/mes US, subiendo; research §2).
//   · D67: $39 SIN anclas (sin priceOld, «-70%», «Total value», «Save $», «launch price» ni valor de los bonos), como
//     las otras 11 landings EN.
//   · D68: los 4 ficheros de dl/catering-business-plan/ (plan Word, proyecciones Excel, calculadora de precios y
//     checklist), dashboard CateringBusinessPlanDashboard.tsx y get-download-urls.ts.
//   · Bonos sin precio y SOLO lo que existe en los ficheros: 1 = §9 del plan + fase 2 del checklist («Kitchen, Van &
//     Permits»); 2 = tabla «US CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» de Instructions!A53:C68 + los 5
//     umbrales del P&L. Sin aggregateRating ni review.
//   · Cifras del caso US: SOLO de scripts/productos-digitales/business-plans-en-4/cifras_caso.json (caché del xlsx EN
//     calibrado en la F2, F2-NOTAS §8): 180 eventos × 60 invitados × $60.00 → $648,000; inversión $185,453 = $107,200 +
//     $78,253; $40,000 + préstamo $146,000; margen bruto 60.6 %; neto $48,466 (7.5 %); equilibrio 151 eventos/año frente
//     a 180 previstos (sin vender la «holgura 20 %»: REVISION-FINAL); DSCR mín 2.60×; 11 personas, 4 puestos; furgoneta
//     $32,000 + frío $9,000; seguros $6,000. $60 por invitado = SIN sales tax y CON el servicio incluido. Los 3
//     presupuestos de ejemplo salen de la hoja «3 Example Quotes» de la calculadora (Kit estimates). Ninguna cifra del ES.
//     Conteos del producto: 10 secciones, más de 6,000 palabras, 9 hojas, más de 700 fórmulas, 68 tareas en 6 fases;
//     umbrales del P&L tal como están en el libro (margen bruto ≥ 60 %, F2-NOTAS §4.2; no el 62 % de D75).
//   · FAQ: People Also Ask de research §3 (qué incluye, cuánto cuesta empezar, ¿desde casa? → NO, cuánto cobrar por
//     invitado, ¿40 invitados?, licencias, seguros, service charge vs gratuity, alcohol, ¿es rentable?, tipos de
//     catering) + concepto, food truck / restaurante, prestamista, cambiar cifras, UK, moneda, suscripción, licencia de
//     uso y garantía. Fuentes legales y de mercado de research §4-§6 (las mismas que cita el docx). schema.faqs = el
//     MISMO array.
//   · Revisión final de los entregables (orquestador): catering desde casa = «en la mayoría de estados, no» (instalación
//     con permiso o comisaria con acuerdo escrito; cottage food no cubre catering), sin atribuirlo a un condado; el
//     service charge no es propina y lo que se reparte al personal es salario (Rev. Rul. 2012-18); sin «plan review solo
//     si alquilas cocina propia»; el pesimista NO baja el coste de personal.
//   · Testimonios (D26, como el Bar): los 8 del ES traducidos con el subtítulo de la edición española y SIN ningún dato
//     que no sea verdad en este kit: fuera «hacer sushi en mi casa» (catering desde casa: no), «96 proveedores»,
//     «guía de especialización», «dossier B2B y contratos MSA», «factor multi-concepto» y todas las cifras (€/pax,
//     márgenes, 3x, 65 %). Se conservan las experiencias personales sin cifras.
//   · Imágenes: fotos sin texto del Kit de Tareas Catering (tareas-catering-*, 1376 px) + la de estaciones temáticas
//     del ES con rótulos EN (plan-catering-tematico-eventos-hero). Fuera las del ES con rótulos en español
//     («TAQUERÍA EL PASTOR», «CEVICHE PERUANO»). OG = recorte 1200×630 de tareas-catering-hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_CATERING_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env var
// el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What should a catering business plan include?',
    a: 'The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a full-service event caterer, plus the Excel financial projections that back them up, a pricing calculator that turns your cost per guest into a quote, and a 68-task startup checklist.',
  },
  {
    q: 'Is it a generic template or built for catering?',
    a: "Built for a full-service, off-site event caterer: food produced in a shared commissary kitchen, one used refrigerated cargo van, corporate events during the week (drop-off lunches, buffets, receptions, year-end parties) and private events on weekends (weddings, rehearsal dinners, private parties). Five service styles — drop-off, buffet, family-style, plated and chef-attended stations such as a taco bar, a carving station or a pasta station — event staff on W-2 payroll, and no alcohol license of its own: the client buys the alcohol and certified bartenders serve it. Nothing to strip out from a restaurant template.",
  },
  {
    q: 'How much does it cost to start a catering business?',
    a: "It depends mostly on the kitchen. Restroworks puts a catering start-up working from a shared kitchen at $20,000 to $65,000, and one with its own kitchen, vehicles and staff at $250,000 or more. The kit's example sits in between: no kitchen of its own, but a used refrigerated van, its own equipment and a cash reserve, for $185,453 in total cash ($107,200 in startup costs plus $78,253 of working capital). The Startup Costs sheet lists every line — the van, its upfit and its refrigeration unit, kitchen and refrigeration equipment, portable cooking and power, commissary storage, LLC and legal, first-year permits, catering software, smallwares, opening inventory, website and launch, chafing dishes, insulated carriers and serving ware — plus the commissary deposit, rent before opening, a contingency and working capital. Replace each line with your own quotes.",
  },
  {
    q: 'Can I start a catering business from home?',
    a: "In most states, no. Food you cater has to be prepared in an approved, permitted food facility: a licensed commercial kitchen of your own, or a commissary kitchen you use under a written agreement. Cottage food laws, which let you sell certain shelf-stable foods made at home, don't cover catering. That's why this plan rents time in a shared commissary kitchen, and why a signed commissary agreement comes before the catering permit in the checklist. Rules vary by state and county, so check with your local health department before you spend.",
  },
  {
    q: 'How much should I charge per person for catering?',
    a: "Start from your costs, not from a competitor's menu. The pricing calculator adds food cost per guest, a non-alcoholic beverage package, disposables, event staff (people × hours × wage, plus payroll taxes), rentals and mileage, divides by (1 − your target margin), rounds up to the next 50 cents, and then adds the service charge, the sales tax and the deposit — and shows the gross margin the quote really leaves. As a reference, couples spent an average of $80 per plate on wedding catering in 2024, according to The Knot 2025 Real Weddings Study (reported by Fox Business), while a corporate drop-off lunch costs much less per guest. The calculator's price per guest excludes the service charge; in the financial model, the example caterer averages $60.00 per guest excluding sales tax and with service included (staff and the service charge you keep).",
  },
  {
    q: 'How much does it cost to cater for 40 guests?',
    a: "It depends on the style of service. In the calculator's first example quote, a corporate drop-off lunch for 40 guests comes to $30.50 per guest: a $1,220 subtotal and $1,317.60 with an 8% example sales tax, with no service charge because no one stays to serve. Add servers, a buffet setup or plated service and the price per guest rises with the staff hours and the rentals: the wedding buffet example for 120 guests comes to $106.50 per guest before the service charge and tax. Both are kit estimates for illustration: type your own costs and the calculator gives you your number.",
  },
  {
    q: 'What licenses and permits do I need for a catering business?',
    a: "It depends on your state, county and city, but most caterers need: a business structure (LLC or another) and an EIN from the IRS; a seller's permit for sales tax; a city or county business license; a written agreement with a permitted commissary kitchen; a catering or food facility permit from the county health department, with an inspection of the kitchen and the van; temporary food event permits for community or public events; the fire marshal's approval for open flame, chafing fuel or tents where required; DMV registration and commercial auto insurance for the van; and a Certified Food Protection Manager plus food handler cards for the team. The startup checklist organizes 68 tasks in 6 phases. Treat it as a starting point and confirm the details with your local authorities.",
  },
  {
    q: 'What insurance do caterers need?',
    a: "Usually general liability (venues often ask for a certificate of insurance and to be named as an additional insured), commercial auto for the van, workers' compensation once you hire, and liquor liability if your staff serve alcohol. Insureon puts the typical monthly cost for a small caterer at about $45 for general liability, $96 for a business owner's policy, $82 for workers' comp, $204 for commercial auto and $28 for liquor liability. The workbook budgets $6,000 a year for insurance in the example; ask an agent who knows caterers for your own quotes.",
  },
  {
    q: "What's the difference between a service charge and a gratuity?",
    a: "A service charge is part of your price: the client has to pay it and you set the amount, so under IRS Revenue Ruling 2012-18 it isn't a tip, and whatever part of it you pay out to your staff counts as wages. A gratuity is voluntary: the client decides whether to leave one and how much. Sales tax on the service charge depends on the state: in California a mandatory service charge is taxable; in New York it isn't taxable only when it's separately stated, identified as a gratuity and paid in full to the staff; in Texas it isn't taxable up to 20% when it's separately stated, identified as a gratuity and paid to qualified employees (servers and bartenders, not chefs), and over 20% all of it is taxable. The calculator keeps them on separate lines, has a switch for whether your state taxes the service charge, and leaves the voluntary gratuity out of the price.",
  },
  {
    q: 'Can a caterer serve alcohol?',
    a: "Serving it and selling it are different things. To sell alcohol, a caterer usually needs an on-premises license plus a caterer's permit — for example the Caterer's Permit in Texas or the Type 58 license in California — often with an authorization for each event. The common model, and the one in this kit, is simpler: the client buys the alcohol, and bartenders certified in your state (through TIPS, ServSafe Alcohol or TABC, for example) serve it under your liquor liability insurance. The checklist includes both the certification and the coverage. Check your state's rules and the venue's before you offer it.",
  },
  {
    q: 'Does it work for a mobile bar?',
    a: "It's built for a caterer that serves food, with alcohol only through the client and certified bartenders. If you're starting a mobile bar instead — a bar trailer or a portable bar, bartenders, mixers, garnish and ice, with the host buying the alcohol (dry hire) — our Mobile Bar Business Plan Kit is written for that: a storage unit with trailer parking instead of a commissary kitchen, W-2 event bartenders and barbacks, the dry hire rules state by state and a pricing calculator that turns your cost per guest into a quote and a shopping list for the host.",
  },
  {
    q: 'Is there a plan for a BBQ caterer?',
    a: "Yes. If smoked meats are your product, our BBQ Catering Business Plan Kit is written for that: a pitmaster who smokes brisket, pulled pork and ribs at a commissary and holds them hot for a staffed buffet with a carving station, a smoker trailer at the event as a paid live pit on site, the fire marshal and the Food Code temperatures for smoked meats, and a pricing calculator that turns pounds of meat per guest into a quote, with a smoke schedule and a shopping list by guest count.",
  },
  {
    q: 'Is there a plan for a paella caterer?',
    a: "Yes. If paella cooked live in front of the guests is your product, our Paella Catering Business Plan Kit is written for that: a paella chef with paella pans and 3-ring propane burners, sofrito, stock and seafood prepped at a commissary, what your county and your fire marshal say about cooking at the event, cooked rice as a TCS food, and a pricing calculator that turns your guest count into pans, rice and a price per guest, with a pan sizing table and a shopping list by guest count.",
  },
  {
    q: 'Is there a business plan for a wedding venue?',
    a: "Yes, but for the business that owns the space, not for the caterer. Our Wedding Venue Business Plan Kit covers a wedding and event venue on a leased barn or estate that earns a venue rental fee plus a commission from its exclusive caterer: a 10-section Word plan, Excel projections with a break-even in events and a 12-month cash flow, a pricing and quote calculator by season and day, venue rental agreement templates, and an 84-task startup checklist with the zoning and permit steps to check with your county. If you want to be that exclusive caterer, or to cater anywhere, this kit is the one for you."
  },
  {
    q: 'How much does a catering business make? Is catering profitable?',
    a: "It can be, but margins are thin: ItsaCheckmate reports an average net margin of 7-8% for caterers, and Galley Solutions puts food cost at 28-35% of the menu price. In the kit's example — 180 events a year with 60 guests at $60.00 per guest (excl. sales tax, service included) — year-1 sales are $648,000 and net income is $48,466, a 7.5% net margin, after paying the owner a salary as executive chef. That's an example, not a promise: the 3-year P&L recalculates from your numbers, checks five ratios against editable kit benchmarks, and the pessimistic scenario shows what a weak year does to your cash.",
  },
  {
    q: 'What are the main types of catering?',
    a: "By client, catering splits into corporate events (drop-off and boxed lunches, buffets, receptions and year-end parties, mostly booked during the week) and social or private events (weddings, rehearsal dinners, birthdays and celebrations of life, mostly on weekends). By service, the kit works with five styles: drop-off, buffet, family-style, plated and chef-attended stations. The plan is written for a caterer that serves both markets; the workbook averages them into events per year, price per guest and guests per event, and the calculator prices each style.",
  },
  {
    q: 'Does it work for a food truck or a restaurant that caters?',
    a: "It's built for a caterer with no storefront. If you're opening a food truck that also works events, our Food Truck Business Plan Kit fits better; if catering is a side line of a restaurant, start from the Restaurant Business Plan Kit. The Excel workbook will still take any numbers you type — events, price per guest, guests per event — but the written plan describes an off-site event caterer, so you'd rewrite more of the text.",
  },
  {
    q: 'Can I present this plan to a lender or investors?',
    a: "Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The loan schedule and the DSCR cover your main loan (bank or SBA 7(a)), the one you enter in the assumptions; the financing sheet also lists an SBA Microloan (up to $50,000, through nonprofit intermediaries), investors or partners and local grants as sources of funds, without amortizing them. In the example, the owner puts in $40,000 and borrows $146,000, with a minimum DSCR of 2.60×. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.",
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: "Yes. The green cells are the ones you type — events per year, price per guest, guests per event, food cost, the corporate marketplace share, commissary rent, wages and any startup cost line — and more than 700 linked formulas recalculate the rest. Client deposits aren't modeled, which keeps the cash flow on the cautious side. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook and the calculator each include an Instructions tab.",
  },
  {
    q: "Does it work in the UK, Canada or Australia?",
    a: "Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. In the UK, event catering pays 20% VAT, and the notes cover council registration 28 days before trading and Temporary Event Notices for alcohol. In Canada, event liquor permits are provincial and servers need Smart Serve, Serving It Right or the local equivalent; in Australia, check your state liquor rules and RSA. The pricing calculator counts miles: type kilometres and your cost per km instead of the IRS rate. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
  },
  {
    q: 'What currency will I pay in?',
    a: 'The price is $39 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The files have no currency symbol: you type amounts in your own currency.',
  },
  {
    q: 'Is it a subscription? Are future updates included?',
    a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we improve the plan or the workbooks, you get the new version at no extra cost — just download the files again.',
  },
  {
    q: 'Can I use it with my clients or for more than one business?',
    a: "One purchase covers one business, however many events it caters. If you're a consultant or an investor, you can use the files with the projects you advise, but you can't hand them copies: each business buys its own.",
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the plan doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: PlanNegocioData = {
  slug: 'catering-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_CATERING_BUSINESS_PLAN',

  seo: {
    title: 'Catering Business Plan Template: Word + Excel Financial Projections + Pricing Calculator | AI Chef Pro',
    description:
      'Catering business plan template for an event catering company: a 10-section Word plan, Excel financial projections (3-year P&L, break-even, cash flow, loan and DSCR), a per-guest pricing calculator and a 68-task startup checklist. $39.',
    keywords:
      'catering business plan, catering business plan template, how to start a catering business, catering startup costs, catering pricing per person, catering pricing calculator, catering license, catering financial projections, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-catering-business-plan.jpg',
  },

  schema: {
    productName: 'Catering Business Plan Kit',
    productDescription:
      'Catering business plan template kit for a full-service event catering company: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a pricing calculator from cost per guest to quote, and a 68-task startup checklist in 6 phases. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Catering Business Plan Kit',
  },

  images: {
    // hero bg (6) — fotos sin texto del Kit de Tareas Catering + las estaciones temáticas del ES (rótulos en inglés).
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-transporte.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-cocina.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el ES.
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-catering-cocina.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-transporte.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-catering-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready catering business plan: Word + Excel + pricing calculator',
    titlePre: 'Catering ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for an Event Catering Company: Word Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist',
    description:
      'Everything you need to plan, price and pitch an event catering company that works from a shared commissary kitchen: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in events per year, 12-month cash flow and loan payments from your own numbers; a pricing calculator that turns your cost per guest into a quote; and a 68-task checklist that takes you from your LLC and your commissary agreement to your first 90 days of events. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section catering business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even and 12-month cash flow',
      'Pricing calculator: cost per guest, service charge, sales tax and deposit',
      'Startup checklist: 68 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      '9 building blocks to test whether your catering company works on paper before you buy a van, price every event and present the plan to a lender or an investor.',
    templates: [
      { icon: 'FileText', title: 'Catering Business Plan (Word, 10 Sections)', desc: 'A complete plan of more than 6,000 words already written for a full-service event caterer working from a shared commissary kitchen: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan (The Knot, WeddingWire, ezCater and direct sales to companies), operations plan (the six phases of an event and food safety in transport), management and staffing, financial plan, legal requirements, permits and licenses, and conclusions with an action plan. Its figures are the ones in the example Excel model.' },
      { icon: 'FileSpreadsheet', title: 'Catering Financial Projections (Excel, 9 Sheets)', desc: 'Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than 700 linked formulas: change events per year, price per guest or guests per event and the whole workbook recalculates.' },
      { icon: 'Calculator', title: 'Catering Pricing Calculator (Cost per Guest to Quote)', desc: 'Guests and guest minimum, service style, food cost per guest, a non-alcoholic beverage package, disposables, event staff hours and wages with payroll taxes, rentals and mileage, your target margin, service charge, sales tax and deposit. Out come the price per guest, the total to quote, the deposit, the balance and the gross margin the quote really leaves. The voluntary gratuity stays off the price, and a switch tells it whether your state taxes the service charge. Three example quotes included.' },
      { icon: 'Coins', title: 'Startup Costs Line by Line', desc: 'A used refrigerated cargo van, its upfit and its refrigeration unit, kitchen and refrigeration equipment, portable cooking and power, commissary storage, LLC and legal, first-year permits, catering software and card reader, smallwares and hotel pans, opening inventory, website and launch, chafing dishes, insulated carriers and serving ware, each with a reference price you replace with your quotes, plus the commissary deposit, rent before opening, a contingency and working capital. The total cash you need is calculated separately.' },
      { icon: 'TrendingUp', title: 'Break-Even in Events per Year', desc: 'How many events a year you need at your price per guest (excl. sales tax) and guest count to cover every cost, and the cash break-even with loan payments in and depreciation out. Your cushion above it, a sensitivity table for price per guest and variable cost per guest, and a plain-English reading of the result.' },
      { icon: 'BarChart3', title: 'Financial Scenarios', desc: 'Three scenarios side by side — pessimistic, base and optimistic — moving events per year, price per guest and guests per event, each with its own estimated cash balance. Useful for a lender or an investor.' },
      { icon: 'Users', title: 'Staffing & Event Labor (4 Roles)', desc: 'Owner / executive chef and sales, sous chef, a pool of hourly event staff (servers, bartenders, attendants) on W-2 payroll and a prep cook who drives the van, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the event hours you need (hours per event × people per event × events) against the hours you hire, and flags any pay below the minimum wage for the hours worked.' },
      { icon: 'ShieldCheck', title: 'Startup Checklist (68 Tasks, 6 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license, your catering contract and a HACCP-based food safety plan), kitchen, van and permits (commissary agreement, county catering permit, temporary event permits, fire marshal, commercial auto, liquor liability if you serve the client's alcohol), equipment, staff (W-2 event staff, food handler cards, alcohol server certification), marketing (The Knot, WeddingWire, ezCater, venues and planners) and your first 90 days." },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25× target, plus an SBA Microloan, investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Catering Temático, la edición española. Sin
  // ningún dato que no sea verdad en este kit (ver cabecera). Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Caterers who planned or grew their event business with the Spanish edition of this plan',
    items: [
      { name: 'Yuki Tanaka', role: 'Sushi chef for premium events, Madrid, Spain', text: 'The plan gave me the structure to grow from a single sushi station to several live stations at multicultural weddings, and to price each one per guest instead of guessing.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Miguel Hernández', role: 'Taco showcooking chef, Madrid, Spain', text: 'I started with tacos al pastor at family birthdays. After the plan I added more stations, and now I cater corporate brand events. Growing one step at a time was the key.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Giuseppe Romano', role: 'Mobile pizzaiolo and event caterer, Toledo, Spain', text: 'I had a mobile wood-fired oven and catered weddings with pizza only. The plan showed me how to build a full menu around it — fresh pasta, antipasti, desserts — and my volume grew.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Diego Ferreyra', role: 'Argentine grill caterer, Madrid, Spain', text: 'The financial plan convinced me to add a second concept to my Argentine asado. Now I cover weddings and outdoor corporate events with two strong concepts.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Carolina Vega', role: 'Peruvian ceviche chef, Barcelona, Spain', text: 'The pricing calculator saved me months of trial and error. I put a quote together in minutes, and I know my real margin before I send it.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Rajesh Patel', role: 'Tandoor chef for weddings and embassies, Madrid, Spain', text: 'I offer a mobile tandoor for multicultural weddings and embassy receptions. The plan made me put numbers on every event before quoting the big ones.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Carmen Soler', role: 'Plant-based caterer, Madrid, Spain', text: 'Plant-based catering is growing fast with companies. The plan helped me position it as a premium service, not a low-cost alternative, and corporate brand events are now most of my revenue.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sam Williams', role: 'Texas BBQ pitmaster, Madrid, Spain', text: 'Slow-smoked BBQ is a niche in Spain. The plan helped me approach companies with a clear offer, and I now cater regularly for two corporate clients.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a catering plan written for the format lenders expect, with a financial model and a pricing calculator that recalculate from your own numbers.',
    reasons: [
      { icon: 'ConciergeBell', title: 'Built for an Event Caterer', desc: "A shared commissary kitchen instead of a lease, one refrigerated van, five service styles from drop-off to plated, chef-attended stations, event staff on W-2 payroll, and the permits of a caterer: a commissary agreement before the catering permit, temporary event permits, alcohol only through the client and certified bartenders. Nothing to strip out from a restaurant template." },
      { icon: 'Calculator', title: 'A Price for Every Quote', desc: 'The pricing calculator turns food cost per guest, staff hours, rentals and mileage into a price per guest, then adds the service charge, the sales tax and the deposit, and shows the gross margin it leaves. Three example quotes show how: a corporate drop-off lunch, a wedding buffet and a plated dinner.' },
      { icon: 'BarChart3', title: 'Numbers Calculated, Not Copied', desc: 'Events per year, price per guest and guests per event drive the whole workbook. The example caterer: 180 events a year with 60 guests at $60.00 per guest (excl. sales tax, service included), $648,000 in year-1 sales, a 60.6% gross margin, and 151 events a year to break even against the 180 planned. Replace them with yours.' },
      { icon: 'Banknote', title: 'Lender-Ready Format', desc: 'Written plan, 3-year P&L, break-even, 3 scenarios, cash flow and a loan schedule with DSCR for your main loan (bank or SBA 7(a)), with SBA Microloans and grants as other sources. Approval is never guaranteed, and it is a planning tool, not financial advice. One-time payment, no subscription.' },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised chefs and entrepreneurs launching catering services for events, combining hands-on operations with financial planning.',
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      'Besides the business plan, the financial model, the pricing calculator and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Catering Permits & Licenses Guide (US + UK Notes)',
        desc: "Section 9 of the plan plus Phase 2 of the checklist: why catering needs a permitted kitchen and not your home kitchen, how the commissary agreement, the county catering permit and temporary event permits fit together, when the fire marshal gets involved, how alcohol works without a license of your own, sales tax on the whole invoice and on the service charge, W-2 event staff and the insurance venues ask for — with notes for the UK. No state forms included: requirements vary by state, county and city.",
        image: '/lovable-uploads/ai-gallery/tareas-catering-transporte.jpg',
      },
      {
        icon: 'BarChart3',
        label: 'BONUS 2',
        title: 'US Catering Benchmarks (Sourced)',
        desc: 'The reference table inside the workbook: food cost, gross margin, labor, net margin, price per guest for weddings and corporate lunches, marketplace commission, deposits, hourly wages, shared kitchen rates, startup investment, insurance and event staff ratios, each with its source or marked "kit estimate" when there isn\'t one — plus five OK / REVIEW checks on your P&L against editable thresholds.',
        image: '/lovable-uploads/ai-gallery/tareas-catering-equipo.jpg',
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
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  guarantee: {
    text:
      "If the business plan doesn't live up to your expectations, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  faqs: FAQS,

  cta: {
    headingPre: "It's Time to Launch Your ",
    headingGold: 'Catering Business',
    subtitle:
      'Plan it before you buy the van: the written plan, the numbers behind it, a price for every quote and the permits list, for a one-time payment.',
    items: [
      '10-section catering business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in events per year, with a sensitivity table',
      'Pricing calculator: from cost per guest to a quote',
      'Startup checklist: 68 tasks in 6 phases',
      'BONUS: Catering Permits & Licenses Guide (included in the plan)',
      'BONUS: US Catering Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'CATERING BUSINESS PLAN — $39',

  // Salientes: el gemelo más cercano (Food Truck), Food Cost (coste por invitado), HACCP (transporte en caliente y
  // frío), Staff Scheduling (personal de eventos), Financial Plan + los otros planes EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/mobile-bar-business-plan', label: 'Mobile Bar Business Plan Kit' },
    { href: '/en/digital-products/bbq-catering-business-plan', label: 'BBQ Catering Business Plan Kit' },
    { href: '/en/digital-products/paella-catering-business-plan', label: 'Paella Catering Business Plan Kit' },
    { href: '/en/digital-products/pizza-shop-business-plan', label: 'Pizza Shop Business Plan Kit' },
    { href: '/en/digital-products/ice-cream-shop-business-plan', label: 'Ice Cream Shop Business Plan Kit' },
    { href: '/en/digital-products/wedding-venue-business-plan', label: 'Wedding Venue Business Plan Kit' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'catering-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
