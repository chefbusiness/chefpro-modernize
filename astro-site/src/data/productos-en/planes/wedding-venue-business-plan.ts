// astro-site/src/data/productos-en/planes/wedding-venue-business-plan.ts
// TIENDA INTERNACIONAL EN — Wedding Venue Business Plan Kit. DUPLICADO de pizza-shop-business-plan.ts (mismo tipo
// PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos). Edicion inglesa del ES
// «Plan de Negocio: Finca de Eventos y Bodas» (hreflang reciproco, familia plan-negocio-finca-eventos-bodas), cuyo
// contenido y cifras NO se reutilizan: el EN es otro mercado (barn/estate venue en EE. UU., SPEC D159).
// SPEC: scripts/productos-digitales/business-plans-en-9/SPEC-delta.md (D156-D177 + §11 O1-O4) + REVISION-FINAL.md (§5).
//   · D156b: title con el NOMBRE DEL PRODUCTO primero; H1 Forma B `Wedding Venue ` + oro `Business Plan` + «Template for an
//     Event Venue with an Exclusive Caterer: …»; meta y keywords de research §9. «wedding venue» en nombre/H1, «event
//     venue» como descriptor, «venue» en prosa.
//   · D157: $49 SIN anclas (sin priceOld, «-x %», «Total value», «Save $» ni valor de los bonos), sin rating ni review.
//   · D158: 5 ficheros de dl/wedding-venue-business-plan/ + la guia comun de equivalencias EN. Los 6 H2 de research §9 no
//     caben como H2 (constantes de UI_PLAN): sus keywords van en los titulos de «why», las tarjetas del grid y la FAQ.
//   · Sin testimonios (los del ES son clientes de Espana; FTC). FAQ = las 8 de research §3 + «Do I need an LLC» (PAA) +
//     canibalizacion (Catering, BBQ Catering, Paella Catering, Mobile Bar) + UK/CA/AU.
//   · Cifras MEDIDAS en el libro tras la revision D174 (REVISION-FINAL §0/§5): 100 events × 90 guests × $68 = $612,000,
//     CAPEX $570,500, caja $669,716, prestamo $470,000, DSCR min 1.86, neto 8.9 % → 14.2 %, equilibrio 86 (84 de caja),
//     holgura 20 %. Calculadora: boda de sabado de temporada alta, 130 guests, $12,690 con impuesto. Nada de volumenes de
//     busqueda (REVISION M4).
//   · Reglas de contenido de la revision: obra sobre propiedad ARRENDADA (lease con prorrogas ≥ plazo del prestamo, «SBA
//     lenders typically require…; confirm with your lender», opcion de compra, consentimiento del propietario, TI
//     allowance; comprar = variante SBA 504); el venue NO sirve alcohol (lo hace el exclusive caterer con licencia); la FTC
//     Cooling-Off Rule NO se afirma («ask your attorney whether…»); el contrato es plantilla, no asesoria legal; permisos
//     siempre «check with your county/state»; comision del caterer 10 % del F&B (≈ 12 % de las ventas del venue).
//   · Imagenes: las plan-finca-*.jpg del ES (abiertas una a una: sin texto ni marcas). OG = recorte del hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_WEDDING_VENUE_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — MEDIDAS en el libro revisado (business-plans-en-9/REVISION-FINAL.md §0, cifras_caso.json) ──────
const CASO = {
  eventos: '100', // B6 — events per year (35 weddings, 25 corporate, 30 private celebrations, 10 micro weddings)
  invitados: '90', // B4 — guests per event, average of the mix
  ticket: '$68', // B5 — revenue per guest excl. sales tax (venue rental & services + caterer commission)
  ventas: '$612,000', // ventas A1 = 100 × 90 × $68
  capex: '$570,500', // 19 partidas $503,500 + imprevistos $37,000 + fianza $10,000 + renta previa $20,000
  partidas: '$503,500',
  caja: '$669,716', // necesidad de caja al lanzamiento
  prestamo: '$470,000', // SBA 7(a) 10 % a 10 anos, sin carencia
  dscr: '1.86×', // DSCR minimo (año 1)
  netoPct1: '8.9%',
  netoPct3: '14.2%',
  equilibrio: '86', // eventos (contable)
  equilibrioCaja: '84', // eventos (caja)
  holgura: '20%', // 19.8 %
  formulas: '700', // "more than N": el libro tiene 734 formulas
  ejemplo: '$12,690', // calculadora: boda de sabado de temporada alta, 130 guests, con sales tax
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: `What should a wedding venue business plan include?`,
    a: `The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements, permits and licenses, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a barn or estate event venue with an exclusive caterer, plus the Excel financial projections behind them, a pricing and quote calculator, venue rental agreement templates and an 84-task startup checklist.`,
  },
  {
    q: `Is it a generic template or built for a wedding venue?`,
    a: `Built for a wedding and event venue on a leased property 30 to 60 minutes from a mid-size city: a barn or estate with a hall for 200 seated guests, an outdoor ceremony site with a pergola, a bridal suite, ADA-compliant restrooms and a prep kitchen for the caterer. The venue earns a venue rental fee plus event services and a commission from its exclusive caterer, and it does not sell food or alcohol. Nothing to strip out from a restaurant or catering template. If your venue is different, the Excel workbook takes any numbers you type, but the written plan describes this venue.`,
  },
  {
    q: `How much does it cost to start a wedding venue?`,
    a: `Published estimates for buying or building a venue run well into six or seven figures, and the property, the build-out and the permits are what move the number. The kit's example is a barn conversion on a leased property and comes in at ${CASO.capex} in startup costs, line by line: architect and code consultant drawings, the conditional use permit and its studies, the barn renovation, a fire sprinkler system, ADA-compliant restrooms, electrical and emergency lighting, a standby generator, HVAC, the caterer's prep kitchen, tables and chairs for 200, the ceremony site, sound, parking and landscaping, plus a lease security deposit, rent during permitting and build-out and a contingency. With working capital, the cash needed at launch is ${CASO.caja}. Sprinklers on a property without city water, a new septic system or a strict county can double some lines: replace every line with your own quotes. They are example prices, not a price list.`,
  },
  {
    q: `Can a wedding venue be profitable? What is a realistic margin?`,
    a: `It can be, and the plan shows the math instead of promising it. In the example the venue holds ${CASO.eventos} events a year (35 weddings, 25 corporate events, 30 private celebrations and 10 micro weddings) averaging ${CASO.invitados} guests at ${CASO.ticket} of venue revenue per guest, which is ${CASO.ventas} in year-1 sales. After rent, staff and loan payments, the net profit is ${CASO.netoPct1} of sales in year 1 and ${CASO.netoPct3} by year 3, with the owner on payroll at $4,500 a month. The loan payment is covered ${CASO.dscr} in the toughest year. The pessimistic scenario (fewer events, fewer guests, a lower price) is in the workbook too. What you earn depends on how many peak-season Saturdays you sell, so replace the example with your own numbers.`,
  },
  {
    q: `How many weddings and events do I need to break even?`,
    a: `In the example, about ${CASO.equilibrio} events a year on the average mix cover every cost, and ${CASO.equilibrioCaja} cover the cash you actually need, with loan payments in and depreciation out. The base case holds 100 events, a cushion of about ${CASO.holgura}. The break-even sheet recalculates from your guests per event, your revenue per guest and your fixed costs, and it comes with a sensitivity table and a plain-English reading of the result.`,
  },
  {
    q: `What zoning and permits do I need to open a wedding venue?`,
    a: `It depends on your county, and it is the first thing to settle. Hosting events on farm or rural land often needs a conditional (special) use permit with a public hearing and conditions such as an event cap, hours and traffic, then a change of occupancy to assembly use and a certificate of occupancy, and a fire marshal who tells you the occupant load, whether sprinklers are required and what the exits and restrooms must be. ADA Title III applies to public accommodations, and septic or well capacity may need an engineer. The plan and the checklist explain each step and tell you to ask your county and your fire marshal in writing before you sign the lease, and to make the lease contingent on the permit. They do not promise that any permit will be granted.`,
  },
  {
    q: `Do I need a liquor license to run a wedding venue?`,
    a: `Not in the model this kit plans for. The venue does not sell alcohol: its exclusive caterer holds the license or permit and serves the bar, and the venue's contract requires a certificate of insurance. If you want to allow BYOB, the plan covers the usual conditions (a licensed bartender and the client's host liquor liability insurance), but alcohol rules are set by each state, so ask your state's alcohol board before you decide. The kit does not promise a license.`,
  },
  {
    q: `Exclusive caterer, preferred vendor list or in-house catering: how does the venue get paid?`,
    a: `The plan is built on an exclusive caterer: one licensed caterer serves at your venue and pays you a commission on its food and beverage sales (10% in the example, negotiable). That is about 12% of the venue's sales in the example, with no kitchen crew on your payroll and the menu's food-safety responsibility with the caterer. A preferred vendor list and in-house catering are explained in the Word plan as alternatives, with their trade-offs, but the Excel does not model them. The agreement templates include an Exclusive Caterer Agreement with the commission, a monthly statement and an audit right.`,
  },
  {
    q: `Are wedding venue deposits non-refundable?`,
    a: `Writing "non-refundable" with no explanation is risky: in many states a court may refuse to enforce a deposit that works as a penalty. The templates use a retainer that is applied to the price, a cancellation schedule that keeps more as the date gets closer (written as a reasonable estimate of the venue's loss), a rebooking credit if you resell the date, and a full refund if the venue cancels. They are templates, not legal advice: state law varies, so have a local attorney review the agreement before you use it.`,
  },
  {
    q: `Do I need an LLC to host events?`,
    a: `Most venue owners set up a business entity, usually an LLC, to separate the business from personal assets, and the lease, the loan and the contracts are signed by that entity. Whether an LLC or an S corporation suits you, and how your state taxes it, is a question for your CPA and your attorney. The checklist puts it first, with the EIN, the state payroll accounts, the business license and the sales tax permit. The couple doesn't need an LLC to hold a celebration at your venue.`,
  },
  {
    q: `Should I rent or buy the property?`,
    a: `The example rents, which avoids the price of the property, but the build-out still puts hundreds of thousands of dollars into somebody else's building. The plan therefore asks you to negotiate a lease whose term, counting extension options that only you can exercise, matches or exceeds the loan term (SBA lenders typically require this; confirm with your lender), plus an option to buy or a right of first refusal, the landlord's consent to the work and to using the lease as collateral, a tenant improvement allowance and a lease that is contingent on the permit. Buying the property is described as a variant, usually an SBA 504 loan, without a financial model.`,
  },
  {
    q: `How does the pricing and quote calculator work?`,
    a: `One sheet turns your rate card into a quote for a specific date. You choose the client (couple or corporate), the event type, the date and the guests; the date sets the season (peak, shoulder or off-peak) and the day of the week, each with its own visible premium or discount, and each season has a guest minimum. Add the extras (ceremony on site, extra hours, premium decor, rehearsal the day before) and you get the price, sales tax, the total, the payment schedule with dates, your estimated caterer commission and the event contribution. It also gives the cancellation tiers with what you keep. The example, a Saturday peak-season wedding for 130 guests, comes to ${CASO.ejemplo} with sales tax. Three worked examples are included, and every rate is an editable example, not a market price.`,
  },
  {
    q: `What is in the venue rental agreement templates?`,
    a: `Three editable Word documents: a rental agreement for couples and private events, an addendum for corporate and organization clients, and an Exclusive Caterer Agreement. They cover permits, a booking contingent on them, the retainer, the cancellation schedule, the guest count and the final headcount, rain plan, maximum occupancy, noise and music curfew, outside vendors, insurance, security deposit and mutual responsibility. They are a template, not legal advice: state law varies, so have a local attorney review and adapt them. If you sign couples at bridal shows or off-site, ask your attorney whether the FTC Cooling-Off Rule or your state's home-solicitation law applies.`,
  },
  {
    q: `Is this for a barn on a farm, an existing event venue or a banquet hall?`,
    a: `The written plan is for a barn or estate venue on a leased property, converted or already permitted. If you already run an event venue, use the Excel, the pricing calculator and the agreements with your real numbers and skip the build-out. A city banquet hall, a hotel ballroom or a venue where you also cater need a different plan: for catering, see the Catering Business Plan Kit.`,
  },
  {
    q: `What is the difference between this kit and the Catering, BBQ Catering, Paella Catering and Mobile Bar business plan kits?`,
    a: `Those four are for businesses that bring the service to the client's location: a caterer, a barbecue caterer, a paella caterer or a mobile bar, each with its own kitchen or bar and a van. This kit is for the business that owns the space: it earns a rental fee and a commission, has no kitchen crew and no food cost, and its big numbers are the build-out, the permits and the Saturdays you sell. A venue's exclusive caterer could be one of those businesses. If you want to cater yourself, start with the Catering Business Plan Kit.`,
  },
  {
    q: `Can I present this plan to a lender or investors?`,
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds, and a loan schedule with the debt service coverage ratio (DSCR), checked against a 1.25x lender target. It is a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice: review the final numbers with your accountant before you apply for a loan.`,
  },
  {
    q: `Can I change the numbers in the Excel model?`,
    a: `Yes. The green cells are the ones you type: events per year, guests per event, revenue per guest, the caterer commission, rent, wages and every startup cost line. More than ${CASO.formulas} linked formulas recalculate the rest. To change a calculated cell, use Review, Unprotect Sheet (there is no password). The workbook, the calculator and the checklist each include an Instructions tab.`,
  },
  {
    q: `Does it work in the UK, Canada or Australia?`,
    a: `Yes, with some work from you. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, and your own minimum wage and employer costs. The plan gives US units with metric beside them (sq ft with sq m). Zoning and event licensing are local everywhere: the plan describes the US process (conditional use permit, certificate of occupancy, fire marshal), so in the UK, Canada and Australia ask your council or local authority which planning, premises and licensing rules apply to events at your property. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.`,
  },
  {
    q: `What currency will I pay in?`,
    a: `The price is $49 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The Excel cells have no currency symbol, so you type amounts in your own currency; the example in the Word plan is in US dollars.`,
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
  slug: 'wedding-venue-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_WEDDING_VENUE_BUSINESS_PLAN',

  seo: {
    title: 'Wedding Venue Business Plan Template: Word + Excel Projections, Pricing Calculator & Rental Agreement | AI Chef Pro',
    description:
      'Wedding and event venue business plan template: Word plan, 3-year Excel projections, pricing calculator, venue rental agreements and an 84-task startup checklist.',
    keywords:
      'wedding venue business plan, event venue business plan, how to start a wedding venue, wedding venue startup costs, venue rental agreement, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-wedding-venue-business-plan.jpg',
  },

  schema: {
    productName: 'Wedding Venue Business Plan Kit',
    productDescription:
      'Wedding venue business plan template kit for a barn or estate event venue with an exclusive caterer: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a pricing and quote calculator by season and day, venue rental agreement templates for couples, corporate clients and the exclusive caterer, and an 84-task startup checklist in 6 phases covering zoning, permits and the build-out. Set up for the US, with notes for the UK.',
    price: '49.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Wedding Venue Business Plan Kit',
  },

  images: {
    // hero bg (6) — el montaje de la mesa imperial bajo los olivos, con la casa y las luces al fondo (ES -hero) abre.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-finca-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-ceremonia.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-banquete.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-cocina.jpg',
    ],
    // strip del ContentGrid (6): el plan entra en lugar del hero; el resto, en otro orden.
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-finca-banquete.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-ceremonia.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-cocina.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-finca-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-finca-banquete.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-finca-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready wedding venue business plan: Word + Excel + pricing calculator + rental agreements',
    titlePre: 'Wedding Venue ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for an Event Venue with an Exclusive Caterer: Word Plan + Excel Projections + Pricing Calculator + Venue Rental Agreements + Startup Checklist',
    description:
      `Everything you need to plan, finance and pitch a wedding and event venue on a leased barn or estate property, earning a venue rental fee plus a commission from its exclusive caterer: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in events, 12-month cash flow and loan payments from your own numbers; a pricing calculator that quotes any date by season and day of the week; venue rental agreement templates for couples, corporate clients and the exclusive caterer; and an 84-task checklist that takes you from your LLC and the zoning check to your first season of events. Set up for the US, with notes for the UK.`,
    checkItems: [
      '10-section wedding venue business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in events and 12-month cash flow',
      'Pricing & quote calculator: season, day of the week, retainer and cancellation schedule',
      'Venue rental agreement templates: couples, corporate clients and exclusive caterer',
      'Startup checklist: 84 tasks in 6 phases, from your LLC to your first season',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $49',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      `What's inside your Wedding Venue Business Plan Kit: 9 building blocks to test whether your venue works on paper before you sign a lease or start the build-out, price every Saturday, and present the plan to a lender or an investor.`,
    templates: [
      { icon: 'FileText', title: 'Wedding Venue Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a barn or estate event venue on a leased property with an exclusive caterer: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan (tours, bookings, event days and the caterer), management and staffing, financial plan, legal requirements, permits and licenses (conditional use permit, occupancy, fire code, ADA, septic), and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Wedding Venue Financial Projections (Excel, 9 Sheets)', desc: `Is a wedding venue profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than ${CASO.formulas} linked formulas: change events per year, guests per event or revenue per guest and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Wedding Venue Pricing & Quote Calculator (Season, Day, Retainer & Cancellation Schedule)', desc: `Wedding venue pricing from your own rate card. Choose the client (couple or corporate), the event type, the date and the guests: the date sets the season and the day of the week, each with a visible premium or discount, and each season has a guest minimum. Add extras such as the ceremony on site, additional hours, premium decor or the rehearsal the day before and you get the price, sales tax, the total, the payment schedule with due dates, your estimated caterer commission, the event contribution and what you keep if the client cancels. Three worked examples; every rate is an example you replace.` },
      { icon: 'ScrollText', title: 'Venue Rental Agreement Templates (Couples, Corporate Clients & Exclusive Caterer)', desc: `Three editable Word documents with brackets for everything you fill in: a rental agreement for couples and private events, a corporate and organization addendum, and an Exclusive Caterer Agreement with the commission, a monthly statement and an audit right. Retainer, cancellation schedule with a rebooking credit, a booking contingent on permits, rain plan, occupancy, insurance and security deposit. Templates, not legal advice: state law varies, so have a local attorney review them.` },
      { icon: 'Coins', title: 'How Much Does It Cost to Start a Wedding Venue? Line by Line', desc: `Architect and code consultant drawings, the conditional use permit and its studies, the barn renovation, a fire sprinkler system, ADA-compliant restrooms, electrical and emergency lighting, a standby generator, HVAC, the caterer's prep kitchen, tables and chairs for 200, the ceremony site, sound, parking and landscaping, brand and launch, each with a reference price you replace with your quotes, plus a lease security deposit, rent before opening, a build-out contingency and working capital. Sprinklers, septic and accessibility drive the budget, and the notes say so.` },
      { icon: 'TrendingUp', title: 'Break-Even in Events + 3 Scenarios', desc: `How many events a year you need at your average guests and revenue per guest to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance: honest about what a slow first season does to your cash.` },
      { icon: 'Users', title: 'Staffing & Seasonal Labor (6 Roles)', desc: `Owner and GM who sells and gives tours, a seasonal venue coordinator, facilities and grounds, event attendants, a part-time weekend sales role and housekeeping, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the hours you hire against the hours you need and flags any pay below the minimum wage.` },
      { icon: 'ShieldCheck', title: 'Startup Checklist (84 Tasks, 6 Phases)', desc: `Business setup (LLC, EIN, state payroll accounts, business license, sales tax permit and your loan package), zoning and permits (the zoning check before you sign, a lease contingent on the conditional use permit, the fire marshal and the building official in writing, septic and well checked by an engineer), build-out and equipment, staff and caterer (seasonal W-2 offer letters, the exclusive caterer agreement, certificates of insurance), brand and bookings (website, listings, bridal shows, open house, pricing guide, the rental agreement) and your first season of events.` },
      { icon: 'Banknote', title: 'Financing Plan', desc: `Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25x target, plus investors or partners as other sources of funds, and a warning if your sources don't cover the cash you need.` },
    ],
  },

  why: {
    subtitle:
      `Not another generic template: a wedding venue plan written for the format lenders expect, with a financial model, a pricing calculator and the rental agreements that recalculate from your own numbers.`,
    reasons: [
      { icon: 'Map', title: 'Built for a Barn or Estate Wedding & Event Venue with an Exclusive Caterer', desc: `A leased barn or estate 30 to 60 minutes from a mid-size city, a hall for 200 seated guests, an outdoor ceremony site, a bridal suite and a prep kitchen for the caterer. The venue earns a venue rental fee and event services plus a caterer commission; it has no kitchen crew and sells no alcohol. How much does it cost to start a wedding venue? The barn conversion, the sprinklers and the restrooms, line by line. Nothing to strip out from a restaurant or catering template.` },
      { icon: 'ShieldCheck', title: 'Zoning and Permits: CUP, Assembly Occupancy, Fire Code and ADA', desc: `Events on farm or rural land usually need local approval before the first booking. The plan and the checklist walk you through the conditional use permit, the change of occupancy to assembly use, the fire marshal's occupant load and sprinkler question, ADA and septic, tell you to ask your county in writing before you sign the lease, and make the lease contingent on the permit. They do not promise that any permit will be granted.` },
      { icon: 'Users', title: 'Exclusive Caterer, Preferred Vendors or In-House Catering: How the Venue Gets Paid', desc: `The example runs on an exclusive caterer who holds the license and pays you a commission on its food and beverage sales. The plan explains the preferred vendor list and in-house catering as alternatives, and the agreement templates include the commission, a monthly statement and an audit right.` },
      { icon: 'BarChart3', title: 'Is a Wedding Venue Profitable? Saturdays, Bookings and Real Margins', desc: `The example: ${CASO.eventos} events a year averaging ${CASO.invitados} guests at ${CASO.ticket} of venue revenue per guest, ${CASO.ventas} in year-1 sales, ${CASO.netoPct1} net in year 1 rising to ${CASO.netoPct3} by year 3, a loan covered ${CASO.dscr} in the toughest year, and about ${CASO.equilibrio} events to break even. It is a venue with rent and debt, not an owned property with no loan, and the plan shows what a slow season does to your cash. Replace the numbers with yours.` },
      { icon: 'Layers', title: 'Venue Rental Agreement: Retainers, Cancellations and What Courts Won\'t Enforce', desc: `A retainer applied to the price, a cancellation schedule written as a reasonable estimate of your loss, a rebooking credit and a full refund if you cancel: the pattern that holds up better than a bare "non-refundable". Templates, not legal advice; have a local attorney review them.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    `CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening restaurants, caterers and event venues, combining hands-on operations with financial planning.`,
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      `Besides the business plan, the financial model, the calculator, the agreements and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves`,
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Wedding Venue Zoning, Permits & Fire Code Guide (US + UK Notes)',
        desc: `Section 9 of the plan plus Phase 2 of the checklist: the zoning check before you sign, a lease contingent on the conditional use permit, change of occupancy to assembly use and the certificate of occupancy, the questions to put to your building official and fire marshal in writing (occupant load, sprinklers, exits, restrooms, tents), ADA, septic and well, who holds the liquor license, sales tax on venue charges, insurance and certificates, and seasonal W-2 staff, with notes for the UK. No county forms included: requirements vary by state, county and city.`,
        image: '/lovable-uploads/ai-gallery/plan-finca-ceremonia.jpg',
      },
      {
        icon: 'BarChart3',
        title: 'US Wedding Venue Benchmarks (Sourced)',
        label: 'BONUS 2',
        desc: `The reference table inside the workbook: venue rental fee ranges from published rate cards, the event mix of the example, the caterer commission, the Saturday ceiling, booking lead times, sales tax on venue charges, noise and curfew conditions and sprinkler rules, each with its source or marked "kit estimate" when there isn't one, plus traffic-light checks on your P&L against editable thresholds.`,
        image: '/lovable-uploads/ai-gallery/plan-finca-plan.jpg',
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
    ctaLabel: 'YES, I WANT THE PLAN — $49',
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
    headingGold: 'Wedding Venue',
    subtitle:
      `Plan it before you sign the lease and start the build-out: the written plan, the numbers behind it, the price of every Saturday and the agreements, for a one-time payment.`,
    items: [
      '10-section wedding venue business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in events, with a sensitivity table',
      'Pricing & quote calculator by season and day',
      'Venue rental agreement templates: couples, corporate and exclusive caterer',
      'Startup checklist: 84 tasks in 6 phases',
      'BONUS: Wedding Venue Zoning, Permits & Fire Code Guide (included in the plan)',
      'BONUS: US Wedding Venue Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $49',
  },

  pricing: {
    price: '$49',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'WEDDING VENUE BUSINESS PLAN — $49',

  // Salientes: Catering, BBQ Catering, Paella Catering y Mobile Bar (los negocios que llevan el servicio al evento; el
  // exclusive caterer del venue puede ser uno de ellos), Catering Checklists (rutinas), Restaurant Business Plan y el resto.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/catering-business-plan', label: 'Catering Business Plan Kit' },
    { href: '/en/digital-products/bbq-catering-business-plan', label: 'BBQ Catering Business Plan Kit' },
    { href: '/en/digital-products/paella-catering-business-plan', label: 'Paella Catering Business Plan Kit' },
    { href: '/en/digital-products/mobile-bar-business-plan', label: 'Mobile Bar Business Plan Kit' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/hotel-checklist-templates', label: 'Hotel Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'New product · Version 2.2 · October 2026',

  alreadyBought: {
    product: 'wedding-venue-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
