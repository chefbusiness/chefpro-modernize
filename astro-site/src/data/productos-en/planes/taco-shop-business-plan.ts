// astro-site/src/data/productos-en/planes/taco-shop-business-plan.ts
// TIENDA INTERNACIONAL EN — Taco Shop Business Plan Kit. DUPLICADO de la ficha gemela de la familia Planes EN (mismo tipo PlanNegocioData,
// misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Edicion inglesa del ES "Plan de Negocio:
// Taqueria" (hreflang reciproco, familia plan-negocio-taqueria), cuyo contenido y cifras NO se reutilizan: el EN es el
// concepto de un counter-service taco shop de EE. UU.
// SPEC: scripts/productos-digitales/plan-taqueria/F1-camino.md §6 + scripts/productos-digitales/business-plans-en-12/.
//   Research: business-plans-en-12/F1-research-us-delta.md (§3 SERP/PAA y FAQ, §6 legal US, §9 jerga y terminos de landing).
//   · Title/meta/H1 SIN anio fijo (AGENTS.md: si algun dia lleva anio, token {year}); NOMBRE DEL PRODUCTO primero; H1 Forma B
//     `Taco Shop ` + oro `Business Plan` + «Template to Open a Taqueria: …»; «taco shop» en nombre/H1, «taqueria» en subtitulo
//     y prosa; nunca «Tex-Mex» como sinonimo ni «authentic» como promesa.
//   · $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating, review ni testimonios.
//   · Ficheros de dl/taco-shop-business-plan/ (plan, proyecciones, checklist de 80 tareas y calculadora de taco y trompo) + la
//     guia comun de equivalencias EN. Los 6 H2 de research §9 no caben como H2 (constantes de UI_PLAN): sus keywords van en
//     los H3 de «why», las tarjetas del grid y la FAQ.
//   · Cifras MEDIDAS (business-plans-en-12/cifras_caso.json y F2-NOTAS §3; caso US: 115 covers × $17.50 × 308 dias):
//     ventas A1 $619,850, CAPEX $197,600 (18 partidas $176,800 + contingencia $9,600 + 2 meses de fianza y 2 de renta previa),
//     necesidad total de caja $275,612, neto A1 ≈ 6 % → ≈ 9 % en A3, equilibrio ≈ 100 covers/dia, COGS 26 %, personal 35 %.
//     Nada movible: ni DSCR, ni prestamo, ni payback, ni saldos. Calculadora: cono de 30 lb, rendimiento 64.8 %, ≈ 207 tacos
//     por cono, taco al pastor ≈ $1.00 de coste y 25 % de food cost a $4.00, equilibrio de la tortilla propia ≈ 656 al dia
//     (todo «kit estimate, editable»).
//   · Honestidad (research §6, §10): no se promete licencia de alcohol, venta desde casa, «gluten-free», una temperatura
//     unica para el trompo (145 °F o 155 °F segun el condado) ni margenes del «15-25 %».
//   · Imagenes: las 7 plan-taqueria-*.jpg del ES (sin texto en espanol), mismos huecos que el ES. OG = hero del ES.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en business-plans-en-12/cifras_caso.json (29-oct). Nada movible (ni DSCR, ni prestamo,
// ni saldos, ni payback). ────────────────────────────────────────────────────────────────────────────────────────────────
const CASO = {
  covers: '115', // B4 — covers per day (dine-in + take-out + marketplace equivalents)
  ticket: '$17.50', // B5 — average check (excl. sales tax and tip)
  dias: '308', // B6 — operating days (closed Mondays and the main holidays)
  ventas: '$619,850', // ventas A1 = 115 × $17.50 × 308
  capex: '$197,600', // 18 partidas $176,800 + contingencia $9,600 + 2 meses de fianza + 2 de renta previa
  partidas: '$176,800', // las 18 partidas de inversion
  necesidad: '$275,612', // CAPEX + working capital ($78,012)
  netoPct1: '6%', // neto A1 ($39,009), redondeado
  netoPct3: '9%', // neto A3 ($62,763), redondeado
  equilibrio: '100', // covers/dia (contable)
  cogsPct: '26%', // COGS 26.3 % (PyG!B52 = 0.2625)
  personalPct: '35%', // personal 34.6 %
  fte: '5', // 5.03 FTE (Personal!C12 = 5.025)
  formulas: '700', // "more than N": el libro tiene 741 formulas
  tacos: '207', // tacos por cono de 30 lb (calculadora, defecto)
  eqTortilla: '656', // equilibrio de la tortilla propia (tortillas por dia)
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `What should a taco shop business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a counter-service taqueria with a trompo, plus the Excel financial projections that back them up, a taco cost and trompo yield calculator, and an 80-task startup checklist.`,
  },
  {
    q: `Is it a generic template or built for a taco shop?`,
    a: `Built for a neighborhood counter-service taqueria in a mid-size US city: about 1,200 sq ft with 30 seats plus a seasonal patio of 12, ordering at the counter, take-out and delivery, a gas trompo for al pastor, a flat-top griddle and comal, a fryer for chips, a steam table and a salsa bar, beer and wine only, closed on Mondays and an owner who is the head taquero and the general manager. Nothing to strip out from a restaurant template. If your concept is different, the Excel workbook takes any numbers you type, but the written plan describes this shop (see the last questions about taco trucks, franchises and full-service Mexican restaurants).`,
  },
  {
    q: `How much does it cost to open a taco shop?`,
    a: `It depends on the space, the hood and the build-out, which move the number more than anything else. The kit's example comes in at ${CASO.capex} in startup costs, and ${CASO.necesidad} in total cash once working capital is added. Line by line it covers architect and permit fees, a second-generation build-out ($42,000), a Type I hood with fire suppression and makeup air ($22,000), electrical, plumbing, gas lines and the grease interceptor, two vertical broilers for the trompo, a flat-top griddle and comal, a fryer, a steam table, a walk-in cooler, a refrigerated prep table and salsa bar, dish and sink equipment, furniture for 30 seats and the patio, POS and online ordering, branding and launch, and opening inventory, plus a deposit, rent before opening and a contingency. In the listings we read, a new gas vertical broiler ran from $999 to $2,844 and a 36-inch flat-top griddle from about $2,100 to $2,500. Replace each line with your own quotes: they are example prices, not a price list.`,
  },
  {
    q: `Is a taco shop profitable? How much do owners make?`,
    a: `It can be, but not at the 15-25% that some templates and articles promise. In the kit's example the shop sells ${CASO.ventas} in year 1 (${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days), with about ${CASO.cogsPct} of sales in cost of goods and about ${CASO.personalPct} in labor, and it leaves a modest net profit of about ${CASO.netoPct1} of sales in year 1, rising to about ${CASO.netoPct3} by year 3, with a break-even of about ${CASO.equilibrio} covers a day. The owner is already on payroll as head taquero and general manager, so any profit is on top of that salary. The pessimistic scenario (fewer covers, a lower check and fewer days) loses money in year 1, and the plan says so. Whether you earn more depends on your sales, your check and what you pay yourself: replace the example with your own numbers before you decide.`,
  },
  {
    q: `What is the food cost of a taco?`,
    a: `It depends on what you pay for the meat, the portion and what you lose on the cone. With the kit's starting values (kit estimates, editable), an al pastor street taco on two small corn tortillas costs about $1.00 and runs about 25% food cost at a $4.00 menu price. The Taco Cost & Trompo Yield Calculator prices ten items from your own ingredient prices and portions (eight kinds of taco, an order of 3 and an al pastor gringa) and gives you the cost, the food cost percentage, the margin and the menu price you need, so you don't set your prices by feel. Street taco prices vary a lot: in the menus we read, a mid-size city charged about $3.00 to $3.75 and big-city shops started around $4.95.`,
  },
  {
    q: `How many tacos come out of a trompo?`,
    a: `There is no single number: it depends on the weight of the cone, the ounces you serve per taco and, above all, what you lose to cooking, drip and the leftover at close. With the calculator's starting values (kit estimates, editable: a 30 lb cone, 8% marinade, a 35% cooking loss plus 5% in trimmings, and 1.5 oz served per taco) the yield is about 64.8% and a cone gives about ${CASO.tacos} tacos. The Trompo Yield sheet does the math with your own numbers and shows you how to measure your own cone, which is what really protects your margin. Weighing is the whole trick.`,
  },
  {
    q: `What temperature does al pastor need? What will my health department ask?`,
    a: `There is no single answer, so the kit doesn't give one. The FDA Food Code is adopted state by state, and the county guidance we read for vertical broilers is not uniform: some counties ask for 145 °F for whole-muscle pork and others for 155 °F, with limits on how long a cone may stay on the broiler and what you do with the leftover. The checklist tells you to get your health department's vertical broiler rules in writing (cook temperature, maximum time on the broiler, leftover cone) before you buy the equipment, and the calculator has a cell for your county's cook temperature. The plan also covers the marinated cone held at 41 °F or below, a probe thermometer and the date marking.`,
  },
  {
    q: `Do I need a Type I hood and fire suppression?`,
    a: `Almost certainly, over the griddle, the fryer and the vertical broilers, and your fire marshal or building department makes the final call. The example budgets a Type I hood with a UL 300 fire suppression system and makeup air at $22,000; published ranges for a hood and suppression run from about $5,000 to about $25,000 depending on size and the duct run to the roof. That is also the filter for the space: if the building can't take a duct to the roof, there is no trompo. A charcoal trompo or grill is a solid fuel operation and falls under NFPA 96 chapter 14 (a separate exhaust, a spark arrestor, ash removed daily), so the example plans for gas and treats charcoal as a variant. The checklist tells you to ask your fire marshal in writing before you sign the lease.`,
  },
  {
    q: `Should I buy corn tortillas or make my own?`,
    a: `At the volume of a neighborhood shop, buying usually wins. The example uses a double 6-inch corn tortilla and spends about 650 a day. Bought ones (Mission 6-inch, 360 to a case at about $0.16 each in the listing we read) cost about $33,000 a year at that volume; making your own with masa harina needs a press or a machine ($7,808 for a commercial tortilla machine in the listing we read) and about three-quarters of a full-time employee. With the kit's starting values (kit estimates, editable) the break-even is about ${CASO.eqTortilla} tortillas a day, right at the edge, so the example buys them at opening and treats a fresh tortilla as a product decision to revisit if your volume grows well past the break-even. The Tortillas sheet lets you compare both with your prices and volume. Nixtamal from whole corn is beyond this kit: we found no US prices for corn or a mill to price it honestly.`,
  },
  {
    q: `How much do DoorDash, Uber Eats and Grubhub charge a taqueria?`,
    a: `Published tiers run from about 15% to 30% of the order for delivery, and from 6% to 10% for pickup orders. DoorDash lists Basic at 15%, Plus at 25% and Premier at 30%, with 6% for pickup; Uber Eats lists 20% (15% in selected cities) for Lite, 25% for Plus and 30% for Premium, with 7% or 10% for pickup; Grubhub lists marketing tiers of 5%, 15% and 20% plus 10% for delivery and a card processing fee (3.05% + $0.30). Tiers change, so check them before you sign. The example uses the 25% tier on 15% of sales and treats counter orders, pickup and direct phone or web orders as commission-free. Tacos are one of the easier foods to send out, but the commission is the first number to check, and the Taco Costing sheet shows the margin per channel.`,
  },
  {
    q: `What food safety and allergen rules apply to a taco shop?`,
    a: `The kit follows the FDA Food Code, which each state adopts in its own edition. Cut tomatoes are a time/temperature control for safety (TCS) food, which makes fresh pico de gallo and salsas TCS foods held at 41 °F or below, or at 135 °F or above; carnitas, birria and braised fillings go on the steam table hot. For a salsa bar kept out of the cooler, the checklist includes a written time as a public health control procedure (up to 4 hours, with the time marked) and asks you to check with your regulator. Guacamole is not named in the Food Code we read, so the plan says to treat it as TCS and ask. The US has 9 major allergens, sesame being the ninth since 2023: a salsa macha is peanuts and sesame, many moles have tree nuts, peanuts and sesame, flour tortillas are wheat and cheese and crema are milk, so the plan has you label the salsa bar. It does not promise gluten-free: corn tortillas are naturally gluten-free, but a shared comal or fryer with flour tortillas makes a gluten-free claim hard to stand behind without a written protocol. A certified food protection manager and food handler cards depend on your state and county.`,
  },
  {
    q: `Can I make tacos at home and sell them?`,
    a: `Usually not, and this plan assumes a permitted shop. Cottage food laws, which let you sell some low-risk foods made at home, differ by state, while cooked meats, fresh salsas and cut tomatoes are TCS foods under the FDA Food Code. We found no federal rule that lets you sell tacos from your home kitchen, so check with your state and county health departments before you spend.`,
  },
  {
    q: `Do I need a license to serve beer and wine?`,
    a: `Probably yes if you want to sell Mexican beer or wine, and it can take months, so the plan treats it as a lease contingency. Cost and timing vary a lot by state, and in states with a quota a license costs far more than in others, so ask your state's alcohol board before you sign. The kit does not promise a license: the checklist walks you through the application, and the plan covers liquor liability insurance. It's a beer and wine shop in the example, not a full bar: for that, start from the Bar Business Plan Kit.`,
  },
  {
    q: `How does the taco cost and trompo yield calculator work?`,
    a: `Four sheets: Trompo Yield, Tortillas, Taco Costing and Instructions. The trompo sheet works in pounds and ounces (16 oz per lb): you type the weight of the cone, the marinade, the cooking loss and the ounces per taco, and it gives you the meat served, the yield, the tacos per cone and the cost of the meat per taco, with a cell for your county's cook temperature. The tortilla sheet compares buying with making your own from masa harina and finds the break-even in tortillas per day. The costing sheet prices ten items from the ingredient prices you type (the example's are kit estimates for October 2026: replace them with your distributor's) and shows the food cost, margin and menu price of each, plus the margin of the order of 3 and the gringa dine-in, on takeout and on a delivery app. In the example, an al pastor taco costs about $1.00 at a 25% food cost on a $4.00 price (editable).`,
  },
  {
    q: `Can I use this for a taco truck?`,
    a: `Not as it stands. This plan is written for a taco shop with a fixed location, a dining room, a patio and a hood. A taco truck has a different license (a mobile food unit), a commissary, a different layout and often no dining room, so the written plan would need heavy rewriting. For a taco truck, the Food Truck Business Plan Kit fits better. The Excel workbook takes any numbers you type, but the text describes a taqueria with a counter and a dining room.`,
  },
  {
    q: `Is this a Mexican restaurant business plan? Is it for a franchise?`,
    a: `It is a taco shop plan, not a full-service Mexican restaurant with table service and a full bar. For that, the Restaurant Business Plan Kit is the general plan, with the same lender-ready format. And it is not for a franchise: a franchise follows its franchisor's system and fee structure (a major taco chain's published initial investment can run into seven figures), which is a different kind of decision. This kit is for the independent owner who writes the concept, picks the space and sets the menu.`,
  },
  {
    q: `Should I buy this or the Restaurant Checklists Kit Pro?`,
    a: `They do different jobs. This plan is for deciding, financing and opening the shop: the written plan, the numbers and an 80-task startup checklist. The Restaurant Checklists Kit Pro is the set of daily, weekly and monthly routines for running a restaurant once it is open: opening, closing, cleaning and food safety checks. Many owners use both: the plan before opening, the checklists after.`,
  },
  {
    q: `Can I present this plan to a lender or investors?`,
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds, and a loan schedule with the debt service coverage ratio (DSCR) you can check against your lender's target. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice: review the final numbers with your accountant before you apply for a loan.`,
  },
  {
    q: `Can I change the numbers in the Excel model?`,
    a: `Yes. The green cells are the ones you type: covers per day, average check, operating days, the split between food and beverage, ingredient costs, cost of goods percentages, delivery share and commission, rent, wages and every startup cost line. More than ${CASO.formulas} linked formulas recalculate the rest. To change a calculated cell, use Review, Unprotect Sheet (there is no password). The workbook, the calculator and the checklist each include an Instructions tab.`,
  },
  {
    q: `Does it work in the UK, Canada or Australia?`,
    a: `Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your menu prices without it. The plan and the checklist give US units with metric beside them (°F with °C, sq ft with sq m, lb with kg), and the calculator works in pounds and ounces only. The plan's UK notes cover registering with your council at least 28 days before trading, the food hygiene rating, 20% VAT on hot food and the 14 UK allergens (which, unlike the 9 US ones, include celery, mustard, molluscs and sulphites). In Canada and Australia, check your provincial or state food premises, fire and liquor rules with your local authority. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.`,
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
  slug: 'taco-shop-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_BUSINESS_PLAN',

  seo: {
    title: 'Taco Shop Business Plan Template: Word + Excel Projections + Taco Cost & Trompo Yield Calculator | AI Chef Pro',
    description:
      'Taco shop business plan template for a counter-service taqueria: Word plan, 3-year Excel projections, taco cost and trompo yield calculator, hood and permit checklist.',
    keywords:
      'taco shop business plan, taqueria business plan, taco restaurant business plan, mexican restaurant business plan, how to open a taco shop, taco shop startup costs, taco shop profit margin, trompo yield, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg',
  },

  schema: {
    productName: 'Taco Shop Business Plan Kit',
    productDescription:
      'Taco shop business plan template kit for a counter-service taqueria with a trompo for al pastor: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a taco cost and trompo yield calculator with a tortilla buy-or-make comparison, and an 80-task startup checklist in 6 phases covering the hood, the gas line and the permits. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Taco Shop Business Plan Kit',
  },

  images: {
    // hero bg (6) — la taqueria con el trompo girando y el mostrador preparado (ES -hero) abre.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-trompo.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-tortilla.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-salsas.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-equipo.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden.
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-taqueria-tortilla.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-trompo.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-salsas.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-taqueria-trompo.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-taqueria-salsas.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready taco shop business plan: Word + Excel + taco cost & trompo yield calculator',
    titlePre: 'Taco Shop ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template to Open a Taqueria: Word Plan + Excel Projections + Taco Cost & Trompo Yield Calculator + Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch a counter-service taqueria with a trompo for al pastor, a salsa bar, dine-in, take-out and delivery: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in covers per day, 12-month cash flow and loan payments from your own numbers; a calculator that prices every taco and every trompo; and an 80-task checklist that takes you from your LLC, your lease and the fire marshal to your first 90 days open. Set up for the US, with notes for the UK.`,
    checkItems: [
      '10-section taco shop business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in covers per day and 12-month cash flow',
      'Taco cost & trompo yield calculator: tacos per cone, food cost per taco, corn tortillas bought or made',
      'Startup checklist: 80 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Taco Shop Business Plan Kit: 9 building blocks to test whether your taqueria works on paper before you sign a lease or buy a trompo, price every taco from its meat and tortillas, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Taco Shop Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a neighborhood counter-service taqueria: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan (trompo, griddle, salsa bar, dine-in, take-out and delivery), management and staffing, financial plan, legal requirements, permits and hood rules, and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Taco Shop Financial Projections (Excel, 9 Sheets)', desc: `Is a taco shop profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than ${CASO.formulas} linked formulas: change covers per day, average check or operating days and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Taco Cost & Trompo Yield Calculator (Trompo Yield + Tortillas + Taco Costing)', desc: `Food cost per taco from your own prices. The trompo sheet works in pounds and ounces: cone weight, marinade, cooking loss and ounces per taco in, the yield and the tacos per cone out. The tortilla sheet compares buying with making your own from masa harina and finds the break-even per day. The costing sheet prices ten items, from al pastor and carnitas tacos to an order of 3 and a gringa, with the cost, the food cost percentage and the menu price you need, using ingredient prices you replace with your distributor's.` },
      { icon: 'Coins', title: 'Taco Shop Startup Costs, Line by Line', desc: `How much does it cost to open a taco shop? Architect and permit fees, a second-generation build-out, electrical, plumbing, gas lines and the grease interceptor, a Type I hood with fire suppression and makeup air, two vertical broilers for the trompo, a flat-top griddle and comal, a fryer and range, a steam table, a walk-in cooler, a refrigerated prep table and salsa bar, dish and sink equipment, furniture and patio, POS and online ordering, LLC and legal, branding and launch, and opening inventory, each with a reference price you replace with your quotes, plus a deposit, rent before opening, a contingency and working capital.` },
      { icon: 'TrendingUp', title: 'Break-Even in Covers per Day + 3 Scenarios', desc: `How many covers a day you need at your average check (excl. sales tax) to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance: honest about what a slow first year does to your cash.` },
      { icon: 'Users', title: 'Staffing & Shift Labor', desc: `Owner / head taquero and GM, a taquero for the trompo and griddle, a prep cook for marinades, carnitas and salsas, a counter lead and cashier, part-time counter and expo, and dish and prep, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need and flags any pay below the minimum wage.` },
      { icon: 'BarChart3', title: 'Dine-In, Take-Out & Delivery Mix', desc: `Dine-in versus take-out and delivery, with the share of sales that goes through third-party delivery marketplaces and the commission you pay on it (the DoorDash and Uber Eats tiers are in the benchmarks table), plus hood cleaning, music licensing, and waste, grease and used-oil hauling as their own cost lines.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (80 Tasks, 6 Phases)', desc: `Business setup (LLC, EIN, state payroll accounts, business license and sales tax permit, your loan application), site, hood, gas and permits (zoning, plan review, building permit and certificate of occupancy, the fire marshal in writing on the hood and the broilers, a licensed gas contractor, the grease interceptor, the beer and wine license as a lease contingency), kitchen, trompo and health (cones held at 41 °F, the salsa bar with a written time as a public health control procedure, your health department's vertical broiler rules in writing), staff, training, safety and allergens (offer letters, I-9, W-4, CFPM and food handler cards, the 9 allergens including sesame, signs at the salsa bar), menu, brand, delivery and suppliers, and your first 90 days.` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year, plus investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: a taco shop plan written for the format lenders expect, with a financial model, a taco cost and trompo yield calculator and the hood and permit rules that recalculate from your own numbers.`,
    reasons: [
      { icon: 'Flame', title: 'Built for a Counter-Service Taco Shop', desc: `A taquero who slices al pastor off the trompo onto double corn tortillas, a griddle and comal, a salsa bar, a dining room of 30 seats plus a patio, take-out and delivery; beer and wine; the owner as head taquero and GM. How much does it cost to open a taco shop? The hood, the broilers and the build-out, line by line. Nothing to strip out from a restaurant or food truck template.` },
      { icon: 'ShieldCheck', title: 'Al Pastor on the Trompo: Yield, Food Safety and Your Health Department', desc: `Tacos per cone, the cost of the meat per taco and what you lose to cooking, drip and the leftover, from your own numbers. The plan explains the cold holding of marinated cones, the cut tomatoes and salsas as TCS foods, and why the cook temperature depends on your county: it does not give one figure, and the checklist tells you to get your health department's rules in writing.` },
      { icon: 'Map', title: 'Hood, Gas and Permits: Type I Hood, Fire Suppression, Fire Marshal', desc: `A trompo, a griddle and a fryer need a Type I hood with fire suppression and a duct to the roof, and the building has to allow it. The plan budgets the hood, explains plan review, the building permit, the certificate of occupancy and the health permit, and tells you to ask the fire marshal in writing. It does not promise a beer and wine license either: it treats it as a lease contingency.` },
      { icon: 'BarChart3', title: 'Honest Numbers, Real Margins (Not the 15-25% Myth)', desc: `The example: ${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days, ${CASO.ventas} in year-1 sales, a net of about ${CASO.netoPct1} in year 1 and about ${CASO.netoPct3} by year 3, and about ${CASO.equilibrio} covers a day to break even, with the owner on payroll and delivery marketplaces priced at their published tiers. The pessimistic scenario loses money, and the plan says so. Replace the numbers with yours.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    `CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening restaurants and taquerias, combining hands-on operations with financial planning.`,
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      `Besides the business plan, the financial model, the calculator and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves`,
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Taco Shop Hood, Gas & Permits Guide (US + UK Notes)',
        desc: `Section 9 of the plan plus Phase 2 of the checklist: plan review before you build, the health permit and inspection, the building permit and certificate of occupancy, the Type I hood and fire suppression, the questions to put to your fire marshal and your health department in writing, a beer and wine license as a lease contingency, CFPM and food handler cards, the 9 US allergens including sesame, a written time as a public health control procedure, liquor liability, W-2 employees and sales tax, with notes for the UK. No state forms included: requirements vary by state, county and city.`,
        image: '/lovable-uploads/ai-gallery/plan-taqueria-trompo.jpg',
      },
      {
        icon: 'BarChart3',
        title: 'US Taco Shop Benchmarks (Sourced)',
        label: 'BONUS 2',
        desc: `The reference table at the end of the workbook's Instructions tab: street taco prices, the al pastor food cost and trompo yield, vertical broiler prices, delivery marketplace tiers, sales tax, hot and cold holding temperatures, minimum wage, labor and rent as a share of sales, and the al pastor cook temperature set by your county, each with its source or marked as a kit estimate when there isn't one. Plus five color-coded ratios on the P&L (gross margin, cost of goods, labor, rent and net income) against thresholds you can edit.`,
        image: '/lovable-uploads/ai-gallery/plan-taqueria-plan.jpg',
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
    headingPre: `It's Time to Launch Your `,
    headingGold: 'Taco Shop',
    subtitle:
      `Plan it before you sign the lease and buy the trompo: the written plan, the numbers behind it, the cost of every taco and the permits list, for a one-time payment.`,
    items: [
      '10-section taco shop business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in covers per day, with a sensitivity table',
      'Taco cost & trompo yield calculator: tacos per cone and food cost per taco',
      'Startup checklist: 80 tasks in 6 phases',
      'BONUS: Taco Shop Hood, Gas & Permits Guide (section 9 of the plan + phase 2 of the checklist)',
      'BONUS: US Taco Shop Benchmarks (table in the workbook)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'TACO SHOP BUSINESS PLAN — $39',

  // Salientes: Restaurant Checklists (rutinas del local abierto; no hay Taco Checklists EN), Food Cost (coste por taco), HACCP
  // (TCS, TPHC), Restaurant Business Plan (el hermano general), Food Truck (el taco truck), Coffee Shop (el hermano de local
  // fijo con campana), Restaurant Financial Plan + Staff Scheduling.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/rotisserie-chicken-restaurant-business-plan', label: 'Rotisserie Chicken Restaurant Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'New product · Version 2.2 · October 2026',

  alreadyBought: {
    product: 'taco-shop-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
