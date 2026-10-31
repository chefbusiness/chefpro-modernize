// astro-site/src/data/productos-en/planes/sushi-restaurant-business-plan.ts
// TIENDA INTERNACIONAL EN — Sushi Restaurant Business Plan Kit. DUPLICADO de la ficha gemela EN de la familia Planes
// (rotisserie-chicken-restaurant-business-plan.ts: mismo tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con
// lang="en", mismo orden de campos). Edicion inglesa del ES "Plan de Negocio: Sushi Bar" (hreflang reciproco, familia
// plan-negocio-sushi-bar), cuyo contenido y cifras NO se reutilizan: el EN es un neighborhood sushi restaurant de EE. UU.
// (sushi bar de 10 taburetes + 30 plazas en mesa, servers W-2 con propinas, take-out y marketplace, abre 6 dias).
// SPEC: scripts/productos-digitales/plan-sushi/F1-camino.md §6-§7 + scripts/productos-digitales/business-plans-en-14/.
//   Research: business-plans-en-14/F1-research-us-delta.md (§3 SERP/PAA, §6 legal US, §9 jerga y terminos de landing).
//   · Title/meta/H1 SIN anio fijo; NOMBRE DEL PRODUCTO primero; H1 Forma B `Sushi Restaurant ` + oro `Business Plan` +
//     «Template for a Sushi Bar with Take-Out and Delivery: …» (research §9). Nunca «sushi-grade» como garantia (sin
//     definicion legal en EE. UU.), ni «authentic», ni un pH «legal» del arroz (cada condado fija el suyo), ni la licencia
//     de beer & wine (contingencia del lease), ni marcas de franquicia.
//   · $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating, review ni testimonios.
//   · Ficheros de dl/sushi-restaurant-business-plan/ (plan, proyecciones, checklist de 80 tareas y calculadora del pescado,
//     el arroz y el escandallo) + la guia comun de equivalencias EN. SOLO se afirma lo que existe en los entregables
//     (F2-NOTAS §3/§7, cifras_caso.json, cifras_calculadora.md; contraste F3 en business-plans-en-14/F3-NOTAS.md).
//   · Cifras MEDIDAS (cifras_caso.json; caso US: 115 covers × $32.50 × 310 dias): ventas A1 $1,158,625, CAPEX $255,100,
//     necesidad total de caja $385,156, neto A1 8.5 % → ≈ 11 % en A3, equilibrio 93 covers/dia, COGS 30.8 %, personal 33.2 %
//     (10 puestos, 8.60 FTE), prime cost 64.0 %. Nada movible: ni DSCR, ni prestamo, ni payback, ni saldos.
//     Calculadora (Fish Yield · Sushi Rice · Costing · Instructions; cifras_calculadora.md): $11.28 / $23.92 / $25.48 por lb
//     util, entero rentable mientras limpiar < ≈ $12.65/lb util, 2.41 lb de shari por lb de arroz, ≈ 51 nigiri por lb,
//     food cost ≈ 23 % nigiri de salmon, ≈ 12 % California, ≈ 39 % spicy tuna, ≈ 25 % platter de 24, ≈ 24 % ponderado;
//     platter de 24: $31.60 en sala / $24.83 por marketplace (todo «kit estimate, editable»).
//   · REVISION-FINAL de la F2: M1 (marketplace ≈ el mismo pedido con la carta un 15 % mas cara, no «un pedido mayor») y M2
//     (el atun esta exento SIN papel; la declaracion escrita es para el pescado de acuicultura) repetidos aqui.
//   · Imagenes: las 7 plan-sushi-bar-*.jpg del ES (sin texto), mismos huecos que la landing ES. OG = hero del ES.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_SUSHI_RESTAURANT_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en business-plans-en-14/cifras_caso.json (31-oct). Nada movible (ni DSCR, ni prestamo, ni
// saldos, ni payback). ───────────────────────────────────────────────────────────────────────────────────────────────────
const CASO = {
  covers: '115', // B4 — covers per day (sushi bar, tables, take-out and delivery; 1 order = 1.6 covers)
  ticket: '$32.50', // B5 — average check (excl. sales tax and tips)
  dias: '310', // B6 — operating days (Tuesday to Sunday)
  ventas: '$1,158,625', // ventas A1 = 115 × $32.50 × 310
  capex: '$255,100', // Startup Costs B31
  necesidad: '$385,156', // CAPEX + working capital ($130,056)
  netoPct1: '8.5%', // neto A1 ($98,649)
  netoPct3: '11%', // neto A3 ($145,689 / $1,277,268 = 11.4 %), redondeado
  equilibrio: '93', // covers/dia (contable)
  cogsPct: '30.8%', // COGS 30.8 %
  personalPct: '33.2%', // personal 33.2 %
  obra: '$75,000', // inv_obra (build-out con la barra de sushi, rotulo y fachada)
  campana: '$18,000', // inv_campana (Type I + UL 300 + makeup air)
  congelador: '$3,500', // inv_congelador (−4 °F con registrador)
  pesimista: '$29,140', // perdida antes de impuestos del escenario pesimista A1
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `What should a sushi restaurant business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a neighborhood sushi restaurant, plus the Excel financial projections that back them up, a calculator for the fish, the sushi rice and the cost of every piece, and an 80-task startup checklist.`,
  },
  {
    q: `Is it a generic template or built for a sushi restaurant?`,
    a: `Built for a neighborhood sushi restaurant in a mid-sized US city: about 1,800 sq ft in a second-generation restaurant space, a sushi bar in view with 10 stools and a refrigerated sushi case, 30 seats at tables, W-2 servers with tips on top of pay, take-out and marketplace delivery, a small hot kitchen for tempura, gyoza and miso, beer, sake and wine only, open Tuesday through Sunday for lunch and dinner, and an owner who is the general manager, with a head sushi chef hired to run the bar. Covers count each take-out or delivery order as 1.6 covers. Nothing to strip out from a restaurant template. If your concept is different, the Excel workbook takes any numbers you type, but the written plan describes this restaurant (see the questions about omakase, poke and franchises).`,
  },
  {
    q: `How much does it cost to open a sushi restaurant?`,
    a: `It depends on the space, the hood and the build-out, which move the number more than anything else. The kit's example comes in at ${CASO.capex} in startup costs, and ${CASO.necesidad} in total cash once working capital is added. Line by line it covers architect, MEP and hood drawings and permit fees, a build-out with the sushi bar counter, signage and facade (${CASO.obra} in the example), electrical, plumbing, grease interceptor, HVAC and gas lines, a Type I hood with UL 300 fire suppression and makeup air (${CASO.campana}), a 6 ft refrigerated sushi case, two gas rice cookers and rice warmers, a −4 °F freezer with a temperature logger (${CASO.congelador}), the fryer, range and griddle, a walk-in cooler, reach-in fish refrigerators and a sake cooler, dish and sink equipment, smallwares from Japanese knives to a calibrated pH meter, furniture and sushi bar seating for 40, POS and online ordering, LLC, legal and the food safety plan, branding and launch, and opening inventory, plus a deposit, two months of rent before opening and a contingency. Replace each line with your own quotes: they are example prices, not a price list.`,
  },
  {
    q: `Is $20,000 enough to open a sushi restaurant?`,
    a: `Not for the restaurant in this plan. The kit's example needs ${CASO.necesidad} in cash at opening, $130,000 of it your own money and the rest an SBA 7(a) loan, and the startup costs alone, before any working capital, come to ${CASO.capex}. The Type I hood (${CASO.campana} in the example) is most of $20,000 on its own. The plan describes smaller formats, such as a take-out and delivery shop with few seats or none (the checklist puts it at 450 to 650 sq ft), but it does not budget them: if that is your concept, type your own numbers into the Excel workbook.`,
  },
  {
    q: `Is a sushi restaurant profitable? How much do owners make?`,
    a: `It can be, with a modest margin. In the kit's example the restaurant sells ${CASO.ventas} in year 1 (${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days), with ${CASO.cogsPct} of sales in cost of goods and ${CASO.personalPct} in labor, and it leaves a net profit of ${CASO.netoPct1} of sales in year 1, rising to about ${CASO.netoPct3} by year 3, with a break-even of ${CASO.equilibrio} covers a day. The owner is on payroll as general manager at $4,500 a month, below what a manager would earn, so think of an owner's draw on top of that from net profit; the head sushi chef is a hire. The pessimistic scenario (fewer covers, a lower check and fewer days) ends year 1 with a pre-tax loss (${CASO.pesimista} in the example), and the plan says so. Replace the example with your own numbers before you decide.`,
  },
  {
    q: `What is the 30/30/30 rule, and how does a sushi restaurant compare?`,
    a: `It is a rule of thumb you will read for restaurants: one common version gives about 30% of sales to cost of goods, 30% to labor and 30% to other operating costs, leaving about 10%. The kit does not start from a rule, it builds the numbers: in the example, cost of goods is ${CASO.cogsPct} of sales, labor ${CASO.personalPct} (servers on payroll, tips on top), prime cost 64.0%, rent 4.7%, EBITDA 15.8% and net profit ${CASO.netoPct1} in year 1. On food the plan uses a 32% food cost, the real usage of the whole menu, against about 24% in the calculator's theoretical costing: the gap is case shrink, trim you do not reuse, rice thrown out, staff meals and comps.`,
  },
  {
    q: `What does a piece of sushi cost you? Should I buy whole salmon or fillets?`,
    a: `It depends on what you pay per pound, how much of the fish you can use and how much fish and rice goes on each piece. With the calculator's starting values (kit estimates, editable), a usable pound costs about $11.28 from a whole farmed salmon, $23.92 from a salmon fillet bought clean and $25.48 from a yellowfin tuna saku block, and breaking down the whole salmon pays off only while your cleaning cost stays below about $12.65 per usable lb (the default assumes 25 minutes per fish: time your own). A pound of raw rice makes about 2.41 lb of sushi rice, or about 51 nigiri. The Costing sheet then puts the food cost at about 23% for a salmon nigiri, 12% for a California roll, 39% for a spicy tuna roll (the piece to watch) and 25% for a 24-piece party platter, and about 24% for the weighted menu. Consulting blogs put sushi food cost at 30% to 40%. Weigh ten slices and ten rice balls from each person at the bar: fish and rice that weigh too much are food cost that never shows up in the costing.`,
  },
  {
    q: `Do I have to freeze fish for sushi? What does the FDA Food Code ask?`,
    a: `Usually, yes. Under the FDA Food Code 2022 (3-402.11; each state adopts its own edition), fish served raw or undercooked is frozen first: at −4 °F (−20 °C) or below for 7 days, or at −31 °F until solid and held 15 hours, or at −31 °F until solid and then held at −4 °F or below for 24 hours. Tuna of the Thunnus species is exempt, and so is farmed fish fed pellet feed, such as salmon, with a written statement from the supplier or the farm; bivalves and roe removed from the skein and rinsed are exempt too. Freezing records are kept 90 days (3-402.12). The kit's procedure is to buy fish already treated or exempt, with the paperwork on file (it also keeps the tuna invoice that names the species), and to hold that stock in a −4 °F freezer with a temperature logger. Tuna, yellowtail and mackerel also carry histamine: receive them at 40 °F or below or send them back. And the consumer advisory for raw fish (3-603.11), a disclosure on every raw dish plus a reminder, goes on the menu, the website and your marketplace listings.`,
  },
  {
    q: `Is there such a thing as "sushi-grade" fish?`,
    a: `Not legally. "Sushi-grade" and "sashimi-grade" have no legal definition in the United States, so the kit does not promise it and the plan tells you not to put it on your menu. What exists are the parasite destruction rules of the Food Code: on the menu and the website, the plan suggests "fish handled for raw service (frozen per Food Code 3-402.11 or exempt, with records)".`,
  },
  {
    q: `Can sushi rice sit at room temperature? TPHC or a variance?`,
    a: `Cooked sushi rice is a time/temperature control for safety (TCS) food, and the Food Code gives you two routes. The default in the kit is time as a public health control (TPHC, 3-501.19): up to 4 hours out of temperature control, with the time stamped on every batch and a written procedure available to the inspector, and at 4 hours the rice is discarded, not chilled or reheated. The other route is a variance with a HACCP plan for acidified rice (3-502.11(C)): the annex of the Code gives a pH below 4.2 as an example critical limit, but each county sets its own, with a calibrated pH meter and a log for every batch. The kit sets no legal pH: the checklist has you settle TPHC or a variance with your health department, in writing, before you open.`,
  },
  {
    q: `Do I need a Type I hood for a sushi restaurant?`,
    a: `For the hot kitchen, almost certainly: the tempura fryer, the range and the griddle go under a Type I hood with UL 300 fire suppression and makeup air (${CASO.campana} in the example), cleaned twice a year (NFPA 96), with the fire marshal's sign-off. Ask the mechanical inspector whether the gas rice cookers go under the hood too, and plan for a grease interceptor. The exhaust duct to the roof is also the filter for the space: if the building will not allow it, the hot kitchen does not fit, which is why the checklist puts the zoning check and the hood and duct route before you sign the lease.`,
  },
  {
    q: `How much do DoorDash, Uber Eats and Grubhub charge a sushi restaurant?`,
    a: `Published plans run from about 15% to 30% of the order on DoorDash and on Uber Eats, and Grubhub has its own tiers; promotions and packaging come on top, and tiers change, so check them before you sign. The example sends 15% of sales through marketplaces at a 25% commission and keeps that share as a ceiling, with the marketplace menu about 15% higher for about the same basket. The Costing sheet shows the margin of every item dine-in, on take-out and pickup, and on a marketplace: with its starting values, the same 24-piece party platter leaves $31.60 dine-in and $24.83 through a marketplace, about a fifth less. Rolls and cold platters travel well, but tempura and gyoza arrive soft, so the plan keeps them off the marketplace menu or puts them in vented containers. Pickup at the restaurant pays no commission.`,
  },
  {
    q: `What are the allergens in sushi? Can I call it gluten-free?`,
    a: `The nine major US allergens are fish, crustacean shellfish, milk, eggs, peanuts, tree nuts, wheat, soy and sesame, the ninth since 2023 under the FASTER Act, and sushi carries most of them: fish and shrimp or crab on the menu itself, soy and wheat in soy sauce (tamari only if the label says so), sesame in seeds and oil, egg in spicy mayo, tamago and tempura batter, milk in cream cheese, and wheat in tempura and panko. Imitation crab often contains wheat starch and egg white, so go by the label. Mollusks and mustard are not major allergens in the United States, though they are in the UK. The plan tells you not to promise "gluten-free" (21 CFR 101.91): soy sauce and tempura contain wheat and the fryer is shared. The checklist has you build an allergen matrix by dish before opening.`,
  },
  {
    q: `Do I need a license to serve beer, sake and wine?`,
    a: `Yes, if you want to sell them. The beer and wine license comes from a state agency plus local approval, and sake usually goes under the wine license, so ask your state's alcohol beverage control agency. The checklist has you apply as soon as you sign the lease and puts a beer and wine license contingency in the lease itself. The kit does not promise a license, and the plan never counts on it. Liquor liability goes in your insurance, with general liability, product liability for raw fish, property and workers' comp ($8,000 a year in the example). It's a beer, sake and wine restaurant in the example, not a full bar: for that, start from the Bar Business Plan Kit.`,
  },
  {
    q: `How much does a sushi chef make? Do I need a head sushi chef?`,
    a: `Indeed puts the average sushi chef pay at $20.72 an hour in June 2026, within a range of $14.48 to $29.64, and a head sushi chef is paid above that. In the example the head sushi chef (itamae) is a hire at $5,199 a month, about $30 an hour, who buys, breaks down and cuts the fish and runs the bar; a sushi chef earns about $21 an hour and a part-time sushi chef about $20 for dinners and weekends. In all, 10 people counting you, 8.60 full-time equivalents and $384,226 in year 1 with employer payroll taxes, ${CASO.personalPct} of sales. The plan's advice: hire the head sushi chef before the build-out and train a second person who can cut, because if the only person who can run the bar is out, the bar does not open.`,
  },
  {
    q: `How does the Sushi Fish, Rice & Costing Calculator work?`,
    a: `Four sheets: Fish Yield, Sushi Rice, Costing and Instructions, in US units (pounds, ounces and fluid ounces). Fish Yield takes the price per pound, the yield and the trim you reuse for a whole farmed salmon, a salmon fillet, a yellowfin tuna saku block and a fish of your own, and gives you the cost per usable lb, per nigiri slice, per sashimi cut and per roll, and whether breaking down the whole fish pays off with your labor. Sushi Rice gives you the sushi rice per pound of raw rice, its cost with the sushi vinegar and the nori, the nigiri per pound and the raw rice to cook each day for your covers. Costing prices 14 products, from nigiri, sashimi and rolls to platters, gyoza, edamame and mochi, from the prices you type (the example's are kit estimates for October 2026: replace them with your distributor's), and shows the food cost, the suggested menu price and the margin dine-in, on take-out and on a marketplace, plus the weighted food cost of the week.`,
  },
  {
    q: `Does it work for an omakase counter, a poke shop or a take-out-only sushi shop?`,
    a: `Not as it stands. The plan is written for a neighborhood sushi restaurant with a sushi bar, tables, take-out and delivery, and it describes the other models so you can choose before you sign: an omakase counter of about 10 seats, with two seatings, a fixed price and reservations, is a different business with different fish; a poke and hand roll bar is counter service with no sushi chef at the bar; a take-out and delivery shop is small and lives on marketplaces; and conveyor-belt (kaiten) or all-you-can-eat formats need many more seats at a set price. The Excel workbook takes any numbers you type, but the written plan describes this restaurant.`,
  },
  {
    q: `Is this for a sushi franchise, a grocery store sushi counter or a food truck?`,
    a: `No. A franchise follows its franchisor's system and fees: the plan tells you to ask for the Franchise Disclosure Document, read Item 7 (the estimated initial investment) and Item 19 (financial performance figures, if it gives them), and compare both accounts before you sign. Grocery store sushi and franchise kiosks are another business again. A food truck has a different license, a commissary and no dining room, while this plan is written for a fixed location with a hood: for a mobile business, the Food Truck Business Plan Kit fits better. This kit is for the independent owner who builds a sushi restaurant of their own. For a full-service restaurant with a full bar, the Restaurant Business Plan Kit is the general plan, with the same lender-ready format.`,
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
    a: `Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your menu prices without it. The plan and the checklist are in US units, with °C and sq m beside the key figures, and the calculator works in pounds and ounces only. The plan's UK note covers registering with your council at least 28 days before you open, the Food Hygiene Rating, freezing fish for raw service with no exemption for tuna, 20% VAT on dine-in and hot food while cold take-away sushi is usually zero-rated, the 14 UK allergens and the premises and personal licences for alcohol. In Canada and Australia, check your provincial or state rules with your local authority. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.`,
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
  slug: 'sushi-restaurant-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_SUSHI_RESTAURANT_BUSINESS_PLAN',

  seo: {
    title: 'Sushi Restaurant Business Plan: Word + Excel Projections + Fish & Rice Cost Calculator | AI Chef Pro',
    description:
      'Sushi restaurant business plan for a sushi bar: Word plan, 3-year Excel projections, fish yield and cost-per-roll calculator and raw-fish permit checklist.',
    keywords:
      'sushi restaurant business plan, sushi bar business plan, how to open a sushi restaurant, sushi restaurant startup costs, how much does it cost to open a sushi restaurant, sushi business plan, sushi restaurant profit margin, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg',
  },

  schema: {
    productName: 'Sushi Restaurant Business Plan Kit',
    productDescription:
      'Sushi restaurant business plan kit for a neighborhood sushi bar with tables, take-out and delivery: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a fish yield, sushi rice and per-piece costing calculator, and an 80-task startup checklist in 6 phases covering the hood, the raw-fish rules and the permits. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Sushi Restaurant Business Plan Kit',
  },

  images: {
    // hero bg (6) — mismos huecos que la landing ES plan-negocio-sushi-bar (el sushi bar de barrio abre).
    gallery: [
      '/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-pescado.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-arroz.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-equipo.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden (= ES).
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-sushi-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-pescado.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-arroz.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-sushi-bar-pescado.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-sushi-bar-barra.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready sushi restaurant business plan: Word + Excel + fish, rice & costing calculator',
    titlePre: 'Sushi Restaurant ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Sushi Bar with Take-Out and Delivery: Word Plan + Excel Projections + Fish Yield & Costing Calculator + Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch a neighborhood sushi restaurant with a sushi bar in view, tables, take-out and marketplace delivery: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in covers per day, 12-month cash flow and loan payments from your own numbers; a calculator that costs every pound of fish, every batch of sushi rice and every piece, roll and platter; and an 80-task checklist that takes you from your LLC, your lease and the hood to the raw-fish logs and your first 90 days open. Set up for the US, with notes for the UK.`,
    checkItems: [
      '10-section sushi restaurant business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in covers per day and 12-month cash flow',
      'Fish, rice & costing calculator: cost per usable lb, nigiri per lb of rice, food cost per piece',
      'Startup checklist: 80 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Sushi Restaurant Business Plan Kit: 9 building blocks to test whether your sushi bar works on paper before you sign a lease or order a sushi case, cost every piece and every platter, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Sushi Restaurant Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a neighborhood sushi restaurant with a sushi bar and tables: executive summary, concept and value proposition (including the sushi models, from take-out-only to omakase, and why this plan takes the middle one), market analysis, competitive analysis, marketing plan, operations plan (fish yield, sushi rice, equipment, food safety and the daily schedule), management and staffing, financial plan, legal requirements, permits and raw-fish rules, and conclusions with an action plan and the thirteen mistakes to avoid. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Sushi Restaurant Financial Projections (Excel, 9 Sheets)', desc: `Is a sushi restaurant profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. Linked formulas throughout: change covers per day, average check or operating days and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Sushi Fish, Rice & Costing Calculator (Excel: Fish Yield + Sushi Rice + Costing)', desc: `The cost of every piece, from your own prices. The fish yield sheet takes a whole farmed salmon, a salmon fillet, a tuna saku block and a fish of your own, and gives you the cost per usable lb, per nigiri slice, per sashimi cut and per roll, and whether breaking down the whole fish pays off with your labor. The sushi rice sheet tells you how much sushi rice a pound of raw rice makes, what it costs with the vinegar and the nori, and how much rice to cook a day. The costing sheet prices 14 products, from nigiri and rolls to platters, gyoza and mochi, with the food cost, the suggested menu price and the margin dine-in, on take-out and on a marketplace.` },
      { icon: 'Coins', title: 'Sushi Restaurant Startup Costs, Line by Line', desc: `How much does it cost to open a sushi restaurant? Architect, MEP and hood drawings and permit fees, the build-out with the sushi bar counter and signage, electrical, plumbing, grease interceptor, HVAC and gas lines, a Type I hood with fire suppression and makeup air, a refrigerated sushi case, gas rice cookers and rice warmers, a −4 °F freezer with a temperature logger, the fryer, range and griddle, a walk-in cooler, reach-in fish refrigerators, dish and sink equipment, smallwares from Japanese knives to a calibrated pH meter, furniture and sushi bar seating, POS and online ordering, LLC and legal, branding and launch, and opening inventory, each with a reference price you replace with your quotes, plus a deposit, rent before opening, a contingency and working capital.` },
      { icon: 'TrendingUp', title: 'Break-Even in Covers per Day + 3 Scenarios', desc: `How many covers a day you need at your average check (excl. sales tax) to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance: honest about what a slow first year does to your cash.` },
      { icon: 'Users', title: 'Staffing & Shift Labor', desc: `The owner as general manager, a head sushi chef (itamae) hired to run the bar, a sushi chef and a part-time sushi chef for dinners and weekends, a kitchen line cook for tempura, gyoza and rice, servers who also host and pack to-go orders, and dish and prep, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need, including the production shift before opening, and takes the higher of the federal and your state or local minimum wage as the pay floor. Tips go on top of pay.` },
      { icon: 'BarChart3', title: 'Sales Mix, Delivery Share & Cost Lines', desc: `Food against beverage (sushi, rolls and the kitchen against beer, sake, wine, soft drinks and tea), the share of sales that goes through third-party delivery marketplaces and the commission you pay on it (the published DoorDash and Uber Eats ranges are in the plan), plus hood cleaning, music licensing, and waste, grease and used-oil hauling as their own cost lines.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (80 Tasks, 6 Phases)', desc: `Business setup (zoning check, your format and how you will meet the parasite rule, LLC, EIN, business license and sales tax permit, the beer and wine license, two SBA 7(a) lenders), hood and permits (a second-generation space, the hood and duct route, a lease with a beer and wine license contingency, plan review, building permit and certificate of occupancy), raw fish and health (a freezer with a temperature logger, supplier parasite letters and aquaculture statements kept 90 days, the consumer advisory, the receiving log for tuna, yellowtail and mackerel, TPHC or a variance for the sushi rice in writing), staff and allergens (the head sushi chef hired before the build-out, CFPM and food handler cards, sushi bar training, the 9 major allergens), menu, brand and delivery (two fish suppliers, cost per piece and platter by channel, marketplace contracts with a share cap), and opening day plus your first 90 days.` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year, plus investors or partners, local grants and an SBA Microloan as other sources of funds, and a red flag if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: a sushi restaurant plan written for the format lenders expect, with a financial model, a fish, rice and costing calculator and the raw-fish and sushi-rice rules that recalculate from your own numbers.`,
    reasons: [
      { icon: 'Fish', title: 'Built for a Neighborhood Sushi Restaurant', desc: `A head sushi chef in view at a sushi bar with 10 stools and a refrigerated sushi case, 30 seats at tables, a small hot kitchen for tempura, gyoza and miso under a Type I hood, take-out, marketplace delivery and platters to order; beer, sake and wine; open Tuesday through Sunday. How much does it cost to open a sushi restaurant? The hood, the sushi case, the freezer and the build-out, line by line. Nothing to strip out from a restaurant template.` },
      { icon: 'Calculator', title: 'The Cost of Every Piece, Roll and Platter', desc: `What a usable pound of whole salmon, salmon fillet or tuna saku really costs, how much sushi rice a pound of raw rice makes, what each nigiri, roll and platter runs in food cost, and what the same platter leaves dine-in and through a marketplace, all from your own numbers. The calculator's starting values are kit estimates, editable, and the checklist reminds you to measure your own yield and the real ounces per piece.` },
      { icon: 'Map', title: 'Raw Fish and Sushi Rice Rules, in Plain English', desc: `Fish served raw is frozen first under Food Code 3-402.11 unless it is exempt (tuna, and farmed fish such as salmon with the supplier's written statement), with records kept 90 days; sushi rice is held under time as a public health control or a variance your health department approves; and the menu carries the consumer advisory. The kit promises no "sushi-grade" fish and no legal pH: it tells you what to ask your health department in writing. It does not promise a beer and wine license either: it treats it as a lease contingency.` },
      { icon: 'BarChart3', title: 'Honest Numbers, Real Margins', desc: `The example: ${CASO.covers} covers a day at ${CASO.ticket} for ${CASO.dias} days, ${CASO.ventas} in year-1 sales, a net of ${CASO.netoPct1} in year 1 and about ${CASO.netoPct3} by year 3, and ${CASO.equilibrio} covers a day to break even, with the owner on payroll, the head sushi chef hired and delivery marketplaces at a 25% commission. The pessimistic scenario loses money, and the plan says so. Replace the numbers with yours.` },
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
    headingGold: 'Sushi Restaurant',
    subtitle:
      `Plan it before you sign the lease and order the sushi case: the written plan, the numbers behind it, the cost of every piece and the raw-fish permits list, for a one-time payment.`,
    items: [
      '10-section sushi restaurant business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in covers per day, with a sensitivity table',
      'Fish, rice & costing calculator: cost per usable lb, nigiri per lb of rice, food cost per piece',
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

  stickyLabel: 'SUSHI RESTAURANT BUSINESS PLAN — $39',

  // Salientes: Restaurant Checklists (rutinas del local abierto; no hay checklists de sushi EN), Food Cost (coste por pieza),
  // HACCP (pescado crudo, TPHC, registros), Restaurant Business Plan (el hermano general), Taco Shop, Rotisserie y Pizza Shop
  // (hermanos de local fijo con campana), Bar (barra completa, FAQ de la licencia), Food Truck (FAQ), Financial Plan + Staff
  // Scheduling y la guia de Food Cost (= cierre del Word).
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
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
    product: 'sushi-restaurant-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
