// astro-site/src/data/productos-en/planes/ice-cream-shop-business-plan.ts
// TIENDA INTERNACIONAL EN — Ice Cream Shop Business Plan Kit. DUPLICADO de pizza-shop-business-plan.ts (mismo tipo
// PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Edicion inglesa del ES
// "Plan de Negocio: Heladeria Artesanal" (hreflang reciproco, familia plan-negocio-heladeria), cuyo contenido y cifras
// NO se reutilizan: el EN es otro caso US (SPEC business-plans-en-10 D186-D203).
// SPEC: scripts/productos-digitales/business-plans-en-10/SPEC-delta.md (D186-D208). Research: F1-research-us-delta.md
//   (§3 FAQ, §6.1 licencias, §6.2 estandares de identidad, §9 jerga y SEO). Revision: REVISION-FINAL.md (D203).
//   · D186b: title con el NOMBRE DEL PRODUCTO primero; H1 Forma B `Ice Cream Shop ` + oro `Business Plan` + «Template to
//     Open a Homemade Ice Cream Shop: …»; meta y keywords TAL CUAL research §9. «gelato» NUNCA en el nombre ni como promesa.
//   · D187: $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating ni review.
//   · D188: ficheros de dl/ice-cream-shop-business-plan/ (plan, proyecciones y checklist de 80 tareas; SIN calculadora) + la
//     guia comun de equivalencias EN. Los 6 H2 de research §9 no caben como H2 (constantes de UI_PLAN): sus keywords van en
//     los H3 de «why», las tarjetas del grid y la FAQ.
//   · D204: SIN testimonios (los del ES son clientes de Espana: no se trasladan ni se inventan, FTC). FAQ = las 8 de
//     research §3 + canibalizacion (Ice Cream Shop Checklists Kit Pro, Restaurant/Bakery) + UK/CA/AU.
//   · Cifras MEDIDAS (F2-NOTAS §7 y REVISION-FINAL §0, caso US de 165 customers × $7.50 × 310 dias): ventas A1 $383,625,
//     CAPEX $204,100 (19 partidas $186,000), caja necesaria $256,871, prestamo $162,000, neto A1 5.6 % → 8.6 % en A3,
//     equilibrio 147 customers/dia (140 de caja), holgura 18.3 %, DSCR 2.26x.
//   · Revision D203, lo que esta ficha NO dice: «retail food establishment in most states», «no hood / no smoke exhaust
//     needed» ni «at least one CFPM» (el CFPM es el person in charge, Food Code 2022 2-102.12). Licencias: siempre «check
//     with your state department of agriculture / local health department»; Georgia solo con su condicion «eaten on the
//     premises». Modelo D190: base pasteurizada COMPRADA; pasteurizar en el local = variante.
//   · Honestidad (research §3/§5.2): neto realista ≈ 5-6 % el ano 1 frente al «10-25 %» de la SERP.
//   · Imagenes: las plan-heladeria-*.jpg del ES, abiertas una a una: SIN la -vitrina (rotulos con texto borroso tipo
//     «LIMON / CHOCOLAT» en las tarjetas del mostrador: descartada); el resto no lleva texto ni marcas. OG =
//     https://aichef.pro/og-ice-cream-shop-business-plan.jpg (recorte 1200x630 del hero).
//   · La -obrador muestra la batch freezer y, al lado, una cuba tapada: en el caso no hay pasteurizador, por eso el pie
//     de foto de esa imagen habla solo de la batch freezer. La -invierno enseña tarta helada y chocolate caliente.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en F2-NOTAS §7 / REVISION-FINAL §0 (business-plans-en-10/cifras_caso.json) ─────────
// Nada movible fuera de lo que el libro calcula con el caso por defecto.
const CASO = {
  customers: '165', // B4 — customers per day (year-1 average)
  ticket: '$7.50', // B5 — average check per person (excl. sales tax)
  dias: '310', // B6 — operating days
  ventas: '$383,625', // ventas A1 = 165 × $7.50 × 310
  partidas: '$186,000', // 19 partidas de inversion
  capex: '$204,100', // 19 partidas + fianza $5,000 + renta previa $5,000 + imprevistos $8,100
  colchon: '$52,771', // fondo de maniobra (3 meses de fijos netos)
  caja: '$256,871', // necesidad total de caja = CAPEX + fondo
  propios: '$95,000', // fondos propios
  prestamo: '$162,000', // prestamo (SBA 7(a) o banco), 10 anos al 10 %
  dscr: '2.26x', // DSCR mínimo del caso
  netoPct1: '5.6%', // neto A1 ($21,585)
  netoPct3: '8.6%', // neto A3
  equilibrio: '147', // customers/dia (contable)
  equilibrioCaja: '140', // customers/dia (de caja)
  holgura: '18.3%', // 165 / 139.5 - 1 (vs break-even de caja)
  cogsPct: '22%', // COGS 22.3 %
  margenPct: '68%', // margen tras variables 68.2 %
  personalPct: '33%', // personal 33.4 %
  saldoMin: '$46,060', // saldo minimo de caja (Mes 1 = marzo)
  pesimista: '$294,000', // ventas del escenario pesimista (-$32,344 de neto)
  formulas: '700', // "more than N": el libro tiene 736 formulas
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `What should an ice cream shop business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a neighborhood ice cream shop that makes its own ice cream, plus the Excel financial projections with summer seasonality that back them up and an 80-task startup checklist.`,
  },
  {
    q: `Is it a generic template or built for an ice cream shop?`,
    a: `Built for an ice cream shop that makes its own ice cream in a mid-size US city: about 1,000 sq ft on a neighborhood main street or next to a park or a school, a production room of about 250 sq ft, dipping cabinets for 18 flavors (10-12 in winter), 20 seats plus a seasonal patio, scoops in cups and cones, sundaes, hand-packed pints and quarts, ice cream cakes to order, coffee and hot chocolate, and a little catering. The owner is the ice cream maker and the general manager. Nothing to strip out from a restaurant template. If your concept is different, the Excel workbook takes any numbers you type, but the written plan describes this shop (see the last questions about soft serve, trucks and franchises).`,
  },
  {
    q: `How much does it cost to open an ice cream shop?`,
    a: `Published estimates run from about $50,000 to $250,000 or more, depending on the size, the build-out and whether you make your own ice cream. The kit's example comes in at ${CASO.capex} of startup costs (19 line items that add up to ${CASO.partidas}, plus a $5,000 security deposit, $5,000 of rent before opening and an $8,100 contingency) and ${CASO.caja} of total cash needed once you add ${CASO.colchon} of working capital for the slow months. The lines that move the number are the build-out of the production room and shop ($48,000), the electrical service ($9,000), plumbing and ventilation ($10,000), a 20-quart horizontal batch freezer ($30,000), a hardening cabinet ($9,000), storage freezers ($7,000) and the 18-flavor dipping cabinets ($11,000). Replace each line with your own quotes: they are example prices, not a price list.`,
  },
  {
    q: `Is an ice cream shop profitable? What is a realistic profit margin?`,
    a: `It can be, but not at the 10-25% net that many blogs and AI summaries quote. For the net margin the sources disagree: some say 10-25%, others 6-9% or about 5.5%. The kit's example sits at the low end and shows why: ${CASO.customers} customers a day at an average check of ${CASO.ticket} for ${CASO.dias} days is ${CASO.ventas} in year-1 sales, about ${CASO.cogsPct} goes to cost of goods, about ${CASO.personalPct} to labor and the margin after variable costs is about ${CASO.margenPct}. The net is ${CASO.netoPct1} in year 1, rising to ${CASO.netoPct3} by year 3, with a break-even of ${CASO.equilibrio} customers a day (${CASO.equilibrioCaja} if you count cash with loan payments in and depreciation out). The pessimistic scenario (140 customers at $7.00 for 300 days, ${CASO.pesimista} of sales) loses money in year 1, and the plan says so. Build your first year on your own numbers, not on the example.`,
  },
  {
    q: `How much does an ice cream shop owner make?`,
    a: `Less than most online articles suggest. In the kit's example the owner is on payroll as ice cream maker and general manager at $4,000 a month, and the shop also leaves a net profit of ${CASO.netoPct1} of sales in year 1 and ${CASO.netoPct3} by year 3. Whether the owner earns more depends on your sales, your season and what you pay yourself, which is why the plan separates the owner's salary from the net result. Replace the example with your own numbers before you decide.`,
  },
  {
    q: `Do I need a dairy license to make my own ice cream? Should I buy a base or make my own mix?`,
    a: `It depends on your state, so ask your state department of agriculture and your local health department before you sign the lease. The kit's example buys a pasteurized ice cream base from a licensed dairy and churns, flavors and hardens it in the shop, the lighter route (your retail food permit and, in some states, a frozen dessert license). Making your own mix is a variant: a batch pasteurizer costs roughly $25,000-45,000, and you usually add a state dairy plant or frozen dessert manufacturer license, 3-A sanitary equipment and inspections. States handle it differently. In Vermont, for example, freezing a pasteurized base needs a Frozen Dessert License from the Agency of Agriculture and only flavorings may be added after pasteurization, while blending your own mix needs a Milk Handler License. In Georgia, a retailer that freezes a mix from a licensed dairy processor is exempt from the Dairy Manufacturer's License only for ice cream eaten on the premises: ask before you sell pints to go, delivery or catering. The kit does not promise a license: the checklist turns the license decision into a task with a responsible person and a date.`,
  },
  {
    q: `What equipment do I need to open an ice cream shop, and what does it cost?`,
    a: `The example plans a 20-quart horizontal batch freezer ($30,000), a hardening cabinet or blast freezer ($9,000), storage freezers kept at 0 °F or colder ($7,000), dipping cabinets for 18 flavors ($11,000), a base refrigerator and flavor prep station ($4,500), prep tables, a three-compartment sink and smallwares ($8,500), and a front counter with dipper wells, espresso, waffle cone irons and hot fudge warmers ($9,000). Dipper wells need running water under the FDA Food Code (3-304.12). Whether your waffle cone irons need an exhaust hood is for your plan reviewer to decide, and the checklist tells you to ask before you sign the lease. All prices are kit estimates for 2026: replace them with your distributor's quotes.`,
  },
  {
    q: `What do ice cream shops do in winter?`,
    a: `The plan treats winter as part of the concept, not a pause. The example opens in March, runs long hours from mid-April to September with the peak between Memorial Day and Labor Day, and from November to February it opens short weekday hours, closes on Mondays and shuts for three weeks in January. Winter sales come from ice cream cakes to order, holiday pies and pints, hot chocolate and catering, with 10-12 flavors in the cabinets. The 12-month cash flow starts in March, shows the lowest cash balance of the year (${CASO.saldoMin}) right after the investment is paid, and puts July at 16.5% of the year's sales and January at 2.5%. The Word plan also describes the alternative of closing from November to February, with no Excel behind it, and what you would lose.`,
  },
  {
    q: `Do I charge sales tax on ice cream?`,
    a: `Usually a scoop to eat now is taxed as prepared food, but the rules differ by state and the answer can change for packaged pints, multipacks and whole ice cream cakes (in Texas, for example, packaged ice cream is generally treated as food and may be exempt). The example uses a single 8% rate for scoops, pints, cakes and drinks as a placeholder and says so: use your blended rate and check with your state department of revenue or your accountant. In the UK, ice cream is standard-rated at 20% VAT, to take away too.`,
  },
  {
    q: `Can teenagers work as scoopers?`,
    a: `Often yes, with limits. Under the federal rules for 14- and 15-year-olds (29 CFR 570.35), on school days they can work up to 3 hours a day and 18 hours a week, outside school weeks up to 8 hours a day and 40 hours a week, between 7 a.m. and 7 p.m., or until 9 p.m. from June 1 to Labor Day. States can be stricter and may require work permits. The example staffs seasonal part-time W-2 scoopers at $15 an hour and a year-round shift lead, with the hours you hire checked against the hours you need.`,
  },
  {
    q: `What can I call my ice cream? Can I say "homemade"?`,
    a: `The federal standard of identity for "ice cream" (21 CFR 135.110) asks for at least 10% milkfat and a minimum weight of 4.5 pounds per gallon, and "frozen custard" has to contain at least 1.4% egg yolk solids: if you call it ice cream, that standard applies to your product. We found no federal rule for "homemade", "small-batch" or "house-made", so use them only if they are true: with a bought base, "made here in small batches" is accurate. The plan keeps "gelato" as a style, not a name or a promise, and it never promises "allergen-free" ice cream, because the batch freezer and the tubs are shared. The US has 9 major allergens, and milk is in most scoops.`,
  },
  {
    q: `Is this plan for soft serve, frozen yogurt, an ice cream truck or a franchise?`,
    a: `No. It is written for a scoop shop with a production room and dipping cabinets. Soft serve and frozen yogurt use a different machine and a different model, a franchise follows its franchisor's system and a shop without production changes most of the numbers, so the written plan would need heavy rewriting. For an ice cream truck, the Food Truck Business Plan Kit fits better. The Excel workbook takes any numbers you type, but the text describes a scoop shop.`,
  },
  {
    q: `Should I buy this or the Ice Cream Shop Checklists Kit Pro?`,
    a: `They do different jobs. This plan is for deciding, financing and opening the shop: the written plan, the numbers and an 80-task startup checklist. The Ice Cream Shop Checklists Kit Pro ($19, a separate kit at aichef.pro/en/digital-products/ice-cream-shop-checklist-templates) is the set of daily, weekly and monthly routines for running the shop once it is open: opening, closing, freezer temperatures, cleaning and production checks. Many owners use both: the plan before opening, the checklists after.`,
  },
  {
    q: `Is this the same as the Restaurant Business Plan Kit or the Bakery Business Plan Kit?`,
    a: `No. The Restaurant Business Plan Kit is written for a general full-service restaurant and the Bakery Business Plan Kit for a bakery. This one is built for a scoop shop: the batch freezer and the hardening cabinet, the dipping cabinets, summer seasonality and the winter plan, the dairy license question and customers per day instead of covers. The financial engine is the same lender-ready format.`,
  },
  {
    q: `Can I present this plan to a lender or investors?`,
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds, and a loan schedule with the debt service coverage ratio (DSCR), checked against a 1.25x lender target (the example shows ${CASO.dscr} in year 1 with a ${CASO.prestamo} loan next to ${CASO.propios} of the owner's own money). It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice: review the final numbers with your accountant before you apply for a loan.`,
  },
  {
    q: `Can I change the numbers in the Excel model?`,
    a: `Yes. The green cells are the ones you type: customers per day, average check, operating days, the sales mix, ingredient and packaging costs, rent, wages and every startup cost line. More than ${CASO.formulas} linked formulas recalculate the rest. To change a calculated cell, use Review, Unprotect Sheet (there is no password). The workbook and the checklist each include an Instructions tab.`,
  },
  {
    q: `Does it work in the UK, Canada or Australia?`,
    a: `Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your menu prices without it. The plan and the checklist give US units with metric beside them (°F with °C, sq ft with sq m, lb with kg). The Word plan's UK notes cover VAT on ice cream and where to check your local rules; in Canada and Australia, check your provincial or state food premises, dairy and liquor rules with your local authority. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.`,
  },
  {
    q: `What currency will I pay in?`,
    a: `The price is $39 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The Excel cells have no currency symbol, so you type amounts in your own currency; the example in the Word plan is in US dollars.`,
  },
  {
    q: `Is it a subscription? Are future updates included?`,
    a: `No subscription: you pay once and get lifetime access to the online dashboard. When we improve the plan or the workbooks, you get the new version at no extra cost: just download the files again.`,
  },
  {
    q: `Can I use it with my clients or for more than one business?`,
    a: `One purchase covers one business. If you're a consultant or an investor, you can use the files with the projects you advise, but you can't hand them copies: each business buys its own.`,
  },
  {
    q: `Is there a money-back guarantee?`,
    a: `Yes. A full 30-day guarantee. If the plan doesn't meet your expectations, we'll refund 100% with no questions asked.`,
  },
];

