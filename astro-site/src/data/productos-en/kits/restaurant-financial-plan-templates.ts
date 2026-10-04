// astro-site/src/data/productos-en/kits/restaurant-financial-plan-templates.ts
// TIENDA INTERNACIONAL EN — Restaurant Financial Plan Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha
// ES astro-site/src/data/productos/kits/kit-plan-financiero.ts (mismo tipo, misma plantilla
// KitExcelLandingPage, mismo orden de campos). Patrón = restaurant-schedule-templates.ts (ola 3).
// SPEC: scripts/productos-digitales/financial-kit/SPEC.md (§6 = esta landing).
//   · D2: nombre «Restaurant Financial Plan Kit Pro»; title SEO y H1 = «Restaurant Financial Plan Kit
//     Pro: Restaurant P&L Template & Financial Projections for Excel». H1 en Forma B como los hermanos
//     EN; el reparto del dorado es el de SPEC §6 (`Restaurant ` + gold `Financial Plan` + ` Kit Pro`).
//     El subtítulo del ES («Planifica, Controla y Presenta tus Números» → «Plan, track and present your
//     numbers») abre la descripción del hero para que el texto del H1 siga siendo exactamente el de D2.
//   · D5: títulos de las 10 plantillas = los de los xlsx EN (§2.1, dl/restaurant-financial-plan-templates/).
//   · D3: $49, pago único. D4: priceOld 190 € → $199; cada bono 14 € → $19. Derivados: bonos $38 ·
//     total $237 · ahorro $150 (199 − 49, como el ES) · descuento 1 − 49/199 = 75,4 % → «-75%» en hero
//     Y buyBox (el «72 %» del buyBoxNote del ES era un quirk y no se copia).
//   · Cifras SOLO de SPEC §3 y §5: sales tax 8 % de ejemplo y trimestral (D8), vidas útiles 10/7/7/5
//     (D10), préstamo de ejemplo tipo SBA 7(a) a 10 años con interest-only opcional (D12), DSCR a cuota
//     completa contra 1.25× (objetivo habitual del prestamista; el suelo SBA «depende de la operación y del
//     SOP vigente»; el 1.15 nunca se presenta como mínimo SBA) y aportación propia «often around 10 % for start-ups» como
//     expectativa habitual, no mínimo (D13, D25, D26 de la revisión final), sq ft (D14), benchmarks US full-service
//     como estimación editable del kit (D15), restaurante de ejemplo con EBITDA ≈ 17.3 % (§5). Sin
//     «bank-approved», «SBA-approved», financiación garantizada ni asesoría fiscal o financiera: la
//     línea «A planning tool, not financial or tax advice» va en el why y en la FAQ del lender.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 8 del ES traducidos tal cual
//     (nombres, negocios y cifras de origen, importes en EUR sin el signo), con el subtítulo de la
//     edición española (TIENDA §3.5). Única adaptación: donde el ES habla de bancos o fiscalidad se
//     precisa que son españoles, para que no se lea como una promesa sobre un banco de EE. UU.
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC §6 y §9: IRR, gráficos y
//     protección), en toda la landing y en el dashboard (RestaurantFinancialPlanKitDashboard.tsx). El
//     resto, como los kits EN hermanos (Excel, LibreOffice, Numbers) + US Letter. Cuando el test pase:
//     añadir la pastilla, el subtítulo de compatApps, una FAQ y el aviso del dashboard.
//   · FAQ: People Also Ask de «restaurant p&l template» (SPEC §6) + las 6 del ES adaptadas + UK +
//     moneda y suscripción (como los hermanos EN). La licencia es la de la tienda EN (un negocio con
//     todos sus locales; consultores sin entregar copias). schema.faqs = el MISMO array (COM-21 del ES).
//   · Imágenes (revisión final): portada propia fin-en-hero.jpg (hero, galería y CTA) y foto de reunión
//     propia fin-en-lender-meeting.jpg (galería y BONUS 2), ambas sin texto; las del ES que se iban
//     (plan-financiero-hero/-reunion) llevaban fechas de 2023-2024 y rótulos de IA. OG propia:
//     og-financial-plan-kit.jpg. Se conservan del ES plan-financiero-restaurante.jpg y las fin-en-* de F3.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_FINANCIAL_PLAN_KIT (resuelto en el wrapper .astro).
import type { KitExcelData, KitExcelFaq } from '../../productos/kits/types';

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: KitExcelFaq[] = [
  {
    q: 'How do you do a P&L for a restaurant?',
    a: 'Start with revenue by line (dine-in, bar, delivery, events), excluding sales tax. Subtract food cost and beverage cost, then labor (wages plus employer payroll taxes), delivery platform fees, rent, utilities and the rest of your operating costs to get EBITDA. Do it every month and compare it with your budget. The Restaurant P&L Template: Monthly Budget vs Actual comes set up that way, with one tab per month (actual, budget, variance and a traffic light) and an annual summary that adds up the 12 months. The Lender & Investor Summary carries the P&L on to depreciation, interest, income tax and net profit over 5 years.',
  },
  {
    q: 'Can I create my own P&L statement?',
    a: "Yes. A P&L (profit and loss statement, or income statement) is revenue minus costs over a period, and to run a restaurant a monthly spreadsheet is enough. What makes it useful is consistency: the same lines every month, revenue excluding sales tax, and a budget to compare against. For your tax return or year-end financial statements, work with your accountant: a management P&L doesn't replace them.",
  },
  {
    q: 'How do you calculate profit and loss for a restaurant?',
    a: 'Revenue (excluding sales tax) minus food and beverage cost gives you gross profit. Gross profit minus labor and operating expenses gives you EBITDA. EBITDA minus depreciation and interest gives you profit before tax (EBT), and EBT minus income tax gives you net profit. Divide each line by revenue to get the percentages you compare month to month: food cost %, labor cost %, prime cost % and EBITDA margin. The templates do every one of these calculations as soon as you enter your numbers.',
  },
  {
    q: 'What is the 30/30/30 rule for restaurants?',
    a: "It's a rule of thumb, not a standard: roughly 30% of sales goes to food and beverage costs, 30% to labor and 30% to operating expenses, leaving about 10% as profit. It works as a quick sanity check, but the right numbers depend on your concept. The Restaurant Financial Ratios & KPI Dashboard measures your own food cost, labor cost and prime cost against an editable Benchmarks table: by default, food cost is fine up to 28% and an alert above 32%, labor up to 30% and above 35%, and prime cost (food + beverage + labor) up to 60% and above 65%. Those defaults are kit estimates for US full-service restaurants: change them to fit your concept.",
  },
  {
    q: 'What is a reasonable profit margin for a restaurant?',
    a: "It depends on the concept, the location and whether you own or lease the space, so be wary of any single number. As a planning reference, the kit's Benchmarks table treats an EBITDA margin of 15% or more as healthy and under 10% as an alert for a full-service restaurant; they are kit estimates you can edit, not an industry statistic. Net profit comes in lower than EBITDA once depreciation, interest and income tax are paid. The kit's example restaurant (60 seats, an average check of 22, 55 covers a day, 26 days a month) comes out at about 17.3% EBITDA.",
  },
  {
    q: "Does it work for a restaurant that's already open?",
    a: 'Yes. The monthly P&L budget vs actual, the KPI dashboard and the cash flow forecast are especially useful for restaurants that are already trading. The financial projections and the Lender & Investor Summary are more for openings or expansions.',
  },
  {
    q: 'Do I need to know accounting?',
    a: 'No. The templates are built for restaurant operators, not accountants. You enter your numbers (sales, costs, investments) and the formulas calculate everything else: ratios, charts and scenarios.',
  },
  {
    q: 'Will a lender accept the Lender & Investor Summary?',
    a: "It gives you the structure lenders and investors usually ask for: an executive summary, 5-year projections, IRR, NPV, payback, solvency ratios with the DSCR, and the collateral you can offer. The example loan follows the shape of an SBA 7(a) loan (10 years, with an optional interest-only period). The DSCR is calculated on the full loan payment and checked against 1.25×, the usual lender target; the SBA floor depends on the transaction and the current SOP. SBA lenders usually expect an owner equity injection (often around 10% for start-ups): check the current SOP with your lender. Approval always depends on your project, your credit and the lender. It's a planning tool, not financial or tax advice: review the final numbers with your accountant before you apply.",
  },
  {
    q: 'Are the templates linked to each other?',
    a: "They're consistent with each other: the same revenue and expense lines, the same ratios and the same base excluding sales tax in 9 of the 10 (the cash flow forecast includes the sales tax you collect because it's cash, and says so on its Instructions tab). Inside each workbook the formulas are chained (month, annual total, summary); between workbooks they aren't, so you can move or open each template on its own without breaking a reference.",
  },
  {
    q: 'Can I use it for several restaurants or with my clients?',
    a: "One purchase covers one business, with all of its locations, which makes it a good fit for restaurant groups and multi-unit operators. If you are a consultant or an investor, you can use the templates with the projects you advise, but you can't hand them copies: each business buys its own.",
  },
  {
    q: 'Does it work in the UK?',
    a: 'Yes. Tax rates are editable cells, so you enter the UK figures once: 20% VAT on sales (eat-in and hot food; most cold takeaway food is zero-rated), the VAT you can reclaim on purchases and on your capex, and your corporation tax rate (19% to 25%) in the Lender & Investor Summary. The notes in the templates point out where the UK differs, such as VAT returns due 1 month and 7 days after the quarter and PAYE paid on the 22nd.',
  },
  {
    q: 'What currency will I pay in?',
    a: 'The price is $49 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The templates themselves have no currency symbol: you type amounts in your own currency.',
  },
  {
    q: 'Is it a subscription? Are future updates included?',
    a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we add new templates or improvements, you get them at no extra cost — just download the files again.',
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If you're not happy, we'll refund 100% with no questions asked.",
  },
];

