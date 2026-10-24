// astro-site/src/data/productos-en/tareas/chocolate-shop-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Chocolate Shop Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-chocolateria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// restaurant-, bar-, coffee-shop-, catering-, pizza-shop-, burger-joint-, ghost-kitchen- e ice-cream-shop-checklist-
// templates.ts. SPEC: scripts/productos-digitales/checklists-kit/chocolate/SPEC.md (delta) + la base.
//   · D2: nombre «Chocolate Shop Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Chocolate Shop Checklists Kit Pro: Opening, Closing & Tempering Templates». Demanda US (SPEC §R): bonbons 90.500/mes,
//     chocolate shop 49.500, chocolatier y chocolate truffles 27.100, chocolate tempering / molds / store 9.900: en
//     keywords y FAQ.
//   · D5: títulos de las 9 plantillas y los 2 bonus = los de los xlsx EN (chocolate/SPEC §2,
//     dl/chocolate-shop-checklist-templates/).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos (el ES los «valora en €33»). Fórmula de la tienda EN.
//   · Cifras SOLO de los xlsx EN de la F2 (chocolate/F2-NOTAS.md, tabla «Cifras para la landing», y
//     chocolate/revision/dump_en.txt tras la ronda 1): 338 tareas en 37 hojas (25 + 16 = 41 en el 01; 19 + 22 = 41 en el
//     02; 15 + 20 + 12 = 47 en el 03; 16 + 16 + 12 = 44 en el 04; 20 + 14 + 14 = 48 en el 05; 15 + 12 + 13 = 40 en el 06;
//     17 + 15 = 32 en el 08 con responsable y hora/«Close»; 13 + 14 = 27 en el 09; 18 en el briefing); 12 meses en el
//     B02. °F = GRADOS_F_SPEC de mapas_chocolate.py: obrador 64–68 °F y 50–60 %, cool room 59–64 °F, vitrina 60–64 °F y
//     < 55 %, tienda 68–72 °F, > 68 °F funde la manteca de cacao, moldes 68–72 °F, enfriado 54–57 °F, nevera 41 °F,
//     curvas de templado (negro 122–131 → 81–82 → 88–90; leche 113–122 → 79–81 → 84–86; blanco 104–113 → 77–79 → 82–84)
//     «typical curve; your couverture's chart rules», temperadora «typically 113 °F», agua de manos 100 °F, hielo 32 °F,
//     granel de ganache a 0 °F. Ronda 1 (F2-NOTAS): ganache de nata fresca = TCS salvo análisis de aw y pH → nevera o
//     vitrina refrigerada a 41 °F, 7 días (3-501.17), nunca en la vitrina de 60–64 °F ni en la cool room; contacto cruzado
//     (pinzas por bandeja, frutos secos y cacahuete al final, temperadora limpia de leche a negro); exclusión por síntomas
//     (2-201.11/12); licor > 0,5 % solo donde el estado lo permite. Food cost 30–35 % = criterio del kit (03 «Weekly
//     Tasks», Friday).
//   · Lo que el ES afirma y el kit no trae, fuera: «software de gestión €40/mes» y «sin internet» (→ la fórmula de los
//     hermanos), «Imprimible A4» (→ US Letter), DDD / BIE / legionela / «SAT de cámaras» (→ servicios contratados US,
//     D11), Reyes, comuniones, 15 de agosto, Todos los Santos y «puente de diciembre» del calendario (→ fechas US, D14),
//     «moldes» en el inventario SEMANAL (el EN los cuenta en el inventario mensual) y, en el dashboard ES, «15 fechas
//     clave» (son 12 meses).
//   · El parche ES de hoy (938e15e3: ganache de nata fresca en frío) NO se toca en la ficha ES (gate de ES idénticas). La
//     ficha ES no daba cifras de vida útil ni temperaturas de vitrina, así que no queda contradicción en su copy.
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD (el ES trae 4,9 y 3 reviews: fuera). Testimonios: los 8 del ES
//     traducidos tal cual (nombres, negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5).
//     Solo se pintan. Ninguno cita una marca o persona real (SPEC §R) ni contradice el kit EN (Sergio Herrera: el 03 sí
//     trae el seguimiento de mermas y el food cost; Andrés Beltrán: las ferias están en septiembre del B02 y en el 06).
//   · Imágenes: las 6 del ES llevan texto o marcas ajenas (hero y vitrina: «Atelier du Chocolat», marca real de una cadena
//     francesa, con rótulos en francés mal escritos; obrador: la marca Selmi y «OBRADOR ARTESÀ»; equipo: el logo «Gami»
//     en la temperadora; servicio: el nombre «Couture Chocolats» en cajas y delantal), salvo «tareas-chocolateria-
//     produccion» (sin texto), que se queda. El resto, fotos YA publicadas en los casos de uso EN de chocolatería y
//     chocolatero, sin español: bombones de colores (hero y OG), vitrina con rótulos en inglés, mesa de templado, relleno
//     de moldes («HANDCRAFTED CHOCOLATES») y bandeja de bombones. OG ES fuera (texto español y «€12»).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'chocolate-shop-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT',

  seo: {
    title: 'Chocolate Shop Checklists Kit Pro: Opening, Closing & Tempering Templates',
    description:
      '11 Excel chocolate shop checklists with 338 tasks already written: opening & closing, tempering, molding, roles, cleaning, holidays, cash count. One-time $19.',
    keywords:
      'chocolate shop checklist, chocolate shop opening checklist, chocolate shop closing checklist, chocolatier checklist, chocolate tempering checklist, chocolate tempering, bonbons, chocolate truffles, chocolate molds, chocolate store checklist, chocolate shop cleaning checklist, chocolatier duties, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/use-case-chocolatero-bombones.jpg',
  },

  schema: {
    productName: 'Chocolate Shop Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for chocolate shops and chocolatiers with 338 tasks already written: opening and closing, tempering dark, milk and white chocolate, molding bonbons and bars, manager, duties by role, cleaning, inventory and maintenance schedule, holiday season, Valentine\'s Day and Easter, whole-shop opening and closing, and a cash drawer count with sales by weight.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a chocolate shop opening checklist?',
        a: "One list in order: personal hygiene, the exhaust fan on first, the tempering machine preheated, the cool room (59–64 °F) and the ganache fridge (41 °F or below) checked with each reading logged, the bonbon display case at 60–64 °F before any product goes in, the shop at 68–72 °F, then the display case, gift boxes, the sample station and the allergen notice on every tray, and the register. Every task has columns for the area, who does it, a check mark and the time.",
      },
      {
        q: 'What goes on a chocolate shop closing checklist?',
        a: "Product out of the display case and back to the cool room (fresh-cream items to the fridge at 41 °F or below), the counter cleaned and sanitized, the tempering machine and molds cleaned, open couverture sealed, closing temperatures and the day's waste logged, then the equipment off except the cool room and fridges, and the alarm. The whole-shop checklist turns the display cases off only once the product is stored and locks up last.",
      },
      {
        q: 'Does it cover tempering dark, milk and white chocolate?',
        a: "Yes. The tempering sheet checks couverture stock and the kitchen air (64–68 °F, 50–60% humidity) before you start, then runs the typical curve for each chocolate (dark: melt to 122–131 °F, cool to 81–82 °F, work at 88–90 °F; milk and white with their own), a temper test and a batch log. Your couverture maker's curve always comes first.",
      },
      {
        q: 'Is there a free chocolate shop checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 338 chocolate shop tasks already written, a counter that skips N/A tasks, °F temperatures, tempering curves, a shelf-life table and a cash count in US dollars. Print it or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, temperatures in °C, fresh-cream items chilled at 8 °C or below and information on the 14 allergens; in Canada and Australia, your local temperatures and allergen list; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Chocolate Shop Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid: fotos sin texto en español ni marcas ajenas (ver cabecera). Mismo reparto que
    // el ES: why = obrador (mesa de templado), buyBox = producción, cta = hero.
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-chocolatero-bombones.jpg',
      '/lovable-uploads/ai-gallery/use-case-chocolateria-display.jpg',
      '/lovable-uploads/ai-gallery/use-case-chocolateria-obrador.jpg',
      '/lovable-uploads/ai-gallery/use-case-chocolateria-team.jpg',
      '/lovable-uploads/ai-gallery/tareas-chocolateria-produccion.jpg',
      '/lovable-uploads/ai-gallery/use-case-chocolateria-bonbons.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-chocolateria-obrador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-chocolateria-produccion.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/use-case-chocolatero-bombones.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Chocolate Shop Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Chocolate Shop Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Opening, Closing & Tempering Templates',
    description:
      "9 templates + 3 bonuses (12 files) in Excel with 338 chocolate shop tasks already written: opening and closing, tempering and molding, manager, roles, cleaning and inventory, holiday season, Valentine's Day, Easter and a cash drawer count with sales by weight. Print it, delegate it to your team, check it off and file it.",
    checkItems: [
      'Production: tempering dark, milk and white, molding bonbons and bars, wrapping and labels, in °F',
      'Whole-shop opening and closing, and a cash drawer count by bill and coin with sales by the pound',
      'Counter: the display case, gift boxes, samples and the allergen notice on every tray',
      'Roles: chocolatier, sales associate and shift lead',
      'Manager: daily, weekly and monthly checklists, food cost included',
      "Seasons: holiday season, Valentine's Day, Easter and a 12-month holiday calendar",
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS CHOCOLATERÍA — €12»).
  stickyLabel: 'CHOCOLATE SHOP CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '9',
    headingRest: ' Chocolate Shop Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '338 chocolate shop tasks already written and sorted by shift, area and role. Adjust them to your shop, print and delegate.',
    templates: [
      {
        icon: 'CakeSlice',
        title: 'Chocolate Shop Opening & Closing Checklists: Kitchen, Display Case & Counter',
        desc: "2 checklists. Opening: personal hygiene and a safe start (the exhaust fan first and a gas check if you have gas), the tempering machine preheated, the cool room (59–64 °F) and the ganache fridge (41 °F or below) checked with each reading logged, the bonbon display case at 60–64 °F before any product goes in and the shop at 68–72 °F, then the display case, gift boxes, the sample station and the allergen notice on every tray. Closing: product back to the cool room (fresh-cream items to the fridge), the counter cleaned and sanitized, the tempering machine and molds cleaned, closing temperatures and the day's waste logged, and the lock-up. 41 tasks already written in this file alone.",
      },
      {
        icon: 'Beaker',
        title: 'Chocolate Tempering & Molding Checklists: Dark, Milk & White, Bonbons & Bars',
        desc: "Tempering: couverture stock, the kitchen air at 64–68 °F and 50–60% humidity before you start, and the typical curve for dark (122–131 → 81–82 → 88–90 °F), milk and white chocolate, with a temper test and a batch log (your couverture maker's curve rules). Molding & Bars: molds slightly warmer than the room, shells of 1/16–1/8 in, chilling at 54–57 °F, fillings set before capping, nut and peanut bars run last, wrapping and labels with ingredients, allergens and net weight, quality control and batch records. Plus a shelf-life table by product type, with fresh-cream ganache treated as TCS: 7 days at 41 °F unless a lab test says otherwise.",
      },
      {
        icon: 'ClipboardList',
        title: 'Chocolate Shop Manager Checklist: Daily, Weekly & Monthly',
        desc: "Daily (the calendar and pre-orders, production vs. stock, the pre-shift meeting, temperatures, online orders, quality, waste, sales vs. goal and the team's time records), weekly with a focus for each day (planning, quality and date marks, the team, sales, food cost against a 30–35% target and a weekend block for the shop at full speed) and monthly (a full inventory, food cost, supplier invoices, sales by category, team reviews and training, the product of the month and your online reviews).",
      },
      {
        icon: 'Users',
        title: 'Chocolate Shop Duties by Role: Chocolatier, Sales Associate & Shift Lead',
        desc: "Checklists for the chocolatier (the production order, tempering by type, bonbons, bars and molded figures, ganaches and fillings, wrapping and labels, temper and weight checks, and the tempering machine cleaned before switching from milk to dark or white), the sales associate (the display case, tray signs with allergens, samples with one set of tongs per tray, custom gift boxes with gloves or tongs, pre-orders, the counter and the display temperatures) and the shift lead (the opening check, tasks by priority, temperatures, waste and a proper close).",
      },
      {
        icon: 'CalendarDays',
        title: 'Chocolate Shop Cleaning Checklist, Inventory & Maintenance Schedule',
        desc: "Weekly (a deep clean of the tempering machine, marble slab, molds and wrapping surfaces, the shop, display glass and sample area, a stock count of couverture, nuts, fillings, packaging and consumables, and equipment checks, with the retail scale legal-for-trade) and monthly (tempering machine service, A/C filters, thermometers checked in ice water at 32 °F, fire extinguishers, a full inventory against theoretical stock, the pest control plan, recipe cards and labels). + a Quarterly & Annual sheet for contracted services and paperwork: pest control by a licensed operator, lab tests of water activity and pH for each new ganache or filling, food handler cards and a certified food protection manager, tempering and panning machine service, refrigeration by an EPA 608-certified tech, calibration, fire extinguishers, gas, hood cleaning (NFPA 96) only if you cook with grease, insurance with spoilage coverage, your health permit and any state candy manufacturing license, and the POS and sales tax (many states tax candy).",
      },
      {
        icon: 'Gift',
        title: "Chocolate Shop Seasonal Checklists: Holiday Season, Valentine's Day & Easter",
        desc: "Holiday season (Nov–Dec: a catalog with bark, toffee, bonbons, molded figures and Hanukkah gelt, extra couverture and packaging, seasonal staff with the federal limits for minors, pre-sales, the pre-order deadline and your carrier's shipping cutoff, corporate gift sets and orders confirmed in writing with allergens and deposit), Valentine's Day (heart bonbons, bars with an engraved message, premium truffles, gift boxes, the countdown and home deliveries) and Easter (eggs, bunnies and chicks, large filled eggs and centerpieces, Easter baskets, a labeled spring collection and an egg-decorating workshop).",
      },
      {
        icon: 'FileEdit',
        title: 'Blank Chocolate Shop Checklist Template (Editable)',
        desc: '3 blank templates (by area, by shift and by role) with the columns for area, person in charge, ✓, time and notes, and the counter already set up: you just type your tasks.',
      },
      {
        icon: 'Building2',
        title: 'Chocolate Store Opening & Closing Checklist (Whole Shop)',
        desc: "The checklist for the whole shop, not just the kitchen: alarm, lights, HVAC, the security gate, outdoor and pre-order signs (and no direct sun on the store window), the POS, the climate-controlled display cases switched on first thing, today's pre-orders, restrooms, the patio, a price and allergen tag on every tray, and the case (60–64 °F, under 55% humidity) and kitchen readings logged, with due-by times for a shop that opens at 10 AM. At close, in a safe order: the cases off only once the product is back in the cool room, the kitchen temperature logged, the POS, a safety check that never unplugs the cool room, the fridges or a melter, HVAC on night mode (never fully off in warm weather) and the lock-up last. Who does it is filled in for all 32 tasks.",
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Opening and closing count of the cash drawer by US bill and coin (rolls included), starting bank and automatic over/short against the POS Z report, with card tips kept out of sales. For sales by weight: the legal-for-trade scale checked with a test weight, the price per pound matched to the POS and the tray sign, and the pounds sold balanced at close; pre-order deposits are rung as deposits, not sales. Plus a monthly cash log with the over/short by formula for every day of the month.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Chocolate Shop Pre-Shift Meeting Template (Huddle Notes)',
        desc: "Pre-shift huddle template: products to make today, planned bonbons and bars, special pieces, couverture needed by type, the kitchen temperature and humidity at start-up, special and online orders, the team on shift, the featured product, active promotions and the previous shift's issues. Print it and post it in the kitchen and at the counter.",
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Chocolate Shop Holiday Calendar & Product Planner (US)',
        desc: "12 months, each with its key US dates and actions, featured products and the season (peak in February and December): Valentine's Day with a pre-order deadline on the 10th, St. Patrick's Day, Easter, Mother's Day and Teacher Appreciation Week, graduations, Father's Day and weddings, July 4 and summer shipping with cold packs, Labor Day and corporate gifting, Sweetest Day, National Chocolate Day and Halloween, Thanksgiving and Small Business Saturday, Christmas and Hanukkah gelt with your shipping cutoff, plus a UK note.",
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a hospitality consultant since 2010.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Filled for Chocolate Shops',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a chocolate shop that makes its own bonbons and bars. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'CakeSlice',
        title: 'Production and Counter Covered',
        desc: "Tempering, molding, bonbons, bars, the display case, the counter and the manager's numbers: the tasks generic checklist apps don't cover for a chocolate shop.",
      },
      {
        icon: 'Users',
        title: 'Role-Specific Checklists',
        desc: 'Checklists for the chocolatier, the sales associate and the shift lead. Everyone knows exactly what to do.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists chocolate shops run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
      },
    ],
    // Pastillas de los hermanos EN: sin Google Sheets hasta el test real (SPEC base §6, §9); «A4» → US Letter.
    compatLabel: 'Compatible with:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has designed operating systems and checklists for hundreds of restaurants, chocolate shops and production kitchens.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Chocolate Shop Pre-Shift Meeting Template',
        desc: "The 5-minute huddle that makes the difference: today's production, special and online orders, the team on shift, the featured product and active promotions.",
        image: '/lovable-uploads/ai-gallery/use-case-chocolateria-team.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Chocolate Shop Holiday Calendar & Product Planner (US)',
        desc: "12 months with the key US dates (Valentine's Day, St. Patrick's Day, Easter, Mother's Day, Father's Day, July 4, Labor Day, Sweetest Day, National Chocolate Day, Halloween, Thanksgiving, Christmas and Hanukkah), featured products, the season and the key actions for each.",
        image: '/lovable-uploads/ai-gallery/use-case-chocolateria-bonbons.jpg',
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
    ctaLabel: 'YES, I WANT THE CHOCOLATE SHOP CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your chocolate shop better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de chocolate/SPEC D5 (chocolate shop / chocolatier / tempering / bonbons) + las
  // del ES adaptadas (tareas ya escritas, producción y tienda, obradores pequeños y cadenas, frente a las apps, varias
  // tiendas con la licencia de la tienda EN, garantía) + ganache TCS y vida útil, temperaturas, alérgenos y etiquetas,
  // licencias estatales, venta al peso y encargos, temporada, limpieza, firma, UK/CA/AU, moneda y suscripción (como los
  // hermanos EN). La de Latinoamérica del ES → la de UK/CA/AU.
  faqs: [
    {
      q: 'What should be on a chocolate shop opening checklist?',
      a: "One list in order. Personal hygiene first (clean uniform and apron, hair tied back, no rings (a plain band is OK), bracelets or watch, hands washed in water at 100 °F or warmer, cuts covered with a waterproof bandage and a glove, and anyone with vomiting, diarrhea or jaundice stays home). Then a safe start: the exhaust fan before any other equipment and, if you have gas equipment, a check that it doesn't smell of gas before you light anything. Next, the equipment: the tempering machine preheated as its maker says (typically 113 °F), the cool room (59–64 °F, 50–60% humidity) and the ganache fridge (41 °F or below) checked for the night with each reading logged, the bonbon display case at 60–64 °F and not fogging up before any product goes in, and the A/C keeping the shop at 68–72 °F. Then the shop: the display case set up (fresh-cream items only in a refrigerated case at 41 °F unless a lab test shows they are not TCS), a price and allergen notice on every tray, gift boxes and ribbons restocked, a sample station with one set of tongs per tray, the chalkboard, online orders and today's pre-orders. The \"Chocolate Shop Opening & Closing Checklists\" workbook has all 25 opening tasks written, and the whole-shop checklist covers the alarm, lights, HVAC, the security gate and restrooms.",
    },
    {
      q: 'What goes on a chocolate shop closing checklist?',
      a: "Product first: bonbons and bars out of the display case and into the cool room, any fresh-cream (TCS) item into the fridge at 41 °F or below, and anything left out covered. Then the counter cleaned and sanitized (approved sanitizer at label strength, checked with a test strip) and the display glass. In the kitchen: the tempering machine cleaned and dried, molds washed, open couverture in airtight containers, the cool room and fridge readings logged, the marble cleaned, sanitized and dried, and the day's waste logged by product and reason. Last, everything off except the cool room and fridges, gas burners off, trash out and the alarm. The whole-shop \"Shop Closing\" tab runs in a safe order: customers out, music, patio and signs in, the display cases turned off only once the product is stored, the kitchen temperature logged, then the POS, trash, a safety check that never unplugs the cool room, the fridges or a melter, HVAC on night mode (wrapped bars on the shelves need the shop at 68 °F or below overnight) and the alarm and lock-up last.",
    },
    {
      q: 'Does it cover tempering dark, milk and white chocolate?',
      a: "Yes. The tempering sheet starts with couverture stock (dark 55–70%, milk 30–40%, white 28–33% cocoa) and a check of the kitchen air before you start: 64–68 °F and 50–60% humidity, because warmer than that the cocoa butter will not crystallize properly. Then it runs the typical curve for each chocolate: dark melted to 122–131 °F, cooled to 81–82 °F on the marble or by seeding and brought back to 88–90 °F; milk 113–122 → 79–81 → 84–86 °F; white 104–113 → 77–79 → 82–84 °F. Each one has a temper test (shine, a clean snap, set in 3–5 minutes) and a batch log. These are typical curves: your couverture maker's chart always rules. The molding sheet then covers shells of 1/16–1/8 in, chilling at 54–57 °F, filling to 80% and letting it set before capping, unmolding and checking the shine.",
    },
    {
      q: 'How does the kit handle fresh-cream ganache and shelf life?',
      a: "Fresh-cream ganache and fillings with high water activity are treated as TCS food (time/temperature control for safety) until a lab test of water activity and pH shows they are not: they are held at 41 °F or below, in the fridge or a refrigerated display case, never in the 60–64 °F bonbon case or the cool room, and carry a date mark of 7 days at most, with the production day as day 1 (FDA Food Code 3-501.17). The Quarterly & Annual sheet schedules that lab test for each new ganache or filling before it goes on sale. At the bottom of the molding sheet there is an editable shelf-life table by product type at 59–64 °F: bars and unfilled chocolate 12–18 months, praline and gianduja bonbons 2–4 months, truffles and coated clusters 3–4 weeks, fresh-cream ganache 7 days at 41 °F, and bonbons with UHT cream, sorbate or alcohol 4–8 weeks only with a lab test. Finished chocolate is never frozen; only bulk ganache, at 0 °F or below for 1–2 months.",
    },
    {
      q: 'What temperatures does a chocolate shop need to log?',
      a: "The kit works with ranges that never mix: the kitchen at 64–68 °F and 50–60% humidity, the cool room for finished chocolate at 59–64 °F, the fridge for ganache and fillings at 41 °F or below, the bonbon display case at 60–64 °F and under 55% humidity, and the shop at 68–72 °F (above 68 °F chocolate softens and bloom risk climbs). Molds go in slightly warmer than the room (68–72 °F) and filled shells chill at 54–57 °F. Readings are logged in °F at opening and close, the sales associate keeps an eye on the case and the shop during the day, and thermometers and probes are checked every month in ice water (32 °F).",
    },
    {
      q: 'How does the kit handle allergens, samples and labels?',
      a: "Every display tray carries a written allergen notice for unwrapped items with the 9 major US allergens (milk, egg, wheat, soy, peanuts, tree nuts, sesame, fish and shellfish), plus any \"may contain\" statement, which is voluntary but has to be true (FDA Food Code 2022 3-602.12(C), where your state has adopted it). Samples go out with one set of tongs per tray, and nut and peanut items never share tongs; bonbons, truffles and samples are never touched with bare hands; custom gift boxes are built with gloves or tongs, and for an allergy request with fresh gloves and pieces from untouched trays. In production, nut and peanut bars run last and the tempering machine is cleaned before switching from milk to dark or white chocolate. Chocolate you wrap and label in the shop carries the product name, ingredients, net weight in oz and g, allergens and your business name and address (FDA Food Code 3-602.11), plus a lot and best-by date as the kit's practice. The UK's 14 allergens are noted.",
    },
    {
      q: 'Do I need a license to make and sell chocolate?',
      a: "Usually a health permit, and in some states also a food manufacturing license to make candy, or to sell wholesale or by mail. Bonbons with alcohol above 0.5% can only be sold where your state allows it, and shipped only to states that allow it; some states set an age limit of 21. Many states also tax candy even where groceries are exempt. The kit flags all of this on the annual sheet and in the shelf-life table, but it is not legal advice: check your state rules before you start.",
    },
    {
      q: "Does it include the holiday season, Valentine's Day and Easter?",
      a: "Yes. The holiday season checklist starts in October: a catalog with bark, toffee, bonbons, molded figures and Hanukkah gelt, extra couverture and packaging, seasonal staff (with the federal hour limits for minors, and no one under 16 running or cleaning the tempering or panning machine), pre-sales, a published pre-order deadline, your carrier's shipping cutoff and the pickup hours for Christmas Eve and New Year's Eve; then peppermint bark, English toffee and nut brittle, chocolate figures, holiday bonbons, gift baskets and corporate gift sets, with every corporate order confirmed in writing (allergens, quantities, date, deposit). Valentine's Day covers heart bonbons, bars with an engraved message, premium truffles, gift boxes and home deliveries; Easter, eggs, bunnies, large filled eggs, centerpieces and Easter baskets. The bonus calendar adds the 12 months with their US dates, from Valentine's Day and Mother's Day to Sweetest Day, National Chocolate Day and Thanksgiving.",
    },
    {
      q: 'Does it handle sales by weight, pre-orders and gift boxes?',
      a: "Yes. If you sell by the pound, the cash drawer checklist turns on a legal-for-trade scale, checks the tare of trays and boxes with a test weight, matches the price per pound on the POS to the tray sign and, at close, balances the pounds rung up against what came off the trays. Pre-orders are confirmed with allergens, quantities, pickup date and time, price, deposit and cancellation terms, and the deposits are rung on the POS as deposits, not as the day's sales, so the over/short stays right. Gift boxes, bags, tissue and ribbons are on the opening, weekend and weekly stock checks.",
    },
    {
      q: 'What should a chocolate shop cleaning checklist include?',
      a: "Daily cleaning belongs in the closing checklists (counter, display glass, tempering machine, molds, marble and floors). On top of that, the kit schedules a weekly deep clean of the tempering machine (taken apart), the marble slab (cleaned, sanitized and dried: water must never touch the chocolate), the molds, the wrapping surfaces, shelving, the shop, the display case inside and out, the store window and the sample area, with sanitizer checked with test strips, and monthly tasks (A/C filters, wiring, thermometers and the fire extinguishers). Contracted services go on the \"Quarterly & Annual\" tab: pest control by a licensed operator, tempering and panning machine service, refrigeration by an EPA 608-certified tech, calibration of thermometers and the scale, the annual extinguisher service, gas lines if you have gas, and hood cleaning under NFPA 96 only if you cook with grease under a hood.",
    },
    {
      q: 'Is there a free chocolate shop checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 338 chocolate shop tasks already written and sorted by shift, area and role, a counter on every checklist that skips the tasks you mark N/A, °F temperatures, tempering curves, a shelf-life table and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a chocolate shop?',
      a: "Yes. Every checklist comes with the real tasks of a chocolate shop that makes its own chocolate already written: tempering, molding, bonbons, bars, wrapping, the display case, the counter and the manager. You'll want to make it yours: adjust tasks to your shop, delete the ones that don't apply and add your own. The editable cells are green.",
    },
    {
      q: 'Does it work for a small chocolatier, a bonbon shop or a chain?',
      a: 'Yes. The kit is written for shops that make their own bonbons, bars and truffles with a tempering machine and sell them over a counter, and it scales: a small chocolatier can start with production, the display case and closing, and a chain can use every role, area and the full calendar. If you resell chocolate you don\'t make, mark the production tasks N/A and the counter leaves them out.',
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for the area, who does it, ✓ (a drop-down with ✓, — for not done, or N/A), the time and notes, and a signature line at the bottom. The whole-shop and cash drawer checklists come with who does it and a due-by time already filled in. The shift lead prints the checklist and hands it out, each person checks off their tasks, and at the end of the shift the shift lead checks it and signs.',
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it in several chocolate shops?',
      a: "Yes. One purchase covers one business with all of its shops, which makes it a good fit for chocolate shop chains. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (the protected sheets have no password). The kit is set up for the US: temperatures in °F, the FDA Food Code (41 °F cold holding), the 9 major allergens and a cash count in US bills and coins. In the UK, the kit's chocolate ranges read in °C (kitchen 18–20 °C, cool room 15–18 °C, bonbon case 16–18 °C, shop 20–22 °C), fresh-cream ganache is chilled food and is kept at 8 °C or below, and allergen information covers 14 allergens (the kit's allergen tasks already note the UK's 14). In Canada and Australia, check your provincial or state food safety rules, licensing and allergen list, and type them into the tasks. For pounds, Canadian or Australian dollars, unprotect the cash count sheet and change the label and value of each bill and coin. The holiday calendar has a UK note (Mothering Sunday, bank holidays and Boxing Day). Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $19 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you.',
    },
    {
      q: 'Is it a subscription? Are future updates included?',
      a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we add new templates or improvements, you get them at no extra cost — just download the files again.',
    },
    {
      q: 'Is there a money-back guarantee?',
      a: "Yes. A full 30-day guarantee. If you're not happy, we'll refund 100% with no questions asked.",
    },
  ],

  cta: {
    heading: 'Stop Repeating the Same Instructions Every Shift',
    subtitle: "9 templates + 3 bonuses (12 files) for your chocolate shop for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists: display case, counter, kitchen, cleaning',
      'Whole-shop opening and closing + cash drawer count with automatic over/short',
      'Production: tempering, molding, bonbons and bars, in °F',
      'Weekly inventory: couverture, nuts, fillings, packaging and consumables',
      'Manager checklists: daily, weekly and monthly',
      'Tasks by role: chocolatier, sales associate, shift lead',
      "Seasons: holiday season, Valentine's Day and Easter",
      'BONUS: Chocolate Shop Pre-Shift Meeting Template',
      'BONUS: Chocolate Shop Holiday Calendar & Product Planner (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE CHOCOLATE SHOP CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Chocolatería / Obrador de Chocolate, la edición española de este kit: por eso conservan sus nombres, negocios y
  // cifras, y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD. Ninguno cita una marca o persona real (SPEC
  // §R) ni choca con el kit EN (comprobado contra revision/dump_en.txt): ninguna frase cambiada.
  testimonials: {
    subtitle:
      'Chocolatiers, shift leads and shop owners who already run their operations with Kit de Tareas Recurrentes: Chocolatería / Obrador de Chocolate, the Spanish edition of this kit',
    items: [
      {
        name: 'Miguel Ángel Roca',
        role: 'Master Chocolatier, Chocolatería Roca',
        text: 'The production checklist saved me. I used to forget to log tempering temperatures and setting times. Now everything is on record and our quality control is spotless.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Elena Montero',
        role: 'Owner, Bombonería La Trufa Dorada',
        text: 'I opened my chocolate shop a year ago and the Christmas chaos was unbearable. With the checklists by shift and area, the team knows exactly what to do without me watching over them.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Javier Solís',
        role: 'Head of Production, Chocolates Artesanos Solís',
        text: 'The production checklists are perfectly structured: tempering, molding, bonbons, bars, wrapping. My new chocolatiers learn the process in half the time.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fuentes',
        role: 'Shop Manager, Cacao & Co.',
        text: 'The display case checklist is great. Bonbons, bars, packaging, cleaning the displays... it is all listed. The shop always looks perfect for the customer.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Carlos Mendoza',
        role: 'Director, Mendoza chocolate shop chain',
        text: 'We have 4 shops and every manager did things differently. Now, with standardized checklists, the customer experience is the same in all of them. Onboarding went from 2 weeks to 4 days.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Hospitality Consultant, chocolate shops and production kitchens',
        text: 'The first thing I do with every chocolate shop client is hand them these checklists. Production, display case, management, seasons... they cover 95% of what any artisan chocolate shop needs.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Andrés Beltrán',
        role: 'Master Chocolatier, Obrador Beltrán',
        text: "The seasonal calendar is pure gold. Christmas, Valentine's Day, Easter, Mother's Day, fairs... I finally have the yearly plan I always wanted.",
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Sergio Herrera',
        role: 'General Manager, Chocolatería Origen',
        text: 'The food cost and production waste control in the manager checklist is exactly what we needed. Couverture waste used to catch us by surprise at the end of the month. Now we keep it under control every day.',
        avatar: '/avatars/avatar-8.jpg',
      },
    ],
  },

  pricing: {
    price: '$19',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    // D4: obligatorio en KitTareasPricing; sin «valor total» ni ahorro (FTC).
    bonusTotalLabel: 'Everything included: 9 templates + 3 bonuses',
  },

  // Saliente extra (como el Ghost Kitchen y el Ice Cream Shop): el caso de uso EN de las chocolaterías, que a su vez lista
  // este kit (products-catalog.ts urlByLang.en).
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/bar-checklist-templates', label: 'Bar Checklists Kit Pro' },
    { href: '/en/digital-products/coffee-shop-checklist-templates', label: 'Coffee Shop Checklists Kit Pro' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
    { href: '/en/digital-products/ghost-kitchen-checklist-templates', label: 'Ghost Kitchen Checklists Kit Pro' },
    { href: '/en/digital-products/ice-cream-shop-checklist-templates', label: 'Ice Cream Shop Checklists Kit Pro' },
    { href: '/en/digital-products/pastry-shop-checklist-templates', label: 'Pastry Shop Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: '/en/use-cases/concept/chocolate-shop', label: 'AI for Chocolate Shops' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.1 · October 2026',

  alreadyBought: {
    product: 'chocolate-shop-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
