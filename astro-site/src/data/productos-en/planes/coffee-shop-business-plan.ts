// astro-site/src/data/productos-en/planes/coffee-shop-business-plan.ts
// TIENDA INTERNACIONAL EN — Coffee Shop Business Plan Kit. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/planes/plan-negocio-cafeteria.ts (mismo tipo PlanNegocioData, misma
// plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Gemela de
// food-truck-business-plan.ts (mismas decisiones; ver su cabecera).
// SPEC: scripts/productos-digitales/business-plans-en/SPEC.md (D1-D5, D20, D23, D25, D26, D28, D29 y §6).
//   · D1/D2: slug `coffee-shop-business-plan`, nombre «Coffee Shop Business Plan Kit», H1 Forma B
//     `Coffee Shop ` + oro `Business Plan` + subtítulo «Template: Word Plan + Excel Financial Projections
//     + Opening Checklist»; el concepto se describe como «coffee shop with brunch» (el modelo del ES).
//   · D3/D4: $39; priceOld $129; bonos $29; total $187; ahorro $90; «-70%» en hero y buyBox.
//   · D5: los 3 ficheros EN (dashboard CoffeeShopBusinessPlanDashboard.tsx y get-download-urls.ts).
//   · §6 aplicado: A3 (checklist = punto de partida), A7 (la tarjeta del DOCX va la PRIMERA del grid y la de
//     «Equipamiento» se funde con «Startup Costs» para seguir en 9), A8 («with reference prices», sin
//     «marcas de referencia»), A9 (fuera la «rotación por franja horaria»), A10 (fuera el «orden
//     recomendado de gestión»), A11 (bono 1 = guía de permisos US + notas UK, §9 del plan + fases 1-2 del
//     checklist; el cuadro de personal ya es una tarjeta del grid), A12-A14 (sin rating/review, sin
//     superlativo, sin ICO/ENISA/licencia inocua/SS/SMI).
//   · Compatibilidad, testimonios y TODO_CIFRA: como food-truck-business-plan.ts. Testimonios: fuera
//     «53 clientes/día con ticket medio €9,50» y «food cost 25-30 %» (cifras de la v1.1).
//   · FAQ: People Also Ask de «coffee shop business plan» (research §2) + las del ES adaptadas + UK,
//     moneda, suscripción, licencia y garantía. schema.faqs = el MISMO array.
//   · Imágenes: fotos propias sin texto (csbp-en-*) + use-case-cafeteria-brunch (sin rótulos). Las del ES
//     son miniaturas de 400 px o llevan precios en € y rótulos en español («CAFETERÍA EL SOL», «TERRAZA»).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_BUSINESS_PLAN (resuelto en el wrapper .astro).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// FAQ on-page Y FAQPage (un solo array).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What does a coffee shop business plan include?',
    a: 'The sections lenders, landlords and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written for a coffee shop with brunch in Word, plus the Excel financial projections that back them up and a 75-task opening checklist.',
  },
  {
    q: 'Is it a generic plan or built for a coffee shop?',
    a: 'Built for a coffee shop with brunch: espresso machine and grinders, pastry case, oven, refrigeration, dishwasher, bar, seating and patio in the startup costs; a coffee and food mix in the P&L; six roles in the staffing sheet (owner-barista, morning barista, afternoon barista-server, brunch cook, weekend extra and relief cover); and the permits of a fixed location: zoning, building permits, certificate of occupancy and the health department plan review.',
  },
  {
    q: 'How much does it cost to open a coffee shop?',
    // TODO_CIFRA: total de caja necesaria del coffee shop de ejemplo (Startup Costs, xlsx EN calibrado por la F2).
    a: "It depends on the space more than on the espresso machine: a unit that was already a cafe needs a fraction of the build-out of an empty shell, and rent and permits vary a lot by city. The Startup Costs sheet lists every line — LLC and legal, licenses and health plan review, architect and building permits, build-out, electrical and HVAC, plumbing with grease interceptor and hand sinks, espresso machine, grinders, oven, pastry case, refrigeration, dishwasher, bar, seating, patio, smallwares, signs, POS, opening inventory and launch marketing — plus deposits, pre-opening months, contingency and working capital. The kit's example coffee shop needs TODO_CIFRA in total cash; replace each line with your own quotes.",
  },
  {
    q: 'Can I open a coffee shop with $50k?',
    a: "A coffee shop with seating and a full build-out usually needs more than that. With $50,000 the realistic routes are a kiosk or a coffee cart, taking over a space that's already built out as a cafe, buying used equipment, or adding a loan or a partner to your own money. Put each option in the Startup Costs sheet: the financing sheet tells you how much you'd need to borrow and whether the loan payments still fit (DSCR).",
  },
  {
    q: 'How much does it cost to run a coffee shop per month?',
    a: 'Rent, payroll with employer taxes, coffee, milk and food, utilities, insurance, card fees, accounting, software, cleaning, waste, pest control, music licenses, marketing and your loan payments. The 12-month cash flow adds them up month by month — with seasonality and quarterly sales tax — and shows your lowest cash balance and the month it happens.',
  },
  {
    q: 'Is owning a coffee shop a profitable business?',
    a: 'It can be, but margins are tight and two lines usually decide it: rent and labor. The model checks your cost of goods, labor, rent and net margin against editable kit benchmarks (for example, rent up to 12% of sales and labor up to 35%) and runs three scenarios, so you can see whether the plan still works in a slow year before you sign a lease.',
  },
  {
    q: 'How much do coffee shop owners make a month?',
    a: "There's no honest single number: it depends on customers per day, average check, rent and how many hours you work behind the bar yourself. The 3-year P&L calculates it from your assumptions — revenue, cost of goods, gross margin, payroll, rent and other fixed costs, EBITDA, income tax and net profit — and the staffing sheet shows what the owner-barista role costs, so you can tell your salary apart from the business profit.",
  },
  {
    q: 'Can I start a cafe with no money?',
    a: "Not really: lenders, including SBA lenders, usually expect an owner equity injection (often around 10% for SBA start-ups; many want 20-30%), and landlords ask for a deposit and often a personal guarantee. What you can do is lower the cash you need: a smaller or second-generation space, used equipment, a partner who invests, or a local grant. The financing sheet shows the gap between what you need and what you have, and warns you when your sources fall short.",
  },
  {
    q: 'What permits do I need to open a coffee shop?',
    a: "It depends on your state, county and city. The usual list: a business structure (LLC or sole proprietorship), an EIN, a seller's permit and a business license; a zoning check before you sign the lease; building permits for the build-out and a certificate of occupancy; a health department plan review and food establishment permit; a sign permit; a sidewalk cafe permit if you put tables outside; and a liquor license only if you serve alcohol. The opening checklist organizes 75 tasks in 6 phases. Treat it as a starting point and confirm the details with your local authorities.",
  },
  {
    q: 'Can I present this plan to a lender, a landlord or investors?',
    a: "Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The financing sheet covers an SBA-guaranteed 7(a) loan through your bank, an SBA Microloan (up to $50,000, through nonprofit intermediaries), investors or partners and local grants. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.",
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: 'Yes. The green cells are the ones you type — rent, customers per day, average check, wages and any startup cost line — and more than 700 linked formulas recalculate the rest. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook includes an Instructions tab.',
  },
  {
    q: 'Does it work in the UK?',
    a: "Yes, with notes. Tax rates are editable cells: enter 20% VAT on eat-in sales and hot food (most cold takeaway food is zero-rated) and the VAT you can reclaim on purchases and on your build-out. The plan and the checklist add UK notes: register your food business with the council at least 28 days before you open, and expect a food hygiene rating inspection in your first months. UK minimum wage and employer National Insurance aren't preloaded: enter the current figures from gov.uk.",
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
  slug: 'coffee-shop-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_BUSINESS_PLAN',

  seo: {
    title:
      'Coffee Shop Business Plan Template: Word + Excel Financial Projections + Opening Checklist | AI Chef Pro',
    description:
      'Coffee shop business plan template: a 10-section Word plan, Excel financial projections (3-year P&L, break-even, 12-month cash flow, loan and DSCR) and a 75-task opening checklist. $39.',
    keywords:
      'coffee shop business plan, cafe business plan, coffee shop business plan template, coffee shop startup costs, how to open a coffee shop, coffee shop financial projections, coffee shop opening checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-coffee-shop-business-plan.jpg',
  },

  schema: {
    productName: 'Coffee Shop Business Plan Kit',
    productDescription:
      'Coffee shop business plan template kit for a coffee shop with brunch: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions) and a 75-task opening checklist in 6 phases. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Coffee Shop Business Plan Kit',
  },

  images: {
    // hero bg (6) — fotos propias sin texto + el brunch de los usos (sin rótulos). Las plan-cafeteria-* del
    // ES son miniaturas de 400 px y varias llevan precios en € o rótulos en español.
    gallery: [
      '/lovable-uploads/ai-gallery/csbp-en-hero.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-barista.jpg',
      '/lovable-uploads/ai-gallery/use-case-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-pastry-case.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-storefront.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el ES.
    gridGallery: [
      '/lovable-uploads/ai-gallery/csbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-barista.jpg',
      '/lovable-uploads/ai-gallery/use-case-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-pastry-case.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-storefront.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-hero.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/csbp-en-barista.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-cafeteria-brunch.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/csbp-en-hero.jpg',
  },


  hero: {
    badge: 'Lender-ready coffee shop business plan: Word + Excel + checklist',
    titlePre: 'Coffee Shop ',
    titleGold: 'Business Plan',
    titleSubtitle: 'Template: Word Plan + Excel Financial Projections + Opening Checklist',
    description:
      'Everything you need to plan and pitch a coffee shop with brunch: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even, 12-month cash flow and loan payments from your own numbers; and a 75-task checklist from the zoning check before you sign the lease to your first 90 days open. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section coffee shop business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even and 12-month cash flow',
      'Startup costs line by line, from build-out to espresso machine',
      'Opening checklist: 75 tasks in 6 phases, from zoning to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      '9 building blocks to test whether your coffee shop works on paper before you sign a lease, and to present it to a lender, a landlord or an investor.',
    templates: [
      { icon: 'FileText', title: 'Coffee Shop Business Plan (Word, 10 Sections)', desc: 'A complete plan already written for a coffee shop with brunch: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements, permits and licenses, and conclusions with an action plan. Its figures are the ones in the example Excel model.' },
      { icon: 'FileSpreadsheet', title: 'Coffee Shop Financial Projections (Excel, 9 Sheets)', desc: 'Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than 700 linked formulas: change a green cell and the whole workbook recalculates.' },
      { icon: 'Coins', title: 'Startup Costs & Equipment', desc: 'Build-out, electrical and HVAC, plumbing with grease interceptor and hand sinks, a 2-group espresso machine, grinders, oven, pastry case, refrigeration, dishwasher, bar, seating and patio, each with a reference price you replace with your quotes, plus deposits, pre-opening months, contingency and working capital. The total cash you need is calculated separately.' },
      { icon: 'TrendingUp', title: 'Break-Even Point', desc: 'How many customers a day you need at your average check (excl. sales tax), and the cash break-even with loan payments in and depreciation out. Margin of safety, a sensitivity table for average check and variable cost, and a plain-English reading of the result.' },
      { icon: 'BarChart3', title: 'Financial Scenarios', desc: 'Three scenarios side by side — pessimistic, base and optimistic — each with its own estimated cash balance. Useful for a lender, a landlord or an investor.' },
      { icon: 'Users', title: 'Staffing & Payroll Costs', desc: 'Six roles — owner-barista, morning barista, afternoon barista-server, brunch cook, weekend extra and relief cover — with gross pay, employer payroll taxes, the real cost of each role and two alerts: pay below the minimum wage for the hours worked, and service hours left uncovered.' },
      { icon: 'ShieldCheck', title: 'Opening Checklist (75 Tasks, 6 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license), location and permits (zoning, lease review, building permits, certificate of occupancy, health plan review), build-out and equipment, staff, pre-opening marketing and your first 90 days." },
      { icon: 'ListChecks', title: 'Coffee Shop Benchmarks', desc: "Your plan's ratios — cost of goods, labor, rent and net margin — each marked OK or REVIEW against an editable kit benchmark, next to a reference table of industry ranges with their source (or \"kit estimate\" when there isn't one)." },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity, an SBA-guaranteed 7(a) loan through your bank, an SBA Microloan, investors or partners and local grants, with the loan amortization schedule, the debt service coverage ratio (DSCR) year by year against a 1.25× target and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Cafetería, la edición española.
  // Las cifras que eran del producto v1.1 se reformulan sin número (ver cabecera). Solo se pintan.
  testimonials: {
    subtitle:
      'Owners and investors who opened their coffee shop or brunch spot with the Spanish edition of this plan',
    items: [
      { name: 'Alejandro Ruiz', role: 'Specialty coffee shop owner, Madrid, Spain', text: 'The financial plan helped me get a government-backed ICO loan in Spain. The startup cost breakdown — coffee machine, oven, furniture — was spot on, with no surprises.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Brunch entrepreneur, Barcelona, Spain', text: 'Thanks to the opening checklist I didn\'t miss a single step. Getting the right activity license in Spain was key to opening fast and without delays.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Hospitality investor', text: 'The break-even calculation is realistic. Numbers that match the real coffee shop market.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Partner, coffee & brunch spot in Seville, Spain', text: 'The financial scenarios gave us the confidence to sign the lease. We knew exactly how much we needed to sell to be profitable.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Hospitality consultant', text: 'I recommend it to anyone who wants to open a coffee shop in Spain. Real industry numbers, not filler templates.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Coffee shop owner, Valencia, Spain', text: 'The coffee cost ratios and the staffing sheet with employer costs saved me mistakes worth thousands of euros before I signed anything.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex-corporate, opened a coffee & brunch spot', text: 'I knew nothing about hospitality licenses. The checklist with its 6 phases guided me step by step. I opened in 3 months without a single legal problem.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Owner, chain of 3 coffee shops', text: 'We\'ve used the Excel financial plan for our 3 openings. You just change the location and you have a professional business plan ready to present.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a coffee shop plan written for the format lenders expect, with a financial model that recalculates from your own numbers.',
    reasons: [
      { icon: 'Coffee', title: 'Built for a Coffee Shop', desc: 'Espresso machine and grinders, pastry case, a coffee and brunch menu mix, an owner-barista on the schedule and the permits of a fixed location. Nothing to strip out from a generic restaurant template.' },
      // TODO_CIFRA: ticket medio (excl. sales tax), margen bruto % y equilibrio en clientes/día del coffee shop
      // de ejemplo (xlsx EN calibrado por la F2).
      { icon: 'BarChart3', title: 'Numbers Calculated, Not Copied', desc: 'Average check, gross margin and break-even come out of the workbook itself, from your assumptions. The example coffee shop: an average check of TODO_CIFRA (excl. sales tax), TODO_CIFRA gross margin and break-even at TODO_CIFRA customers a day. Replace them with yours.' },
      { icon: 'ShieldCheck', title: 'Zoning, Permits and 75 Tasks', desc: 'Zoning before you sign, building permits, certificate of occupancy, health plan review, sign and sidewalk cafe permits, employer registrations and a privacy notice for your loyalty list. A starting point: requirements vary by state, county and city.' },
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised owners of coffee shops, brunch spots and cafes, combining hands-on operations with financial planning.',

  bonus: {
    subtitle:
      'Besides the business plan, the financial model and the opening checklist, you get these extra resources — worth $58',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Coffee Shop Permits & Licenses Guide (US + UK Notes)',
        value: '$29',
        desc: 'Section 9 of the plan plus Phases 1 and 2 of the checklist: what a fixed-location coffee shop usually needs and in what order — zoning check before you sign, building permits, certificate of occupancy, health department plan review and food establishment permit, sign permit, sidewalk cafe permit and a liquor license only if you serve alcohol — with notes for the UK. No state forms included: requirements vary by state, county and city.',
        image: '/lovable-uploads/ai-gallery/csbp-en-storefront.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Coffee Shop Benchmarks (Reference Table)',
        value: '$29',
        desc: 'The reference table inside the workbook: cost of goods, labor, rent and net margin, each with its source or marked "kit estimate", and the OK / REVIEW check that tells you where your plan departs from the benchmark. Every threshold is an editable cell.',
        image: '/lovable-uploads/ai-gallery/csbp-en-owner-plan.jpg',
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
    headingGold: 'Coffee Shop',
    subtitle:
      'Test it on paper before you sign the lease: the written plan, the numbers behind it and the permits list, for a one-time payment.',
    items: [
      '10-section coffee shop business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even and cash break-even, with a sensitivity table',
      '3 financial scenarios (pessimistic, base, optimistic)',
      'Opening checklist: 75 tasks in 6 phases',
      'BONUS: Coffee Shop Permits & Licenses Guide ($29)',
      'BONUS: Coffee Shop Benchmarks ($29)',
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

  stickyLabel: 'COFFEE SHOP BUSINESS PLAN — $39',

  // D29: salientes a Financial Plan, HACCP y Staff Scheduling (+ el plan hermano).
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'coffee-shop-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
