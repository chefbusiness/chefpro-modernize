// astro-site/src/data/productos-en/planes/mobile-bar-business-plan.ts
// TIENDA INTERNACIONAL EN — Mobile Bar Business Plan Kit. DUPLICADO de catering-business-plan.ts (gemelo estructural y
// motor de eventos: mismo tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de
// campos) con el copy del bar móvil. Edición inglesa del ES astro-site/src/data/productos/planes/plan-negocio-cocteleria-
// eventos.ts (hreflang recíproco), cuyo contenido y cifras NO se reutilizan: el EN es otro concepto (SPEC D84).
// SPEC: scripts/productos-digitales/business-plans-en-5/SPEC-delta.md (§0 jerga, D81-D95) + las heredadas
//   business-plans-en-4 (D66-D80), -3 (D48-D65), -2 (D30-D47) y business-plans-en/SPEC.md (D1-D29).
//   · §0 / D81b: jerga US en las 3 capas (research §9). Title con el NOMBRE DEL PRODUCTO primero y la keyword detrás;
//     H1 Forma B `Mobile Bar ` + oro `Business Plan` + «Template for a Dry-Hire Mobile Bartending Company: …»; meta,
//     FAQ en la redacción del comprador (las 8 de research §9) y keywords de research §9. «dry hire» lleva su glosa
//     en la primera mención del cuerpo (hero.description) DESDE EL PUNTO DE VISTA DEL EMPRENDEDOR, que es quien lee
//     la landing: «(your client buys the alcohol; you bring the bar, the bartenders and everything else)»; la del
//     research §9 («you supply… we bring…») es la que el operador dice a su cliente (corrección de la revisión final,
//     13-oct). Sin «agente del cliente» que compra el alcohol ni gratuity pactada como vía segura (MO 24-01: tips,
//     gratuities y donativos pueden ser venta). «mobile bar» = el negocio; «portable bar» = el mueble;
//     «signature cocktails»; «W-2 event bartenders»; «cash bar» solo para decir que no cabe en dry hire.
//     Los 6 H2 de research §9 NO caben como H2: los de esta plantilla son constantes del diccionario (UI_PLAN) salvo
//     el del CTA final. Sus keywords van en las tarjetas (H3), en las razones (H3), en el bono 1 y en la FAQ.
//   · D82: $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $», «launch price» ni valor de los bonos).
//   · D83: los 4 ficheros de dl/mobile-bar-business-plan/, dashboard MobileBarBusinessPlanDashboard.tsx y
//     get-download-urls.ts (mismas claves que el ES y que el catering).
//   · Bonos sin precio y SOLO lo que existe en los ficheros: 1 = §9 del plan + fase 2 del checklist («Trailer &
//     Permits»); 2 = tabla «US MOBILE BAR BENCHMARKS (sourced) AND KIT ESTIMATES» de Instructions!A53:D68 + los 5
//     umbrales del P&L. Sin aggregateRating ni review.
//   · Cifras del caso US: SOLO de scripts/productos-digitales/business-plans-en-5/cifras_caso.json y F2-NOTAS §8:
//     160 eventos × 95 invitados × $14.00 (sin sales tax ni alcohol) → $212,800; inversión $76,972 = $47,530 +
//     $29,442; propios $28,000 + préstamo $49,000 al 10 % a 7 años; margen bruto 69.8 %; neto $18,790 (8.8 %);
//     equilibrio 134 eventos/año frente a 160; DSCR mín 2.93×; 9 personas, 4 puestos; seguros $4,000; pesimista
//     120 × $12.60 × 86 → caja −$2,664 («the cash runs out»). Caso = cuartil alto (Check Cherry): la mediana del primer
//     año son 3 eventos y se dice. Los 3 presupuestos de ejemplo salen de «3 Example Quotes» de la calculadora (Kit
//     estimates: $19.00 / $16.50 / $16.00 por invitado). Ninguna cifra del ES.
//     Conteos del producto: 10 secciones, más de 6,500 palabras (6,796), 9 hojas, más de 700 fórmulas (722), 68
//     tareas en 6 fases (11/13/12/10/12/10), 10 recetas de signature cocktails (9 + 1 mocktail).
//   · FAQ «Does it work in the UK, Canada or Australia?» (John, 13-oct; estilo de la del catering en PR #126),
//     comprobada contra los ficheros: VAT en Assumptions!C39/C41 e Instructions!A16 de la calculadora; oz con (ml) en
//     «Signature Cocktail Specs», lb con (kg) en el hielo, millas en la calculadora, sq ft en el checklist; notas UK
//     del docx §9 [108] (personal licence, TEN, licencia del local).
//   · Testimonios (D26, como Bar y Catering): los 8 del ES traducidos con el subtítulo de la edición española y SIN
//     ningún dato que no sea verdad en este kit: fuera «10 experiencias», «proveedores», «plantilla de proveedores»,
//     «modelo de contrato», «40 horas», «Bodas.net, Zankyou», «freelance» y todas las cifras (50 eventos, 70K, 42 %,
//     150K, 1/4, 1.400 EUR, mes 10).
//   · Imágenes: las del ES de coctelería SIN texto en español (hero, -3, -4, -5, -6; fuera -1 «MADRID 2026» y -2 «EL
//     GRAN CLAVO») + consultor-bartender-coctel (signature cocktail, sin texto). OG = recorte 1200×630 del hero.
//     Ninguna enseña un remolque-barra: pendiente de John si se generan las 2 de D95.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_MOBILE_BAR_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What should a mobile bar business plan include?',
    a: 'The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a dry hire mobile bar, plus the Excel financial projections that back them up, a pricing calculator that turns your cost per guest into a quote and a shopping list for the host, and a 68-task startup checklist.',
  },
  {
    q: 'Is it a generic template or built for a mobile bar?',
    a: "Built for a mobile bar and bartending service sold as dry hire: the host buys the alcohol, and you bring the bar, the bartenders, mixers, garnishes, ice and cups, with setup and breakdown included. A converted bar trailer works the photogenic events and a portable bar covers the second crew and the ballrooms the trailer can't enter; the owner's own pickup tows the trailer. Weddings, corporate events and private parties, signature cocktails and a mocktail on every menu, specialty bars (mimosa, espresso martini, tiki) as an upcharge, and W-2 event bartenders with their alcohol server certification. Nothing to strip out from a restaurant template.",
  },
  {
    q: 'Do I need a liquor license for a dry hire mobile bar?',
    a: "Often not, as long as you only sell the service — but it varies by state, so ask yours first. Missouri's Industry Circular 24-01 says a person who solely provides bartending services doesn't need a state liquor license, and warns that admission fees, tips, gratuities, donations and surcharges on the alcohol can count as a sale. Montana's Mobile Bars fact sheet adds that the bar may not be pre-stocked, the host buys the alcohol separately and the events must be private. The plan sets out the conditions it works with: your client buys and owns the alcohol and keeps the leftovers; no cash bar, drink tickets or ticketed entry that includes drinks; and your invoice charges for the service, never for the drinks. The first permit task in the checklist is to ask your state alcohol authority and keep the answer in writing.",
  },
  {
    q: 'How hard is it to get a liquor license for a mobile bar?',
    a: "Much harder than working dry hire, and it depends on your state. In Texas, a Caterer's Permit is an add-on to a Mixed Beverage Permit, which is tied to a fixed address. In California, the Type 58 caterer license is only for on-sale licensees. In Florida, selling alcohol without a license is a crime, so a cash bar needs a licensed partner such as a 13CT caterer. In New York, the SLA issues a Caterer's Alcohol Permit per event. That's why the kit is built on dry hire, and why the plan explains the full-service routes — a licensed partner, your own license tied to a venue, or an event permit where one exists — as options, not as the case. The pricing calculator has a licensed package too, to use only if you hold the license.",
  },
  {
    q: 'How much does it cost to start a mobile bartending business?',
    a: "It depends mostly on whether you start with a portable bar or a bar trailer. Check Cherry puts a lean start with a portable bar at $2,000 to $7,000, and says a converted trailer often costs tens of thousands of dollars. The kit's example is a trailer build: $47,530 in startup costs plus $29,442 of working capital, for $76,972 in total cash needed. The Startup Costs sheet lists every line — the used bar trailer ($9,000) and its conversion ($12,000), wrap and bar facade, a portable bar for the second crew, an inverter generator, storage unit fit-out, LLC and legal, first-year permits and server certifications, booking software, bar tools, opening inventory of mixers and cups, website and launch, glassware, coolers and ice bins. The owner's pickup tows the trailer; if you need one, Check Cherry puts a used tow vehicle at $10,000 to $30,000. There's no alcohol inventory: in dry hire the host buys it. Replace each line with your own quotes.",
  },
  {
    q: 'How much does a mobile bar make?',
    a: "Be realistic about year one. Check Cherry's data on mobile bars with at least a year in business shows a median of 3 events and $1,650 in the first year, while the top 10% did about 39 events; its median price is $750 per event, excluding alcohol and tips. The kit's example is a full-time operator with two crews and a marketing budget, in the upper quarter of the market: 160 events a year with 95 guests at $14.00 per guest (excl. sales tax and alcohol), $212,800 in year-1 sales and $18,790 of net income (8.8%), after paying the owner as lead bartender, with a break-even of 134 events a year. In the pessimistic scenario — 120 events at $12.60 per guest and 86 guests — the cash runs out in year 1, and the plan says so. Build your first year on your own bookings, not on the example.",
  },
  {
    q: 'How much should I charge per guest for a mobile bar?',
    a: "Start from your costs. The pricing calculator turns staff hours and wages (with payroll taxes), mixers, garnishes and N/A drinks, cups, ice and mileage into a price per guest that meets your target margin, rounded up to the next 50 cents, and shows its hourly equivalent; then it adds any flat bar fee, specialty bar upcharge, service charge and sales tax, works out the deposit and the balance, and shows the gross margin the quote really leaves. The host's alcohol is never in your price. Its three example quotes, all dry hire and kit estimates: a wedding for 120 guests over 5 hours at $19.00 per guest, a corporate holiday party for 100 guests over 4 hours at $16.50 and a private birthday for 60 guests with a limited bar and a mimosa bar at $16.00. As a market reference, Check Cherry reports a median of $750 per event and about $75-$120 per bartender hour for bartender-only service.",
  },
  {
    q: 'How many bartenders do I need per guest?',
    a: "As a kit estimate, one bartender for every 50 guests with a full bar and one for every 75 with beer, wine and one signature cocktail, plus a barback at large weddings. For drinks, plan 2 per guest in the first hour and 1 per hour after that (eventplanning.com), and about 1.5 lb (0.68 kg) of ice per guest. The calculator suggests the number of bartenders for each package and turns guests and hours into drinks, ice, cups and a shopping list for the host: bottles of spirits, wine, beer and sparkling wine for the toast.",
  },
  {
    q: 'What insurance do I need for a mobile bar?',
    a: "General liability plus a separate liquor liability policy, because general liability usually excludes alcohol; Insurance Canopy quotes general and liquor liability for mobile bartenders from about $550 a year, or from $275 per event. Add commercial auto that covers the trailer, workers' compensation for your W-2 staff and coverage for your gear in transit. Venues ask for a certificate of insurance (COI) naming them as additional insured, and the host's own liquor liability is the host's purchase. The example budgets $4,000 a year for insurance; ask an agent who insures mobile bars for your own quotes.",
  },
  {
    q: 'Can an LLC own a mobile bar?',
    a: "Yes, and the example in the kit is one. The checklist starts with choosing your structure with your accountant (single-member LLC, sole proprietor or S corp), getting your free EIN from the IRS, registering the LLC with your Secretary of State with a registered agent and an operating agreement, opening a business bank account and getting your seller's permit and business license. In dry hire the LLC sells a bartending service, not alcohol.",
  },
  {
    q: 'Can I accept tips at a dry hire event?',
    a: "Ask your state before you do. At a dry hire event, money that guests or your client hand over can look like a sale of alcohol: Missouri's Industry Circular 24-01 warns that tips, gratuities and donations — not just a tip jar — can be treated as a sale. So don't treat a tip jar or a gratuity line as safe until your state alcohol authority tells you so in writing, and price the service itself so it pays your bartenders properly without them. Where tips are allowed, a voluntary tip belongs to your staff under the FLSA, not to you. A mandatory service charge is part of your price: under IRS Revenue Ruling 2012-18 it isn't a tip, and whatever part you pay out to staff counts as wages. The calculator keeps the service charge on its own line and leaves any voluntary gratuity out of the price.",
  },
  {
    q: 'Does it work for a bar with its own premises, a caterer or a food truck?',
    a: "It's built for a dry hire mobile bar with no storefront and no alcohol inventory. If you're opening a bar with its own premises and liquor license, our Bar Business Plan Kit fits better; if you'll serve food at events, start from the Catering Business Plan Kit; and if you'll sell food and drinks to walk-up customers, the Food Truck Business Plan Kit. The Excel workbook takes any numbers you type, but the written plan describes a mobile bartending company, so you'd rewrite more of the text.",
  },
  {
    q: 'Can I present this plan to a lender or investors?',
    a: "Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The loan schedule and the DSCR cover your main loan, the one you enter in the assumptions; the financing sheet also lists an SBA Microloan, investors or partners and local grants as sources of funds, without amortizing them. In the example, the owner puts in $28,000 and borrows $49,000 at 10% over 7 years — a size that fits within the SBA Microloan cap of $50,000 — with a minimum DSCR of 2.93×. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.",
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: "Yes. The green cells are the ones you type — events per year, price per guest, guests per event, the share of add-ons, the cost of mixers, garnish and ice, the marketplace share, storage rent, wages and any startup cost line — and more than 700 linked formulas recalculate the rest. The 30% client deposit isn't modeled, which keeps the cash flow on the cautious side. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook and the calculator each include an Instructions tab.",
  },
  {
    q: 'Does it work in the UK, Canada or Australia?',
    a: "Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your price per guest without it. The cocktail specs give ounces with milliliters for metric jiggers and the ice comes in lb with kg alongside; the calculator counts miles, so type kilometers and your cost per km instead, and storage sizes are in sq ft. The plan's UK notes cover the personal licence, Temporary Event Notices and working under a venue's premises licence. In Canada, liquor rules are provincial and servers need Smart Serve, Serving It Right or the local equivalent; in Australia, check your state liquor rules and RSA. Ask your council, province or state before you sell a package.",
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
    a: "One purchase covers one business, however many events it works. If you're a consultant or an investor, you can use the files with the projects you advise, but you can't hand them copies: each business buys its own.",
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the plan doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: PlanNegocioData = {
  slug: 'mobile-bar-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_MOBILE_BAR_BUSINESS_PLAN',

  seo: {
    title: 'Mobile Bar Business Plan Kit: Word Template + Excel Financial Projections + Pricing Calculator | AI Chef Pro',
    description:
      'Mobile bar business plan template for a dry-hire bartending company: Word plan, 3-year Excel projections, per-guest pricing calculator and startup checklist.',
    keywords:
      'mobile bar business plan, mobile bartending business plan, mobile bar business plan template, how to start a mobile bar business, dry hire mobile bar, mobile bar pricing, mobile bar license, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-mobile-bar-business-plan.jpg',
  },

  schema: {
    productName: 'Mobile Bar Business Plan Kit',
    productDescription:
      'Mobile bar business plan template kit for a dry hire mobile bartending company: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a pricing calculator from cost per guest to quote with a shopping list for the host and 10 signature cocktail specs, and a 68-task startup checklist in 6 phases. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Mobile Bar Business Plan Kit',
  },

  images: {
    // hero bg (6) — las del ES de coctelería sin texto en español + un signature cocktail sin texto.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-4.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-6.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-5.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-3.jpeg',
      '/lovable-uploads/ai-gallery/consultor-bartender-coctel.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el catering.
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-6.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/consultor-bartender-coctel.jpg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-4.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-3.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-5.jpeg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-4.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-6.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready mobile bar business plan: Word + Excel + pricing calculator',
    titlePre: 'Mobile Bar ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Dry-Hire Mobile Bartending Company: Word Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist',
    description:
      'Everything you need to plan, price and pitch a mobile bar that works dry hire (your client buys the alcohol; you bring the bar, the bartenders and everything else): a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in events per year, 12-month cash flow and loan payments from your own numbers; a pricing calculator that turns your cost per guest into a quote and a shopping list for the host; and a 68-task checklist that takes you from your LLC and your state\'s alcohol rules to your first 90 days of events. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section mobile bar business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in events per year and 12-month cash flow',
      "Pricing calculator: cost per guest to quote, plus the host's shopping list",
      'Startup checklist: 68 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      "What's inside your Mobile Bar Business Plan Kit: 9 building blocks to test whether your mobile bartending business works on paper before you buy a trailer, price every event and present the plan to a lender or an investor.",
    templates: [
      { icon: 'FileText', title: 'Mobile Bar Business Plan (Word, 10 Sections)', desc: 'A complete plan of more than 6,500 words already written for a dry hire mobile bar with a converted bar trailer and a portable bar: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan (The Knot, WeddingWire, Zola, GigSalad, venues and wedding planners), operations plan (the event timeline, ice, garnish and glassware), management and staffing, financial plan, legal requirements, permits and licenses (dry hire vs. full-service, state by state), and conclusions with an action plan. Its figures are the ones in the example Excel model.' },
      { icon: 'FileSpreadsheet', title: 'Mobile Bar Financial Projections (Excel, 9 Sheets)', desc: 'Is your mobile bar business profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than 700 linked formulas: change events per year, price per guest or guests per event and the whole workbook recalculates.' },
      { icon: 'Calculator', title: 'Mobile Bar Pricing Calculator (Cost per Guest to Quote + Shopping List)', desc: "Three bar packages — full bar and limited bar in dry hire, and a licensed full bar only if you hold the license — with guests, hours, drinks per guest, bartenders and barbacks with wages and payroll taxes, mixers, garnish, cups, ice and mileage, a flat bar fee, a specialty bar upcharge, the marketplace fee, your target margin, service charge, sales tax and deposit. Out come the price per guest and its hourly equivalent, the total to quote, the deposit, the balance and the gross margin it really leaves. Plus the host's shopping list, 10 signature cocktail specs in oz (with ml) scaled to 50, 100 and 200 drinks, and 3 example quotes." },
      { icon: 'Coins', title: 'Mobile Bar Startup Costs, Line by Line', desc: 'A used bar trailer and its conversion (bar top, cabinets, hand sink, water tanks, LED lighting), wrap and bar facade, a portable bar for the second crew, an inverter generator, storage unit fit-out, LLC and legal, first-year permits and server certifications, a health permit only if your county requires it, booking software, bar tools, opening inventory of mixers and cups, website and launch, glassware, coolers and ice bins — each with a reference price you replace with your quotes, plus the storage deposit, rent before opening, a contingency and working capital. No alcohol inventory: the host buys it.' },
      { icon: 'TrendingUp', title: 'Break-Even in Events per Year', desc: 'How many events a year you need at your price per guest (excl. sales tax) and guest count to cover every cost, and the cash break-even with loan payments in and depreciation out. Your cushion above it, a sensitivity table for price per guest and variable cost per guest, and a plain-English reading of the result.' },
      { icon: 'BarChart3', title: 'Financial Scenarios', desc: 'Three scenarios side by side — pessimistic, base and optimistic — moving events per year, price per guest and guests per event, each with its own estimated cash balance. Useful for a lender or an investor, and honest about what a slow first year does to your cash.' },
      { icon: 'Users', title: 'Staffing & Event Labor (4 Roles)', desc: 'Owner & Lead Bartender, a second-crew lead bartender on part-time W-2 hours, hourly W-2 event bartenders and barbacks / setup crew, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the event hours you need (hours per event × people per event × events) against the hours you hire, and flags any pay below the minimum wage for the hours worked.' },
      { icon: 'ShieldCheck', title: 'Startup Checklist (68 Tasks, 6 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license, your service agreement with dry hire clauses), trailer and permits (your state's alcohol rules in writing, the county health department on garnish and ice, venue requirements, DMV, general and liquor liability, workers' comp), equipment, staff (W-2 bartenders and barbacks, TABC, RBS or TIPS certification, responsible service), marketing (The Knot, WeddingWire, Zola, GigSalad, The Bash, Thumbtack, venues and planners) and your first 90 days." },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25× target, plus an SBA Microloan, investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Coctelería para Eventos, la edición española.
  // Sin ningún dato que no sea verdad en este kit (ver cabecera). Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Bartenders and event pros who planned their mobile bar with the Spanish edition of this plan',
    items: [
      { name: 'Nadia and Lidia', role: 'Founders of an event cocktail bar company, Spain', text: 'We were looking for a plan built for our mobile bar model with themed bars, and this was exactly what we needed. It saved us months of research.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Alejandro Vela', role: 'Bartender, second year with a mobile bar, Madrid, Spain', text: 'I wish I had had this plan when I started two years ago. The pricing calculator is gold: now I charge what each event is really worth, not what I guessed.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Laura Manchón', role: 'Wedding planner, Madrid, Spain', text: 'I recommend this plan to every mobile bar that joins my network of vendors. It gives them a professional starting point.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Carlos Ferreras', role: 'Event bartender starting his own company, Spain', text: 'The financial plan convinced me to take the step. Next I am working through the checklist, and I launch in September.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'María Pino', role: 'Cocktail school instructor, Madrid, Spain', text: 'I recommend it in all my advanced courses. Nobody had put together so clearly how to start this business.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ferran Llopis', role: 'Hospitality entrepreneur, Barcelona, Spain', text: 'I was about to open a bar with its own premises. After reading this plan I switched to a mobile bar for events, with far less money at risk.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Former bar worker starting his mobile bar, Spain', text: 'I came from a traditional bar and knew nothing about winning weddings. The marketing plan, with wedding planners and the wedding platforms, gave me a clear roadmap.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Hospitality investor', text: 'The financial plan is realistic. This is what I expect from a professional business plan, not an inflated slide deck.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a mobile bar plan written for the format lenders expect, with a financial model and a pricing calculator that recalculate from your own numbers.',
    reasons: [
      { icon: 'Martini', title: 'Built for a Dry Hire Mobile Bar', desc: 'A converted bar trailer for the photos and a portable bar for the second crew and indoor venues, W-2 bartenders with their alcohol server certification, signature cocktails and a mocktail on every menu, mixers, garnish, ice and cups included, setup and breakdown, and a shopping list so the host buys the right bottles. Specialty bars — mimosa, espresso martini, tiki — as the upcharge. Nothing to strip out from a restaurant template.' },
      { icon: 'ShieldCheck', title: 'Dry Hire vs. Full-Service, Explained', desc: "Do you need a liquor license for a mobile bar? In dry hire, often not — if the host buys and owns the alcohol and you never charge for drinks. The plan sets out those conditions with Missouri's and Montana's rules as examples, and the full-service routes in Texas, California, Florida and New York, so you ask your state the right question before you sell a package." },
      { icon: 'Calculator', title: 'Mobile Bar Pricing per Guest and per Hour', desc: "The calculator turns staff hours, mixers, ice and mileage into a price per guest and its hourly equivalent, adds the service charge, the sales tax and the deposit, shows the margin it leaves and builds the host's shopping list. Three example quotes: a wedding, a corporate holiday party and a private birthday with a mimosa bar." },
      { icon: 'BarChart3', title: 'Honest Numbers, Calculated', desc: 'The example: 160 events a year with 95 guests at $14.00 per guest (excl. sales tax and alcohol), $212,800 in year-1 sales and 134 events a year to break even — a full-time operator with two crews, in the upper quarter of the market. The median new mobile bar does 3 events in its first year (Check Cherry), and the pessimistic scenario shows what a slow start does to your cash. Replace the numbers with yours.' },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised event companies, bartenders and wedding planners on launching and growing mobile bars, combining hands-on operations with financial planning.',
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      'Besides the business plan, the financial model, the pricing calculator and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Mobile Bar Insurance, Permits & Venue Requirements Guide (US + UK Notes)',
        desc: "Section 9 of the plan plus Phase 2 of the checklist: the conditions of dry hire, the full-service routes in Texas, California, Florida and New York, what to ask your county about garnish, ice and a hand sink, sales tax on the bar service, W-2 staff, the liquor liability and the COI venues ask for, and registering the trailer with the DMV — with notes for the UK. No state forms included: requirements vary by state, county and city.",
        image: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-hero.jpg',
      },
      {
        icon: 'BarChart3',
        label: 'BONUS 2',
        title: 'US Mobile Bar Benchmarks (Sourced)',
        desc: 'The reference table inside the workbook: price per event, by guest count and by event length, bartender-only rates, deposit and travel fee, seasonality, the real first year of a new mobile bar, drinks per guest, bartender ratio and wages, marketplace commission, startup costs, insurance, and ice, mixers and garnish per guest, each with its source or marked "kit estimate" when there isn\'t one — plus five OK / REVIEW checks on your P&L against editable thresholds.',
        image: '/lovable-uploads/ai-gallery/consultor-bartender-coctel.jpg',
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
    headingGold: 'Mobile Bar Business',
    subtitle:
      'Plan it before you buy the trailer: the written plan, the numbers behind it, a price for every quote and the permits list, for a one-time payment.',
    items: [
      '10-section mobile bar business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in events per year, with a sensitivity table',
      'Pricing calculator: from cost per guest to a quote',
      "The host's shopping list and 10 signature cocktail specs",
      'Startup checklist: 68 tasks in 6 phases',
      'BONUS: Mobile Bar Insurance, Permits & Venue Requirements Guide (included in the plan)',
      'BONUS: US Mobile Bar Benchmarks',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'MOBILE BAR BUSINESS PLAN — $39',

  // Salientes: los gemelos más cercanos (Bar con local, Catering de eventos, Food Truck), Inventory (inventario de
  // barra), Staff Scheduling (personal por evento), Financial Plan + los otros planes EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/catering-business-plan', label: 'Catering Business Plan Kit' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'mobile-bar-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
