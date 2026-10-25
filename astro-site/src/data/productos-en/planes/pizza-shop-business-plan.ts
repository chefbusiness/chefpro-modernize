// astro-site/src/data/productos-en/planes/pizza-shop-business-plan.ts
// TIENDA INTERNACIONAL EN — Pizza Shop Business Plan Kit. DUPLICADO de bar-business-plan.ts con el patron vigente de
// paella-catering-business-plan.ts (mismo tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en",
// mismo orden de campos). Edicion inglesa del ES "Plan de Negocio: Pizzeria Napolitana" (hreflang reciproco, familia
// plan-negocio-pizzeria), cuyo contenido y cifras NO se reutilizan: el EN es otro concepto (SPEC D136).
// SPEC: scripts/productos-digitales/business-plans-en-8/SPEC-delta.md (D133-D155) + las heredadas business-plans-en-7 …
//   business-plans-en/SPEC.md. Research: F1-research-us-delta.md (§3 FAQ, §6.9 «Neapolitan-style» vs VPN, §9 jerga, §10).
//   · D133b: title con el NOMBRE DEL PRODUCTO primero («Pizza Shop Business Plan Template: Word + Excel Financial
//     Projections + Dough & Food Cost Calculator | AI Chef Pro»); H1 Forma B `Pizza Shop ` + oro `Business Plan` +
//     «Template to Open a Neapolitan-Style Pizzeria: …»; meta y keywords de research §9. «pizza shop» en nombre/H1,
//     «pizzeria» en la prosa; «Neapolitan-style» (nunca «authentic», «verace» ni «VPN-certified» como promesa).
//   · D134: $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating ni review.
//   · D135: ficheros de dl/pizza-shop-business-plan/ (plan, proyecciones, checklist de 80 tareas y calculadora de masa y
//     coste) + la guia comun de equivalencias EN. Los 6 H2 de research §9 no caben como H2 (constantes de UI_PLAN): sus
//     keywords van en los H3 de «why», las tarjetas del grid y la FAQ.
//   · D151: SIN testimonios (el ES no los tiene). FAQ = las 8 de research §3 + canibalizacion (Pizza Shop Checklists,
//     Restaurant Plan, Food Truck) + UK/CA/AU.
//   · Cifras MEDIDAS (F2-NOTAS §3, caso US calibrado el 25-oct: 62 covers × $36.00 × 300 dias): ventas A1 $669,600,
//     CAPEX $242,550, neto A1 5.9 % → 9.0 % en A3, equilibrio 55 covers/dia. Nada movible: ni DSCR, ni prestamo, ni saldos.
//     Calculadora (D145): Margherita ≈ 16 % de food cost y ≈ $0.40 por bola «in the example, editable».
//   · Honestidad (research §10): el neto realista de una pizzeria de barrio frente al "10-20 % / 15-25 %" que vende la SERP
//     (PMQ Pizza Power Report 2026: 2-3 %). No se promete licencia de alcohol, venta desde casa, «gluten-free»,
//     «VPN-certified» ni «15-25 %».
//   · Imagenes: las plan-pizzeria-*.jpg del ES (sin texto en espanol). OG = https://aichef.pro/lovable-uploads/ai-gallery/
//     plan-pizzeria-hero.jpg (D151/encargo; el recorte og-pizza-shop-business-plan.jpg queda como opcion del orquestador).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en F2-NOTAS §3 (25-oct) (business-plans-en-8/F2-NOTAS.md, cifras_caso.json) ─────────
// Libro final tras la vuelta unica de calibracion D15 (B5 $36). Nada movible (ni DSCR, ni prestamo, ni saldos).
const CASO = {
  covers: '62', // B4 — covers per day
  ticket: '$36', // B5 — average check (excl. sales tax and tip)
  dias: '300', // B6 — operating days
  ventas: '$669,600', // ventas A1 = 62 × $36.00 × 300
  capex: '$242,550', // 18 partidas $217,300 + deposit + 2 meses de renta previa + imprevistos $9,250
  partidas: '$217,300', // D139: las 18 partidas de inversion
  netoPct1: '5.9%', // neto A1 ($39,275)
  netoPct3: '9.0%', // neto A3 (a regimen)
  equilibrio: '55', // covers/dia (contable)
  cogsPct: '26%', // COGS 26.0 %
  personalPct: '33%', // personal 32.8 %
  personas: '8', // 8 personas = 4.72 FTE
  formulas: '700', // "more than N": el libro tiene 741 formulas
  pizzas: '8', // pizzas de la calculadora
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `What should a pizza shop business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a Neapolitan-style pizzeria, plus the Excel financial projections that back them up, a dough and food cost calculator, and an 80-task startup checklist.`,
  },
  {
    q: `Is it a generic template or built for a pizza shop?`,
    a: `Built for a neighborhood Neapolitan-style pizzeria in a mid-size US city: about 1,500 sq ft with 50 seats plus a seasonal patio, dine-in, take-out and delivery, a wood-fired dome oven (a gas or electric oven as a variant), beer and wine only, closed on Mondays and an owner who is the head pizzaiolo and the general manager. Nothing to strip out from a restaurant template. If your concept is different, the Excel workbook takes any numbers you type, but the written plan describes this shop (see the last questions about slice shops, franchises and food trucks).`,
  },
  {
    q: `How much does it cost to open a pizza shop?`,
    a: `Published estimates run from about $80,000 for a small shop to well over $400,000 for a brick-and-mortar pizzeria, and the oven, the hood and flue, and the build-out are what move the number. The kit's example comes in at ${CASO.capex} in startup costs, line by line: architect and permit fees, including a beer and wine license in a non-quota state ($14,000 for the group), a second-generation build-out and signage ($46,500), the flue, spark arrestor and insulated hearth pad ($12,000), a UL 2162-listed wood-fired dome oven ($22,000), a spiral mixer ($8,000), the walk-in, reach-ins and dough-ball cabinets, a Type I hood for the support line, furniture for 50 seats and the patio, POS and online ordering, opening inventory, plus a deposit, rent before opening and a contingency. Replace each line with your own quotes: they are example prices, not a price list.`,
  },
  {
    q: `How much do pizza shop owners make?`,
    a: `Less than the SERP suggests. In the kit's example the owner is on payroll as head pizzaiolo and general manager at $4,500 a month, below the BLS median for food service managers ($33.36 an hour in May 2025), and the shop also leaves a net profit of ${CASO.netoPct1} of sales in year 1 and ${CASO.netoPct3} by year 3. Whether the owner earns more depends on your sales, your oven schedule and what you pay yourself, which is why the plan separates the owner's salary from the net result. Replace the example with your own numbers before you decide.`,
  },
  {
    q: `Is a pizza shop profitable? What is a realistic profit margin?`,
    a: `It can be, but not at the 15-25% that many templates and articles promise. Industry reference points: food cost of 25-30% of sales, labor of 25-35% and a prime cost (food plus labor) at or below 60%. For the net margin the sources disagree: some blogs say 10-20% or even 15-25%, while the PMQ Pizza Power Report 2026 quotes an owner who calls 2-3% "lean and mean". The kit's example sits in between and says why: about ${CASO.cogsPct} cost of goods and ${CASO.personalPct} labor, ${CASO.ventas} of year-1 sales (${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days) and a net of ${CASO.netoPct1}, rising to ${CASO.netoPct3} by year 3, with a break-even of ${CASO.equilibrio} covers a day. The pessimistic scenario (fewer covers, a lower check and fewer days) loses money in year 1, and the plan says so. Build your first year on your own numbers, not on the example.`,
  },
  {
    q: `Wood-fired, gas or electric pizza oven: which one should I plan for?`,
    a: `The example plans a wood-fired dome oven, 47-51 inches across and UL 2162-listed, with the flue, spark arrestor and hearth pad budgeted separately; published prices for commercial Neapolitan ovens start around $12,950 and go past $25,000, and some makers publish none, and a gas or electric oven is a legitimate variant, cheaper to run and easier where wood burning is restricted. Wood-fired cooking falls under NFPA 96 chapter 14 for solid fuel (the chapter and the edition depend on your local authority), usually with a dedicated exhaust, a spark arrestor, ash removed daily and fuel stored away from the oven. Whether your listed oven needs a Type I hood or fixed suppression is decided by your fire marshal and your local code, so the checklist tells you to ask in writing: hood? suppression? UL 2162 file number? The plan does not promise that you won't need a hood. Only a wood-burning dome oven can qualify for the VPN certification (see the next question).`,
  },
  {
    q: `Can I call my pizza "Neapolitan"? Do I need VPN certification?`,
    a: `You can write "Neapolitan-style" on your menu: we found no US federal rule that restricts the term (in the European Union, "Pizza Napoletana" is a protected name, but that rule has no effect in the US). "VPN-certified" is different: the Verace Pizza Napoletana certification is a private, voluntary seal from the AVPN, and you can use it only if you hold the certificate. The AVPN's published fees for the US and Canada are $2,500 for the certification, $300 for the inspection and $400 a year to renew; it requires a shop that is already open, a wood-burning dome oven (gas only if wood is banned and documented), a bake at about 900 °F and specific flours and mixers. Saying "VPN-certified" without the certificate is misleading advertising. The kit's calculator checks your dough against the traditional Neapolitan ratios and tells you plainly that matching them does not make you VPN-certified. The plan has a section on what you can and can't put on your menu.`,
  },
  {
    q: `How much do DoorDash, Uber Eats and Grubhub charge a pizza shop?`,
    a: `Published tiers run from about 15% to 30% of the order for delivery, and from 6% to 10% for pickup orders. DoorDash lists Basic at 15%, Plus at 25% and Premier at 30%, with 6% for pickup; Uber Eats lists 20% (15% in selected cities) for Lite, 25% for Plus and 30% for Premium, with 7% or 10% for pickup; Grubhub lists marketing tiers of 5%, 15% and 20% plus 10% for delivery and card processing. Tiers change, so check them before you sign. The example uses the 25% tier on 12% of sales and 0% for pickup orders placed by phone or on your own website. Pizza travels badly, so it keeps delivery small and puts the effort into take-out.`,
  },
  {
    q: `Can I make pizza at home and sell it?`,
    a: `Usually not, and this plan assumes a permitted shop. Cottage food laws, which let you sell some low-risk foods made at home, differ by state while a cheese pizza is a time/temperature control for safety (TCS) food: mozzarella, cooked toppings and cut tomatoes all count under the FDA Food Code. We found no federal rule that lets you sell pizza from your home kitchen, so check with your state and county health departments before you spend.`,
  },
  {
    q: `What food safety and allergen rules apply to a pizza shop?`,
    a: `The kit follows the FDA Food Code, which each state adopts in its own edition: mozzarella, ham, sausage and cut tomatoes are TCS foods held at 41 °F or below, or at 135 °F or above. For a cold pizza table or dough balls kept out of the cooler, the checklist includes a written time as a public health control procedure (up to 4 hours, with the time marked) and the plan asks you to check with your regulator about dough, because the Food Code does not say. Wheat and milk are on every pizza, and the US has 9 major allergens, sesame being the ninth since 2023, so the plan covers peels, shared tables and flour in the air. It does not promise "gluten-free" pizza, because airborne wheat flour and shared peels make a gluten-free claim hard to stand behind without a written protocol and testing. A certified food protection manager and food handler cards depend on your state and county.`,
  },
  {
    q: `Do I need a license to serve beer and wine?`,
    a: `Almost certainly yes, and it can take months, so the plan treats it as a lease contingency. The example budgets $14,000 for architect and permit fees, with a beer and wine license in a non-quota state included; in states with a quota, a license costs far more, so ask your state's alcohol board before you sign. The kit does not promise a license: the checklist walks you through the application, and the plan covers liquor liability insurance. It's a beer and wine shop in the example, not a full-liquor bar: for that, start from the Bar Business Plan Kit.`,
  },
  {
    q: `How does the dough and food cost calculator work?`,
    a: `Two sheets, Dough and Food Cost. The dough sheet works in grams, with ounces and pounds echoed beside them: you type the number of balls, the ball weight, the waste and your recipe (per liter of water or in baker's percentages), and it gives you the flour, water, salt and yeast for the batch, your baker's percentages and the dough cost per ball. It compares your ratios with the traditional Neapolitan ratios (the EU specification the AVPN also uses; a reference, not a US rule) with a Within / Outside flag. The food cost sheet prices ${CASO.pizzas} pizzas, from Margherita and Marinara to Diavola, Bufalina and a sausage and broccoli rabe pizza, from the ingredient prices you type (the example's are kit estimates for October 2026: replace them with your distributor's). In the example, a Margherita comes out at about 16% food cost and about $0.40 per dough ball, in the example and editable.`,
  },
  {
    q: `Should I buy this or the Pizza Shop Checklists Kit Pro?`,
    a: `They do different jobs. This plan is for deciding, financing and opening the shop: the written plan, the numbers and an 80-task startup checklist. The Pizza Shop Checklists Kit Pro is the set of daily, weekly and monthly routines for running the shop once it is open: opening, closing, dough, oven and cleaning checks. Many owners use both: the plan before opening, the checklists after.`,
  },
  {
    q: `Is this the same as the Restaurant Business Plan Kit?`,
    a: `No. The Restaurant Business Plan Kit is written for a general full-service restaurant. This one is built for a pizzeria: the wood-fired oven and its flue, the dough and the pizzaiolo, take-out and delivery marketplaces, and a beer and wine license instead of a full bar. The financial engine is the same lender-ready format, driven by covers per day and average check.`,
  },
  {
    q: `Is this plan for a slice shop, a franchise, a pizza food truck or a ghost kitchen?`,
    a: `No. It is written for a sit-down Neapolitan-style pizzeria with take-out and delivery. A New York-style slice shop sells a different product with a different oven and a different check, a franchise follows its franchisor's system and a ghost kitchen has no dining room, so the written plan would need heavy rewriting. For a pizza food truck, the Food Truck Business Plan Kit fits better. The Excel workbook takes any numbers you type, but the text describes a pizzeria with a dining room.`,
  },
  {
    q: `Can I present this plan to a lender or investors?`,
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds, and a loan schedule with the debt service coverage ratio (DSCR), checked against a 1.25x lender target. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice: review the final numbers with your accountant before you apply for a loan.`,
  },
  {
    q: `Can I change the numbers in the Excel model?`,
    a: `Yes. The green cells are the ones you type: covers per day, average check, operating days, the split between food and beverage, ingredient costs, delivery share and commission, rent, wages and every startup cost line. More than ${CASO.formulas} linked formulas recalculate the rest. To change a calculated cell, use Review, Unprotect Sheet (there is no password). The workbook, the calculator and the checklist each include an Instructions tab.`,
  },
  {
    q: `Does it work in the UK, Canada or Australia?`,
    a: `Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your menu prices without it. The calculator works in grams and ounces, degrees Fahrenheit with Celsius, and square feet with square meters. The plan's UK notes cover registering with your council at least 28 days before trading, the food hygiene rating, 20% VAT on hot food, and the 14 UK allergens (which, unlike the 9 US ones, include molluscs, celery and mustard). In Canada and Australia, check your provincial or state food premises, fire and liquor rules with your local authority. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.`,
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
  slug: 'pizza-shop-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_BUSINESS_PLAN',

  seo: {
    title: 'Pizza Shop Business Plan Template: Word + Excel Financial Projections + Dough & Food Cost Calculator | AI Chef Pro',
    description:
      'Pizza shop business plan template for a Neapolitan-style pizzeria: Word plan, 3-year Excel projections, dough and food cost calculator, wood-fired oven and permit checklist.',
    keywords:
      'pizza shop business plan, pizzeria business plan, pizza shop business plan template, how to open a pizza shop, pizza shop startup costs, wood fired pizza oven cost, pizza shop profit margin, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg',
  },

  schema: {
    productName: 'Pizza Shop Business Plan Kit',
    productDescription:
      'Pizza shop business plan template kit for a Neapolitan-style pizzeria: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a dough and food cost calculator for 8 pizzas with Neapolitan dough ratios, and an 80-task startup checklist in 6 phases covering the wood-fired oven, hood and permits. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Pizza Shop Business Plan Kit',
  },

  images: {
    // hero bg (6) — el pizzaiolo sacando una Margherita del horno de lena, con la sala al fondo (ES -hero) abre.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-sala.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-equipo.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden.
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-sala.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-pizzeria-horno.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready pizza shop business plan: Word + Excel + dough & food cost calculator',
    titlePre: 'Pizza Shop ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template to Open a Neapolitan-Style Pizzeria: Word Plan + Excel Projections + Dough & Food Cost Calculator + Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch a Neapolitan-style pizzeria with a wood-fired oven, dine-in, take-out and delivery: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in covers per day, 12-month cash flow and loan payments from your own numbers; a dough and food cost calculator for ${CASO.pizzas} pizzas; and an 80-task checklist that takes you from your LLC, your lease and the fire marshal to your first 90 days open. Set up for the US, with notes for the UK.`,
    checkItems: [
      '10-section pizza shop business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in covers per day and 12-month cash flow',
      'Dough & food cost calculator: Neapolitan dough ratios and food cost per pizza',
      'Startup checklist: 80 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Pizza Shop Business Plan Kit: 9 building blocks to test whether your pizzeria works on paper before you sign a lease or order an oven, price every pizza from its dough and cost, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Pizza Shop Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a neighborhood Neapolitan-style pizzeria: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan (dough, oven, dine-in, take-out and delivery), management and staffing, financial plan, legal requirements, permits and oven rules, a section on Neapolitan-style versus VPN-certified (what you can and can't put on your menu), and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Pizza Shop Financial Projections (Excel, 9 Sheets)', desc: `Is a pizza shop profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than ${CASO.formulas} linked formulas: change covers per day, average check or operating days and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Pizza Dough & Food Cost Calculator (Neapolitan Dough + Food Cost for 8 Pizzas)', desc: `Pizza food cost from your own prices. The dough sheet works in grams (with ounces and pounds beside them): balls, ball weight, waste and your recipe in, flour, water, salt and yeast, baker's percentages and the dough cost per ball out, plus a Within / Outside check against the traditional Neapolitan ratios. The food cost sheet prices ${CASO.pizzas} pizzas, from Margherita and Marinara to Bufalina, with the cost per pizza, the food cost percentage and the menu price you need, using ingredient prices you replace with your distributor's.` },
      { icon: 'Coins', title: 'Pizza Shop Startup Costs, Line by Line', desc: `How much does it cost to open a pizza shop? Architect and permit fees (including a beer and wine license), a second-generation build-out, the flue, spark arrestor and hearth pad, a UL 2162-listed wood-fired dome oven, a spiral mixer, a prep table, walk-in and reach-ins, a Type I hood for the support line, dish and sink equipment, peels and smallwares, a beer and wine bar, furniture and patio, POS and online ordering, LLC and legal, branding and launch, and opening inventory, each with a reference price you replace with your quotes, plus a deposit, rent before opening, a contingency and working capital.` },
      { icon: 'TrendingUp', title: 'Break-Even in Covers per Day + 3 Scenarios', desc: `How many covers a day you need at your average check (excl. sales tax) to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance: honest about what a slow first year does to your cash.` },
      { icon: 'Users', title: 'Staffing & Shift Labor (7 Roles)', desc: `Owner / head pizzaiolo and GM, a pizzaiolo, a prep and dough cook, a front-of-house lead for the beer and wine bar, part-time servers, a weekend runner for the counter and pickup, and relief cover, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need and flags any pay below the minimum wage.` },
      { icon: 'BarChart3', title: 'Dine-In, Take-Out & Delivery Mix', desc: `Dine-in versus take-out and delivery, with the share of sales that goes through third-party delivery marketplaces and the commission you pay on it (DoorDash, Uber Eats and Grubhub tiers are in the benchmarks), plus firewood, music licensing and waste, grease and ash removal as their own cost lines.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (80 Tasks, 6 Phases)', desc: `Business setup (LLC, EIN, state payroll accounts, business license and sales tax permit, your loan application), site, hood and permits (zoning, plan review, building permit and certificate of occupancy, the fire marshal in writing on the oven, the flue and the hood, the beer and wine license as a lease contingency), kitchen, oven and health (grease interceptor, gas contractor, Class K and 2-A extinguishers, a written time as a public health control procedure), staff and safety (offer letters, I-9, W-4, CFPM and food handler cards, the 9 allergens including sesame), menu, brand and delivery (the marketplace tiers, W-2 drivers, local packaging rules, music licensing, a menu that says Neapolitan-style and not VPN-certified) and your first 90 days.` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25x target, plus investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: a pizza shop plan written for the format lenders expect, with a financial model, a dough and food cost calculator and the oven and permit rules that recalculate from your own numbers.`,
    reasons: [
      { icon: 'Flame', title: 'Built for a Neapolitan-Style Pizza Shop', desc: `A pizzaiolo who stretches dough to order and bakes it in 60 to 90 seconds at about 900 °F in a wood-fired dome oven; a dining room of 50 seats plus a patio, take-out and delivery; beer and wine; the owner as head pizzaiolo and GM. How much does it cost to open a pizza shop? The oven, the hood and flue and the build-out, line by line. Nothing to strip out from a restaurant or slice shop template.` },
      { icon: 'ShieldCheck', title: 'Wood-Fired Oven Rules: NFPA 96, Hood, Spark Arrestor and Fire Marshal', desc: `A wood-fired oven is a solid fuel cooking operation. The plan budgets a UL 2162-listed oven, a flue and a spark arrestor, explains what NFPA 96 chapter 14 usually asks for (a dedicated exhaust, ash out daily, fuel away from the oven) and tells you to ask the fire marshal in writing: hood? suppression? UL 2162 file number? It does not promise that you won't need a hood.` },
      { icon: 'Map', title: 'Neapolitan-Style vs VPN-Certified: What You Can Put on Your Menu', desc: `We found no US federal rule that restricts "Neapolitan-style" on a menu; "VPN-certified" is a private seal that you can use only with the AVPN certificate ($2,500 + $300 inspection + $400 a year, published fees). The plan has a section on what you can say, the calculator checks your dough against the traditional ratios, and neither promises a certification.` },
      { icon: 'BarChart3', title: 'Honest Numbers, Real Margins (Not the 15-25% Myth)', desc: `The example: ${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days, ${CASO.ventas} in year-1 sales, a net of ${CASO.netoPct1} in year 1 and ${CASO.netoPct3} by year 3, and ${CASO.equilibrio} covers a day to break even, with the owner on payroll and delivery marketplaces priced at their published tiers. Many articles promise 15-25%; one industry report quotes 2-3%. The pessimistic scenario loses money, and the plan says so. Replace the numbers with yours.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    `CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening restaurants and pizzerias, combining hands-on operations with financial planning.`,
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      `Besides the business plan, the financial model, the calculator and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves`,
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Pizza Shop Oven, Hood & Permits Guide (US + UK Notes)',
        desc: `Section 9 of the plan plus Phase 2 of the checklist: plan review before you build, the health permit and inspection, the building permit and certificate of occupancy, what NFPA 96 chapter 14 asks of a wood-fired oven, the questions to put to your fire marshal in writing, a beer and wine license as a lease contingency, CFPM and food handler cards, the 9 US allergens including sesame, a written time as a public health control procedure, liquor liability, W-2 delivery drivers and sales tax, plus a section on Neapolitan-style versus VPN-certified, with notes for the UK. No state forms included: requirements vary by state, county and city.`,
        image: '/lovable-uploads/ai-gallery/plan-pizzeria-horno.jpg',
      },
      {
        icon: 'BarChart3',
        title: 'US Pizza Shop Benchmarks (Sourced)',
        label: 'BONUS 2',
        desc: `The reference table inside the workbook: Margherita menu prices at Neapolitan-style pizzerias, Neapolitan dough ratios, bake time and temperature, the AVPN certification fees, DoorDash and Uber Eats tiers, sales tax, minimum wage, labor percentage, rent, firewood and prime cost, each with its source or marked "kit estimate" when there isn't one, plus five OK / REVIEW checks on your P&L against editable thresholds.`,
        image: '/lovable-uploads/ai-gallery/plan-pizzeria-plan.jpg',
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
    headingGold: 'Pizza Shop',
    subtitle:
      `Plan it before you sign the lease and order the oven: the written plan, the numbers behind it, the cost of every pizza and the permits list, for a one-time payment.`,
    items: [
      '10-section pizza shop business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in covers per day, with a sensitivity table',
      'Dough & food cost calculator: Neapolitan ratios and food cost per pizza',
      'Startup checklist: 80 tasks in 6 phases',
      'BONUS: Pizza Shop Oven, Hood & Permits Guide (included in the plan)',
      'BONUS: US Pizza Shop Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'PIZZA SHOP BUSINESS PLAN — $39',

  // Salientes: Pizza Shop Checklists (rutinas del local abierto), Food Cost (coste por pizza), HACCP (TCS, TPHC), Restaurant
  // Business Plan (el hermano general), Restaurant Financial Plan + Staff Scheduling + los otros planes EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'New product · Version 1.0 · October 2026',

  alreadyBought: {
    product: 'pizza-shop-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
