// astro-site/src/data/productos-en/planes/coffee-cart-business-plan.ts
// TIENDA INTERNACIONAL EN — Coffee Cart Business Plan Kit. DUPLICADO de wedding-venue-business-plan.ts (mismo tipo
// PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Edicion inglesa del ES
// «Plan de Negocio: Cafeteria Movil para Eventos» (hreflang reciproco, familia plan-negocio-cafeteria-movil-eventos), cuyo
// contenido y cifras NO se reutilizan: el EN es otro mercado (coffee catering en EE. UU.).
// SPEC: scripts/productos-digitales/business-plans-en-11/SPEC-delta.md (D216-D235) + F1-research-us-delta.md §9.
//   · D216b: title con el NOMBRE DEL PRODUCTO primero; H1 Forma B `Coffee Cart ` + oro `Business Plan` + «Template for a Mobile
//     Espresso Bar & Coffee Catering Company: …»; meta y keywords de research §9. «coffee cart» en nombre/H1; «coffee truck»
//     y «coffee trailer» SOLO como formatos/descriptor (meta, keywords, FAQ, schema); nunca «mobile cafeteria»/«mobile cafe».
//   · D217: $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating ni review.
//   · D218: 5 ficheros de dl/coffee-cart-business-plan/ + la guia comun de equivalencias EN (la guia LatAm del ES no cruza).
//     Los 6 H2 de research §9 no caben como H2 (constantes de UI_PLAN): sus keywords van en los titulos de «why», las
//     tarjetas del grid y la FAQ.
//   · Sin testimonios (los del ES son clientes de Espana; FTC). FAQ = las 8 de research §9 + canibalizacion (Coffee Shop, Food
//     Truck, Mobile Bar) + UK/CA/AU + las genericas de la familia.
//   · Cifras MEDIDAS en el libro (cifras_caso.json, F2-NOTAS §3): 170 events × 95 guests × $12.60 = $203,490, CAPEX $71,290,
//     caja $100,290, prestamo $71,000 (SBA 7(a), 10 %, 7 anos), DSCR min 2.58x, EBITDA 21.8 %, neto 9.9 % → 15.1 %, equilibrio
//     141 events (138 de caja), holgura 24 %. Nada de neto del ano 3 en prosa de venta, nada de volumenes de busqueda.
//   · Reglas de contenido (research §10): nada de «demanda creciente»; commissary «usually yes, ask your county in writing before
//     you buy the cart»; plan review como ejemplo con fuente; generador «ask your fire marshal»; cottage food fuera; vasos
//     compostables como regla LOCAL; Flashquotes ≠ ingresos esperados; sin espresso martinis (licencia: partner with a licensed
//     mobile bar); sin cifras moviles de leyes ni sales tax de un estado; el contrato es plantilla, no asesoria legal.
//   · Imagenes: las 7 plan-cafeteria-movil-*.jpg del ES (compartidas, sin texto). OG = recorte del hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_COFFEE_CART_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en el libro (business-plans-en-11/cifras_caso.json, F2-NOTAS §3) ─────────────────────
const CASO = {
  eventos: '170', // B4 — events per year (weekday corporate = the volume, weddings = the ticket, private parties, markets)
  invitados: '95', // B6 — guests per event
  ticket: '$12.60', // B5 — revenue per guest excl. sales tax
  ventas: '$203,490', // ventas A1 = 170 × 95 × $12.60
  capex: '$71,290', // 19 partidas $67,100 + fianza $700 + 1 mes previo $700 + contingencia $2,790
  partidas: '$67,100',
  caja: '$100,290', // necesidad de caja al lanzamiento (CAPEX + working capital $29,000)
  prestamo: '$71,000', // SBA 7(a) 10 % a 7 anos
  dscr: '2.58×', // DSCR minimo
  ebitda: '21.8%',
  netoPct1: '9.9%',
  equilibrio: '141', // eventos (contable)
  equilibrioCaja: '138', // eventos (caja)
  holgura: '24%',
  formulas: '700', // "more than N": el libro tiene 722 formulas
  porEvento: '$1,197', // ventas por evento
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `How much does it cost to start a coffee cart business?`,
    a: `cart-king.com puts the cart itself at $4,000 to $25,000 (from a basic new cart to a custom premium one) and a complete single-cart setup at about $16,600 to $49,000, with $24,000 typical. A coffee trailer or truck costs more. The kit's example is a coffee catering company with two stations, an espresso cart and a portable espresso bar, towed in an enclosed trailer by the owner's own vehicle, and it comes in at ${CASO.capex} in startup costs, line by line: the cart and the bar, two espresso machines and four grinders, the trailer, the mobile food unit plan review, a 5,500 W inverter generator, point of sale and smallwares. With working capital, the cash you need is ${CASO.caja}, and the Excel model recalculates all of it from your own numbers.`,
  },
  {
    q: `Is a coffee cart business profitable?`,
    a: `It can be, and the plan shows the math instead of promising it. In the example the company runs ${CASO.eventos} events a year averaging ${CASO.invitados} guests at ${CASO.ticket} per guest, which is ${CASO.ventas} in year-1 sales, an operating profit (EBITDA) of ${CASO.ebitda} and a net profit of ${CASO.netoPct1} after interest and taxes. The loan payment is covered ${CASO.dscr} in the toughest year against the 1.25× most lenders look for. Summer is the weak spot: published booking data shows July as the slowest month, so the 12-month cash flow starts in March and shows the dip. The pessimistic scenario is in the workbook too, so you can see how a bad year can run the cash out, and what to do about it. These are the example's results, not a forecast for your market.`,
  },
  {
    q: `How much should I charge for a coffee cart at an event?`,
    a: `Operators price in a few ways: a base fee plus an hourly rate for service hours, a price per guest, and a minimum for small events. In one published sample of 25,860 coffee cart bookings from 578 operators, the median booking was $1,040, the middle half ran from about $764 to $1,700, and a typical event had 100 guests. Local rate cards vary a lot with your metro, the number of baristas and the hours. The kit's calculator builds a price per guest from your own cost per drink, drinks per guest by event length, barista hours, travel and sales tax, and shows the same price per service hour and per drink, so you can compare it with a base fee plus an hourly rate or set a minimum for small events. It adds a retainer and a cancellation schedule and shows your margin, so you can check a price before you send it.`,
  },
  {
    q: `How many drinks per hour can one barista make?`,
    a: `Operators publish figures of about 50 to 65 drinks per hour for one cart with one barista, and roughly 100 per hour with two carts and two baristas. Treat that as a planning range, not a guarantee: it drops with milk-heavy menus, latte art, cold-weather lines and a slow machine. The calculator turns your guest count, event length and menu into drinks per hour and then into baristas, stations, grinders, pounds of beans, gallons of milk, cups and gallons of water, so you can staff the event instead of guessing.`,
  },
  {
    q: `Do you need a commissary kitchen for a coffee cart?`,
    a: `Usually yes, but it depends on your county. Milk is a time-and-temperature controlled food, so a coffee cart is generally treated as a mobile food unit, with a health permit, a plan review and a base of operations for water, waste water and storage. Some counties exempt self-contained units, and the FDA Food Code leaves the decision to the local authority. Ask your county in writing before you buy the cart. The kit includes a commissary line in the startup costs and a Phase 2 of the checklist ("Permits & Commissary") with the questions to ask. It is not legal advice.`,
  },
  {
    q: `What permits do I need to run a coffee cart?`,
    a: `It depends on your city, county and state. Expect a business license, a sales tax permit, a mobile food unit permit with a plan review of your cart, a commissary agreement, food handler cards for your team (and a certified food protection manager in some counties), a temporary event permit for festivals and markets, and a certificate of insurance for the venues that ask for one. An espresso cart usually has no grease-producing equipment, but a generator needs its own placement and fire rules, so ask your fire marshal. The checklist lists each step in order, and the Word plan's permits section explains the process with examples. Always confirm with your local agencies.`,
  },
  {
    q: `Can I use this as a coffee truck or coffee trailer business plan?`,
    a: `Yes for events and catering: a coffee truck or a coffee trailer that serves weddings, corporate events and private parties follows the same model. The example uses a cart and a portable bar towed in an enclosed trailer, and the Word plan compares cart, trailer and truck and when each makes sense. Change the equipment lines in the Excel and everything recalculates. If you plan to park a truck on a street or at a lot every day to sell to walk-up customers, that is a different business with different permits and economics: see the Food Truck Business Plan Kit.`,
  },
  {
    q: `Can I sell pastries or espresso martinis from my coffee cart?`,
    a: `Pastries: cottage food rules usually let a home baker sell directly to consumers, but resale through a business is often outside them, so plan to buy from a licensed bakery and check with your county. Espresso martinis: serving alcohol needs a license, and this plan does not include it. The model sells coffee, tea and non-alcoholic drinks, and for a cocktail hour the usual route is to partner with a licensed mobile bar (see the Mobile Bar Business Plan Kit).`,
  },
  {
    q: `What should a coffee cart business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a coffee catering company, with an Excel model whose numbers match the text, so you edit instead of starting from a blank page.`,
  },
  {
    q: `Is it a generic template or built for a coffee cart?`,
    a: `Built for a mobile espresso bar that works events: corporate offices and conferences on weekdays (the volume), weddings and private parties (the ticket) and festivals or farmers markets paid by the guest as an extra. It covers the equipment, the commissary, power at the venue (110V or 220V, amps and a generator), pricing by guest and by service hour, barista staffing and the contracts. It does not cover a coffee shop with a storefront (see the Coffee Shop Business Plan Kit).`,
  },
  {
    q: `Do I need a generator or power at the venue?`,
    a: `A two-group espresso machine typically runs on a dedicated 220V circuit and draws 15 to 17 amps, while many venues only offer 110V outlets. The plan covers the options: ask the venue for a dedicated circuit in writing, use a compact machine on 110V, or bring an inverter generator and charge a generator fee. The calculator flags the amps and outlet type each event needs, and the service agreement has a clause for it. Generator placement and fuel rules are set by your fire marshal, so ask before you buy one.`,
  },
  {
    q: `Do I charge sales tax on a coffee cart event?`,
    a: `It depends on your state and on who pays. In many places a hosted event (the host pays you) is taxed as a catering service, while a festival or market where each guest pays per drink is a retail sale of a prepared drink, and some states also tax the service charge. The model has one sales tax rate with an example value that you replace with yours, and the Instructions tab has notes on what to check. Confirm the rules with your state revenue agency or your CPA. This is not tax advice.`,
  },
  {
    q: `What is the difference between a coffee cart, a coffee trailer and a coffee truck?`,
    a: `A cart is the cheapest and lightest option: it is towed or carried, fits indoor venues and is the most common format at events. A trailer adds storage and a bigger bar, but you need a tow vehicle and a place to park it. A truck brings the engine and the kitchen in one vehicle and costs the most, and it shines for daily street routes more than for events. The Word plan compares the three on cost, permits, power and where each one works best.`,
  },
  {
    q: `What is in the pricing calculator?`,
    a: `Four sheets. Cost per Drink works out the cost of every drink on your menu from beans, milks (including oat and other alternatives), syrups and cups, with the menu price and cost percentage. The Pricing Calculator turns a private, corporate or festival event into a quote: guests, service format, hours, power, barista pay with payroll taxes, travel, sales tax, the drinks, baristas and stations you need, price per guest, per service hour and per drink, retainer and balance, and a cancellation schedule. Three Example Quotes show a wedding, a corporate event and a community festival with a guest-pay minimum sales guarantee. An Instructions tab explains each field.`,
  },
  {
    q: `What is in the coffee catering service agreement template?`,
    a: `One editable Word document with brackets for everything you fill in. It covers the event details, the service window, the guest count and final headcount, pricing, a retainer applied to the price, a cancellation schedule with a rebooking credit, power and access requirements, setup space, weather, insurance and the certificate of insurance, food-safety and allergen notes, and an annex for corporate clients and festivals (W-9, purchase orders, net terms, a minimum sales guarantee and vendor fees). It is a template, not legal advice: have a local attorney review it for your state.`,
  },
  {
    q: `What is the difference between this kit and the Coffee Shop, Food Truck and Mobile Bar business plan kits?`,
    a: `The Coffee Shop kit is for a storefront with daily walk-in traffic, the Food Truck kit is for a vehicle that sells food on a daily route, and the Mobile Bar kit is for a licensed cocktail and bar service. This kit is for a coffee business that books events: the customer is a host, a company or an organizer, you quote per guest and per service hour, and the big numbers are the booking calendar, the barista hours and the power at each venue.`,
  },
  {
    q: `Can I present this plan to a lender or investors?`,
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds, and a loan schedule with the debt service coverage ratio (DSCR), checked against a 1.25x lender target. It is a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice: review the figures with your accountant before presenting them.`,
  },
  {
    q: `Can I change the numbers in the Excel model?`,
    a: `Yes. The green cells are the ones you type: events per year, guests per event, revenue per guest, rent for the commissary, wages and every startup cost line. More than ${CASO.formulas} linked formulas recalculate the rest. To change a calculated cell, use Review, Unprotect Sheet (there is no password). The workbook, the calculator and the checklist each include an Instructions tab.`,
  },
  {
    q: `Does it work in the UK, Canada or Australia?`,
    a: `Yes, with some work from you. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, and your own minimum wage and employer costs. The plan gives US units with metric beside them. Permits and food-safety rules are local everywhere: the plan describes the US process (mobile food unit permit, commissary, fire marshal), and the Equivalents Guide that comes with the kit maps the terms and rules for the UK, Canada and Australia. Check with your local authority.`,
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
  slug: 'coffee-cart-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_COFFEE_CART_BUSINESS_PLAN',

  seo: {
    title: 'Coffee Cart Business Plan Template for Coffee Catering: Word + Excel Projections + Pricing Calculator | AI Chef Pro',
    description:
      'Coffee cart business plan for coffee catering (cart, trailer or truck): Word plan, 3-year Excel projections, per-guest pricing calculator and startup checklist.',
    keywords:
      'coffee cart business plan, coffee truck business plan, mobile coffee business plan, coffee trailer business plan, how to start a coffee cart business, coffee catering, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-coffee-cart-business-plan.jpg',
  },

  schema: {
    productName: 'Coffee Cart Business Plan Kit',
    productDescription:
      'Coffee cart business plan template kit for a mobile espresso bar and coffee catering company (cart, trailer or truck formats): a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a pricing calculator from cost per drink to quote per guest, a 68-task startup checklist and a coffee catering service agreement template, set up for the US on Letter paper.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Coffee Cart Business Plan Kit',
  },

  images: {
    // hero bg (6) — las 7 plan-cafeteria-movil-*.jpg del ES, compartidas.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-empresa.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-feria.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-equipo.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden.
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-empresa.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-feria.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-equipo.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-empresa.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready coffee cart business plan: Word + Excel + pricing calculator + service agreement',
    titlePre: 'Coffee Cart ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Mobile Espresso Bar & Coffee Catering Company: Word Plan + Excel Projections + Per-Guest Pricing Calculator + Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch a coffee catering company that serves corporate events, weddings, private parties and markets from an espresso cart and a portable espresso bar: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in events, 12-month cash flow and loan payments from your own numbers; a pricing calculator that goes from cost per drink to a quote per guest and per service hour; a 68-task startup checklist; and a coffee catering service agreement template. Works for a cart, a trailer or a truck that books events.`,
    checkItems: [
      '10-section coffee cart business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in events and 12-month cash flow',
      'Pricing calculator: cost per drink, quote per guest and per service hour, retainer and cancellation schedule',
      'Coffee catering service agreement template',
      'Startup checklist: 68 tasks in 6 phases, from your LLC to your first events',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Coffee Cart Business Plan Kit: 9 building blocks to test whether your coffee catering company works on paper before you buy the cart, price every event, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Coffee Cart Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a coffee catering company with an espresso cart and a portable espresso bar: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan (commissary, equipment, power, event days), management and staffing, financial plan, legal requirements and permits, and conclusions. Edit it with your own city, name and numbers.` },
      { icon: 'FileSpreadsheet', title: 'Coffee Cart Financial Projections (Excel, 9 Sheets)', desc: `Is a coffee cart profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than ${CASO.formulas} linked formulas: change events per year, guests per event or revenue per guest and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Coffee Cart Pricing Calculator (Cost per Drink to Quote per Guest)', desc: `Coffee cart pricing from your own costs. Cost per Drink prices every drink on your menu from beans, milks, syrups and cups. The Pricing Calculator turns a private, corporate or festival event into a quote: guests, service format, hours, power (110V, 220V or generator), barista pay, travel, sales tax, drinks per hour, baristas and stations, price per guest, per service hour and per drink, retainer and cancellation schedule. Three example quotes included.` },
      { icon: 'ScrollText', title: 'Coffee Catering Service Agreement Template', desc: `One editable Word document with brackets for everything you fill in: service window, guest count and final headcount, retainer applied to the price, a cancellation schedule with a rebooking credit, power and access, weather, insurance and a certificate of insurance, plus an annex for corporate clients and festivals. A template, not legal advice.` },
      { icon: 'Coins', title: 'How Much Does It Cost to Start a Coffee Cart Business? (Cart vs. Trailer vs. Truck)', desc: `The example line by line: the cart and the portable bar, two espresso machines, four grinders, an enclosed trailer, the mobile food unit plan review, an inverter generator, point of sale and smallwares. Plus the Word plan's comparison of a cart, a trailer and a truck on cost, power, permits and where each works best.` },
      { icon: 'TrendingUp', title: 'Break-Even in Events + 3 Scenarios', desc: `How many events a year you need at your average guests and revenue per guest to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side.` },
      { icon: 'Users', title: 'Staffing & Event Baristas (4 Roles)', desc: `Owner and lead barista, a part-time lead barista, event baristas and an on-call barista or driver, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (68 Tasks, 6 Phases)', desc: `Business setup (LLC, EIN, bank, business license, sales tax permit and your loan package), permits and commissary (the mobile food unit permit and plan review, the fire marshal and the generator, the trailer at the DMV), equipment and supplies, hiring baristas, brand and bookings, and your first events with a 90-day review.` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25x target, plus investors or partners as other sources of funds, and a warning if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: a coffee catering plan written for the format lenders expect, with a financial model, a pricing calculator and a service agreement that recalculate from your own numbers.`,
    reasons: [
      { icon: 'Map', title: 'Built for a Mobile Espresso Bar & Coffee Catering Company', desc: `An espresso cart and a portable espresso bar towed in an enclosed trailer, baristas on W-2 payroll, a commissary as your base, and an events-first calendar: corporate offices on weekdays are the volume, weddings are the ticket, and festivals and markets are a guest-pay extra. It is not a coffee shop plan with a cart bolted on.` },
      { icon: 'Coins', title: 'How Much Does It Cost to Start a Coffee Cart Business? Cart vs. Trailer vs. Truck', desc: `cart-king.com puts a complete single-cart setup at about $16,600 to $49,000, with $24,000 typical. The example, with two stations and a trailer, runs ${CASO.capex} in startup costs and ${CASO.caja} in total cash needs, line by line, so you can see where the money goes and what to cut.` },
      { icon: 'Calculator', title: 'Coffee Cart Pricing: What to Charge per Guest and per Service Hour', desc: `A price per guest built from your cost per drink, drinks per guest and barista hours, with the same price shown per service hour and per drink so you can compare it with a base fee plus an hourly rate or set a minimum for small events. A retainer, a final headcount and a cancellation schedule come with it.` },
      { icon: 'BarChart3', title: 'Is a Coffee Cart Business Profitable? Corporate Events, Weddings and the Summer Dip', desc: `The example: ${CASO.eventos} events a year averaging ${CASO.invitados} guests at ${CASO.ticket} per guest, ${CASO.ventas} in year-1 sales, ${CASO.netoPct1} net in year 1, a loan covered ${CASO.dscr} in the toughest year, and about ${CASO.equilibrio} events to break even. July is the slowest month in published booking data, so the cash flow shows the dip instead of hiding it.` },
      { icon: 'ShieldCheck', title: 'Coffee Cart Permits: Health Department, Commissary and Fire Marshal', desc: `Milk makes a coffee cart a mobile food unit in most counties. The plan and the checklist walk you through the health permit and plan review, the commissary question, the fire marshal and your generator, and tell you to ask each agency in writing. Local rules vary, so confirm with your county.` },
      { icon: 'Layers', title: 'Coffee Truck or Coffee Cart: Which Business Plan Do You Need?', desc: `Events and catering with a cart, trailer or truck: this kit. A truck that sells to walk-ups on a daily route is a different business: see the Food Truck Business Plan Kit. A storefront: see the Coffee Shop Business Plan Kit.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    `CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening restaurants, caterers, bars and coffee businesses, combining hands-on operations with financial planning.`,
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      `Besides the business plan, the financial model, the calculator, the agreement and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves`,
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Coffee Cart Permits, Commissary & Power Guide (US + UK Notes)',
        desc: `Section 9 of the plan plus Phase 2 of the checklist: the mobile food unit permit and plan review, the commissary question and what to ask your county, the fire marshal and generator placement, temporary event permits for festivals and markets, and the 110V versus 220V question for every venue. Examples, not legal advice: confirm with your local agencies.`,
        image: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-montaje.jpg',
      },
      {
        icon: 'BarChart3',
        title: 'US Coffee Catering Benchmarks (Sourced)',
        label: 'BONUS 2',
        desc: `The reference table inside the workbook: what coffee cart operators charge for typical events, drinks per guest by event length, cost per drink ranges, the weekday corporate share of bookings and seasonality, each with its source or marked "kit estimate" when there isn't one, plus traffic-light checks on your P&L against editable thresholds.`,
        image: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-plan.jpg',
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
    headingGold: 'Coffee Cart',
    subtitle:
      `Plan it before you buy the cart: the written plan, the numbers behind it, the price of every event and the agreement, for a one-time payment.`,
    items: [
      '10-section coffee cart business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in events, with a sensitivity table',
      'Pricing calculator: cost per drink to quote per guest',
      'Coffee catering service agreement template',
      'Startup checklist: 68 tasks in 6 phases',
      'BONUS: Coffee Cart Permits, Commissary & Power Guide (included in the plan)',
      'BONUS: US Coffee Catering Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'COFFEE CART BUSINESS PLAN — $39',

  // Salientes: Coffee Shop (siguiente paso: local), Mobile Bar (espresso martinis / barra de cocteles), Food Truck (ruta diaria),
  // Catering, Coffee Shop Checklists (rutinas) y el resto de la familia.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/mobile-bar-business-plan', label: 'Mobile Bar Business Plan Kit' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/catering-business-plan', label: 'Catering Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-checklist-templates', label: 'Coffee Shop Checklists Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'New product · Version 2.2 · October 2026',

  alreadyBought: {
    product: 'coffee-cart-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
