// astro-site/src/data/productos-en/planes/bar-business-plan.ts
// TIENDA INTERNACIONAL EN — Bar Business Plan Kit. DUPLICADO de restaurant-business-plan.ts (hermano más cercano:
// mismo tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos) con el
// copy del Bar. Edición inglesa del ES astro-site/src/data/productos/planes/plan-negocio-tapas-bar.ts.
// SPEC: scripts/productos-digitales/business-plans-en-3/SPEC-delta.md (D48-D65) + las heredadas
//   business-plans-en-2/SPEC-delta.md (D30-D47) y business-plans-en/SPEC.md (D1-D29), que mandan en lo demás.
//   · D48/D48b: slug `bar-business-plan`, nombre «Bar Business Plan Kit», H1 Forma B `Bar ` + oro `Business Plan` +
//     «Template for a Neighborhood Bar with Small Plates: …». Keyword principal «bar business plan» (1.900/mes US).
//   · D49: $39, SIN anclas (sin priceOld, «-70%», «Total value», «Save $», «launch price» ni valor de los bonos):
//     el mismo patrón que dejó en main el commit a4cc7a14 en las otras 10 landings EN.
//   · D50: los 3 ficheros de dl/bar-business-plan/ (dashboard BarBusinessPlanDashboard.tsx y get-download-urls.ts).
//   · D62: tarjeta DOCX la primera del grid; bonos sin precio (1 = §9 del plan + fases 1 y 2 del checklist, que en el
//     Bar son las de licencias; la fase 6 es «First 90 Days»; 2 = §3 + tabla D19); la tabla de referencias no se
//     cuenta dos veces (la tarjeta del grid se queda en «Instructions & Ratio Checks»). Sin aggregateRating ni review.
//   · Cifras: SOLO datos estables del producto (3 ficheros, 10 secciones, 9 hojas, >700 fórmulas, 73 tareas en 6
//     fases, 7 puestos, umbrales D56, DSCR 1.25× de la SPEC) y rangos de mercado con su fuente del research
//     (F1-research-us-delta.md §4-§5). NINGUNA cifra del caso (ventas, inversión, break-even, DSCR, payback): la
//     revisión adversarial de los entregables puede moverlas.
//   · Testimonios (D26 / riesgo §8.3): los 8 del ES traducidos con el subtítulo de la edición española y SIN ningún dato
//     que no sea verdad en este kit: fuera «préstamo ICO», «120K EUR», «34 clientes», «food cost 28-32 %», «63
//     trámites» y el superlativo de David Torres. Se conservan las experiencias personales sin cifras de producto.
//   · FAQ: People Also Ask de research §3 (qué incluye, coste, ¿con $100k?, cuánto gana el dueño, bar vs restaurante,
//     ¿es rentable?, por qué cierran —sin tasa—, licencia, liquor liability) + cómo abrir, tipos de bar, prestamista,
//     cambiar cifras, UK, moneda, suscripción, licencia de uso y garantía. schema.faqs = el MISMO array.
//   · Imágenes: las del ES (plan-tapas-bar-*) son miniaturas de 400 px con rótulos en español («TAPAS», «VERMUT»,
//     «TABERNA ALMA MADRID»): se usan las fotos sin texto del Kit de Tareas Bar (tareas-bar-*, 1376 px) + la cocina de
//     los usos (use-case-casual-kitchen, sin rótulos). OG = recorte 1200×630 de tareas-bar-cristaleria.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_BAR_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env var el
// CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// FAQ on-page Y FAQPage (un solo array).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What should a bar business plan include?',
    a: 'The sections lenders, landlords and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits (for a bar, above all the liquor license), and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a neighborhood bar with small plates, plus the Excel financial projections that back them up and a 73-task opening checklist.',
  },
  {
    q: 'Is it a generic plan or built for a bar?',
    a: 'Built for a neighborhood bar where drinks bring in most of the sales and a short kitchen serves small plates (tapas-style): the bar build with underbar stations, a draft beer system, back-bar coolers, glassware, a griddle, fryer and oven, a Type I hood and grease interceptor, the patio and the liquor license in the startup costs; food and beverage sales with the alcohol share in the P&L; seven roles on the staffing sheet (owner / general manager, kitchen lead, bartenders, servers for the floor and patio, line / prep cook, barback / weekend extra and relief cover); and the permits of a bar that serves food.',
  },
  {
    q: 'How much does it cost to open a bar?',
    a: "It depends on the space and the liquor license more than on anything else. Restaurant365 puts the range at $100,000 to $850,000 or more, and a RestaurantOwner.com survey quoted by Poster found $110,000 to $550,000 for a bar in a leased space, with an average of $425,500. A second-generation space that was already a bar or restaurant, with its hood and grease interceptor in place, needs a fraction of the build-out of an empty shell; in a state with a license quota, the liquor license alone can cost more than the build-out. The Startup Costs sheet lists every line — LLC and legal, liquor license and local permits, architect and permit fees, build-out, electrical and HVAC, plumbing, hood and grease interceptor, kitchen equipment, refrigeration, the bar build, the draft beer system, furniture, patio, glassware, decor and sound, signage, launch marketing, opening inventory and POS — plus deposit, rent before opening, contingency and working capital, and calculates the total cash you need. Replace each line with your own quotes.",
  },
  {
    q: 'Can you open a bar with $100k?',
    a: "It's tight, and in most cities it means compromises: a beer and wine license instead of full liquor (from about $3,000, according to Poster), a second-generation space that needs little build-out, used equipment and a smaller room. Most surveys put a bar in a leased space above that figure, and you still need a cash reserve for the first months. Type your own numbers into the workbook: it recalculates the total cash you need and warns you if your sources of funds don't cover it.",
  },
  {
    q: 'How much does a bar owner make?',
    a: "There's no reliable typical figure: it depends on sales, the mix of drinks and food, pour cost, rent and how much of the work the owner does. The workbook doesn't promise an income. It budgets the owner / general manager as a salaried role on the staffing sheet and then calculates the net income left over in a 3-year P&L, so you can see both before you sign a lease — and check the pessimistic scenario, not only the base case.",
  },
  {
    q: 'Is a bar more profitable than a restaurant?',
    a: "Per dollar of sales it often is, because drinks cost less than food: BevSpot puts a typical whole-bar pour cost at 18-24% of the price, while food usually costs 25-35% of its price. But a bar carries costs a restaurant may not — a liquor license that can be the biggest startup line in a quota state, liquor liability insurance, late hours and security — and its sales depend on a few busy nights a week. If most of your sales will be food, the Restaurant Business Plan Kit is built for that.",
  },
  {
    q: 'Is owning a bar profitable?',
    a: 'It can be, if three lines stay under control: pour cost, labor and rent. The model checks your P&L against editable kit benchmarks — gross margin of at least 68%, cost of goods up to 28%, labor up to 35%, rent up to 10% and net margin of at least 5% — and marks each one OK or REVIEW. It also runs three scenarios (pessimistic, base and optimistic), so you can see whether the plan still works in a slow year before you sign a lease.',
  },
  {
    q: 'Why do so many bars fail?',
    a: "Usually for the same few reasons: running out of cash before the bar finds its regulars, a pour cost or labor cost that's too high for the sales it actually makes, a concept or location the neighborhood doesn't support, and opening dates that slip because the liquor license took longer than planned. Each one has a check in the kit: the 12-month cash flow shows your lowest cash balance and the month it happens, the benchmarks flag the cost lines out of range, the break-even sheet tells you how many guests a day you need and your cushion above that point, and the checklist has you apply for the liquor license right after signing the lease.",
  },
  {
    q: 'How much does a liquor license cost?',
    a: "It depends entirely on your state and city. Poster puts a beer and wine license from about $3,000 and a full liquor license at $12,000 to $400,000. In states that cap the number of licenses you usually buy or transfer an existing one at market price: R Street reports bar licenses in Boston selling for north of $450,000. The kit's startup costs include a liquor license and local permits line with an example for a state without a quota, and a note to replace it with your state's fees or the market price of a transfer. It often takes 3 to 12 months, so the checklist has you apply right after signing the lease.",
  },
  {
    q: 'Do I need liquor liability (dram shop) insurance?',
    a: "In practice, yes. Under dram shop laws a bar can be held responsible for harm caused by a guest who was served while visibly intoxicated or underage, and liquor liability insurance covers that risk. Insureon reports a median of $2,039 a year for small bars; bigger venues pay more. The workbook has an insurance line for general liability, liquor liability and property together, and the checklist includes the policy and responsible beverage service training (TIPS or ServSafe Alcohol), which many states and insurers require.",
  },
  {
    q: 'How do I open a bar, step by step?',
    a: "Test the numbers before you look at spaces, check the zoning before you sign a lease, form your LLC and get your EIN, seller's permit and business license, and apply for your liquor license right after signing. Then go through the architect's drawings, building permits and health department plan review before the build-out, install the hood, grease interceptor and draft system, hire and train your team (responsible beverage service included), open your distributor accounts, get your music licenses and open with a soft opening. The opening checklist organizes those steps into 73 tasks in 6 phases, from business setup to your first 90 days.",
  },
  {
    q: 'Does it work for a wine bar, cocktail bar or sports bar?',
    a: "Yes, with your own numbers. The green cells set the food and beverage mix, the alcohol share, the cost of each, the average check, guests per day and every startup cost line, so a wine bar, a cocktail bar or a sports bar fits the same model. The written plan describes a neighborhood bar with small plates, so you'll adapt the concept, menu and marketing text. It isn't built for a nightclub (door staff, DJ and capacity drive that model) or for a brewery that brews its own beer (that needs its own federal and state permits).",
  },
  {
    q: 'Does it work for a mobile bar or a bartending service?',
    a: "It's built for a bar with its own premises, its own liquor license and a kitchen. If you'll take the bar to weddings, corporate events and private parties instead — a bar trailer or a portable bar, with the host buying the alcohol (dry hire) — our Mobile Bar Business Plan Kit is written for that: no storefront and no alcohol inventory, a storage unit for the trailer, a break-even in events per year, W-2 event bartenders, the dry hire rules state by state and a pricing calculator from cost per guest to quote.",
  },
  {
    q: 'Can I present this plan to a lender, a landlord or investors?',
    a: "Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The loan schedule and the DSCR cover your main loan (bank or SBA 7(a)), the one you enter in the assumptions; the financing sheet also lists an SBA Microloan (up to $50,000, through nonprofit intermediaries), investors or partners and local grants as sources of funds, without amortizing them. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.",
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: "Yes. The green cells are the ones you type — rent, guests per day, average check, the food and beverage mix, food cost and pour cost, wages and any startup cost line — and more than 700 linked formulas recalculate the rest. Tips aren't modeled: bartenders, barbacks and servers are budgeted at a full base wage, which keeps the plan on the safe side. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook includes an Instructions tab.",
  },
  {
    q: "Does it work in the UK, Canada or Australia?",
    a: "Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type the average check without it. The UK notes cover the premises and personal licences (England and Wales), council food registration and the 14 allergens. In Canada, liquor licences are provincial and servers need Smart Serve, Serving It Right or the local equivalent; in Australia, a state liquor licence and RSA for staff who serve. Check with your council, province or state. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
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
    q: 'Can I use it for several locations or with my clients?',
    a: "One purchase covers one business, with all of its locations. If you're a consultant or an investor, you can use the files with the projects you advise, but you can't hand them copies: each business buys its own.",
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the plan doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: PlanNegocioData = {
  slug: 'bar-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_BAR_BUSINESS_PLAN',

  seo: {
    title: 'Bar Business Plan Template: Word + Excel Financial Projections + Opening Checklist | AI Chef Pro',
    description:
      'Bar business plan template for a neighborhood bar with small plates: a 10-section Word plan, Excel financial projections (3-year P&L, break-even, cash flow, loan and DSCR) and a 73-task opening checklist, liquor license included. $39.',
    keywords:
      'bar business plan, bar business plan template, how to open a bar, bar startup costs, how much does it cost to open a bar, liquor license cost, liquor liability insurance, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-bar-business-plan.jpg',
  },

  schema: {
    productName: 'Bar Business Plan Kit',
    productDescription:
      'Bar business plan template kit for a neighborhood bar with small plates: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions) and a 73-task opening checklist in 6 phases, liquor license included. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Bar Business Plan Kit',
  },

  images: {
    // hero bg (6) — fotos sin texto del Kit de Tareas Bar + la cocina de los usos (sin rótulos). Las plan-tapas-bar-*
    // del ES son miniaturas de 400 px con rótulos en español.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      '/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el ES.
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      '/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
  },

  hero: {
    badge: 'Lender-ready bar business plan: Word + Excel + checklist',
    titlePre: 'Bar ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for a Neighborhood Bar with Small Plates: Word Plan + Excel Financial Projections + Opening Checklist',
    description:
      'Everything you need to plan and pitch a neighborhood bar where drinks lead and a short kitchen serves small plates: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even, 12-month cash flow and loan payments from your own numbers, with food cost and pour cost kept apart; and a 73-task checklist that puts the liquor license on the critical path, right after you sign the lease. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section bar business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even and 12-month cash flow',
      'Startup costs line by line, from the bar build and draft system to the liquor license',
      'Opening checklist: 73 tasks in 6 phases, liquor license first',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      '9 building blocks to test whether your bar works on paper before you sign a lease, and to present it to a lender, a landlord or an investor.',
    templates: [
      { icon: 'FileText', title: 'Bar Business Plan (Word, 10 Sections)', desc: 'A complete plan of more than 7,000 words already written for a neighborhood bar with small plates: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan (pour cost and bar inventory control included), management and staffing, financial plan, legal requirements, permits and licenses, and conclusions with an action plan. Its figures are the ones in the example Excel model.' },
      { icon: 'FileSpreadsheet', title: 'Bar Financial Projections (Excel, 9 Sheets)', desc: 'Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than 700 linked formulas: change a green cell and the whole workbook recalculates.' },
      { icon: 'Coins', title: 'Startup Costs Line by Line', desc: 'LLC and legal, liquor license and local permits, architect and permit fees, build-out, electrical and HVAC, plumbing with grease interceptor and Type I hood, kitchen equipment (griddle, fryer, oven), walk-in and back-bar coolers, the bar build with underbar stations, a draft beer system, tables, high-tops and bar stools, patio, glassware, decor, lighting and sound, signage, launch marketing, opening inventory (liquor, beer, wine and food) and POS, each with a reference price you replace with your quotes, plus deposit, rent before opening, contingency and working capital. The total cash you need is calculated separately.' },
      { icon: 'TrendingUp', title: 'Break-Even Point', desc: 'How many guests (covers) a day you need at your average check (excl. sales tax) and the seat turns that implies, plus the cash break-even with loan payments in and depreciation out. Your cushion above the cash break-even, a sensitivity table for average check and variable cost, and a plain-English reading of the result.' },
      { icon: 'BarChart3', title: 'Financial Scenarios', desc: 'Three scenarios side by side — pessimistic, base and optimistic — each with its own estimated cash balance. Useful for a lender, a landlord or an investor.' },
      { icon: 'Users', title: 'Staffing & Payroll Costs', desc: "Seven roles — owner / general manager, kitchen lead, bartenders for the peak shifts, servers for the floor and patio, line / prep cook, barback / weekend extra and relief cover — with gross pay, employer payroll taxes, the real cost of each role, the team's full-time equivalents and two alerts: pay below the minimum wage for the hours worked, and service hours left uncovered. Tips aren't modeled: bartenders, barbacks and servers are budgeted at a full base wage." },
      { icon: 'ShieldCheck', title: 'Opening Checklist (73 Tasks, 6 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license, health permit application), location and licenses (zoning check, lease, the liquor license application right after signing, patio and entertainment permits, liquor liability insurance, noise check), build-out and equipment (plan review, Type I hood, grease interceptor, draft system), staff (responsible beverage service training included), marketing (distributor accounts and music licenses included) and your first 90 days." },
      { icon: 'ListChecks', title: 'Instructions & Ratio Checks', desc: 'An Instructions tab that explains every sheet and which cells to type, plus five checks on the P&L — gross margin, cost of goods, labor, rent and net margin — each marked OK or REVIEW against an editable kit benchmark.' },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25× target, plus an SBA Microloan, investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Tapas Bar, la edición española. Sin ningún dato
  // que no sea verdad en este kit (ver cabecera). Solo se pintan.
  testimonials: {
    subtitle:
      'Owners and investors who opened their bar with the Spanish edition of this plan',
    items: [
      { name: 'Alejandro Ruiz', role: 'Tapas bar owner, Madrid, Spain', text: 'The financial plan helped me get my bank loan in Spain. The breakdown of startup costs for the kitchen and the bar was spot on, with no surprises.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Gastrobar founder, Barcelona, Spain', text: 'The opening checklist was key. I found out that my kitchen needed a different activity license in Spain than the one I had planned for. It saved me months of delays and fines.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Hospitality investor', text: 'The break-even in guests per day is realistic for a well-located tapas bar, and the margins on tapas and drinks give me a lot of confidence to invest.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Gastrobar partner, Seville, Spain', text: 'The financial scenarios gave me the confidence I needed. I knew exactly the minimum sales to be profitable and how far it could go if everything went well.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Hospitality consultant', text: 'I recommend it to every client who wants to open a tapas bar or a gastrobar.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Tapas bar owner, Valencia, Spain', text: 'The food cost ratios for tapas and the drink margins saved me a lot of money. I knew exactly where the profit was before I opened.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex-executive who opened a gastrobar', text: 'I knew nothing about kitchen exhaust or activity licenses in Spain. The checklist guided me step by step through every procedure, and I opened without a single legal problem or delay.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Owner of a group of 4 gastrobars', text: 'I have used this plan for the openings of all 4 of my gastrobars. You change the numbers for each location and you have a professional business plan ready to present.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a bar plan written for the format lenders expect, with a financial model that recalculates from your own numbers.',
    reasons: [
      { icon: 'Wine', title: 'Built for a Bar with Small Plates', desc: 'A bar build with underbar stations, a draft beer system and back-bar coolers; a short kitchen with griddle, fryer and oven, Type I hood and grease interceptor; food and beverage sales with the alcohol share; seven roles from bartenders to barback; and the permits of a bar that serves food, liquor license first. Nothing to strip out from a generic template.' },
      { icon: 'BarChart3', title: 'Pour Cost and Margins Calculated, Not Copied', desc: 'Average check, food cost, pour cost, gross margin and break-even come out of the workbook itself, from your assumptions. Food and beverage costs are kept apart, because in a bar the pour cost decides the margin, and five ratio checks flag what is out of range. Replace the example figures with yours.' },
      { icon: 'ShieldCheck', title: 'Liquor License First, Then 73 Tasks', desc: 'Zoning before you sign, the liquor license application right after, liquor liability insurance, building permits and health plan review, hood and fire inspections, music licenses, responsible beverage service training and employer registrations. A starting point: requirements vary by state, county and city.' },
      { icon: 'Banknote', title: 'Lender-Ready Format', desc: 'Written plan, 3-year P&L, break-even, 3 scenarios, cash flow and a loan schedule with DSCR for your main loan (bank or SBA 7(a)), with SBA Microloans and grants as other sources. Approval is never guaranteed, and it is a planning tool, not financial advice. One-time payment, no subscription.' },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised entrepreneurs, investors and owners on opening bars and restaurants, combining hands-on operations with financial planning.',

  bonus: {
    subtitle:
      'Besides the business plan, the financial model and the opening checklist, you get these extra resources, plus a licensing guide drawn from the plan itself',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Bar Licensing & Liquor License Guide (US + UK Notes)',
        desc: 'Section 9 of the plan plus Phases 1 and 2 of the checklist: what a bar that serves food usually needs and in what order — zoning check before you sign, the liquor license (state agency and local approval, beer and wine vs full liquor, quota states, typical timelines), dram shop liability and liquor liability insurance, responsible service, health department plan review and permit, building permits and certificate of occupancy, hood and grease interceptor, music licenses and entertainment permits — with notes for the UK. No state forms included: requirements vary by state, county and city.',
        image: '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
      },
      {
        icon: 'BarChart3',
        label: 'BONUS 2',
        title: 'US Bar Industry Benchmarks (Sourced)',
        desc: 'The market section of the plan plus the reference table inside the workbook: pour cost for the whole bar and for beer, spirits and wine, food cost, labor, rent, prime cost, startup costs for a leased bar, the liquor license, liquor liability insurance and the operating cash reserve, each with its source or marked "kit estimate" when there isn\'t one. Compare them with your own numbers before you talk to a lender.',
        image: '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      },
      {
        icon: 'Globe',
        label: 'BONUS 3',
        title: 'US · UK · Canada · Australia Equivalents Guide',
        desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.',
        image: '/lovable-uploads/ai-gallery/en-equivalents-guide.jpg',
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
    headingPre: "It's Time to Open Your ",
    headingGold: 'Bar',
    subtitle:
      'Test it on paper before you sign the lease: the written plan, the numbers behind it and the licensing path, liquor license first, for a one-time payment.',
    items: [
      '10-section bar business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in guests a day, with a sensitivity table',
      '3 financial scenarios (pessimistic, base, optimistic)',
      'Opening checklist: 73 tasks in 6 phases',
      'BONUS: Bar Licensing & Liquor License Guide (included in the plan)',
      'BONUS: US Bar Industry Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'BAR BUSINESS PLAN — $39',

  // D64: salientes al hermano (Restaurant), Financial Plan, Inventory (stock de barra), Staff Scheduling, Food Cost
  // (pour cost) + los otros planes EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/bar-checklist-templates', label: 'Bar Checklists Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/catering-business-plan', label: 'Catering Business Plan Kit' },
    { href: '/en/digital-products/mobile-bar-business-plan', label: 'Mobile Bar Business Plan Kit' },
    { href: '/en/digital-products/food-cost-menu-engineering-guide', label: 'Food Cost + Menu Engineering Guide' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'bar-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