const data: KitExcelData = {
  slug: 'restaurant-financial-plan-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_FINANCIAL_PLAN_KIT',

  seo: {
    title: 'Restaurant Financial Plan Kit Pro: Restaurant P&L Template & Financial Projections for Excel',
    description:
      '10 Excel templates for restaurant financial planning: P&L template budget vs actual, 3- and 5-year projections, break-even, cash flow, startup costs, KPIs and a lender summary with IRR, NPV and DSCR. $49',
    keywords:
      'restaurant p&l template, restaurant profit and loss template, restaurant budget template, restaurant financial projections, restaurant pro forma template, restaurant startup costs spreadsheet, restaurant break-even calculator, restaurant cash flow forecast, restaurant kpi dashboard, restaurant loan proposal, restaurant business plan financials, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-financial-plan-kit.jpg',
  },

  schema: {
    productName: 'Restaurant Financial Plan Kit Pro',
    productDescription:
      '10 Excel templates with automatic formulas for restaurant financial planning: 3- and 5-year projections, break-even, cash flow, startup costs, monthly P&L budget vs actual, KPI ratios and a lender and investor summary with IRR, NPV, payback and DSCR.',
    price: '49.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Restaurant Financial Plan Kit Pro',
  },

  images: {
    // hero bg (6) — el set del ES con portada y reunión propias (ContentGrid usa el mismo set → gridGallery se omite).
    gallery: [
      '/lovable-uploads/ai-gallery/fin-en-hero.jpg',
      '/lovable-uploads/ai-gallery/fin-en-owner-desk.jpg',
      '/lovable-uploads/ai-gallery/fin-en-lender-meeting.jpg',
      '/lovable-uploads/ai-gallery/fin-en-projections.jpg',
      '/lovable-uploads/ai-gallery/plan-financiero-restaurante.jpg',
      '/lovable-uploads/ai-gallery/fin-en-partners-review.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/fin-en-owner-desk.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/fin-en-owner-desk.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/fin-en-hero.jpg',
  },

  hero: {
    // El ES va en rojo con una frase de alarma; el badge EN de la SPEC §6 es positivo → dorado,
    // como los hermanos EN.
    badgeTone: 'gold',
    badge: 'Lender-ready: IRR, NPV, payback and DSCR calculated for you',
    // D2 + SPEC §6: titlePre + titleGold + « Kit Pro» = «Restaurant Financial Plan Kit Pro».
    titlePre: 'Restaurant ',
    titleGold: 'Financial Plan',
    titlePost: ' Kit Pro: ',
    titleSubtitle: 'Restaurant P&L Template & Financial Projections for Excel',
    description:
      'Plan, track and present your numbers: 10 Excel templates with automatic formulas to build your financial projections, find your break-even point, track your P&L against budget, manage cash flow and present a professional summary to a lender or investor.',
    checkItems: [
      '3- and 5-year financial projections with automatic charts',
      'Break-even calculator with 3 scenarios',
      '12-month cash flow forecast with low-cash alerts',
      'Monthly P&L budget vs actual with a variance traffic light',
      'Lender & investor summary with IRR, NPV, payback and DSCR',
    ],
    ctaLabel: 'BUY NOW — $49',
  },

  // variant="tareas" en la SPA del ES (igual que el Staff Scheduling Kit), NO variant="kit".
  compatApps: {
    titleHtml: 'Print, Delegate and <span class="text-[#FFD700]">Control</span>',
    subtitleHtml:
      'Excel templates set up to print on US Letter. Compatible with Excel, LibreOffice and Numbers',
  },

  grid: {
    countGold: '10',
    headingRest: ' Financial Plan Templates',
    subtitle:
      "The 10 templates agree with each other: the same revenue and expense lines, the same ratios and the same base excluding sales tax (except the cash flow forecast, which includes the sales tax you collect because it's cash). Benchmarks for US full-service restaurants, as editable kit estimates.",
    // fourCols omitido (3 columnas, como el ES)
    templates: [
      { icon: 'TrendingUp', title: 'Restaurant Financial Projections: 3-Year Pro Forma P&L', desc: 'Revenue and expense projections for 3 years with a monthly breakdown. Revenue lines (dine-in, bar, delivery, events) excluding sales tax, food and beverage cost, labor, delivery platform fees, fixed costs, EBITDA and automatic charts.' },
      { icon: 'TrendingUp', title: 'Restaurant Financial Projections: 5-Year Pro Forma P&L', desc: 'The same structure as the 3-year plan, projected over 5 years. Built for lenders, investors or franchise applications that ask for a longer horizon.' },
      { icon: 'Target', title: 'Restaurant Break-Even Calculator', desc: 'Works out the minimum covers per day, the break-even revenue and the average check you need for the covers you expect, with a revenue vs costs chart. Operating and cash break-even, with the loan payment kept outside EBITDA, and 3 scenarios: pessimistic, base and optimistic.' },
      { icon: 'Wallet', title: 'Restaurant Cash Flow Forecast (12 Months)', desc: 'Monthly cash flow with the lag on card payments and supplier bills, seasonality, payroll taxes deposited the following month and sales tax remitted quarterly (8% example rate: enter your state and local rate). Automatic red alert when the balance drops below your safety threshold.' },
      { icon: 'Building2', title: 'Restaurant Startup Costs & Capex Budget', desc: 'Line by line: build-out, kitchen equipment, dining room FF&E, technology, licenses and permits, and other opening costs (opening inventory, deposits, contingency and working capital). Budget vs actual with % variance, a recoverable tax column (0 in the US, where sales tax is part of the cost; 20% VAT in the UK) and straight-line depreciation by useful life.' },
      { icon: 'BarChart3', title: 'Restaurant P&L Template: Monthly Budget vs Actual', desc: 'Every month compares actual vs budget with % variance and a traffic light (green under 5%, yellow 5-10%, red over 10%) that never flags selling more or spending less than planned. Food cost, beverage cost, labor cost and prime cost calculated automatically, plus an annual summary.' },
      { icon: 'PieChart', title: 'Restaurant Financial Ratios & KPI Dashboard', desc: 'Food cost %, labor cost %, prime cost %, GOP, EBITDA, occupancy (rent) %, RevPASH per seat-hour and cost per cover, each one compared with an editable benchmark table for US full-service restaurants (kit estimates you can change), plus annual sales per sq ft.' },
      { icon: 'FileText', title: 'Restaurant Loan Proposal: Lender & Investor Summary', desc: 'A professional summary for a lender or investor: executive summary, 5-year projections, IRR, NPV and payback, a loan amortization schedule (SBA 7(a)-style example: 10 years, optional interest-only period), the DSCR on the full loan payment against 1.25×, the usual lender target, and a collateral sheet.' },
      { icon: 'Shuffle', title: 'BONUS: What-If Scenario Simulator', desc: 'Change the average check, covers per day and food cost and see the impact on profitability instantly. 3 scenarios compared side by side.' },
      { icon: 'ClipboardList', title: 'BONUS: Pre-Opening Financial Checklist (54 Tasks)', desc: "54 tasks in 7 phases: business formation, financing, licenses and permits, suppliers, insurance, cash management and employer obligations, from the EIN and the seller's permit to workers' comp. Each one with a status, an owner and a due date." },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic finance templates. They're tools designed by a chef who has worked in kitchens since the age of 17 and has advised restaurant openings as a consultant since 2010.",
    reasons: [
      { icon: 'Utensils', title: 'Built for Restaurants', desc: 'Ratios, benchmarks and a cost structure specific to restaurants: food cost, beverage cost, labor cost, prime cost, GOP and RevPASH. Not generic finance templates.' },
      { icon: 'Calculator', title: 'Templates That Agree With Each Other', desc: "The same revenue and expense lines, the same ratios and the same base excluding sales tax in 9 of the 10 (the cash flow forecast includes it because it's cash, and says so on its Instructions tab). Inside each workbook the formulas are chained: month, annual total and summary." },
      { icon: 'ShieldCheck', title: 'Lender-Ready Format', desc: 'The Lender & Investor Summary follows the structure lenders and investors usually ask for: executive summary, projections, IRR, NPV, payback, DSCR and collateral. It gives your application a clear structure; approval always depends on your project and the lender. A planning tool, not financial or tax advice.' },
      { icon: 'RefreshCw', title: 'An Advisor Bills by the Hour. This Is $49, Once', desc: 'The same tools a financial consultant uses to build a restaurant business plan, in Excel, for a one-time payment. No subscription.' },
    ],
    // Pastillas del ES (orden incluido) sin Google Sheets hasta el test real (SPEC §6, §9); «A4» → US Letter.
    compatLabel: 'Compatible with:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised on the opening and the financial plan of more than 200 hospitality businesses.',
  authorBadges: ['Restaurant consultant', '200+ openings advised'],

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle:
      'Besides the 8 core templates, you get these extra resources — worth $38',
    items: [
      {
        icon: 'Shuffle',
        label: 'BONUS 1',
        title: 'What-If Scenario Simulator',
        value: '$19',
        desc: 'Change the average check, covers per day and food cost and see the impact on profitability instantly. Compare 3 scenarios side by side: pessimistic, base and optimistic.',
        image: '/lovable-uploads/ai-gallery/fin-en-projections.jpg',
      },
      {
        icon: 'ClipboardList',
        label: 'BONUS 2',
        title: 'Pre-Opening Financial Checklist (54 Tasks)',
        value: '$19',
        desc: 'The 54 tasks to tick off before opening day, in 7 phases: business formation, financing, licenses and permits, suppliers, insurance, cash management and employer obligations. Each one with a status, an owner and a due date, so the big items don\'t slip through.',
        image: '/lovable-uploads/ai-gallery/fin-en-lender-meeting.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE FINANCIAL PLAN KIT — $49',
  },

  guarantee: {
    // headingPre por defecto = ui.guaranteeHeadingPreDefault («Satisfaction Guarantee »).
    text:
      "If the templates don't help you plan your restaurant's finances better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  faqs: FAQS,

  cta: {
    heading: 'Stop Opening or Running Your Restaurant Blind',
    subtitle:
      "10 professional templates for less than one hour of a financial consultant's time.",
    // D4: los valores de los bonos repiten los de bonus.items.
    items: [
      '3- and 5-year financial projections with charts',
      'Break-even calculator with 3 scenarios',
      '12-month cash flow forecast with low-cash alerts',
      'Startup costs and capex budget with variances',
      'Monthly P&L budget vs actual with a traffic light',
      'KPI dashboard with editable benchmarks',
      'Lender & investor summary (IRR, NPV, payback, DSCR)',
      'BONUS: What-If Scenario Simulator ($19)',
      'BONUS: Pre-Opening Financial Checklist ($19)',
    ],
    ctaLabel: 'YES, I WANT THE FINANCIAL PLAN KIT — $49',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit Plan
  // Financiero, la edición española de este kit: por eso conservan sus nombres, negocios y cifras (en
  // EUR, sin el signo), y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Owners, investors and consultants who already plan their finances with the Kit Plan Financiero, the Spanish edition of this kit',
    items: [
      { name: 'Ricardo Gómez', role: 'Owner, newly opened casual restaurant', text: 'The 3-year financial projection was exactly what my bank in Spain asked for the loan. I presented it as it was, with the charts and the scenarios, and they approved EUR 120,000 in 2 weeks.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Ana Beltrán', role: 'Restaurant consultant, 15+ years', text: 'I use it with every client who is about to open. The scenario simulator is brilliant: you change the average check or the occupancy and instantly see how it affects profitability. It makes any opening project look professional.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Javier Morales', role: 'General Manager, group of 3 restaurants in Valencia, Spain', text: 'The monthly P&L budget vs actual changed my life. I used to find out at the end of the year that something was wrong. Now I spot variances every month with the traffic light and fix them in time.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Isabel Campos', role: 'Finance Director, restaurant chain', text: 'The financial ratios dashboard with industry benchmarks is exactly what I needed for our management committee meetings. Food cost, labor cost, prime cost, GOP — all automatic.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Fernando Reyes', role: 'Chef and entrepreneur, first restaurant', text: 'The break-even calculator opened my eyes. I found out I needed 45 covers a day at an average check of EUR 22 to be profitable. Without it I would have opened blind.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'María Herrero', role: 'Tax advisor specializing in hospitality, Spain', text: 'The cash flow forecast with low-cash alerts is what I value most. My clients now see 3 months ahead when they are going to be tight on cash. Prevention is infinitely cheaper than the cure.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pablo Navarro', role: 'Investor, 2 restaurants + a ghost kitchen', text: 'The capex budget with actual vs budget variance saved me from surprises during the build-out. Every line under control: kitchen, furniture, technology, licenses. I always knew how much I had left.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Daniel Ortiz', role: 'Director of Operations, restaurant franchise', text: 'The feasibility report for Spanish banks is flawless. IRR, NPV, payback period — all calculated automatically. Our franchisees use it to get financing without hiring consultants.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  pricing: {
    priceOld: '$199',
    price: '$49',
    discountBadge: '-75%',
    heroNote: 'Special launch price. Going up soon',
    buyBoxNote: 'Special launch price — 75% off',
    bonusTotalLabel: 'Total value of the complete kit: $237 — 8 templates ($199) + 2 bonuses ($38)',
    bonusSaveLine: 'Save $150 TODAY!',
  },

  // Etiqueta corta (el ES también abrevia: «KIT PLAN FINANCIERO»): el nombre completo no cabe en la barra móvil.
  stickyLabel: 'FINANCIAL PLAN KIT PRO — $49',
  // stickyVariant omitido → default 'v2', como el ES.

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'restaurant-financial-plan-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
