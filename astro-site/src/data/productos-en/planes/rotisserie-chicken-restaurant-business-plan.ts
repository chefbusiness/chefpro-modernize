// astro-site/src/data/productos-en/planes/rotisserie-chicken-restaurant-business-plan.ts
// TIENDA INTERNACIONAL EN — Rotisserie Chicken Restaurant Business Plan Kit. DUPLICADO de la ficha gemela EN de la familia Planes
// (mismo tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Edicion inglesa del ES
// "Plan de Negocio: Polleria y Asador de Pollos" (hreflang reciproco, familia plan-negocio-polleria), cuyo contenido y cifras NO se
// reutilizan: el EN es el concepto de un counter-service rotisserie chicken restaurant de EE. UU. (estilo peruano, pollo a la brasa).
// SPEC: scripts/productos-digitales/plan-polleria/F1-camino.md §6-§7 + scripts/productos-digitales/business-plans-en-13/.
//   Research: business-plans-en-13/F1-research-us-delta.md (§3 SERP/PAA y FAQ, §6 legal US, §9 jerga y terminos de landing).
//   · Title/meta/H1 SIN anio fijo (AGENTS.md: si algun dia lleva anio, token {year}); NOMBRE DEL PRODUCTO primero; H1 Forma B
//     `Rotisserie Chicken Restaurant ` + oro `Business Plan` + «Template for a Peruvian Pollo a la Brasa or Charcoal Chicken Shop: …»;
//     «pollo asado» NUNCA como sinonimo (en EE. UU. es pollo mexicano a la parrilla); peri-peri solo como estilo y sin marcas
//     («PERi-PERi», «Broaster»); nunca «authentic» como promesa.
//   · $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating, review ni testimonios.
//   · Ficheros de dl/rotisserie-chicken-restaurant-business-plan/ (plan, proyecciones, checklist de 80 tareas y calculadora del
//     pollo, el asador y el escandallo) + la guia comun de equivalencias EN. SOLO se afirma lo que existe en los entregables
//     (F2-NOTAS, cifras_caso.json y calculadora_pol.py): UN solo bonus (la guia de equivalencias); no se describen «bonus» que
//     sean secciones del plan por analogia con otro producto.
//   · Cifras MEDIDAS (business-plans-en-13/cifras_caso.json y F2-NOTAS §3; caso US: 130 covers × $17.50 × 360 dias):
//     ventas A1 $819,000, CAPEX $237,832, necesidad total de caja $335,708, neto A1 ≈ 7 % → ≈ 10 % en A3, equilibrio ≈ 110
//     covers/dia, COGS 28 %, personal 33 % (10 puestos, 6.60 FTE). Nada movible: ni DSCR, ni prestamo, ni payback, ni saldos.
//     Calculadora (hojas Chicken Yield, Rotisserie, Costing, Instructions): pollo de 3.0 lb WOG a $1.75/lb, ≈ $5.99 por pollo
//     entero, rendimiento 72 %, food cost 31.5 % del pollo entero a $19.00, family meal ≈ 30 %, 96 pollos por carga con dos
//     rotisseries de 8 spits, 192 pollos antes de la 1:30 pm del domingo (todo «kit estimate, editable»).
//   · Honestidad (research §6, §10): no se promete licencia de alcohol, «gluten-free», una temperatura de display unica segun el
//     condado, ni margenes del «15-25 %»; el carbon es variante (NFPA 96, escape propio), el caso es de gas.
//   · Imagenes: las 7 plan-polleria-*.jpg del ES (sin texto en espanol), mismos huecos que el resto de la familia EN. OG = hero del ES.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_ROTISSERIE_CHICKEN_RESTAURANT_BUSINESS_PLAN (resuelto en el wrapper .astro; sin
// la env var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en business-plans-en-13/cifras_caso.json (29-oct). Nada movible (ni DSCR, ni prestamo, ni
// saldos, ni payback). ───────────────────────────────────────────────────────────────────────────────────────────────────
const CASO = {
  covers: '130', // B4 — covers per day (counter, pickup, pre-order and marketplace equivalents)
  ticket: '$17.50', // B5 — average check (excl. sales tax and tip)
  dias: '360', // B6 — operating days (open 7 days a week)
  ventas: '$819,000', // ventas A1 = 130 × $17.50 × 360
  capex: '$237,832', // inversion en obra, campana, rotisseries, equipo y apertura (PyG/Inversion B31)
  necesidad: '$335,708', // CAPEX + working capital ($97,876)
  netoPct1: '7%', // neto A1 ($57,946), redondeado
  netoPct3: '10%', // neto A3 ($90,465), redondeado
  equilibrio: '110', // covers/dia (contable)
  cogsPct: '28%', // COGS 28.0 %
  personalPct: '33%', // personal 33.1 %
  fte: '6.6', // 6.60 FTE, 10 puestos
  obra: '$53,000', // inv_obra
  campana: '$26,000', // inv_campana (Type I + supresion + makeup air)
  pesimista: '$27,945', // perdida del escenario pesimista A1
  ave: '$5.99', // coste del pollo entero (calculadora, defecto)
  porCarga: '96', // pollos por carga (2 rotisseries × 8 spits × 6)
  domingo: '192', // capacidad antes de las 1:30 pm del domingo
  fcEntero: '31.5%', // food cost del pollo entero a $19.00
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `What should a rotisserie chicken restaurant business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a counter-service rotisserie chicken restaurant, plus the Excel financial projections that back them up, a calculator for the chicken, the rotisserie and the plate costing, and an 80-task startup checklist.`,
  },
  {
    q: `Is it a generic template or built for a rotisserie chicken restaurant?`,
    a: `Built for a neighborhood counter-service rotisserie chicken restaurant, Peruvian style (pollo a la brasa), in a mid-size US city: about 1,600 sq ft with 40 seats, ordering at the counter, take-out, marketplace delivery and whole-chicken pre-orders, two gas rotisseries with 8 spits each, a heated display, two fryers for yuca fries and fries, beer and wine only, open 7 days a week and an owner who is the general manager and head of the rotisserie. Nothing to strip out from a restaurant template. If your concept is different, the Excel workbook takes any numbers you type, but the written plan describes this shop (see the last questions about food trucks, franchises and full-service restaurants).`,
  },
  {
    q: `How much does it cost to open a rotisserie chicken restaurant?`,
    a: `It depends on the space, the hood and the build-out, which move the number more than anything else. The kit's example comes in at ${CASO.capex} in startup costs, and ${CASO.necesidad} in total cash once working capital is added. Line by line it covers architect and permit fees, a build-out (${CASO.obra} in the example, signage included), a Type I hood with fire suppression and makeup air (${CASO.campana}), electrical, plumbing, gas and grease, two gas rotisseries, the heated display, the fryers and range, a walk-in cooler for the marinade, a refrigerated line, dish and sink equipment, the sauce station and smallwares, furniture for 40 seats, POS and online ordering, LLC and legal, branding and launch, and opening inventory, plus a deposit, rent before opening and a contingency. Replace each line with your own quotes: they are example prices, not a price list. A charcoal rotisserie is a different budget (see the question about gas, electric and charcoal).`,
  },
  {
    q: `Is a rotisserie chicken restaurant profitable? How much do owners make?`,
    a: `It can be, but not at the 15-25% that some templates and articles promise. In the kit's example the shop sells ${CASO.ventas} in year 1 (${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days), with about ${CASO.cogsPct} of sales in cost of goods and about ${CASO.personalPct} in labor, and it leaves a modest net profit of about ${CASO.netoPct1} of sales in year 1, rising to about ${CASO.netoPct3} by year 3, with a break-even of about ${CASO.equilibrio} covers a day. The owner is already on payroll as general manager and head of the rotisserie, so any profit is on top of that salary. The pessimistic scenario (fewer covers, a lower check and fewer days) loses money in year 1 (${CASO.pesimista} in the example), and the plan says so. Whether you earn more depends on your sales, your check and what you pay yourself: replace the example with your own numbers before you decide.`,
  },
  {
    q: `What does a rotisserie chicken cost you?`,
    a: `It depends on what you pay per pound, the weight of the bird and what you lose to cooking and holding. With the calculator's starting values (kit estimates, editable: a 3.0 lb bird, without giblets, at $1.75 per lb delivered, plus a marinade and 5% of the bird cost for display waste) a whole bird costs about ${CASO.ave}, and a cooked yield of 72% leaves about 2.2 lb of cooked chicken. The Costing sheet prices nine items from your own ingredient prices and portions (whole, half and quarter chicken with two sides, a family meal, a chicken sandwich or bowl, salchipapas, yuca fries, maduros and a drink) and gives you the cost, the food cost percentage, the margin and the menu price you need. In the example the whole bird at $19.00 runs about ${CASO.fcEntero} food cost, and the family meal about 30%. Chicken prices move from week to week, so weigh your birds and replace the starting price with your supplier's.`,
  },
  {
    q: `Gas, electric or charcoal rotisserie: which one should I plan for?`,
    a: `The kit's example uses two gas rotisseries, because they go under a standard Type I hood with a gas service sized for them, and gas costs only a few cents per cooked bird in the calculator (a kit estimate, with a cell for the price per therm on your gas bill). Charcoal is the soul of pollo a la brasa, but it is a solid fuel operation: NFPA 96 asks for a separate exhaust, a spark arrester and ash removed daily, your fire marshal wants a listed appliance, your health department wants certified equipment, and the plan puts the extra cost at about $45,000 to $60,000 in startup costs (a kit estimate; listed charcoal rotisseries alone run $27,500 to $35,950). Rotisseries imported from Peru may not carry a US listing. The plan treats charcoal as a variant and the checklist tells you to ask your fire marshal in writing before you sign the lease. Air quality rules for solid fuel vary by district: ask your local air district.`,
  },
  {
    q: `Do I need a Type I hood and fire suppression?`,
    a: `Almost certainly, over the rotisseries and the fryers, and your fire marshal or building department makes the final call. The example budgets a Type I hood with a UL 300 fire suppression system and makeup air at ${CASO.campana}. A ventless unit is only an option with listed equipment that comes with its own hood, and the fryers still go under a Type I hood unless they are ventless too. That is also the filter for the space: if the building can't take a duct to the roof, the concept does not fit. The plan also budgets hood cleaning as a recurring cost line. The checklist tells you to ask your fire marshal in writing before you sign the lease.`,
  },
  {
    q: `Do the rotisseries have enough capacity for Sunday?`,
    a: `That is what the Rotisserie sheet of the calculator tells you. With the starting values (kit estimates, editable: two rotisseries with 8 spits each and 6 birds per spit, an 80-minute cook plus 15 minutes to unload and reload, the first load at 9:00 am) a load is ${CASO.porCarga} birds and two loads are done by 1:30 pm, so the example has ${CASO.domingo} birds ready for the Sunday lunch peak. It also gives you the latest time to put on the first load and the gas for the day, and a traffic light for a normal Sunday and for a holiday or peak day. No spec sheet publishes the cook time of a 3 lb bird, so measure it with your own rotisserie and type it in.`,
  },
  {
    q: `How long can rotisserie chickens stay hot? What will my health department ask?`,
    a: `The FDA Food Code is adopted state by state, so the checklist tells you to get your county's rules for cooking and hot holding chicken in writing. In the Food Code 2022, poultry is cooked to 165 °F and hot food is held at 135 °F or above. The plan's procedure keeps the heated display at 135 °F or above, with the time marked on every load and a 4-hour limit of your own: at 4 hours, or if a bird drops below 135 °F, it is cooled at once with a log for the next day's sandwich or bowl, or thrown away, and it never goes back on the display without being reheated to 165 °F. The alternative, time as a public health control (TPHC), lets a bird sit out of temperature control for up to 4 hours with the time marked and a written procedure, but at 4 hours it is sold or thrown away, never cooled or reheated. The calculator has a cell for the share of leftovers you reuse after correct cooling, and cooked rice and beans are time/temperature control foods too.`,
  },
  {
    q: `How much do DoorDash, Uber Eats and Grubhub charge a chicken restaurant?`,
    a: `Published tiers run from about 15% to 30% of the order for delivery, and from 6% to 10% for pickup orders. DoorDash lists Basic at 15%, Plus at 25% and Premier at 30%, with 6% for pickup; Uber Eats lists 20% (15% in selected cities) for Lite, 25% for Plus and 30% for Premium, with 7% or 10% for pickup; Grubhub lists marketing tiers of 5%, 15% and 20% plus 10% for delivery and a card processing fee (3.05% + $0.30). Tiers change, so check them before you sign. The example uses the 25% tier on 15% of sales and treats counter orders, pickup, pre-orders and direct phone or web orders as commission-free. The Costing sheet shows the margin of each item at the counter, on pickup and pre-orders, and on a marketplace with a menu markup you can edit.`,
  },
  {
    q: `Can I sell whole chickens for pickup and pre-orders?`,
    a: `Yes, and the plan is built around it: whole birds and family meals for birthdays, offices, churches and holidays, with a pickup time. The Word plan covers the pre-order cards, the Sunday and holiday peaks and the local outreach to take them, and the checklist has a phase for the menu, the brand and the pre-orders. Pickup at the counter pays no commission, and the Costing sheet shows its margin after packaging. Rules for selling to the public vary by state and county, so check yours with your health department.`,
  },
  {
    q: `Is Peruvian chicken gluten-free? What are the allergens?`,
    a: `The kit does not promise it. A typical pollo a la brasa marinade has soy sauce (soy and wheat) and beer (wheat and barley), and sauces such as aji verde or huancaina can bring egg or milk depending on the recipe, so the checklist has you label the counter against the 9 major US allergens, sesame being the ninth since 2023. The plan tells you not to promise "gluten-free": under the FDA rule (21 CFR 101.91) it means less than 20 ppm of gluten, and a marinade with soy sauce and beer plus a fryer shared with breaded foods make that impossible to guarantee, for the chicken and for the yuca fries. A certified food protection manager and food handler cards depend on your state and county.`,
  },
  {
    q: `Do I need a license to serve beer and wine?`,
    a: `Probably yes if you want to sell beer or wine, and it can take months, so the plan treats it as a lease contingency. Cost and timing vary a lot by state, so ask your state's alcohol board before you sign. The kit does not promise a license: the checklist walks you through the application, and the plan covers liquor liability insurance. It's a beer and wine shop in the example, not a full bar: for that, start from the Bar Business Plan Kit.`,
  },
  {
    q: `How does the Rotisserie Chicken Yield & Costing Calculator work?`,
    a: `Four sheets: Chicken Yield, Rotisserie, Costing and Instructions. The yield sheet works in pounds and ounces (16 oz per lb): you type the weight of the bird, the price per pound, the marinade and the holding waste, and it gives you the cooked yield, the cost per whole bird and per cooked pound, and the birds to order for a party. The rotisserie sheet gives you the birds per load, the capacity before your Sunday deadline and the gas per bird. The costing sheet prices nine items from the ingredient prices you type (the example's are kit estimates for October 2026: replace them with your distributor's) and shows the food cost, margin and menu price of each, plus the margin on pickup and pre-orders and on a delivery app.`,
  },
  {
    q: `Can I use this for a food truck?`,
    a: `Not as it stands. This plan is written for a rotisserie chicken restaurant with a fixed location, a dining room and a hood. A food truck has a different license (a mobile food unit), a commissary, a different layout and often no dining room, so the written plan would need heavy rewriting. For a mobile business, the Food Truck Business Plan Kit fits better. The Excel workbook takes any numbers you type, but the text describes a restaurant with a counter and a dining room.`,
  },
  {
    q: `Is this for a franchise or a fried chicken shop?`,
    a: `No. A franchise follows its franchisor's system and fee structure, which is a different kind of decision, and fried chicken, hot chicken and wings are another business with another kitchen. This kit is for the independent owner who writes the concept, picks the space and sets the menu of a rotisserie chicken restaurant. For a full-service restaurant with table service and a full bar, the Restaurant Business Plan Kit is the general plan, with the same lender-ready format.`,
  },
  {
    q: `Should I buy this or the Restaurant Checklists Kit Pro?`,
    a: `They do different jobs. This plan is for deciding, financing and opening the restaurant: the written plan, the numbers and an 80-task startup checklist. The Restaurant Checklists Kit Pro is the set of daily, weekly and monthly routines for running a restaurant once it is open: opening, closing, cleaning and food safety checks. Many owners use both: the plan before opening, the checklists after.`,
  },
  {
    q: `Can I present this plan to a lender or investors?`,
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds, and a loan schedule with the debt service coverage ratio (DSCR) you can check against your lender's target. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice: review the final numbers with your accountant before you apply for a loan.`,
  },
  {
    q: `Can I change the numbers in the Excel model?`,
    a: `Yes. The green cells are the ones you type: covers per day, average check, operating days, the split between food and beverage, cost of goods percentages, delivery share and commission, rent, wages and every startup cost line. The linked formulas recalculate the rest. To change a calculated cell, use Review, Unprotect Sheet (there is no password). The workbook, the calculator and the checklist each include an Instructions tab.`,
  },
  {
    q: `Does it work in the UK, Canada or Australia?`,
    a: `Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your menu prices without it. The plan and the checklist give US units with metric beside them (°F with °C, sq ft with sq m, lb with kg), and the calculator works in pounds and ounces only. The plan's UK note covers registering with your council at least 28 days before you open, the Food Hygiene Rating, 20% VAT on hot food including take-away, the 14 UK allergens and the premises and personal licences for alcohol. In Australia, where charcoal chicken is the big name, check your council's food premises registration and the Food Safety Supervisor rules, and in Canada your provincial rules, with your local authority. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.`,
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
  slug: 'rotisserie-chicken-restaurant-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_ROTISSERIE_CHICKEN_RESTAURANT_BUSINESS_PLAN',

  seo: {
    title: 'Rotisserie Chicken Restaurant Business Plan: Word + Excel Projections + Chicken Cost Calculator | AI Chef Pro',
    description:
      'Rotisserie chicken restaurant business plan for a Peruvian pollo a la brasa shop: Word plan, 3-year Excel projections, chicken cost calculator and permit checklist.',
    keywords:
      'rotisserie chicken restaurant business plan, chicken restaurant business plan, how to open a rotisserie chicken restaurant, peruvian chicken restaurant, pollo a la brasa, chicken shop business plan, rotisserie chicken restaurant startup costs, rotisserie chicken profit margin, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-polleria-hero.jpg',
  },

  schema: {
    productName: 'Rotisserie Chicken Restaurant Business Plan Kit',
    productDescription:
      'Rotisserie chicken restaurant business plan kit for a counter-service pollo a la brasa shop with two gas rotisseries: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a chicken yield, rotisserie and plate costing calculator, and an 80-task startup checklist in 6 phases covering the hood, the gas line and the permits. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Rotisserie Chicken Restaurant Business Plan Kit',
  },

  images: {
    // hero bg (6) — la polleria con las espadas del asador girando y el mostrador preparado (ES -hero) abre.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-polleria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-asador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-mostrador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-brasa.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-equipo.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden.
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-polleria-mostrador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-asador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-brasa.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-polleria-asador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-polleria-brasa.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-polleria-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready rotisserie chicken restaurant business plan: Word + Excel + chicken cost & rotisserie calculator',
    titlePre: 'Rotisserie Chicken Restaurant ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Peruvian Pollo a la Brasa or Charcoal Chicken Shop: Word Plan + Excel Projections + Chicken Cost & Rotisserie Calculator + Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch a counter-service rotisserie chicken restaurant with two gas rotisseries, a heated display, take-out, marketplace delivery and whole-chicken pre-orders: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in covers per day, 12-month cash flow and loan payments from your own numbers; a calculator that costs every bird, every plate and every load of the rotisserie; and an 80-task checklist that takes you from your LLC, your lease and the fire marshal to your first 90 days open. Set up for the US, with notes for the UK.`,
    checkItems: [
      '10-section rotisserie chicken restaurant business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in covers per day and 12-month cash flow',
      'Chicken cost & rotisserie calculator: cost per bird, food cost per plate, birds per load',
      'Startup checklist: 80 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Rotisserie Chicken Restaurant Business Plan Kit: 9 building blocks to test whether your chicken shop works on paper before you sign a lease or buy a rotisserie, cost every bird and every plate, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Rotisserie Chicken Restaurant Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a neighborhood counter-service rotisserie chicken restaurant: executive summary, concept and value proposition, market analysis (including the five styles of rotisserie chicken your guests have in mind), competitive analysis, marketing plan, operations plan (rotisseries, heated display, fryers, take-out, delivery and pre-orders), management and staffing, financial plan, legal requirements, permits and hood rules, and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Rotisserie Chicken Restaurant Financial Projections (Excel, 9 Sheets)', desc: `Is a rotisserie chicken restaurant profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. Linked formulas throughout: change covers per day, average check or operating days and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Rotisserie Chicken Yield & Costing Calculator (Excel: Chicken Yield + Rotisserie + Costing)', desc: `The cost of every bird, from your own prices. The yield sheet works in pounds and ounces: bird weight, price per pound, marinade and holding waste in, the cooked yield, the cost per whole bird and the birds to order for a party out. The rotisserie sheet gives you the birds per load, the capacity before your Sunday deadline and the gas per bird. The costing sheet prices nine items, from a whole chicken and a family meal to a sandwich, salchipapas and yuca fries, with the cost, the food cost percentage and the menu price you need, using ingredient prices you replace with your distributor's.` },
      { icon: 'Coins', title: 'Rotisserie Chicken Restaurant Startup Costs, Line by Line', desc: `How much does it cost to open a rotisserie chicken restaurant? Architect and permit fees, the build-out, electrical, plumbing, gas and grease, a Type I hood with fire suppression and makeup air, two gas rotisseries, a heated display, fryers and range, a walk-in cooler, the refrigerated line, dish and sink equipment, the sauce station and smallwares, furniture, POS and online ordering, LLC and legal, branding and launch, and opening inventory, each with a reference price you replace with your quotes, plus a deposit, rent before opening, a contingency and working capital.` },
      { icon: 'TrendingUp', title: 'Break-Even in Covers per Day + 3 Scenarios', desc: `How many covers a day you need at your average check (excl. sales tax) to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance: honest about what a slow first year does to your cash.` },
      { icon: 'Users', title: 'Staffing & Shift Labor', desc: `The owner as general manager and head of the rotisserie, and the crew for a shop that is open 7 days: counter, packing and expo, fry and line, and a prep and relief rotisserie cook who covers the days off, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need and flags any pay below the minimum wage.` },
      { icon: 'BarChart3', title: 'Dine-In, Take-Out, Delivery & Pre-Order Mix', desc: `Counter and dining room versus take-out, pickup and pre-orders, with the share of sales that goes through third-party delivery marketplaces and the commission you pay on it (the DoorDash and Uber Eats tiers are in the plan), plus hood cleaning, music licensing, and waste, grease and used-oil hauling as their own cost lines.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (80 Tasks, 6 Phases)', desc: `Business setup (LLC, EIN, state payroll accounts, business license and sales tax permit, your loan application), hood, gas and permits (zoning, building permit and certificate of occupancy, the fire marshal in writing on the hood and the rotisseries, a licensed gas contractor, the beer and wine license as a lease contingency), rotisserie and health (plan review and the health permit, the heated display with its 4-hour limit, cooling and the leftover), staff and allergens (offer letters, I-9, W-4, CFPM and food handler cards, the 9 allergens including sesame), menu, brand and pre-orders, and opening day plus your first 90 days.` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year, plus investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: a rotisserie chicken restaurant plan written for the format lenders expect, with a financial model, a chicken cost and rotisserie calculator and the hood and permit rules that recalculate from your own numbers.`,
    reasons: [
      { icon: 'Flame', title: 'Built for a Counter-Service Rotisserie Chicken Restaurant', desc: `Birds turning on the spits in view of the street, a heated display, yuca fries and rice and beans on the side, aji verde on the counter, a dining room of 40 seats, take-out, delivery and whole-chicken pre-orders; beer and wine; the owner as general manager and head of the rotisserie. How much does it cost to open a rotisserie chicken restaurant? The hood, the rotisseries and the build-out, line by line. Nothing to strip out from a restaurant or food truck template.` },
      { icon: 'Calculator', title: 'The Cost of Every Bird, Plate and Load', desc: `What a whole bird costs once you count the marinade and the birds that pass their holding window, what each plate and each family meal runs in food cost, and whether two rotisseries reach the Sunday peak, all from your own numbers. The calculator's starting values are kit estimates, editable, and the checklist reminds you to weigh your own birds.` },
      { icon: 'Map', title: 'Hood, Gas or Charcoal, and Permits: What the Fire Marshal Asks', desc: `Two rotisseries and the fryers need a Type I hood with fire suppression and a duct to the roof, and the building has to allow it. Charcoal is a solid fuel operation under NFPA 96 with its own exhaust, so the example plans for gas and treats charcoal as a variant. The plan explains plan review, the building permit, the certificate of occupancy and the health permit, and tells you to ask the fire marshal in writing. It does not promise a beer and wine license either: it treats it as a lease contingency.` },
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
    `CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening restaurants and chicken shops, combining hands-on operations with financial planning.`,
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  // UN solo bonus (la guia comun de equivalencias EN): los entregables propios (plan, proyecciones, checklist, calculadora) ya
  // estan en la rejilla y no se re-empaquetan como «bonus» (honestidad: solo lo que existe como fichero).
  bonus: {
    subtitle:
      `Besides the business plan, the financial model, the calculator and the startup checklist, you get this extra resource`,
    items: [
      {
        icon: 'Globe',
        label: 'BONUS',
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
    headingGold: 'Rotisserie Chicken Restaurant',
    subtitle:
      `Plan it before you sign the lease and buy the rotisseries: the written plan, the numbers behind it, the cost of every bird and the permits list, for a one-time payment.`,
    items: [
      '10-section rotisserie chicken restaurant business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in covers per day, with a sensitivity table',
      'Chicken cost & rotisserie calculator: cost per bird, food cost per plate, birds per load',
      'Startup checklist: 80 tasks in 6 phases',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'ROTISSERIE CHICKEN RESTAURANT BUSINESS PLAN — $39',

  // Salientes: Restaurant Checklists (rutinas del local abierto; no hay checklists de polleria EN), Food Cost (coste por plato),
  // HACCP (hot holding, TPHC, enfriado), Restaurant Business Plan (el hermano general), Food Truck (el pollo sobre ruedas),
  // Coffee Shop y Bar (hermanos de local fijo con campana), Restaurant Financial Plan + Staff Scheduling.
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
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'New product · Version 2.2 · October 2026',

  alreadyBought: {
    product: 'rotisserie-chicken-restaurant-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
