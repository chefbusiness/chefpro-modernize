// astro-site/src/data/productos-en/planes/restaurant-business-plan.ts
// TIENDA INTERNACIONAL EN — Restaurant Business Plan Kit. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/planes/plan-negocio-bar-restaurante.ts (mismo tipo PlanNegocioData, misma
// plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Hermana de food-truck- y
// coffee-shop-business-plan.ts (mismas decisiones de la SPEC heredada; ver sus cabeceras).
// SPEC: scripts/productos-digitales/business-plans-en-2/SPEC-delta.md (D30-D47 y §4 R1-R12) + la heredada
//   scripts/productos-digitales/business-plans-en/SPEC.md (D1-D29, §6), que manda en lo demás.
//   · D30: slug `restaurant-business-plan`, nombre «Restaurant Business Plan Kit», H1 Forma B `Restaurant ` +
//     oro `Business Plan` + «Template for a Casual Restaurant & Bar: …». «bar business plan» solo como
//     «Restaurant & Bar» (subtítulo, title, FAQ): es un restaurante con barra, no un bar de copas.
//   · D31: $39; priceOld $129; bonos $29; total $187; ahorro $90; «-70%» en hero y buyBox.
//   · D32: los 3 ficheros EN (dashboard RestaurantBusinessPlanDashboard.tsx y get-download-urls.ts).
//   · D45: tarjeta DOCX la PRIMERA del grid (el ES no vendía el Word). Bonos rehechos: 1 «Restaurant Permits &
//     Licenses Guide (US + UK notes, liquor license included)» = §9 del plan + fases 1, 2 y 6 del checklist;
//     2 «US Market Data & Industry Benchmarks (sourced)» = §3 del docx + tabla D19. Para no contar dos veces
//     la tabla de referencias, la tarjeta del grid se queda en «Instructions & Ratio Checks» (semáforo).
//   · §4: R1 (sin «~80K-150K EUR» ni «~133K EUR»: la caja del caso US es TODO_CIFRA), R2 (bono 1 ya no es
//     el cuadro de personal), R3 (sin «Análisis de Mercado España 2026» ni tasa de cierre: no hay fuente),
//     R4 (SBA 7(a) / Microloan, sin «orden recomendado de gestión»), R5 (los 7 puestos reales del libro, sin
//     jefe de sala), R6/R10 (sin SS 33 %, 14 pagas, «Datos reales España», rating, superlativo ni «737»).
//   · D37/D38: licencia de alcohol con nota de cupo (la cifra de la fila es TODO_CIFRA), sin propinas ni
//     tip credit en el modelo (servers y bartenders a salario base completo).
//   · Compatibilidad y testimonios (decisión del orquestador, como FT/CAF): solo Microsoft Excel (.xlsx) y
//     Word (.docx) en US Letter; los 8 testimonios del ES traducidos con el subtítulo de la edición española,
//     sin las cifras que el producto EN no tiene («50+ trámites», «Seg. Social al 33,4 % y 14 pagas», los
//     ratios «28-32 %», «las 6 fases» —son 7—). Se conservan las cifras personales (135.000 EUR, 10 días,
//     300 EUR al mes, 4 meses, 3 aperturas).
//   · Cifras del caso US: TODO_CIFRA con comentario encima (las rellena el orquestador con cifras_caso.json
//     de la F2). Los conteos del producto (10 secciones, 9 hojas, 64 tareas en 7 fases, 7 puestos) y los
//     parámetros de la SPEC (DSCR 1.25×, Microloan hasta $50,000, umbrales D41) sí van.
//   · FAQ: People Also Ask de «restaurant business plan» (research delta §2) + «how to open a restaurant»,
//     «restaurant startup costs», «liquor license cost», «bar business plan» + UK, moneda, suscripción,
//     licencia y garantía. schema.faqs = el MISMO array.
//   · Imágenes: fotos propias sin texto (rbp-en-*) + use-case-casual-kitchen (sin rótulos). Las del ES son
//     miniaturas de 400 px y use-case-casual-bar lleva pizarras en español («TAPAS», «VINOS»).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_RESTAURANT_BUSINESS_PLAN (resuelto en el wrapper .astro).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// FAQ on-page Y FAQPage (un solo array).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What should a restaurant business plan include?',
    a: 'The sections lenders, landlords and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written for a casual restaurant with a bar in Word, plus the Excel financial projections that back them up and a 64-task opening checklist.',
  },
  {
    q: 'Is it a generic plan or built for a restaurant with a bar?',
    a: 'Built for a casual, full-service restaurant with a bar: cooking line, convection oven, fryers, refrigerated prep tables, walk-in cooler, Type I hood with fire suppression, dishwasher, sinks with grease interceptor, the bar with beer taps and a wine fridge, tables, stools, glassware, POS and patio in the startup costs; food and beverage sales with the alcohol share in the P&L; seven roles in the staffing sheet (general manager-owner, head chef, line cook, server-bartender, part-time server, weekend extra and relief cover); and the permits of a full-service restaurant, liquor license included.',
  },
  {
    q: 'How much does it cost to open a restaurant?',
    // TODO_CIFRA: caja total necesaria del restaurante de ejemplo (Startup Costs, xlsx EN calibrado por la F2).
    a: "It depends on the space more than on the kitchen equipment: a unit that was already a restaurant, with its hood and grease interceptor in place, needs a fraction of the build-out of an empty shell, and rent, permits and the liquor license vary a lot by city and state. A survey of independent owners by RestaurantOwner.com put the median opening cost at around $375,000. The Startup Costs sheet lists every line — lease review, build-out, architect and permits, cooking line, hood and fire suppression, walk-in cooler, dishwasher, the bar, furniture, POS, patio, brand and launch, LLC and legal, liquor license and opening inventory — plus deposits, pre-opening months, contingency and working capital. The kit's example restaurant needs TODO_CIFRA in total cash; replace each line with your own quotes.",
  },
  {
    q: 'What is the 30/30/30/10 rule for restaurants?',
    a: "It's an informal rule of thumb that splits sales into roughly 30% cost of goods, 30% labor, 30% other operating costs and 10% profit. Use it as a quick sanity check, not as a target. The model checks your own ratios against editable kit benchmarks — gross margin of at least 65%, cost of goods up to 32%, labor up to 35%, rent up to 10% and net margin of at least 5% — and marks each one OK or REVIEW. Add cost of goods and labor and you get your prime cost: full-service restaurants usually aim for about 60-65% of sales.",
  },
  {
    q: 'Is a restaurant a profitable business?',
    a: 'It can be, but margins are tight and three lines usually decide it: cost of goods, labor and rent. The model checks them against editable kit benchmarks and runs three scenarios (pessimistic, base and optimistic), so you can see whether the plan still works in a slow year before you sign a lease.',
  },
  {
    q: 'What are the most common reasons restaurants fail?',
    a: "Running out of cash before the restaurant finds its rhythm, costs that are too high for the sales it actually makes (usually rent and labor), and a concept or a location the local market doesn't support. Each one has a check in the kit: the 12-month cash flow shows your lowest cash balance and the month it happens, the benchmarks flag the cost lines out of range, and the break-even sheet tells you how many covers a day you need and your margin of safety.",
  },
  {
    q: 'How much does a liquor license cost?',
    // TODO_CIFRA: importe de la fila «Liquor license + permits (non-quota state example)» del xlsx EN (D37 fija $15,000; confirmar con la F2).
    a: "It depends entirely on your state and city: from a few hundred dollars for a beer and wine license in some places to well over $100,000 in states that cap the number of licenses, where you buy an existing one from another business. Start early, because approval can take months. The kit's startup costs include a liquor license line of TODO_CIFRA as a non-quota state example, with a note to replace it with your state's fee or the market price of a transfer, and the plan reminds you to add liquor liability to your insurance.",
  },
  {
    q: 'How do I open a restaurant, step by step?',
    a: "Test the numbers before you look at spaces, check the zoning before you sign a lease, form your LLC and get your EIN, seller's permit and business license, then go through the health department plan review and building permits before the build-out. Apply for your liquor license early, hire and train your team, pass the final inspections and open with a soft opening. The opening checklist organizes those steps into 64 tasks in 7 phases, from business setup to your first 90 days.",
  },
  {
    q: 'What permits do I need to open a restaurant?',
    a: "It depends on your state, county and city. The usual list: a business structure (LLC or sole proprietorship), an EIN, a seller's permit and a business license; a zoning check before you sign the lease; building, electrical, plumbing and gas permits for the build-out; a health department plan review and food establishment permit; hood, fire suppression and fire marshal inspections; a certificate of occupancy; a liquor license if you serve alcohol; and sign and sidewalk cafe permits if they apply. The opening checklist covers them in 64 tasks. Treat it as a starting point and confirm the details with your local authorities.",
  },
  {
    q: 'Does it work as a bar business plan?',
    a: "It's built for a restaurant with a full bar, so the bar side is already there: the bar build, beer taps, wine fridge, glassware, bar stock, the alcohol share of beverage sales and the liquor license. If you're opening a bar that serves little or no food, the Excel model still works — lower the food share and adjust the startup costs and staffing — but the written plan describes a restaurant & bar, so you'll rewrite more of the text.",
  },
  {
    q: 'Can I present this plan to a lender, a landlord or investors?',
    a: "Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The financing sheet covers an SBA-guaranteed 7(a) loan through your bank, an SBA Microloan (up to $50,000, through nonprofit intermediaries), investors or partners and local grants. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.",
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: "Yes. The green cells are the ones you type — rent, covers per day, average check, wages and any startup cost line — and more than 700 linked formulas recalculate the rest. Tips aren't modeled: servers and bartenders are budgeted at a full base wage, which keeps the plan on the safe side. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook includes an Instructions tab.",
  },
  {
    q: 'Does it work in the UK?',
    a: "Yes, with notes. Tax rates are editable cells: enter 20% VAT on restaurant sales and the VAT you can reclaim on purchases and on your build-out. The plan and the checklist add UK notes: register your food business with the council at least 28 days before you open, expect a food hygiene rating inspection in your first months, and to sell alcohol you need a premises licence plus a personal licence for your designated premises supervisor. UK minimum wage and employer National Insurance aren't preloaded: enter the current figures from gov.uk.",
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
    q: 'Can I use it for several locations or with my clients?',
    a: "One purchase covers one business, with all of its locations. If you're a consultant or an investor, you can use the files with the projects you advise, but you can't hand them copies: each business buys its own.",
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the plan doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: PlanNegocioData = {
  slug: 'restaurant-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_RESTAURANT_BUSINESS_PLAN',

  seo: {
    title:
      'Restaurant Business Plan Template: Word + Excel Financial Projections + Opening Checklist (Restaurant & Bar) | AI Chef Pro',
    description:
      'Restaurant business plan template for a casual restaurant & bar: a 10-section Word plan, Excel financial projections (3-year P&L, break-even, cash flow, loan and DSCR) and a 64-task opening checklist. $39.',
    keywords:
      'restaurant business plan, restaurant business plan template, bar business plan, restaurant startup costs, how to open a restaurant, restaurant financial projections, restaurant opening checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-restaurant-business-plan.jpg',
  },

  schema: {
    productName: 'Restaurant Business Plan Kit',
    productDescription:
      'Restaurant business plan template kit for a casual restaurant with a bar: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions) and a 64-task opening checklist in 7 phases, liquor license included. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Restaurant Business Plan Kit',
  },

  images: {
    // hero bg (6) — fotos propias sin texto + la cocina de los usos (sin rótulos). Las plan-bar-restaurante-*
    // del ES son miniaturas de 400 px.
    gallery: [
      '/lovable-uploads/ai-gallery/rbp-en-hero.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-bar.jpg',
      '/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-dining.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-storefront.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el ES.
    gridGallery: [
      '/lovable-uploads/ai-gallery/rbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-dining.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-bar.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-storefront.jpg',
      '/lovable-uploads/ai-gallery/rbp-en-hero.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/rbp-en-dining.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/rbp-en-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready restaurant business plan: Word + Excel + checklist',
    titlePre: 'Restaurant ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Casual Restaurant & Bar: Word Plan + Excel Financial Projections + Opening Checklist',
    description:
      'Everything you need to plan and pitch a casual restaurant with a bar: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even, 12-month cash flow and loan payments from your own numbers; and a 64-task checklist from the zoning check before you sign the lease to your liquor license and your first 90 days open. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section restaurant business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even and 12-month cash flow',
      'Startup costs line by line, from build-out and hood to the bar',
      'Opening checklist: 64 tasks in 7 phases, liquor license included',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      '9 building blocks to test whether your restaurant works on paper before you sign a lease, and to present it to a lender, a landlord or an investor.',
    templates: [
      { icon: 'FileText', title: 'Restaurant Business Plan (Word, 10 Sections)', desc: 'A complete plan already written for a casual restaurant with a bar: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements, permits and licenses, and conclusions with an action plan. Its figures are the ones in the example Excel model.' },
      { icon: 'FileSpreadsheet', title: 'Restaurant Financial Projections (Excel, 9 Sheets)', desc: 'Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than 700 linked formulas: change a green cell and the whole workbook recalculates.' },
      { icon: 'Coins', title: 'Startup Costs Line by Line', desc: 'Build-out, architect and permits, cooking line, convection oven, fryers, refrigerated prep tables, walk-in cooler, Type I hood with fire suppression, dishwasher, sinks with grease interceptor, the bar, tables and stools, beer taps, glassware, POS, patio and the liquor license, each with a reference price you replace with your quotes, plus deposits, pre-opening months, contingency and working capital. The total cash you need is calculated separately.' },
      { icon: 'TrendingUp', title: 'Break-Even Point', desc: 'How many covers a day you need at your average check (excl. sales tax) and the table turns that implies, plus the cash break-even with loan payments in and depreciation out. Margin of safety, a sensitivity table for average check and variable cost, and a plain-English reading of the result.' },
      { icon: 'BarChart3', title: 'Financial Scenarios', desc: 'Three scenarios side by side — pessimistic, base and optimistic — each with its own estimated cash balance. Useful for a lender, a landlord or an investor.' },
      { icon: 'Users', title: 'Staffing & Payroll Costs', desc: "Seven roles — general manager-owner, head chef, line cook, server-bartender, part-time server, weekend extra and relief cover — with gross pay, employer payroll taxes, the real cost of each role and two alerts: pay below the minimum wage for the hours worked, and service hours left uncovered. Tips aren't modeled: servers and bartenders are budgeted at a full base wage." },
      { icon: 'ShieldCheck', title: 'Opening Checklist (64 Tasks, 7 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license), location and permits (zoning, lease, building permits, health plan review), build-out and equipment, staff, marketing and launch, what must be in place before you open (final inspections, liquor license, insurance, pest control and music licenses) and your first 90 days." },
      { icon: 'ListChecks', title: 'Instructions & Ratio Checks', desc: 'An Instructions tab that explains every sheet and which cells to type, plus five checks on the P&L — gross margin, cost of goods, labor, rent and net margin — each marked OK or REVIEW against an editable kit benchmark.' },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity, an SBA-guaranteed 7(a) loan through your bank, an SBA Microloan, investors or partners and local grants, with the loan amortization schedule, the debt service coverage ratio (DSCR) year by year against a 1.25× target and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Bar-Restaurante, la edición española.
  // Las cifras del producto ES que el EN no tiene se reformulan sin número (ver cabecera). Solo se pintan.
  testimonials: {
    subtitle:
      'Owners and investors who opened their restaurant with the Spanish edition of this plan',
    items: [
      { name: 'Alejandro Ruiz', role: 'Restaurant & bar owner, Madrid, Spain', text: 'I took the financial plan to my bank in Spain and they approved the loan in 10 days. The 3-year projections with scenarios gave them a lot of confidence. Total investment: EUR 135,000.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Hospitality entrepreneur, Barcelona, Spain', text: 'The opening checklist saved me months of work. Every step organized by phase, from setting up the company to the activity license in Spain. I didn\'t leave a single thing pending.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Restaurant investor', text: 'I use this plan as the starting point to evaluate restaurant projects. The break-even point and the financial scenarios are exactly what I need to make investment decisions.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Restaurant manager, Seville, Spain', text: 'The staffing sheet with employer costs was an eye-opener. I used to underestimate labor costs. Now I have just the right team to be profitable.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Hospitality consultant', text: 'I recommend it to every client who wants to open a restaurant in Spain. Real industry numbers, not filler templates.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Gastropub owner, Valencia, Spain', text: 'The reference ratios helped me negotiate a better lease. I saved more than EUR 300 a month in rent.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex-executive who opened his own restaurant', text: 'I came from the corporate world and knew nothing about hospitality licenses. The opening checklist guided me step by step, phase by phase. I opened in 4 months without a single legal problem.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Founding partner, restaurant group', text: 'We\'ve used the Excel financial plan for 3 different openings. You just change the numbers for each location and you have a professional business plan ready to present to investors.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a restaurant & bar plan written for the format lenders expect, with a financial model that recalculates from your own numbers.',
    reasons: [
      { icon: 'UtensilsCrossed', title: 'Built for a Restaurant with a Bar', desc: 'A cooking line, walk-in cooler, Type I hood with fire suppression and a grease interceptor; a bar with beer taps and a wine fridge; food and beverage sales with the alcohol share; seven roles on the staffing sheet; and the permits of a full-service restaurant, liquor license included. Nothing to strip out from a generic template.' },
      // TODO_CIFRA: ticket medio (excl. sales tax), margen bruto % y equilibrio en cubiertos/día del restaurante
      // de ejemplo (xlsx EN calibrado por la F2).
      { icon: 'BarChart3', title: 'Numbers Calculated, Not Copied', desc: 'Average check, gross margin and break-even come out of the workbook itself, from your assumptions. The example restaurant: an average check of TODO_CIFRA (excl. sales tax), TODO_CIFRA gross margin and break-even at TODO_CIFRA covers a day. Replace them with yours.' },
      { icon: 'ShieldCheck', title: 'Permits, Liquor License and 64 Tasks', desc: 'Zoning before you sign, building permits, health plan review, hood and fire inspections, certificate of occupancy, liquor license, insurance with liquor liability and employer registrations. A starting point: requirements vary by state, county and city.' },
      { icon: 'Banknote', title: 'Lender-Ready Format', desc: 'Written plan, 3-year P&L, break-even, 3 scenarios, cash flow and a loan schedule with DSCR, covering SBA 7(a) loans and SBA Microloans. Approval is never guaranteed, and it is a planning tool, not financial advice. One-time payment, no subscription.' },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and restaurant groups on opening restaurants and bars, combining hands-on operations with financial planning.',

  bonus: {
    subtitle:
      'Besides the business plan, the financial model and the opening checklist, you get these extra resources — worth $58',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Restaurant Permits & Licenses Guide (US + UK Notes, Liquor License Included)',
        value: '$29',
        desc: 'Section 9 of the plan plus Phases 1, 2 and 6 of the checklist: what a full-service restaurant usually needs and in what order — zoning check before you sign, building permits, health department plan review and food establishment permit, hood, fire suppression and fire marshal inspections, certificate of occupancy, and the liquor license (state and local approval, quota states, liquor liability and responsible service) — with notes for the UK. No state forms included: requirements vary by state, county and city.',
        image: '/lovable-uploads/ai-gallery/rbp-en-storefront.jpg',
      },
      {
        icon: 'BarChart3',
        label: 'BONUS 2',
        title: 'US Market Data & Industry Benchmarks (Sourced)',
        value: '$29',
        desc: 'The market section of the plan plus the reference table inside the workbook: industry ranges for cost of goods, labor, prime cost, overhead and rent, each with its source or marked "kit estimate" when there isn\'t one. Compare them with your own numbers before you talk to a lender.',
        image: '/lovable-uploads/ai-gallery/rbp-en-owner-plan.jpg',
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
    headingPre: "It's Time to Open Your ",
    headingGold: 'Restaurant',
    subtitle:
      'Test it on paper before you sign the lease: the written plan, the numbers behind it and the permits list, liquor license included, for a one-time payment.',
    items: [
      '10-section restaurant business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in covers a day, with a sensitivity table',
      '3 financial scenarios (pessimistic, base, optimistic)',
      'Opening checklist: 64 tasks in 7 phases',
      'BONUS: Restaurant Permits & Licenses Guide ($29)',
      'BONUS: US Market Data & Industry Benchmarks ($29)',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    priceOld: '$129',
    price: '$39',
    discountBadge: '-70%',
    heroNote: 'Special launch price. Going up soon',
    buyBoxNote: 'Special launch price — 70% off',
    bonusTotalLabel: 'Total value: $187 — business plan kit ($129) + 2 bonuses ($58)',
    bonusSaveLine: 'Save $90 TODAY!',
  },

  stickyLabel: 'RESTAURANT BUSINESS PLAN — $39',

  // D47: salientes a Financial Plan, HACCP y Staff Scheduling + los 3 planes hermanos.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'restaurant-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
