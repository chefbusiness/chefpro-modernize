// astro-site/src/data/productos-en/planes/food-truck-business-plan.ts
// TIENDA INTERNACIONAL EN — Food Truck Business Plan Kit. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/planes/plan-negocio-food-truck.ts (mismo tipo PlanNegocioData, misma
// plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos).
// SPEC: scripts/productos-digitales/business-plans-en/SPEC.md (D1-D5, D20, D23, D25, D26, D28, D29 y §6).
//   · D1/D2: slug `food-truck-business-plan`, nombre «Food Truck Business Plan Kit», H1 Forma B
//     `Food Truck ` + oro `Business Plan` + subtítulo «Template: Word Plan + Excel Financial Projections
//     + Startup Checklist»; title SEO de D2.
//   · D3/D4: $39; priceOld $129; bono 2 $29 (el 1 «Included in the plan», m19); total $158; ahorro $90 (129 − 39); «-70%» en hero y buyBox.
//   · D5: los 3 ficheros EN (dashboard FoodTruckBusinessPlanDashboard.tsx y get-download-urls.ts).
//   · §6 aplicado: A1 (benchmarks con fuente real o «kit estimate», D19), A2 (equilibrio de caja «loan
//     payments in, depreciation out», sin el «además»), A3 (checklist = punto de partida, no «verificado»),
//     A4 (sin el rango 45-85K EUR), A5 (bono 1 = §9 del plan + fase 2 del checklist, sin formularios
//     estatales), A12 (sin aggregateRating ni review), A13 (sin superlativo), A14 (SBA 7(a)/Microloan,
//     «lender-ready format; approval not guaranteed», sin ICO/ENISA/SMI/SS 33 %/14 pagas).
//   · Compatibilidad (decisión del orquestador, 4-oct): solo lo que son los ficheros — Microsoft Excel
//     (.xlsx) y Microsoft Word (.docx), tamaño US Letter. Sin Google Sheets/Docs/LibreOffice/Numbers hasta
//     un test real (D25): compatPills + compatSubtitle (sustituye la frase del marquee de la plantilla).
//   · Revisión final (4-oct, ronda de arreglos): B1 (el cuadro y el DSCR cubren SOLO el préstamo principal,
//     banco o SBA 7(a)), m3 (regla CDL completa, 49 CFR 383.91), m13 (el equipo va en varias líneas, no una
//     por aparato), m19 (el bono 1 es la §9 del plan + una fase del checklist: «Included», total $158) y
//     cifras del caso recalculadas con la comisión de tarjeta al 3.5 % (margen bruto 58.2 %).
//   · Testimonios (D26 + decisión del orquestador): los 8 del ES traducidos, subtítulo de la edición
//     española; fuera las cifras que ya no son verdad en el producto (59 trámites, 27 clientes/día a 12 €,
//     ratios «food cost 30 %, margen 65 %, retorno 12-24 meses», guía «por CCAA»): esas frases se
//     reformulan sin número. Las cifras personales del testimonio (su inversión, sus plazos) se conservan.
//   · Cifras del caso de ejemplo US: las de `scripts/productos-digitales/business-plans-en/cifras_caso.json`
//     (caché del xlsx EN calibrado por la F2, D15/D22; F2-NOTAS §7). Ninguna cifra del ES ni inventada. Los conteos del producto (10 secciones,
//     9 hojas, 68 tareas en 6 fases, 3 escenarios) y los parámetros decididos en la SPEC (DSCR 1.25×,
//     Microloan hasta $50,000, aportación propia «often around 10%», umbrales D16) sí van.
//   · FAQ: People Also Ask de «food truck business plan» (research §2) + las del ES adaptadas + UK,
//     moneda, suscripción, licencia y garantía (como los hermanos EN). schema.faqs = el MISMO array.
//   · Imágenes: fotos propias sin texto (ftbp-en-*) + use-case-food-truck-grill (sin rótulos). Las del ES
//     llevan rótulos («CERVECERÍA», «TAPAS», «MADRID») o carteles con precios: no se reutilizan.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_BUSINESS_PLAN (resuelto en el wrapper .astro).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What does a food truck business plan include?',
    a: 'The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written for a food truck in Word, plus the Excel financial projections that back them up and a 68-task startup checklist.',
  },
  {
    q: 'How much money is needed to start a food truck?',
    a: "It depends mostly on the truck: a used truck with a refit costs a fraction of a new custom build, and permits, commissary rent and insurance vary a lot from city to city. The Startup Costs sheet lists every line — truck, build-out and wrap, cooking and refrigeration equipment, generator, propane and fire suppression, water tanks and hand sinks, LLC and legal, first-year permits, plan review, POS, smallwares and packaging, opening inventory and launch marketing — plus deposits, pre-opening months, contingency and working capital. The kit's example truck needs $146,399 in total cash; replace each line with your own quotes.",
  },
  {
    q: 'What permits do I need to run a food truck?',
    a: "It depends on your state, county and city, but most food trucks need: a business structure (LLC or sole proprietorship) and an EIN from the IRS; a state sales tax registration or seller's permit; a city or county business license; a health department plan review, then a mobile food unit permit and inspection; a commissary agreement (most health departments require one); a mobile vending license in each city where you sell; a fire marshal inspection of propane and fire suppression in many cities; DMV registration for the truck; and food protection manager and food handler certificates. The startup checklist organizes 68 tasks in 6 phases. Treat it as a starting point and confirm the details with your local authorities.",
  },
  {
    q: 'What does the truck itself need?',
    a: "Health departments usually check fresh and gray water tanks (the gray water tank is normally larger than the fresh one), a hand sink, refrigeration that holds safe temperatures, and surfaces that can be cleaned. Fire marshals look at propane, extinguishers and the hood fire suppression system (NFPA 96 where it has been adopted). Under federal rules (49 CFR 383.91) you need a commercial driver's license (CDL) if the truck's gross vehicle weight rating is 26,001 lb or more, or if you tow a trailer rated over 10,000 lb and the combination is rated 26,001 lb or more; your state DMV may add its own rules. All of it is budgeted in the Startup Costs sheet (kitchen and refrigeration equipment, generator, water tanks and sinks, propane and fire suppression) and listed as tasks in the checklist; your county's plan review sets the exact specs.",
  },
  {
    q: 'How much money does a food truck owner make?',
    a: "There's no single answer: it depends on customers per day, average check, operating days and what you pay for food, labor, commissary and permits. That is exactly what the 3-year P&L calculates from your assumptions — revenue, cost of goods, gross margin, labor, fixed costs, EBITDA, income tax and net profit — with each ratio checked against an editable kit benchmark. Your location, your menu and your event calendar decide the rest.",
  },
  {
    q: 'Why do so many food trucks fail?',
    a: "We won't quote a failure rate: the figures that circulate online rarely cite a source. The usual reasons are easier to pin down: underestimating startup costs, running out of cash in the slow months, spots or events that don't bring enough customers, and permits that take longer than planned. The kit is built around those risks: a 12-month cash flow with seasonality that shows your lowest cash balance and when it happens, a break-even that tells you how many customers a day you need, three scenarios, and a checklist that puts permits before equipment.",
  },
  {
    q: 'Is a food truck a tax write-off?',
    a: "The truck and its equipment are business assets: in general they're depreciated over their useful life, and in the US some owners can deduct them faster (Section 179 or bonus depreciation). Whether that applies to you depends on your situation, so ask your accountant. The financial model uses straight-line book depreciation (7 years for the truck and its build-out and 7 for equipment, both editable) and mentions the faster US options in a note. It's a planning tool, not tax advice.",
  },
  {
    q: 'Is owning a food truck worth it?',
    a: "It can be, if the numbers work in your city. Compared with a restaurant you invest less and you can move when a spot doesn't work, but you depend on locations, events, weather and permits. Before you buy a truck, put your own numbers in the model: if the break-even, the cash flow and the debt service coverage still look healthy in the pessimistic scenario, you have a plan worth pitching.",
  },
  {
    q: 'Do food trucks pay to park at events?',
    a: "Often, yes: many events and markets charge a vendor fee, a share of sales or both, and some need their own temporary food event permit. On private property you need the owner's written permission; on public streets, the city's vending and parking rules apply. You can model events in your operating days and fixed costs, and the checklist includes temporary event permits.",
  },
  {
    q: 'Can I present this plan to a lender or investors?',
    a: "Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The loan schedule and the DSCR cover your main loan (bank or SBA 7(a)), the one you enter in the assumptions; the financing sheet also lists an SBA Microloan (up to $50,000, through nonprofit intermediaries), investors or partners and local grants as sources of funds, without amortizing them. Lenders usually expect an owner equity injection (often around 10% for SBA start-ups; many want 20-30%). It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.",
  },
  {
    q: 'How is it different from a free food truck business plan template?',
    a: "Free templates give you headings to fill in. This kit gives you a plan already written for a food truck, an Excel model with more than 700 linked formulas (change one assumption and the P&L, the cash flow and the financing recalculate), payroll with employer taxes and a minimum wage alert, a calculated break-even and a 68-task startup checklist. The figures in the Word plan are the ones in the Excel model, so the two documents tell the same story.",
  },
  {
    q: 'Does it work in the UK?',
    a: "Yes, with notes. Tax rates are editable cells: enter 20% VAT on hot food (most cold takeaway food is zero-rated) and the VAT you can reclaim on purchases and equipment. The plan and the checklist add UK notes: register your food business with the council at least 28 days before you start trading (for a van, the council where it's kept), get a street trading licence or consent from each council where you sell, and expect a food hygiene rating inspection. UK minimum wage and employer National Insurance aren't preloaded: enter the current figures from gov.uk.",
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
    q: 'Can I use it for more than one truck or with my clients?',
    a: "One purchase covers one business, with all of its trucks. If you're a consultant or an investor, you can use the files with the projects you advise, but you can't hand them copies: each business buys its own.",
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the plan doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: PlanNegocioData = {
  slug: 'food-truck-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_BUSINESS_PLAN',

  seo: {
    title:
      'Food Truck Business Plan Template: Word + Excel Financial Projections + Startup Checklist | AI Chef Pro',
    description:
      'Food truck business plan template: a 10-section Word plan, Excel financial projections (3-year P&L, break-even, 12-month cash flow, loan and DSCR) and a 68-task startup checklist. $39.',
    keywords:
      'food truck business plan, food truck business plan template, food truck business plan example, food truck startup costs, food truck financial projections, food truck permits, how to start a food truck business, food truck startup checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-food-truck-business-plan.jpg',
  },

  schema: {
    productName: 'Food Truck Business Plan Kit',
    productDescription:
      'Food truck business plan template kit: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions) and a 68-task startup checklist in 6 phases. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Food Truck Business Plan Kit',
  },

  images: {
    // hero bg (6) — fotos propias sin texto + la parrilla de los usos (sin rótulos).
    gallery: [
      '/lovable-uploads/ai-gallery/ftbp-en-hero.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-window.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-truck-park.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-commissary.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el ES (que reordena el del hero).
    gridGallery: [
      '/lovable-uploads/ai-gallery/ftbp-en-owner-plan.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-window.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-commissary.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-truck-park.jpg',
      '/lovable-uploads/ai-gallery/ftbp-en-hero.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/ftbp-en-window.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/ftbp-en-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready food truck business plan: Word + Excel + checklist',
    titlePre: 'Food Truck ',
    titleGold: 'Business Plan',
    titleSubtitle: 'Template: Word Plan + Excel Financial Projections + Startup Checklist',
    description:
      'Everything you need to plan and pitch a food truck: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your 3-year P&L, break-even, 12-month cash flow and loan payments from your own numbers; and a 68-task checklist that takes you from filing your LLC to your first 90 days of service. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section food truck business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even and 12-month cash flow',
      'Startup costs line by line, with a loan schedule and DSCR',
      'Startup checklist: 68 tasks in 6 phases, from EIN to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      "9 building blocks for a food truck plan you can defend in front of a lender: the written plan, the numbers behind it and the permits list that gets you on the street.",
    templates: [
      { icon: 'FileText', title: 'Food Truck Business Plan (Word, 10 Sections)', desc: 'A complete plan already written for a food truck: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements, permits and licenses, and conclusions with an action plan. Its figures are the ones in the example Excel model.' },
      { icon: 'FileSpreadsheet', title: 'Food Truck Financial Projections (Excel, 9 Sheets)', desc: "Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. You type only in the green cells; everything else recalculates on its own and is protected, without a password, so a formula can't break by accident." },
      { icon: 'TrendingUp', title: 'Break-Even Point', desc: 'How many customers a day you need at your average check (excl. sales tax) to cover every cost, and the cash break-even (loan payments in, depreciation out). Contribution margin, operating days and a sensitivity table with 20 combinations of average check and variable cost.' },
      { icon: 'BarChart3', title: 'Financial Scenarios', desc: 'Three scenarios side by side — pessimistic, base and optimistic — each with its own estimated cash balance, ready to show a lender or an investor.' },
      { icon: 'Users', title: 'Staffing & Payroll (4 Roles)', desc: 'A lean food truck team — the owner full time, a cook-cashier, extra hands for events and holiday cover — with gross pay, employer payroll taxes and the real cost of each role. The workbook flags in red any pay that falls below the minimum wage for the hours worked.' },
      { icon: 'ShieldCheck', title: 'Startup Checklist (68 Tasks, 6 Phases)', desc: "LLC or sole proprietorship, EIN, seller's permit and business license; health department plan review, mobile food unit permit and commissary agreement; city vending licenses, DMV and fire marshal inspection; equipment, staff, marketing and your first 90 days." },
      { icon: 'Wrench', title: 'Mobile Kitchen Equipment', desc: 'Griddle, fryer, generator, fresh and gray water tanks, hand sink, hood with filters, propane and fire suppression: all budgeted in the startup costs (kitchen and refrigeration equipment, generator, water tanks and sinks, propane and fire suppression), with reference prices you replace with your own quotes.' },
      { icon: 'ListChecks', title: 'Food Truck Benchmarks', desc: "Your plan's ratios — cost of goods, gross margin, labor, commissary and parking, net margin — each marked OK or REVIEW against an editable kit benchmark, next to a reference table of industry ranges with their source (or \"kit estimate\" when there isn't one). Payback isn't promised: the cash flow sheet calculates it from your own numbers." },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Its own sheet: owner equity and your loan (bank or SBA 7(a)) with its amortization schedule year by year and the debt service coverage ratio (DSCR) checked against a 1.25× target, plus an SBA Microloan, investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Food Truck, la edición española.
  // Conservan nombres, negocios y lo que cuenta cada uno de su caso (importes en EUR sin el signo); las
  // cifras que eran del producto v1.1 y ya no son verdad se reformulan sin número (ver cabecera). Solo se
  // pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Food truck owners, mobile food fleets and investors who planned their business with the Spanish edition of this plan',
    items: [
      { name: 'Alejandro Ruiz', role: 'Food truck owner, Madrid, Spain', text: 'I took the financial plan to my bank in Spain and they approved the microloan in 2 weeks. The 3-year projections with scenarios gave them a lot of confidence. Total investment: EUR 62,000.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Street food entrepreneur, Barcelona, Spain', text: 'The opening checklist saved me months of work. City permits, the vehicle inspection, the street vending license… I didn\'t leave a single thing pending.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Food & beverage investor', text: 'What convinced me most was seeing exactly how many customers a day it takes to cover costs at a given average check. The investment is much lower than a restaurant\'s and the payback is faster.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Partner, 2 food trucks in Seville, Spain', text: 'I started with one truck and opened the second one 18 months later. The Excel financial plan let me project the expansion with real numbers. Mobility is the key to this business.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Hospitality consultant', text: 'I recommend it to every client who wants to start a business with low risk. A food truck needs less investment and fewer staff, and you can move if a location doesn\'t work.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Food truck owner, Valencia, Spain', text: 'The reference ratios helped me negotiate with suppliers and choose the best locations to get the most out of every service.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex-corporate, opened a food truck', text: 'I quit my corporate job and launched my food truck in 3 months. The permits checklist and the licensing section of the plan were essential so I didn\'t waste time.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Owner, fleet of 5 trucks', text: 'We\'ve used the Excel financial plan for all 5 launches. You just change the numbers for each location and you have a professional business plan ready for investors.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      "Not another generic template: a food truck plan written for the format lenders expect, with a financial model that recalculates from your own numbers.",
    reasons: [
      { icon: 'Truck', title: 'Less Capital Than a Restaurant', desc: "No dining room lease, a smaller team, and the option to move when a spot doesn't work. The model shows what that means in your numbers: startup costs line by line and the cash you need before your first sale." },
      { icon: 'BarChart3', title: 'Numbers Calculated, Not Copied', desc: 'Average check, cost of goods, gross margin and break-even come out of the workbook itself, from your assumptions. The example truck: an average check of $14 (excl. sales tax), 29.3% cost of goods, 58.2% gross margin and break-even at 68 customers a day, against 80 expected. Replace them with yours.' },
      { icon: 'ShieldCheck', title: 'Permits Before Equipment', desc: '68 tasks in 6 phases, from your LLC and EIN to the health department plan review, the commissary agreement, city vending licenses, DMV and the fire marshal inspection. A starting point: requirements vary by state, county and city.' },
      { icon: 'Banknote', title: 'Lender-Ready Format', desc: 'Written plan, 3-year P&L, break-even, 3 scenarios, cash flow and a loan schedule with DSCR for your main loan (bank or SBA 7(a)). Approval is never guaranteed, and it is a planning tool, not financial advice. One-time payment, no subscription.' },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised food truck owners, mobile food fleets and street food operators, combining hands-on operations with financial planning.',
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      'Besides the business plan, the financial model and the startup checklist, you get these extra resources — worth $29, plus a permits guide drawn from the plan itself',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Food Truck Permits & Licenses Guide (US + UK Notes)',
        value: 'Included in the plan',
        desc: "Section 9 of the plan plus Phase 2 of the checklist: why vending licenses are issued city by city and can't be transferred, how the health department plan review, the mobile food unit permit and the commissary agreement fit together, what the fire marshal and the DMV check, and how event permits work — with notes for the UK. No state forms included: requirements vary by state, county and city.",
        image: '/lovable-uploads/ai-gallery/ftbp-en-truck-park.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Food Truck Benchmarks (Reference Table)',
        value: '$29',
        desc: "The reference table inside the workbook: cost of goods, gross margin, labor and net margin, each with its source or marked \"kit estimate\", and the OK / REVIEW check (commissary and parking included) that tells you where your plan departs from the benchmark. Every threshold is an editable cell.",
        image: '/lovable-uploads/ai-gallery/ftbp-en-owner-plan.jpg',
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
    headingGold: 'Food Truck',
    subtitle:
      'Plan it before you buy the truck: the written plan, the numbers behind it and the permits list, for a one-time payment.',
    // D4: los valores de los bonos repiten los de bonus.items.
    items: [
      '10-section food truck business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even and cash break-even, with a sensitivity table',
      '12-month cash flow and a loan schedule with DSCR',
      'Startup checklist: 68 tasks in 6 phases',
      'BONUS: Food Truck Permits & Licenses Guide (included in the plan)',
      'BONUS: Food Truck Benchmarks ($29)',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    priceOld: '$129',
    price: '$39',
    discountBadge: '-70%',
    heroNote: 'Special launch price. Going up soon',
    buyBoxNote: 'Special launch price — 70% off',
    bonusTotalLabel: 'Total value: $158 — business plan kit ($129) + Benchmarks bonus ($29)',
    bonusSaveLine: 'Save $90 TODAY!',
  },

  stickyLabel: 'FOOD TRUCK BUSINESS PLAN — $39',

  // D29: salientes a Financial Plan, HACCP y Staff Scheduling (+ el plan hermano).
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'food-truck-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
