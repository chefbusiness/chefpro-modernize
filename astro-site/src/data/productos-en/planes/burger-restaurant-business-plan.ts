// astro-site/src/data/productos-en/planes/burger-restaurant-business-plan.ts
// TIENDA INTERNACIONAL EN — Burger Restaurant Business Plan Kit. DUPLICADO de la ficha gemela EN de la familia Planes
// (sushi-restaurant-business-plan.ts: mismo tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en",
// mismo orden de campos). Edicion inglesa del ES "Plan de Negocio: Hamburgueseria Smash" (hreflang reciproco, familia
// plan-negocio-hamburgueseria), cuyo contenido y cifras NO se reutilizan: el EN es un independent smash burger restaurant de
// EE. UU. (counter service, 44 plazas, take-out y marketplace, abre 7 dias, sin servers ni tip credit).
// SPEC: scripts/productos-digitales/plan-hamburgueseria/F1-camino.md §6 + scripts/productos-digitales/business-plans-en-15/.
//   Research: business-plans-en-15/F1-research-us-delta.md (§3 SERP/PAA, §6 legal US, §9 jerga y terminos de landing).
//   · Title/meta/H1 SIN anio fijo; NOMBRE DEL PRODUCTO primero; H1 Forma B `Burger Restaurant ` + oro `Business Plan` +
//     «Template for a Smash Burger Restaurant with Take-Out and Delivery: …» (research §9). Nunca «gourmet» como promesa,
//     ni «authentic», ni marcas de la competencia, ni cifras de franquicia como caso.
//   · NO decir (revision EN): que la smash «viaja bien» (viaja PEOR que en sala: la crust se ablanda), ninguna temperatura
//     de coccion distinta de 155 °F 17 s para toda smash, consumer advisory siempre obligatorio (solo si el dueno ofrece
//     cooked to order, tambien en los listados de marketplace), grinding logs como obligatorios, limite federal del aceite
//     (TPM) ni de acrilamida (Prop 65 solo en California), «gluten-free», ley espanola, € ni «comensal».
//   · $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating, review ni testimonios.
//   · Ficheros de dl/burger-restaurant-business-plan/ (plan, proyecciones, checklist de 80 tareas y calculadora de la carne,
//     las fries y el escandallo) + la guia comun de equivalencias EN. SOLO se afirma lo que existe en los entregables
//     (F2-NOTAS §3/§7, cifras_caso.json, cifras_calculadora.md).
//   · Cifras MEDIDAS (cifras_caso.json; caso US: 195 covers × $16.50 × 360 dias): ventas A1 $1,158,300, CAPEX $257,450,
//     necesidad total de caja $382,704 (prestamo $253,000 + $130,000 propios), neto A1 7.6 % → 9.3 % → 10.3 %, equilibrio
//     160 covers/dia (contable) y 157 (caja), holgura 24 %, DSCR 3.37×, COGS 31.2 %, personal 31.5 % (12 puestos, 9.05 FTE),
//     prime cost 62.7 %. Calculadora (Beef & Patty · Fries & Oil · Costing · Instructions; cifras_calculadora.md): $5.41 /
//     $5.15 por lb util, picar en casa compensa solo bajo ≈ $0.26/lb util, 5.3 bolas de 3 oz por lb, 58.5 lb de carne al dia,
//     single $2.00 (24 %), double $3.21 (29 %), combo 25 %, triple 32.7 %, ponderado 25.7 % (el plan usa 34 %), fries
//     congeladas $0.46 por racion (frescas $0.35 antes de mano de obra), aceite ≈ $0.10 por racion, combo $12.07 en sala →
//     $11.52 take-out → $9.12 marketplace (todo «kit estimate, editable»).
//   · Imagenes: las 7 plan-hamburgueseria-*.jpg del ES (sin texto), mismos huecos que la landing ES. OG = hero del ES.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_BURGER_RESTAURANT_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en business-plans-en-15/cifras_caso.json (31-oct). Nada movible. ──────────────────────────
const CASO = {
  covers: '195', // B4 — covers per day (each take-out or delivery order counts as 1.6 covers)
  ticket: '$16.50', // B5 — average check (excl. sales tax)
  dias: '360', // B6 — operating days (7 days a week)
  ventas: '$1,158,300', // ventas A1 = 195 × $16.50 × 360
  capex: '$257,450', // Startup Costs B31
  necesidad: '$382,704', // CAPEX + working capital ($125,254)
  prestamo: '$253,000', // SBA 7(a)-style loan, 10 %, 10 years
  propios: '$130,000', // owner equity
  netoPct1: '7.6%', // neto A1 ($87,459)
  netoPct2: '9.3%', // neto A2
  netoPct3: '10.3%', // neto A3
  equilibrio: '160', // covers/dia (contable)
  equilibrioCaja: '157', // covers/dia (de caja)
  holgura: '24%', // holgura de caja
  dscr: '3.37×', // DSCR minimo
  cogsPct: '31.2%', // COGS 31.2 %
  personalPct: '31.5%', // personal 31.5 %
  primePct: '62.7%', // prime cost
  obra: '$67,500', // inv_obra (build-out)
  campana: '$12,000', // inv_campana (Type I hood + UL 300 fire suppression)
  conducto: '$8,000', // inv_conducto (duct and makeup air, en la obra)
  pesimista: '$23,372', // beneficio antes de impuestos del escenario pesimista (A1, +)
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `What should a burger restaurant business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for an independent smash burger restaurant, plus the Excel financial projections that back them up, a calculator for the beef, the fries and the cost of every burger, and an 80-task startup checklist.`,
  },
  {
    q: `Is it a generic template or built for a smash burger restaurant?`,
    a: `Built for an independent smash burger restaurant in a mid-sized US city: about 1,700 sq ft in a second-generation restaurant space, 44 seats, counter service (guests order at the register or a kiosk and the food comes out on a tray or at the expo, with no servers), two gas flat-tops, three fryers with filtration under a Type I hood, take-out and marketplace delivery, and shakes and soft drinks (beer is optional), open seven days a week for lunch and dinner. The owner is the general manager. Covers count each take-out or delivery order as 1.6 covers. Nothing to strip out from a restaurant template. If your concept is different, the Excel workbook takes any numbers you type, but the written plan describes this restaurant (see the questions about servers, franchises and trucks).`,
  },
  {
    q: `How much does it cost to open a burger restaurant?`,
    a: `It depends on the space, the hood and the build-out, which move the number more than anything else. The kit's example comes in at ${CASO.capex} in startup costs, and ${CASO.necesidad} in total cash once working capital is added. Line by line it covers architect, MEP and permit fees, a build-out of a second-generation restaurant space (${CASO.obra} in the example), electrical, HVAC, plumbing and a grease interceptor, a Type I hood with UL 300 fire suppression (${CASO.campana}) and the duct and makeup air (${CASO.conducto}), two gas flat-tops with smash presses and scrapers, three fryers with filtration, a bun toaster and a shake machine, a walk-in cooler, reach-in and undercounter refrigeration, the freezer and the ice machine, dish and sink equipment, smallwares from a digital scale to probe thermometers, furniture for 44, POS, a self-order kiosk, a kitchen display and online ordering, LLC and legal, signage and facade, branding and launch, opening inventory and pre-opening training, plus a deposit, two months of rent before opening and a contingency. Replace each line with your own quotes: they are example prices, not a price list. The $30,000 to $130,000 you may see quoted for an independent burger startup describes a pop-up or a very small format, not a restaurant with a hood.`,
  },
  {
    q: `Is $20,000 enough to open a burger restaurant?`,
    a: `Not for the restaurant in this plan. The kit's example needs ${CASO.necesidad} in cash at opening, ${CASO.propios} of it your own money and ${CASO.prestamo} a loan, and the startup costs alone, before any working capital, come to ${CASO.capex}. The Type I hood with its fire suppression (${CASO.campana} in the example) is more than half of $20,000 on its own, before the duct. The plan describes smaller formats, such as a pop-up, a ghost kitchen or a take-out shop, but it does not budget them: if that is your concept, type your own numbers into the Excel workbook.`,
  },
  {
    q: `Is a smash burger restaurant profitable? Do small restaurants make money?`,
    a: `It can be, with a modest margin. In the kit's example the restaurant sells ${CASO.ventas} in year 1 (${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days), with ${CASO.cogsPct} of sales in cost of goods and ${CASO.personalPct} in labor, and it leaves a net profit of ${CASO.netoPct1} of sales in year 1, ${CASO.netoPct2} in year 2 and ${CASO.netoPct3} in year 3, with a break-even of ${CASO.equilibrio} covers a day (${CASO.equilibrioCaja} on a cash basis, which leaves ${CASO.holgura} of headroom at ${CASO.covers}). The owner is on payroll as general manager at $4,500 a month, below what a manager would earn, so think of an owner's draw on top of that from net profit. The pessimistic scenario (180 covers a day at $15.50 for 355 days) still ends year 1 with a small profit (${CASO.pesimista}); the optimistic one reaches about $230,000. Beef is the risk the plan names: a rise in the price per pound moves the food cost of every burger, so the calculator makes you type your own price. Replace the example with your own numbers before you decide.`,
  },
  {
    q: `What is the 30/30/30 rule for restaurants, and how does a burger restaurant compare?`,
    a: `It is a rule of thumb you will read for restaurants: one common version gives about 30% of sales to cost of goods, 30% to labor and 30% to other operating costs, leaving about 10%. The kit does not start from a rule; it builds the numbers: in the example, cost of goods is ${CASO.cogsPct} of sales, labor ${CASO.personalPct} (counter service, no servers), prime cost ${CASO.primePct}, rent 4.7%, EBITDA 14.5% and net profit ${CASO.netoPct1} in year 1. On food the plan uses a 34% food cost, the real usage of the whole menu, against 25.7% in the calculator's weighted costing: the gap is the real shrink, waste, over-portioned balls, staff meals and comps that a recipe costing does not show.`,
  },
  {
    q: `What does a smash burger cost you? How many balls come out of a pound?`,
    a: `It depends on what you pay per pound, how much of it ends up on the flat-top and how many ounces go in each ball. With the calculator's starting values (kit estimates, editable), a usable pound of 80/20 beef bought already ground costs about $5.41, and about $5.15 if you buy whole chuck, before the labor of grinding it. Grinding in-house pays off only if the labor stays below about $0.26 per usable lb, so the calculator's default verdict is to buy the blend ground. A pound makes about 5.3 balls of 3 oz (about 5.2 once you count the end-of-day shrink), and the example restaurant goes through about 58.5 lb of beef a day. The Costing sheet then puts a single at about $2.00 of food cost (24% of its price), a double at $3.21 (29%), a combo at about 25% and a triple at 32.7%, which it flags as "Watch the cost". Weigh every ball on a scale: ounces that are too heavy are food cost that never shows up in the costing.`,
  },
  {
    q: `How much do fries and frying oil cost per serving?`,
    a: `The Fries & Oil sheet takes the pounds of fries per serving, the price per pound, the price of oil and how many days it lasts. With its starting values (kit estimates, editable), a 5 oz serving of frozen fries costs about $0.46 and fresh-cut fries about $0.35 before labor, plus about $0.10 of oil per serving, and the example fryers go through about 320 lb of oil a month. The default verdict is that frozen pays off once you count labor. There is no federal limit that tells you when to change fryer oil (the usual yardstick is total polar materials, which your oil supplier or fryer maker will give you a target for), so the sheet asks you to type your own oil life.`,
  },
  {
    q: `What temperature must a smash burger reach?`,
    a: `The plan has every burger cooked through: under the FDA Food Code 2022 (3-401.11, which each state adopts in its own edition), ground beef is cooked to 155 °F (68 °C) for 17 seconds, and the kit's procedure applies that to every smash, checked with a probe thermometer and written on the cooking log. Because the beef is smashed thin on the flat-top and cooked all the way, there is nothing rare or medium on the menu. Ask your health department which Food Code edition your state follows.`,
  },
  {
    q: `Do I need a consumer advisory on my menu and delivery listings?`,
    a: `Only if you offer burgers cooked to order (medium or medium-rare, for instance). The plan's example cooks everything through, so it does not need one. If you decide to offer them, the Food Code's consumer advisory (3-603.11) is a disclosure on the menu, with a reminder, and it goes on your website and your marketplace listings too. The checklist has you settle this with your health department before you print a menu.`,
  },
  {
    q: `Do I have to keep grinding logs?`,
    a: `The kit does not tell you they are required. The plan buys beef already ground or already in balls from a supplier and keeps the supplier's invoices and lot information. If you grind your own, a simple log of the cuts, the lots and the times is a good practice, and the checklist lists it as optional. Ask your health department what it expects from a restaurant that grinds, since the answer can depend on your state and county.`,
  },
  {
    q: `Do I need a grease trap and a Type I hood for a burger restaurant?`,
    a: `Almost certainly: the flat-tops and the fryers go under a Type I hood with UL 300 fire suppression and makeup air (${CASO.campana} for the hood and ${CASO.conducto} for the duct and makeup air in the example), cleaned every quarter in the example because burgers are greasy (NFPA 96 sets the frequency by the type of cooking), with the fire marshal's sign-off, and a grease interceptor sized by your plumbing inspector. The exhaust duct to the roof also decides whether a space works: if the building will not allow it, the cooking line does not fit, which is why the checklist puts the zoning check and the hood and duct route before you sign the lease.`,
  },
  {
    q: `Is acrylamide in fries regulated?`,
    a: `There is no federal limit on acrylamide for restaurants, and the kit does not set one. California's Proposition 65 lists acrylamide and can apply to businesses in that state, so if you open there, ask a local advisor what, if anything, you have to post. The plan sticks to what you control: fry times and temperatures set by your fryer maker and your oil quality.`,
  },
  {
    q: `Which of the 9 major allergens are in a burger? Can I call it gluten-free?`,
    a: `The nine major US allergens are milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soy and sesame, the ninth since 2023 under the FASTER Act. A burger meal carries most of them: wheat, milk, egg, soy and often sesame in the bun, milk in cheese and shakes, egg in mayo-based sauces, wheat in the breading of a chicken sandwich, and cross-contact on shared flat-tops, utensils and fryers. Mustard is not a major allergen in the United States, though it is in the UK. The plan tells you not to promise "gluten-free": the buns contain wheat and the fryers are shared. The checklist has you build an allergen matrix by item before opening, and print it for the counter crew.`,
  },
  {
    q: `Can I run it without servers? What about tips?`,
    a: `Yes, that is the format. It is counter service: guests order at the register or a kiosk, and a counter crew takes the payment, calls the order and packs the to-go bags. In the example there are 12 people counting you, 9.05 full-time equivalents and about $365,000 a year in labor with employer payroll taxes, ${CASO.personalPct} of sales. Pay runs from $15.50 an hour for the counter crew to $17 for the grill cooks and $21 for the shift lead, and the example counts no tips and no tip credit, so every hour is paid at or above the federal and your state minimum, whichever is higher. A burger bar with servers is a variant, described in the written plan, but the Excel workbook is built for counter service.`,
  },
  {
    q: `How much do DoorDash, Uber Eats and Grubhub charge a burger restaurant?`,
    a: `Published plans run from about 15% to 30% of the order on DoorDash and on Uber Eats, and Grubhub has its own tiers; promotions and packaging come on top, and tiers change, so check them before you sign. The example sends 19% of sales through marketplaces at a 25% commission and keeps that share as a ceiling, with the marketplace menu about 15% higher for about the same basket. The Costing sheet shows the margin of every item dine-in, on take-out and on a marketplace: with its starting values, the same combo leaves $12.07 dine-in, $11.52 on take-out and $9.12 through a marketplace, about a quarter less. Delivery also hurts the product itself: a smash burger travels worse than it eats in the dining room, because the crust softens in the bag within minutes, so the plan has you test your packaging and vent it, and keep pickup at the restaurant, which pays no commission, in front of the customer.`,
  },
  {
    q: `Can I use the plan for a burger truck, a drive-thru or a franchise?`,
    a: `No. A food truck has a different license, a commissary and no dining room, while this plan is written for a fixed location with a hood: for a mobile business, the Food Truck Business Plan Kit fits better. A drive-thru is another site and another build-out. A franchise follows its franchisor's system and fees: the plan tells you to ask for the Franchise Disclosure Document, read Item 7 (the estimated initial investment) and Item 19 (financial performance figures, if it gives them), and compare both accounts before you sign. This kit is for the independent owner who builds a burger restaurant of their own. For a full-service restaurant with a full bar, the Restaurant Business Plan Kit is the general plan, with the same lender-ready format.`,
  },
  {
    q: `Should I buy this or the Burger Joint Checklists Kit Pro?`,
    a: `They do different jobs. This plan is for deciding, financing and opening the restaurant: the written plan, the numbers and an 80-task startup checklist. The Burger Joint Checklists Kit Pro is the set of daily, weekly and monthly routines for running a burger restaurant once it is open: opening and closing, the flat-top and fryer stations, cleaning and food safety checks. Many owners use both: the plan before opening, the checklists after.`,
  },
  {
    q: `How does the Smash Burger Patty, Fries & Costing Calculator work?`,
    a: `Four sheets: Beef & Patty, Fries & Oil, Costing and Instructions, in US units (lb, oz and °F). Beef & Patty takes the price per pound of your blend, the end-of-day shrink and the ounces per ball (2, 3 or 4 oz), and gives you the cost per usable lb, the balls per lb, the beef you need a day and the cost of a single, a double and a triple, and whether grinding in-house pays off with your labor. Fries & Oil gives you the cost per serving of frozen and fresh-cut fries and of the oil. Costing prices 14 products from the burger, fries, chicken sandwich, shake and drink prices you type (the defaults are kit estimates for October 2026: replace them with your distributor's prices and your own menu), and shows the food cost, the suggested menu price and the margin dine-in, on take-out and on a marketplace, plus the weighted food cost of the week against your target.`,
  },
  {
    q: `Can I present this plan to a lender or investors?`,
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds, and a loan schedule with the debt service coverage ratio (DSCR), ${CASO.dscr} at its lowest in the example, which you can check against your lender's target. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice: review the final numbers with your accountant before you apply for a loan.`,
  },
  {
    q: `Can I change the numbers in the Excel model?`,
    a: `Yes. The green cells are the ones you type: covers per day, average check, operating days, the split between food and beverage, cost of goods percentages, delivery share and commission, rent, wages and every startup cost line. The linked formulas recalculate the rest. To change a calculated cell, use Review, Unprotect Sheet (there is no password). The workbook, the calculator and the checklist each include an Instructions tab.`,
  },
  {
    q: `Does it work in the UK, Canada or Australia?`,
    a: `Yes, with notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so in the Excel model type your average check without it. The plan, the checklist and the calculator are in US units (lb, oz, °F and sq ft), and the plan has short notes for the UK and Australia. In Canada and Australia, check your provincial or state rules with your local authority. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.`,
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
  slug: 'burger-restaurant-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_BURGER_RESTAURANT_BUSINESS_PLAN',

  seo: {
    title: 'Burger Restaurant Business Plan: Word + Excel Projections + Patty Cost Calculator | AI Chef Pro',
    description:
      'Burger restaurant business plan for a smash burger shop: Word plan, 3-year Excel projections, cost-per-burger calculator and permit checklist.',
    keywords:
      'burger restaurant business plan, smash burger business plan, how to open a burger restaurant, burger restaurant startup costs, burger joint business plan, how much does it cost to open a burger restaurant, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-hamburgueseria-hero.jpg',
  },

  schema: {
    productName: 'Burger Restaurant Business Plan Kit',
    productDescription:
      'Burger restaurant business plan kit for an independent smash burger restaurant with counter service, take-out and delivery: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a smash burger patty, fries and costing calculator, and an 80-task startup checklist in 6 phases covering the hood, the beef and health rules and the permits. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Burger Restaurant Business Plan Kit',
  },

  images: {
    // hero bg (6) — mismos huecos que la landing ES plan-negocio-hamburgueseria.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-plancha.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-carne.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-patatas.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-equipo.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden (= ES).
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-plancha.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-carne.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-patatas.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-hamburgueseria-carne.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-hamburgueseria-plancha.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-hamburgueseria-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready burger restaurant business plan: Word + Excel + patty, fries & costing calculator',
    titlePre: 'Burger Restaurant ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Smash Burger Restaurant with Take-Out and Delivery: Word Plan + Excel Projections + Patty & Fries Costing Calculator + Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch an independent smash burger restaurant with counter service, take-out and marketplace delivery: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in covers per day, 12-month cash flow and loan payments from your own numbers; a calculator that costs the beef by usable pound, every ball, the fries and the oil, and 14 products you can rename; and an 80-task checklist that takes you from your LLC, your lease and the hood to the beef and health rules and your first 90 days open. Set up for the US, with notes for the UK.`,
    checkItems: [
      '10-section burger restaurant business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in covers per day and 12-month cash flow',
      'Patty, fries & costing calculator: cost per usable lb, balls per lb, food cost per burger',
      'Startup checklist: 80 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Burger Restaurant Business Plan Kit: 9 building blocks to test whether your smash burger restaurant works on paper before you sign a lease or order a flat-top, cost every burger and combo, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Burger Restaurant Business Plan (Word, 10 Sections)', desc: `A complete plan already written for an independent smash burger restaurant with counter service: executive summary, concept and value proposition (including the other burger models, from a bar with servers to a ghost kitchen, and why this plan takes counter service), market analysis, competitive analysis, marketing plan, operations plan (the ball, the flat-top, the fryers, equipment, food safety and the daily schedule), management and staffing, financial plan, legal requirements, permits and beef rules, and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Burger Restaurant Financial Projections (Excel, 9 Sheets)', desc: `Is a smash burger restaurant profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. Linked formulas throughout: change covers per day, average check or operating days and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Smash Burger Patty, Fries & Costing Calculator (Excel: Beef & Patty + Fries & Oil + Costing)', desc: `The cost of every ball, from your own prices. The beef sheet takes your price per pound, the end-of-day shrink and the ounces per ball, and gives you the cost per usable lb, the balls per lb, the pounds of beef a day and the cost of a single, a double and a triple, and whether grinding in-house pays off with your labor. The fries sheet costs a serving of frozen or fresh-cut fries and the oil. The costing sheet prices 14 products with the food cost, the suggested menu price and the margin dine-in, on take-out and on a marketplace.` },
      { icon: 'Coins', title: 'Burger Restaurant Startup Costs, Line by Line', desc: `How much does it cost to open a burger restaurant? Architect, MEP drawings and permit fees, the build-out of a second-generation restaurant space, electrical, HVAC, plumbing and the grease interceptor, a Type I hood with fire suppression and makeup air, two gas flat-tops with smash presses and scrapers, three fryers with filtration, the bun toaster and shake machine, a walk-in cooler, reach-in and undercounter refrigeration, dish and sink equipment, smallwares from a digital scale to probe thermometers, furniture for 44, POS, kiosk and online ordering, LLC and legal, signage and facade, branding and launch, and opening inventory, each with a reference price you replace with your quotes, plus a deposit, rent before opening, a contingency and working capital.` },
      { icon: 'TrendingUp', title: 'Break-Even in Covers per Day + 3 Scenarios', desc: `How many covers a day you need at your average check (excl. sales tax) to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance: honest about what a slow first year does to your cash.` },
      { icon: 'Users', title: 'Staffing & Shift Labor', desc: `The owner as general manager, a shift lead, grill cooks for the smash station, a fry and prep cook, the counter crew (register, expo and to-go packing), dish and prep, and part-time weekend crew, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need, including the production shift before opening, and takes the higher of the federal and your state or local minimum wage as the pay floor. Counter service: no servers and no tip credit in the example.` },
      { icon: 'BarChart3', title: 'Sales Mix, Delivery Share & Cost Lines', desc: `Food against beverage (burgers, chicken and fries against shakes, soft drinks and optional beer), the share of sales that goes through third-party delivery marketplaces and the commission you pay on it (the published DoorDash and Uber Eats ranges are in the plan), disposables as their own line, plus maintenance with the quarterly hood cleaning, and music licensing and waste, grease and used-oil hauling as their own cost lines.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (80 Tasks, 6 Phases)', desc: `Business setup (zoning check, LLC, EIN, business license and sales tax permit, two SBA 7(a) lenders), hood and permits (a second-generation space, the hood and duct route, plan review, building permit and certificate of occupancy), beef and health (cooking every burger to 155 °F for 17 seconds, the consumer advisory if you ever cook to order, the supplier paperwork for the beef, cold holding, the fryer and flat-top routines), staff and allergens (CFPM and food handler cards, the 9 major allergens, training the counter crew), menu, brand and delivery (the cost per burger and per combo by channel, marketplace contracts with a share cap), and opening day plus your first 90 days.` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year, plus investors or partners, local grants and an SBA Microloan as other sources of funds, and a red flag if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: a burger restaurant plan written for the format lenders expect, with a financial model, a patty, fries and costing calculator and the beef rules that recalculate from your own numbers.`,
    reasons: [
      { icon: 'Flame', title: 'Built for an Independent Smash Burger Restaurant', desc: `Counter service for 44, two gas flat-tops and three fryers under a Type I hood, take-out, marketplace delivery, shakes and soft drinks, open seven days. How much does it cost to open a burger restaurant? The hood, the flat-tops, the walk-in and the build-out, line by line. Nothing to strip out from a restaurant template.` },
      { icon: 'Calculator', title: 'The Cost of Every Ball, Burger and Combo', desc: `What a usable pound of beef really costs, how many 3 oz balls it makes, what a single, a double and a triple run in food cost, and what the same combo leaves dine-in and through a marketplace, all from your own numbers. The calculator's starting values are kit estimates, editable, and the checklist reminds you to weigh your own balls on a scale.` },
      { icon: 'Map', title: 'Beef and Fryer Rules, in Plain English', desc: `Every burger cooked to 155 °F for 17 seconds under Food Code 3-401.11, the consumer advisory only if you ever cook to order, the 9 major allergens, the hood, the grease interceptor and the quarterly cleaning. The kit does not promise "gluten-free", and it does not say a grinding log is required: it tells you what to ask your health department in writing.` },
      { icon: 'BarChart3', title: 'Honest Numbers, Real Margins', desc: `The example: ${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days, ${CASO.ventas} in year-1 sales, a net of ${CASO.netoPct1} in year 1 rising to ${CASO.netoPct3} by year 3, and ${CASO.equilibrio} covers a day to break even, with the owner on payroll and delivery marketplaces at a 25% commission. Beef is the risk the plan names, and the calculator makes you type your own price. Replace the numbers with yours.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    `CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening restaurants, combining hands-on operations with financial planning.`,
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
    headingGold: 'Burger Restaurant',
    subtitle:
      `Plan it before you sign the lease and order the flat-top: the written plan, the numbers behind it, the cost of every ball and the permits and beef rules list, for a one-time payment.`,
    items: [
      '10-section burger restaurant business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in covers per day, with a sensitivity table',
      'Patty, fries & costing calculator: cost per usable lb, balls per lb, food cost per burger',
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

  stickyLabel: 'BURGER RESTAURANT BUSINESS PLAN — $39',

  // Salientes: Burger Joint Checklists (rutinas del local abierto; hermano de tareas EN), Restaurant Checklists, Food Cost
  // (coste por burger), HACCP, Restaurant Business Plan (el hermano general), Sushi, Taco Shop, Rotisserie y Pizza Shop
  // (hermanos de local fijo con campana), Bar, Food Truck (FAQ), Financial Plan + Staff Scheduling y la guia de Food Cost.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/sushi-restaurant-business-plan', label: 'Sushi Restaurant Business Plan Kit' },
    { href: '/en/digital-products/taco-shop-business-plan', label: 'Taco Shop Business Plan Kit' },
    { href: '/en/digital-products/rotisserie-chicken-restaurant-business-plan', label: 'Rotisserie Chicken Restaurant Business Plan Kit' },
    { href: '/en/digital-products/pizza-shop-business-plan', label: 'Pizza Shop Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'New product · Version 2.2 · October 2026',

  alreadyBought: {
    product: 'burger-restaurant-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
