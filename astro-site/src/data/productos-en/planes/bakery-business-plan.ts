// astro-site/src/data/productos-en/planes/bakery-business-plan.ts
// TIENDA INTERNACIONAL EN — Bakery Business Plan Kit. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/planes/plan-negocio-panaderia.ts (mismo tipo PlanNegocioData, misma
// plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Gemela de
// restaurant-business-plan.ts (mismas decisiones; ver su cabecera).
// SPEC: scripts/productos-digitales/business-plans-en-2/SPEC-delta.md (D30-D47 y §4 R1-R12) + la heredada.
//   · D30: slug `bakery-business-plan`, nombre «Bakery Business Plan Kit», H1 Forma B `Bakery ` + oro
//     `Business Plan` + «Template for a Retail & Wholesale Bakery: …». Concepto: «artisan bakery with a
//     storefront, a small cafe corner and wholesale to cafes».
//   · D31: $39; priceOld $129; bonos $29; total $187; ahorro $90; «-70%» en hero y buyBox.
//   · D32: los 3 ficheros EN (dashboard BakeryBusinessPlanDashboard.tsx y get-download-urls.ts).
//   · D36 (E3): parte EXENTA del sales tax en la línea de panadería (para llevar + mayorista con resale
//     certificate); se describe sin cifra (H10 es editable). D39: obrador COMERCIAL, no cottage food (FAQ).
//   · D45: tarjeta DOCX la primera del grid; «Equipamiento» fundida con «Startup Costs» (sigue en 9);
//     «Ratios de Referencia» fundida con «Instructions» (si no, doble cómputo con el bono 2). Bonos: 1 «Bakery
//     Permits & Licenses Guide (commercial vs cottage food, US + UK notes)» = §9 + fases 1 y 2 del checklist;
//     2 «Bakery Industry Benchmarks (sourced)» = §3 del docx + tabla D19.
//   · §4: R6 (sin SS 33 %, 14 pagas, RGSEAA, licencia clasificada, «Registro Sanitario + 66 trámites»), R7
//     (sin leasing de horno), R8 (el mayorista va dentro de la línea de panadería con su parte exenta; los
//     escenarios mueven transacciones, ticket y días, no el mix), R9 (una sola tabla de referencias, la del
//     bono 2), R10 (sin rating, superlativo ni «737 fórmulas»), R11 (cifras del xlsx EN, no del docx v1.1).
//   · Testimonios (orquestador, como FT/CAF): los 8 del ES traducidos con el subtítulo de la edición
//     española, sin lo que el producto EN no tiene («60+ trámites», «leasing del horno», «break-even por
//     kilos de pan», «plus nocturnidad», «margen real superior al 25 %», «materia prima 22-28 %, merma 3-5 %,
//     margen bollería >75 %», «mix de producción»). Se conservan las cifras personales (65.000 EUR, 800 EUR
//     al mes, 4 meses, 3 aperturas) y las «6 fases» (el checklist EN también tiene 6).
//   · Cifras del caso US: TODO_CIFRA con comentario encima (cifras_caso.json de la F2).
//   · FAQ: People Also Ask de «bakery business plan» (research delta §2) + «how to start a bakery business»,
//     «bakery startup costs», cottage food vs comercial (D39), sales tax del pan (D36) + UK, moneda,
//     suscripción, licencia y garantía. schema.faqs = el MISMO array.
//   · Imágenes: fotos propias sin texto (bbp-en-*) + use-case-panadero-panes (sin rótulos). Las del ES son
//     en parte miniaturas de 400 px.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_BAKERY_BUSINESS_PLAN (resuelto en el wrapper .astro).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// FAQ on-page Y FAQPage (un solo array).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What should a bakery business plan include?',
    a: 'The sections lenders, landlords and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written for a retail and wholesale bakery in Word, plus the Excel financial projections that back them up and a 66-task opening checklist.',
  },
  {
    q: 'Is it a generic plan or built for a bakery?',
    a: 'Built for an artisan bakery with a storefront, a small cafe corner and wholesale to cafes: deck or rack oven, spiral mixer, divider-rounder, proofer and retarder, refrigeration, stainless benches, sheeter, display case and counter in the startup costs; a bakery line that combines retail and wholesale, with an editable tax-exempt share, plus coffee and drinks in the P&L; six roles in the staffing sheet (head baker-owner, baker, bakery assistant, counter staff, weekend extra and relief cover) with the early-morning production shift; and the permits of a commercial bakery.',
  },
  {
    q: 'How much does it cost to open a bakery?',
    // TODO_CIFRA: caja total necesaria de la bakery de ejemplo (Startup Costs, xlsx EN calibrado por la F2).
    a: "It depends on the model and on the space: a storefront bakery with its own production room costs far more than a home-based cottage food business, and a unit that already has the electrical service and ventilation for commercial ovens saves a big part of the build-out. Equipment is usually the largest line, and buying part of it used is the most common way to lower it. The Startup Costs sheet lists every line — LLC and legal, licenses and plan review, build-out, electrical service for the ovens, ventilation, deck or rack oven, spiral mixer, divider-rounder, proofer and retarder, refrigeration, benches and shelving, sheeter, display case and counter, shop furniture, POS with scale, signs, launch marketing and opening inventory — plus deposits, pre-opening months, contingency and working capital. The kit's example bakery needs TODO_CIFRA in total cash; replace each line with your own quotes.",
  },
  {
    q: 'Is a bakery a profitable business?',
    a: 'It can be, but margins are thin across food retail, and a bakery adds two pressures of its own: labor, because bread is made by hand in the early hours, and waste from product that doesn\'t sell. The model checks your numbers against editable kit benchmarks — gross margin of at least 60%, cost of goods up to 33%, labor up to 38%, rent up to 10% and net margin of at least 5% — marks each one OK or REVIEW and runs three scenarios, so you can see whether the plan still works in a slow year.',
  },
  {
    q: 'How much does a bakery owner make per month?',
    a: "There's no honest single number: it depends on transactions per day, average check, wholesale volume, rent and how many hours you bake yourself. The 3-year P&L calculates it from your assumptions — revenue, cost of goods, gross margin, payroll, rent and other fixed costs, EBITDA, income tax and net profit — and the staffing sheet shows what the head baker-owner role costs, so you can tell your salary apart from the business profit.",
  },
  {
    q: 'How do I start a small bakery business?',
    a: "Decide your model first — retail storefront, wholesale to cafes and restaurants, a bakery-cafe or a home-based cottage food business — because each one has different costs and permits. Then test the numbers, check the zoning before you sign a lease, form your LLC and get your EIN, seller's permit and business license, get your kitchen licensed by the health or agriculture department, install and inspect the ovens, hire your team and open with a soft launch. The opening checklist organizes those steps into 66 tasks in 6 phases.",
  },
  {
    q: 'Can I start a bakery with no money?',
    a: "Not a storefront bakery: lenders, including SBA lenders, usually expect an owner equity injection (often around 10% for SBA start-ups; many want 20-30%), and landlords ask for a deposit and often a personal guarantee. Lower-cost ways in are selling under your state's cottage food law from home, renting time in a shared commercial kitchen, buying used equipment or bringing in a partner. When you're ready for your own space, the financing sheet shows the gap between what you need and what you have, and warns you when your sources fall short.",
  },
  {
    q: "What's the difference between a cottage food bakery and a commercial bakery?",
    a: "Cottage food laws let you make certain lower-risk foods in your home kitchen and sell them, usually direct to consumers and within limits that vary by state. A bakery with a storefront that also sells to cafes and restaurants is a commercial food business: it needs a licensed commercial kitchen, inspections and the permits of a fixed location. This kit is built for that commercial bakery; section 9 of the plan and the checklist explain the difference so you know which rules apply to you.",
  },
  {
    q: 'What permits do I need to open a bakery?',
    a: "It depends on your state, county and city. The usual list: a business structure (LLC or sole proprietorship), an EIN, a seller's permit and a business license; a zoning check before you sign the lease; building, electrical, plumbing and gas permits, with ventilation for the ovens; a food establishment permit from the health department or a license from the state agriculture department, depending on your state and on how much you sell wholesale; FDA food facility registration if you sell mainly wholesale rather than direct to consumers; ingredient and allergen labels for what you sell packaged or wholesale; and a sign permit. The opening checklist covers them in 66 tasks. Treat it as a starting point and confirm the details with your local authorities.",
  },
  {
    q: 'Do I charge sales tax on bread and pastries?',
    a: "It depends on your state. In many states, bakery goods sold to go count as exempt food while food eaten on the premises is taxed, and a sale to a cafe that resells your bread goes with a resale certificate. The workbook has an editable tax-exempt share for the bakery line, so the cash flow only collects sales tax on the taxable part. Check your state's rules: set the share to 0 and everything is taxed.",
  },
  {
    q: 'Can I present this plan to a lender, a landlord or investors?',
    a: "Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The financing sheet covers an SBA-guaranteed 7(a) loan through your bank, an SBA Microloan (up to $50,000, through nonprofit intermediaries), investors or partners and local grants. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.",
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: 'Yes. The green cells are the ones you type — rent, transactions per day, average check, the tax-exempt share, wages and any startup cost line — and more than 700 linked formulas recalculate the rest. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook includes an Instructions tab.',
  },
  {
    q: 'Does it work in the UK?',
    a: "Yes, with notes. Tax rates are editable cells: most bread and cold bakery goods sold to take away are zero-rated, while hot food and anything eaten in pays 20% VAT, so set the exempt share and the rate to match your sales, plus the VAT you can reclaim on purchases and on your build-out. The plan and the checklist add UK notes: register your food business with the council at least 28 days before you open, expect a food hygiene rating inspection in your first months, and label the 14 allergens. UK minimum wage and employer National Insurance aren't preloaded: enter the current figures from gov.uk.",
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
  slug: 'bakery-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_BAKERY_BUSINESS_PLAN',

  seo: {
    title:
      'Bakery Business Plan Template: Word + Excel Financial Projections + Opening Checklist | AI Chef Pro',
    description:
      'Bakery business plan template for a retail and wholesale bakery: a 10-section Word plan, Excel financial projections (3-year P&L, break-even, cash flow, loan and DSCR) and a 66-task opening checklist. $39.',
    keywords:
      'bakery business plan, bakery business plan template, how to start a bakery business, bakery startup costs, bakery financial projections, bakery opening checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-bakery-business-plan.jpg',
  },

  schema: {
    productName: 'Bakery Business Plan Kit',
    productDescription:
      'Bakery business plan template kit for an artisan bakery with a storefront and wholesale accounts: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions) and a 66-task opening checklist in 6 phases. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Bakery Business Plan Kit',
  },

  images: {
    // hero bg (6) — fotos propias sin texto + los panes de los usos (sin rótulos).
    gallery: [
      '/lovable-uploads/ai-gallery/bbp-en-hero.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-oven.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-bench.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-wholesale.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el ES.
    gridGallery: [
      '/lovable-uploads/ai-gallery/bbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-oven.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-bench.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-wholesale.jpg',
      '/lovable-uploads/ai-gallery/bbp-en-hero.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/bbp-en-bench.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/bbp-en-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready bakery business plan: Word + Excel + checklist',
    titlePre: 'Bakery ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Retail & Wholesale Bakery: Word Plan + Excel Financial Projections + Opening Checklist',
    description:
      'Everything you need to plan and pitch an artisan bakery with a storefront and wholesale accounts: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even, 12-month cash flow and loan payments from your own numbers; and a 66-task checklist from the zoning check before you sign the lease to your first 90 days open. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section bakery business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even and 12-month cash flow',
      'Startup costs line by line, from deck oven and mixer to display case',
      'Opening checklist: 66 tasks in 6 phases, commercial bakery permits included',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      '9 building blocks to test whether your bakery works on paper before you sign a lease, and to present it to a lender, a landlord or an investor.',
    templates: [
      { icon: 'FileText', title: 'Bakery Business Plan (Word, 10 Sections)', desc: 'A complete plan already written for an artisan bakery with a storefront, a small cafe corner and wholesale to cafes: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements, permits and licenses, and conclusions with an action plan. Its figures are the ones in the example Excel model.' },
      { icon: 'FileSpreadsheet', title: 'Bakery Financial Projections (Excel, 9 Sheets)', desc: 'Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than 700 linked formulas: change a green cell and the whole workbook recalculates.' },
      { icon: 'Coins', title: 'Startup Costs & Equipment', desc: 'Build-out, electrical service for the ovens, bakery ventilation, deck or rack oven, spiral mixer, divider-rounder, proofer and retarder, refrigeration, stainless benches and shelving, sheeter, display case and counter, shop furniture, POS with scale and signs, each with a reference price you replace with your quotes, plus deposits, pre-opening months, contingency and working capital. The total cash you need is calculated separately.' },
      { icon: 'TrendingUp', title: 'Break-Even Point', desc: 'How many transactions a day you need at your average check (excl. sales tax), and the cash break-even with loan payments in and depreciation out. Margin of safety, a sensitivity table for average check and variable cost, and a plain-English reading of the result.' },
      { icon: 'BarChart3', title: 'Financial Scenarios', desc: 'Three scenarios side by side — pessimistic, base and optimistic — that move transactions per day, average check and opening days, each with its own estimated cash balance. Useful for a lender, a landlord or an investor.' },
      { icon: 'Users', title: 'Staffing & Payroll Costs', desc: 'Six roles — head baker-owner, baker, bakery assistant, counter staff, weekend extra and relief cover — with gross pay, employer payroll taxes, the real cost of each role and two alerts: pay below the minimum wage for the hours worked, and hours left uncovered across opening hours and the early-morning production shift.' },
      { icon: 'ShieldCheck', title: 'Opening Checklist (66 Tasks, 6 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license, the health or agriculture license), location and permits (zoning, lease, building and gas permits, oven ventilation, electrical service), equipment, staff, marketing (wholesale accounts with cafes and restaurants included) and your first 90 days." },
      { icon: 'ListChecks', title: 'Instructions & Ratio Checks', desc: 'An Instructions tab that explains every sheet and which cells to type, plus five checks on the P&L — gross margin, cost of goods, labor, rent and net margin — each marked OK or REVIEW against an editable kit benchmark.' },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity, an SBA-guaranteed 7(a) loan through your bank, an SBA Microloan, investors or partners and local grants, with the loan amortization schedule, the debt service coverage ratio (DSCR) year by year against a 1.25× target and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Panadería, la edición española.
  // Las cifras del producto ES que el EN no tiene se reformulan sin número (ver cabecera). Solo se pintan.
  testimonials: {
    subtitle:
      'Master bakers, artisan bakery owners and investors who opened their bakery with the Spanish edition of this plan',
    items: [
      { name: 'Alejandro Ruiz', role: 'Master baker, Madrid, Spain', text: 'I took the plan to my bank in Spain and they approved EUR 65,000 of financing. The 3-year projection with seasonality was key for them to trust the project.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Bakery entrepreneur, Barcelona, Spain', text: 'The checklist got me through the maze of Spain\'s food registry and the bakery license. It would have taken me twice as long without a guide organized by phase.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Food industry investor', text: 'I use this plan to evaluate bakery projects in my portfolio. The break-even point and the cost ratios are exactly what I need to see.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Artisan bakery owner, Seville, Spain', text: 'The staffing sheet with the early-morning shift was an eye-opener. I used to get the head baker\'s costs wrong. Now my margins are real.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Hospitality & bakery consultant', text: 'I recommend it to all my bakery clients in Spain. Real industry numbers, not filler templates.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Bakery-cafe owner, Valencia, Spain', text: 'The reference ratios helped me renegotiate prices with my flour mill. I saved EUR 800 a month.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex-corporate, opened a bakery', text: 'I came from finance and knew nothing about bakery licenses in Spain. The checklist with its 6 phases guided me step by step. I opened in 4 months without legal delays.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Partner, chain of 3 bakeries', text: 'We\'ve used the Excel financial plan for our 3 openings. You just change the numbers for each location and you have a professional business plan ready for investors.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a bakery plan written for the format lenders expect, with a financial model that recalculates from your own numbers.',
    reasons: [
      { icon: 'Wheat', title: 'Built for a Bakery', desc: 'Deck or rack oven, spiral mixer, divider-rounder, proofer and retarder, sheeter and display case; a bakery line that combines retail and wholesale with an editable tax-exempt share; the early-morning production shift on the staffing sheet; and the permits of a commercial bakery, not a home kitchen. Nothing to strip out from a generic restaurant template.' },
      // TODO_CIFRA: ticket medio (excl. sales tax), margen bruto % y equilibrio en transacciones/día de la bakery
      // de ejemplo (xlsx EN calibrado por la F2).
      { icon: 'BarChart3', title: 'Numbers Calculated, Not Copied', desc: 'Average check, gross margin and break-even come out of the workbook itself, from your assumptions. The example bakery: an average check of TODO_CIFRA (excl. sales tax), TODO_CIFRA gross margin and break-even at TODO_CIFRA transactions a day. Replace them with yours.' },
      { icon: 'ShieldCheck', title: 'Commercial Bakery Permits and 66 Tasks', desc: 'Zoning before you sign, building, electrical and gas permits, oven ventilation, the health department or state agriculture license, allergen labels for what you sell packaged or wholesale and employer registrations, plus how a commercial bakery differs from a cottage food operation. A starting point: requirements vary by state, county and city.' },
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
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised master bakers, artisan bakery owners and bakery chains, combining hands-on operations with financial planning.',

  bonus: {
    subtitle:
      'Besides the business plan, the financial model and the opening checklist, you get these extra resources — worth $58',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Bakery Permits & Licenses Guide (Commercial vs Cottage Food, US + UK Notes)',
        value: '$29',
        desc: 'Section 9 of the plan plus Phases 1 and 2 of the checklist: why a bakery with a storefront and wholesale accounts needs a licensed commercial kitchen and not a cottage food permit, who licenses it in your state (health department or agriculture department), zoning, building and gas permits, oven ventilation, when FDA food facility registration applies, sales tax on bakery goods to go and resale certificates for wholesale — with notes for the UK. No state forms included: requirements vary by state, county and city.',
        image: '/lovable-uploads/ai-gallery/bbp-en-wholesale.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Bakery Industry Benchmarks (Sourced)',
        value: '$29',
        desc: 'The market section of the plan plus the reference table inside the workbook: industry ranges for cost of goods, labor and margin in bakeries, each with its source or marked "kit estimate" when there isn\'t one. Compare them with your own numbers before you talk to a lender.',
        image: '/lovable-uploads/ai-gallery/bbp-en-owner-plan.jpg',
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
    headingGold: 'Bakery',
    subtitle:
      'Test it on paper before you sign the lease: the written plan, the numbers behind it and the permits list for a commercial bakery, for a one-time payment.',
    items: [
      '10-section bakery business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in transactions a day, with a sensitivity table',
      '3 financial scenarios (pessimistic, base, optimistic)',
      'Opening checklist: 66 tasks in 6 phases',
      'BONUS: Bakery Permits & Licenses Guide ($29)',
      'BONUS: Bakery Industry Benchmarks ($29)',
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

  stickyLabel: 'BAKERY BUSINESS PLAN — $39',

  // D47: salientes a Financial Plan, HACCP y Staff Scheduling + los 3 planes hermanos.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'bakery-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