const data: PlanNegocioData = {
  slug: 'ice-cream-shop-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN',

  seo: {
    title: 'Ice Cream Shop Business Plan Template: Word + Excel Financial Projections + Startup Checklist | AI Chef Pro',
    description:
      'Ice cream shop business plan template: Word plan, 3-year Excel projections with summer seasonality, dairy license guide and an 80-task opening checklist. $39, instant download.',
    keywords:
      'ice cream shop business plan, ice cream parlor business plan, how to open an ice cream shop, ice cream shop startup costs, batch freezer, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-ice-cream-shop-business-plan.jpg',
  },

  schema: {
    productName: 'Ice Cream Shop Business Plan Kit',
    productDescription:
      'Ice cream shop business plan template kit for a neighborhood shop that makes its own ice cream: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow starting in March, financing with a loan schedule and DSCR, and instructions) and an 80-task startup checklist in 6 phases covering permits, production and health, staff and food safety, brand and menu, and opening and the season. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Ice Cream Shop Business Plan Kit',
  },

  images: {
    // hero bg (6) — la scooper sirviendo un cono doble desde el dipping cabinet de sabores (ES -hero) abre.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-cucurucho.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-tarrinas.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-invierno.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-plan.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden. Sin la -vitrina (descartada).
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-heladeria-cucurucho.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-tarrinas.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-invierno.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-heladeria-obrador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-heladeria-cucurucho.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready ice cream shop business plan: Word + Excel + startup checklist',
    titlePre: 'Ice Cream Shop ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template to Open a Homemade Ice Cream Shop: Word Plan + Excel Projections with Seasonality + 80-Task Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch a neighborhood ice cream shop that makes its own ice cream, with scoops, pints, ice cream cakes and a plan for the winter: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in customers per day, 12-month cash flow (starting in March, so the winter is in the numbers) and loan payments from your own numbers; and an 80-task checklist that takes you from your LLC, your lease and your dairy license question to Opening Day and your first season. Set up for the US, with notes for the UK.`,
    checkItems: [
      '10-section ice cream shop business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in customers per day and 12-month cash flow with seasonality',
      'Startup checklist: 80 tasks in 6 phases, from your LLC to Opening Day',
      'Buy a base or make your own mix: the license question, task by task',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Ice Cream Shop Business Plan Kit: 8 building blocks to test whether your shop works on paper before you sign a lease or order a batch freezer, plan the winter before the first summer, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Ice Cream Shop Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a neighborhood ice cream shop that makes its own ice cream: executive summary, concept and value proposition, market analysis (seasonality, Memorial Day to Labor Day), competitive analysis, marketing plan, operations plan (production room, dipping cabinets, pints and ice cream cakes), management and staffing, financial plan, legal requirements, permits and licenses (buying a base versus making your own mix), and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Ice Cream Shop Financial Projections (Excel, 9 Sheets)', desc: `Is an ice cream shop profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than ${CASO.formulas} linked formulas: change customers per day, average check or operating days and the whole workbook recalculates.` },
      { icon: 'Coins', title: 'Ice Cream Shop Startup Costs, Line by Line', desc: `How much does it cost to open an ice cream shop? Architect and permit fees, the build-out of the production room and shop, the electrical service, plumbing and ventilation, a batch freezer, a hardening cabinet, storage freezers, dipping cabinets, the front counter with dipper wells, furniture and patio, POS, an ice cream training course, branding and launch, and opening inventory, each with a reference price you replace with your quotes, plus a deposit, rent before opening, a contingency and working capital for the slow months.` },
      { icon: 'TrendingUp', title: 'Break-Even in Customers per Day + 3 Scenarios', desc: `How many customers a day you need at your average check (excl. sales tax) to cover every cost, and the cash break-even with loan payments in and depreciation out, with a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance: honest about what a slow first year does to your cash.` },
      { icon: 'Snowflake', title: '12-Month Cash Flow with Seasonality (Month 1 = March)', desc: `The month-by-month cash flow starts in March, ramps up through the spring, peaks in July and shows what November to February does to your balance, with the sales tax you collect remitted in the months you actually pay it. The question that decides a loan: in which month does the cash run out?` },
      { icon: 'Users', title: 'Staffing & Seasonal Labor (6 Roles)', desc: `Owner / ice cream maker and GM, a year-round shift lead, a seasonal scooper (April to September), a summer scooper (June to August), a production assistant (May to September) and relief cover, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need and flags any pay below the minimum wage.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (80 Tasks, 6 Phases)', desc: `Business setup (LLC, EIN, state payroll accounts, business license and sales tax permit, your loan application and the license decision), site and permits (zoning, plan review, building permit and certificate of occupancy, the patio), production and health (the base supplier agreement, cold chain, dipper wells, allergens, the health permit), staff and food safety (offer letters, I-9, W-4, a certified food protection manager and food handler cards, teen scooper hours), brand and menu, and opening and the season (Opening Day, your first 90 days and the winter plan).` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25x target, plus investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: an ice cream shop plan written for the format lenders expect, with a financial model that has the summer and the winter in it and a checklist that puts the license decision on your calendar.`,
    reasons: [
      { icon: 'IceCream', title: 'Built for an Ice Cream Shop That Makes Its Own Ice Cream', desc: `A batch freezer in view of the counter, 18 flavors in summer and 10-12 in winter, scoops, hand-packed pints, ice cream cakes to order, a patio and the owner as ice cream maker and GM. How much does it cost to open an ice cream shop? ${CASO.capex} of startup costs and ${CASO.caja} of total cash needed in the example, line by line. Nothing to strip out from a restaurant or bakery template.` },
      { icon: 'BarChart3', title: 'Is an Ice Cream Shop Profitable? Real Margins vs the 10-25% Claims', desc: `The example: ${CASO.customers} customers a day at ${CASO.ticket} for ${CASO.dias} days, ${CASO.ventas} in year-1 sales, a net of ${CASO.netoPct1} in year 1 and ${CASO.netoPct3} by year 3, and ${CASO.equilibrio} customers a day to break even, with the owner on payroll. Many articles quote 10-25%; other sources say 6-9%. The pessimistic scenario loses money, and the plan says so. Replace the numbers with yours.` },
      { icon: 'Scale', title: 'Buy a Base or Make Your Own Mix? Dairy Licenses by State', desc: `The example buys a pasteurized base from a licensed dairy; making your own mix is a variant with a batch pasteurizer and, usually, a state dairy plant or frozen dessert manufacturer license. States differ (Vermont and Georgia, for example, handle it differently), so the plan never says "no license needed": it tells you to ask your state department of agriculture and your health department, and the checklist turns the decision into a task.` },
      { icon: 'Sun', title: 'Seasonality: Open in March and Get Through the Winter', desc: `Summer sales run well above the yearly average and winter well below it. The cash flow starts in March, the lowest balance of the year (${CASO.saldoMin} in the example) comes right after you pay for the investment, and the winter plan (ice cream cakes, holiday pies and pints, hot chocolate, catering and three weeks closed in January) is part of the concept, not an afterthought.` },
      { icon: 'ClipboardCheck', title: 'Sales Tax, Teen Scoopers and Permits', desc: `A scoop to eat now is generally taxed as prepared food, while packaged pints and whole cakes may be treated as groceries in your state. Scoopers aged 14 and 15 follow federal hour limits (29 CFR 570.35) and your state may add work permits. The plan and the checklist cover sales tax, FLSA hours, plan review, the health permit and the building permit, with no state forms included: requirements vary by state, county and city.` },
      { icon: 'Layers', title: 'Plan Now, Run It Daily: This Kit vs the Ice Cream Shop Checklists Kit Pro', desc: `This kit gets the shop decided, financed and opened: the plan, the numbers and an 80-task startup checklist. The Ice Cream Shop Checklists Kit Pro ($19, a separate kit, link below) is the set of daily, weekly and monthly routines for running it once it is open. Different jobs: many owners use the plan before opening and the checklists after.` },
      { icon: 'Banknote', title: 'Lender-Ready Format, Not a Guarantee', desc: `A written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses and a loan schedule with the DSCR against a 1.25x target (${CASO.dscr} in the example, with a ${CASO.prestamo} loan next to ${CASO.propios} of the owner's own money). A planning tool, not financial, tax or legal advice: review your final numbers with your accountant.` },
      { icon: 'Globe', title: 'US Units, With Notes for the UK, Canada and Australia', desc: `°F with °C, sq ft with sq m, lb with kg; tax, wage and unit cells you can edit; UK notes on VAT for ice cream; and the US · UK · Canada · Australia Equivalents Guide included as a bonus, with the local terms, taxes, food safety and staff rules side by side.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    `CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening restaurants, bakeries and ice cream shops, combining hands-on operations with financial planning.`,
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      `Besides the business plan, the financial model and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves`,
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Ice Cream Shop Dairy License, Permits & Food Safety Guide (US + UK Notes)',
        desc: `Section 9 of the plan plus the permit and production phases of the checklist: the license decision (buy a base or make your own mix), plan review before you build, the health permit and inspection, the building permit and certificate of occupancy, running water for the dipper wells, cold chain at 41 °F and 0 °F, the supplier agreement for the base, a certified food protection manager and food handler cards, the 9 US allergens, sales tax and teen scooper hours, with notes for the UK. No state forms included: requirements vary by state, county and city.`,
        image: '/lovable-uploads/ai-gallery/plan-heladeria-obrador.jpg',
      },
      {
        icon: 'BarChart3',
        title: 'US Ice Cream Shop Benchmarks (Sourced)',
        label: 'BONUS 2',
        desc: `The reference table inside the workbook: peak season, ice cream cost, the federal "ice cream" standard, storage and serving temperatures, buying a base versus making your own mix, labor and rent as a share of sales, production waste, electrical service, sales tax and minimum wage, each with its source or marked "kit estimate" when there isn't one, plus five OK / REVIEW checks on your P&L against editable thresholds.`,
        image: '/lovable-uploads/ai-gallery/plan-heladeria-plan.jpg',
      },
      {
        icon: 'Globe',
        label: 'BONUS 3',
        title: 'US · UK · Canada · Australia Equivalents Guide',
        desc: `Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.`,
        image: '/lovable-uploads/ai-gallery/en-equivalents-guide.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  guarantee: {
    text:
      `If the business plan doesn't live up to your expectations, we'll refund 100% of your money. No questions, no hassle.`,
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  faqs: FAQS,

  cta: {
    headingPre: `It's Time to Open Your `,
    headingGold: 'Ice Cream Shop',
    subtitle:
      `Plan it before you sign the lease and order the batch freezer: the written plan, the numbers behind it, the winter plan and the license checklist, for a one-time payment.`,
    items: [
      '10-section ice cream shop business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in customers per day and a 12-month cash flow with seasonality',
      'Startup checklist: 80 tasks in 6 phases',
      'BONUS: Dairy License, Permits & Food Safety Guide (included in the plan)',
      'BONUS: US Ice Cream Shop Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'ICE CREAM SHOP BUSINESS PLAN — $39',

  // Salientes: Ice Cream Shop Checklists Kit Pro (rutinas del local abierto, $19), Food Cost (coste por sabor y por tarrina),
  // HACCP (cadena de frio), Restaurant Business Plan (el hermano general), Restaurant Financial Plan + Staff Scheduling +
  // los otros planes EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/ice-cream-shop-checklist-templates', label: 'Ice Cream Shop Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/pizza-shop-business-plan', label: 'Pizza Shop Business Plan Kit' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'New product · Version 2.2 · October 2026',

  alreadyBought: {
    product: 'ice-cream-shop-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
