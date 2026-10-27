// astro-site/src/data/productos-en/tareas/pastry-shop-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Pastry Shop Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-pasteleria.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones; como el ES, 13 tarjetas en el grid y los bonus
// solo en su sección, y `gridGallery` propio), con las decisiones de sus hermanos EN *-checklist-templates.ts. SPEC:
// scripts/productos-digitales/checklists-kit/pastry/SPEC.md (delta) + la base.
//   · D2: nombre «Pastry Shop Checklists Kit Pro»; title SEO = H1 (Forma B, titlePost «: » + subtitleLine en bloque):
//     «Pastry Shop Checklists Kit Pro: Opening, Closing & Cake Order Templates». Demanda US (SPEC §R): pastry shop
//     40.500/mes, bakery case 590, cake order form 480, allergen chart y food temperature log 320, bakery order form 260,
//     temperature log sheet 210, receiving log 140, pastry chef duties 110: en keywords, títulos y FAQ.
//   · D5: títulos de las 13 plantillas y los 2 bonus = los de los xlsx EN (pastry/SPEC §2,
//     dl/pastry-shop-checklist-templates/).
//   · D3/D4: $19, pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine ni `value` en los bonos (el ES los «valora en €31»). Fórmula de la tienda EN.
//   · Cifras de los xlsx EN de la F2, CONFIRMADAS contra el volcado de la ronda 1 (4c4a158b, revision/dump_en.txt;
//     pastry/F3-NOTAS.md §3): 413 tareas en los 9 checklists y el briefing (22 + 20 = 42 en el 01;
//     26 + 18 + 13 = 57 en el 02; 16 + 18 + 14 + 6 = 54 en el 03; 14 + 13 + 11 + 12 = 50 en el 04; 18 + 13 + 13 = 44 en
//     el 05; 26 + 11 + 13 + 9 + 17 + 14 = 90 en el 06; 20 + 19 = 39 en el 08; 11 + 12 = 23 en el 09; 14 en el briefing;
//     el censo ES dice 429 porque cuenta además las 16 fechas del calendario, que no son tareas); 17 fechas en el B02;
//     32 productos en 5 categorías en el 10; 43 productos de partida en la matriz del 12. °F = GRADOS_F_SPEC de
//     mapas_pastry.py: vitrina y cámara 32–41 °F (41 °F, 3-501.16), cámara de masas 36–41 °F, congelador 0 °F, abatidor
//     135 → 70 °F en 2 h → 41 °F en 4 h (3-501.14), huevos en aire a 45 °F, masa 72–75 °F, fermentación ≤ 82 °F, horno
//     375–400 °F, base en blanco 350 °F, almíbar 250 °F, caramelo 320–340 °F, tienda 68–72 °F, hielo 32 °F; date marking
//     7 días (24 h = objetivo del kit con huevo, 3-501.17); depósito 30-50 % y food cost 28-35 % = criterio del kit.
//   · Lo que el ES afirma y el kit no trae, fuera: «Trail cobra €60-75 al mes» y «sin internet» (→ la fórmula de los
//     hermanos), «merma en euros» (→ «in your currency»), «14 UE» (→ 9 de EE. UU. + sulfitos + los 14 del Reino Unido),
//     «Imprimible A4» (→ US Letter), «más de 30 productos» en la matriz (el EN trae 43), la FAQ «¿Qué incluye la
//     versión 2.0?» (es la primera edición inglesa → FAQ de los 4 registros) y las fechas españolas (Reyes con roscón y
//     turrones, Semana Santa con torrijas y monas, comuniones, Todos los Santos con huesos de santo y panellets → las US
//     del 06 y el B02, D14).
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC base §6 y §9), como los hermanos EN.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 10 del ES traducidos tal cual (nombres, negocios y
//     cifras de origen), con el subtítulo de la edición española (TIENDA §3.5). Solo se pintan. Las marcas reales que
//     cita la SPEC §R (Hotel Meliá Valencia, Grupo Europastry, Escuela Hofmann) están SOLO en el marquee de la SPA
//     (src/data/testimonials-pasteleria.ts); la ficha ES de Astro ya los trae neutralizados («hotel boutique en
//     Valencia», «obrador industrial en Barcelona», «escuela de pastelería en Barcelona») y así se traducen. Ninguno
//     choca con el kit EN (Isabel García: el B02 trae Three Kings Day).
//   · Imágenes: fuera las del ES con texto o marcas ajenas (horno: la marca MIWE; vitrina: cartel «PATISSERIE ATELIER»
//     con «RAZPBERRY ENTREMET» mal escrito; equipo: logos inventados en las chaquetillas y un saco de harina con texto) y
//     la OG ES (texto español y «€12»). Se quedan hero, masas, decoración y producción (sin texto; «ELIZA» en una
//     placa). Entran fotos YA publicadas en la tienda EN sin texto: la vitrina de How to Open a Pastry Shop
//     (guia-pasteleria-1, etiquetas en blanco), su obrador con laminadora (guia-pasteleria-hero) y la vitrina de bollería
//     del Coffee Shop Business Plan Kit (csbp-en-pastry-case). OG = el hero (obrador con croissants).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'pastry-shop-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT',

  seo: {
    title: 'Pastry Shop Checklists Kit Pro: Opening, Closing & Cake Order Templates',
    description:
      '15 Excel pastry shop checklists and logs: 413 tasks already written, a cake order form, allergen chart, temperature log and waste log. One-time $19.',
    keywords:
      'pastry shop checklist, bakery checklist, bakery opening checklist, bakery closing checklist, cake order form, custom cake order form, bakery order form, bakery allergen chart, allergen chart, food temperature log, temperature log sheet, receiving log, food prep labels, shelf life chart, bakery cleaning schedule, bakery production schedule, bakery waste log, pastry chef duties, bakery case, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
  },

  schema: {
    productName: 'Pastry Shop Checklists Kit Pro',
    productDescription:
      '13 templates + 3 bonuses (16 files) for pastry shops and bakeries: 413 tasks already written in 9 Excel checklists and the pre-shift huddle (doughs and fermentation, creams and fillings, decorating, the bakery case, manager, roles, cleaning, holidays and celebration cakes, whole-shop opening and closing, cash drawer) and 4 logs ready to fill in: production schedule and waste log, cake order form and order log, bakery allergen chart (9 major allergens, UK 14) and food temperature and receiving logs.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'What should be on a bakery or pastry shop opening checklist?',
        a: "Two lists. In the kitchen: ovens, mixers and the retarder-proofer on, walk-in and freezer readings logged (41 °F and 0 °F or below), the doughs checked, the day's mise en place and production order, surfaces sanitized, and the bakery cases at 41 °F or below before stocking. In the shop: the cases on at least 45 minutes before stocking, the POS and starting bank, today's custom orders, the case stocked with price and allergen labels, and a team huddle before the door opens.",
      },
      {
        q: 'Does it include a cake order form?',
        a: "Yes. A printable cake order form with the customer, pickup or delivery, size in inches, the cake message, the customer's allergies with a separate consent, total, deposit and balance due, plus a monthly order log, a pickup schedule by time slot and the day's order sheet for the kitchen.",
      },
      {
        q: 'Is there a bakery allergen chart?',
        a: 'Yes. An allergen matrix with 43 starter items to check against your recipes and suppliers (it says DO NOT PUBLISH until you verify and date it), a customer-facing chart that fills itself in, a bakery case sign and case labels. It covers the 9 major US allergens plus sulfites, and the UK\'s 14.',
      },
      {
        q: 'Does it include a food temperature log and a receiving log?',
        a: 'Yes. A monthly temperature log by unit with morning and afternoon readings that turn red out of range, a receiving log with rejection criteria, prep labels with date and time made and use-by, and a shelf-life chart in °F.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, chilled food at 8 °C or below, frozen at −18 °C and information on the 14 allergens (the allergen chart already has them); in Canada and Australia, your local temperatures and allergen list; for pounds, Canadian or Australian dollars, change the bills and coins in the cash count. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Pastry Shop Checklists Kit Pro',
  },

  images: {
    // hero bg (6): fotos sin texto en español ni marcas ajenas (ver cabecera). Como el ES, el strip del ContentGrid difiere
    // en la 6.ª (el obrador con laminadora en vez de la producción). Mismo reparto: why = masas, buyBox = horno/obrador,
    // cta = hero.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-1.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-masas.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-decoracion.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-pastry-case.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-produccion.jpg',
    ],
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-1.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-masas.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-decoracion.jpg',
      '/lovable-uploads/ai-gallery/csbp-en-pastry-case.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-pasteleria-masas.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $19, once',
    // D2: titlePre + titleGold = «Pastry Shop Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Pastry Shop Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Opening, Closing & Cake Order Templates',
    description:
      '13 Excel templates: 9 checklists with the real tasks of a pastry shop already written (doughs, fermentation, creams, decorating, the bakery case) and 4 logs ready to fill in (production and waste, cake orders, allergens, temperatures). Print it, delegate it to your team, check it off and file it.',
    checkItems: [
      'Kitchen opening and closing: ovens, mixers, the retarder-proofer, walk-ins and the bakery case',
      'Production stations: doughs and fermentation, creams and fillings, decorating',
      'Roles: head pastry chef, pastry cook, pastry assistant and counter associate',
      "Holidays and events: the holiday season with Three Kings Day, Valentine's Day, Easter, celebration cakes and Thanksgiving pies",
      'Blank templates + a pre-shift meeting template',
      'Production schedule with a waste log, cake order form, bakery allergen chart (9 major allergens, UK 14) and food temperature log',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS PASTELERÍA — €12»).
  stickyLabel: 'PASTRY SHOP CHECKLISTS KIT PRO — $19',

  grid: {
    countGold: '13',
    headingRest: ' Pastry Shop Checklists & Logs + 3 Bonuses (16 files)',
    subtitle:
      '9 checklists with the real tasks of a pastry shop already written and 4 logs ready to fill in. Adjust them, print and delegate.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Pastry Kitchen & Bakery Case Opening and Closing Checklists',
        desc: "2 checklists (kitchen opening and closing) in 6 blocks with 42 tasks already written: ovens, mixers and the retarder-proofer on, walk-in and freezer readings logged (41 °F and 0 °F or below), the day's mise en place and production order, surfaces sanitized with a test strip, the refrigerated bakery cases at 41 °F or below before stocking, price and allergen labels, and at close the doughs labeled with date and time, the day's waste logged, the gas, the alarm and the lock-up. Each task with its area, who does it, a due-by time and initials.",
      },
      {
        icon: 'Croissant',
        title: 'Pastry Kitchen Production Checklists: Doughs, Creams & Fillings, Decorating',
        desc: 'Doughs and fermentation (croissant dough checked at 72–75 °F, laminated, proofed at no more than 82 °F and baked twice a day; artisan bread baked with steam; sweet and savory tart bases), creams and fillings (pastry cream cooled from 135 to 70 °F in 2 hours and to 41 °F in 4 more, buttercream, ganache, curds, mousses made with cooked meringue or pasteurized whites, entremets, mirror glaze and caramel) and decorating and finishing (glazing, custom cakes from their order form, and the bakery case stocked and restocked every 2 hours), with a Target / Spec column for the key parameters.',
      },
      {
        icon: 'ClipboardList',
        title: 'Pastry Shop Manager Checklist: Daily, Weekly, Monthly & Shift Handover',
        desc: "Daily (custom orders, attendance, critical ingredients, deliveries, walk-in and case temperatures, sales vs. production, the day's waste and tomorrow's plan), weekly with a focus for each day (Monday planning, Tuesday team, Wednesday quality and allergen labels, Thursday suppliers, Friday weekend prep), monthly (food cost against a 28–35% target, waste against a target under 5%, margin per piece, oven, mixer and sheeter maintenance, thermometers calibrated at 32 °F) and a shift handover.",
      },
      {
        icon: 'Users',
        title: 'Pastry Chef Duties by Role: Head Pastry Chef, Pastry Cook, Assistant & Counter',
        desc: 'Checklists for the head pastry chef (the production plan, task assignments, quality control, new recipes, spec sheets and recipe costing), the pastry cook (doughs, lamination, fermentation, baking, creams, cakes and custom orders), the pastry assistant (mise en place, pans, egg wash, cleaning and FIFO) and the counter associate (stocking the case, allergen labels and questions, custom cake orders, restocking every 2 hours and the cash out).',
      },
      {
        icon: 'CalendarDays',
        title: 'Bakery Cleaning Schedule, Equipment Maintenance & Weekly Inventory',
        desc: 'A weekly deep clean by area (ovens, spiral and planetary mixers, the dough sheeter, marble benches, hood filters, with the ducts cleaned by a certified company if you cook with grease (NFPA 96), walk-ins with a full FIFO review, the bakery cases, register and scale), monthly equipment maintenance (oven gaskets, thermostats and steam system, walk-in coils, gaskets and drains, the probe checked against the display, mixer gears, sheeter belts and the scale, legal-for-trade if you sell by weight) and a weekly inventory of ingredients, decorations and packaging.',
      },
      {
        icon: 'PartyPopper',
        title: "Pastry Shop Holiday & Event Checklists: Holidays, Valentine's, Easter, Mother's Day, Celebration Cakes & Thanksgiving",
        desc: "The holiday season (cookie tins, Yule logs, stollen and panettone, pickup slots for Dec 22–24 and New Year's Eve) with Three Kings Day (Three Kings bread or rosca de Reyes and King cake, the baby figurine packed separately), Valentine's Day, Easter (hot cross buns, Easter breads, carrot cake, chocolate eggs), Mother's & Father's Day, celebration cakes for First Communions, graduations and showers (consultation, written quote, tasting, deposit, tiered cake assembly and delivery) and Thanksgiving pies, with the custard pies cooled fast and held at 41 °F. Each campaign closes with its wrap-up.",
      },
      {
        icon: 'FileEdit',
        title: 'Blank Pastry Shop Checklist Template (Editable)',
        desc: '3 blank templates (by time of day, by area and by role) to build your own task lists, with the same columns and done counter as the rest of the kit.',
      },
      {
        icon: 'Store',
        title: 'Pastry Shop Opening & Closing Checklist (Whole Shop)',
        desc: "The shop, not the kitchen: the refrigerated bakery cases on at least 45 minutes before stocking and at 41 °F or below, the shop at 68–72 °F, the POS and starting bank, today's custom orders, the cases stocked in order (custard-, cream- or cheese-filled pieces and savory items such as quiche in the refrigerated case at 41 °F or below) with price and allergen labels and the allergen sign in view, and a team huddle before the door opens. At close: markdown product first, tomorrow's orders set aside, leftovers logged, recoverable items labeled, donate or discard (good-faith donations are protected by the Bill Emerson Good Samaritan Food Donation Act), the cash out and the lock-up last. Due-by times for a shop that opens at 8 AM.",
      },
      {
        icon: 'Wallet',
        title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log',
        desc: 'Starting bank, the closing count by US bill and coin (rolls included), card sales without tips, the POS Z report and the over/short worked out every day, plus a monthly cash log with net cash sales, card sales and the bank deposit for each day.',
      },
      {
        icon: 'CalendarRange',
        title: 'Bakery Production Schedule & Waste Log: Weekly Plan, Made vs. Sold & Summary',
        desc: 'A weekly plan by item and day with 32 bakery items already listed in 5 categories (viennoiserie, cakes and pastries, bread, savory, cookies and small cakes) and free rows in each, made vs. sold with the leftover, waste % and waste cost in your currency, an action column with the condition for each choice, and a weekly summary by category against a waste target you set (5% to start).',
      },
      {
        icon: 'ShoppingCart',
        title: "Cake Order Form & Custom Order Log: Order Form, Log, Pickups & Today's Orders",
        desc: "A printable cake order form (customer, pickup or delivery, size in inches, cake message, the customer's allergies with a separate consent, total, deposit and balance due, a deposit policy line and a privacy notice), a monthly order log with status and the balance due calculated, a weekly pickup schedule by time slot and the day's order sheet for the kitchen.",
      },
      {
        icon: 'ShieldAlert',
        title: 'Bakery Allergen Chart (9 Major Allergens, UK 14): Matrix, Chart, Case Sign & Labels',
        desc: 'An allergen matrix with 43 starter items to check against your recipes and suppliers\' spec sheets (until you date it, it says DO NOT PUBLISH), the customer-facing allergen chart that fills itself in, a sign for the bakery case and cut-out case labels with price and allergens. The 9 major US allergens plus sulfites and the UK\'s 14.',
      },
      {
        icon: 'Thermometer',
        title: 'Food Temperature Log, Receiving Log, Prep Labels & Shelf Life Chart',
        desc: 'A monthly temperature log by unit with morning and afternoon readings (walk-in and bakery cases 32–41 °F, dough retarder 36–41 °F in retard mode, freezer 0 °F or below, blast chiller 135 → 70 °F in 2 h and 41 °F in 4 more) that turns red out of range, a receiving log with rejection criteria, prep labels with date and time made, use-by and batch, and a shelf-life chart in °F.',
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef and hospitality consultant working since 2010, in kitchens since the age of 17.",
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Filled for Pastry Shops',
        desc: "Don't start from scratch. Every checklist comes with the real tasks of a pastry kitchen. Just adjust them, delete what doesn't apply and add what's missing.",
      },
      {
        icon: 'Croissant',
        title: 'Full Artisan Production',
        desc: "Doughs, fermentation, lamination, creams, mousses, decorating and the bakery case: the tasks generic checklist apps don't cover.",
      },
      {
        icon: 'Users',
        title: 'Role-Specific Checklists',
        desc: 'Checklists for the head pastry chef, the pastry cook, the pastry assistant and the counter associate. Everyone knows exactly what to do every shift.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $19, Once',
        desc: 'The same task lists bakeries run in premium checklist apps like Trail, in Excel, for a one-time payment. No subscription.',
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
    'John Guerrero, CEO of AI Chef Pro. Chef and hospitality consultant: in kitchens since the age of 17 and advising businesses since 2010. He has been a chef-owner and has run operations for restaurant groups. He has designed operating systems and checklists for hundreds of restaurants, pastry shops and bakeries. More at johnguerrero.es.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 13 templates in the kit, you get these three extra resources',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Pastry Shop Pre-Shift Meeting Template',
        desc: "The 5-minute huddle that separates good pastry shops from great ones: today's production, custom orders, allergen alerts and the team on shift.",
        image: '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Pastry Shop Holiday & Events Calendar (US)',
        desc: "17 key dates and occasions for a US pastry shop (Three Kings Day and King cake, Valentine's Day, Pi Day, Easter, Mother's Day, Thanksgiving pies, Christmas, wedding season) with the special production and the lead time for each.",
        image: '/lovable-uploads/ai-gallery/guia-pasteleria-1.jpg',
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
    ctaLabel: 'YES, I WANT THE PASTRY SHOP CHECKLISTS KIT — $19',
  },

  guarantee: {
    text: "If the checklists don't help you run your pastry shop better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US de pastry/SPEC D5 (pastry shop / bakery checklist, cake order form, allergen
  // chart, food temperature log, receiving log) + las del ES adaptadas (tareas ya rellenas y registros, producción
  // artesanal, pastelería pequeña y obrador grande, frente a Trail, varias tiendas con la licencia de la tienda EN,
  // garantía) + temperaturas, plan de producción y mermas, festivos, limpieza, firma, UK/CA/AU, moneda y suscripción (como
  // los hermanos EN). La de la versión 2.0 del ES → la de los 4 registros; la de Latinoamérica → la de UK/CA/AU.
  faqs: [
    {
      q: 'What should be on a bakery or pastry shop opening checklist?',
      a: "Two lists, because the kitchen and the shop open at different times. The kitchen checklist starts at 5:00 AM: ovens preheated, the spiral and planetary mixers, the retarder-proofer (temperature and humidity logged), the tempering machine and the sheeter if you use them, walk-in and freezer readings logged (41 °F and 0 °F or below), and a check of the gas and power supply. Then the setup: the doughs out of the retarder and checked, butter tempered for laminating, the day's mise en place and production order, pans and parchment ready, surfaces and marble sanitized (sanitizer at label strength, checked with a test strip) and the critical ingredients checked. The whole-shop checklist turns the refrigerated bakery cases on at least 45 minutes before stocking, until they hold 41 °F or below, then the lights, the shop at 68–72 °F, the POS and starting bank, today's custom orders, the cases stocked in order (viennoiserie first, then the refrigerated case for cream-filled pastries, savory last, with quiche, empanadas and ham & cheese croissants also in the refrigerated case) with a price and allergen label for each item and the allergen sign in view, and a team huddle before the door opens at 8 AM.",
    },
    {
      q: 'What goes on a bakery closing checklist?',
      a: "In the kitchen: doughs into the retarder-proofer and prepped items into the walk-in, wrapped and labeled with date and time (date marking), the mixers and utensils cleaned, tables and marble cleaned and sanitized, ovens off (or set for the pre-dawn start) and scraped, the walk-in and freezer readings logged, the case emptied with leftovers going to a labeled markdown area or to waste (never back into tomorrow's regular case), the day's waste logged, gas off and the alarm. The whole-shop \"Shop Closing\" tab starts with selling, not clearing: the markdown product grouped and signed in the last hour, tomorrow's custom orders set aside with their order form, the door locked to the public, then the leftovers logged item by item, recoverable items labeled into the walk-in, the rest donated or discarded (the Bill Emerson Good Samaritan Food Donation Act protects good-faith donations), the cash out against the POS Z report, the cases cleaned and left as their maker says with the closing temperature logged, and the final checks, trash, alarm and lock-up last.",
    },
    {
      q: 'Does it include a cake order form?',
      a: "Yes, it is one of the four logs. The printable order form takes the order number and channel, the customer, pickup in store or a delivery address, the date and the time it leaves the kitchen, the product, size in inches, cake or base, frosting and finish, and the cake message in capitals. The customer's allergies are checked against the allergen chart, with a consent box that is separate from the optional marketing box (marketing texts need prior written consent under the TCPA; emails must offer an unsubscribe). Then the total, the deposit and the balance due, which calculates itself, a deposit policy line you fill in (a 30–50% deposit is common practice, not law: check your state's rules on nonrefundable deposits), the customer's signature and a privacy notice. The same workbook has a monthly order log with status, a weekly pickup schedule by hourly time slot, and \"Today's Orders\" to hang in the kitchen.",
    },
    {
      q: 'Is there a bakery allergen chart?',
      a: "Yes. The allergen matrix comes with 43 starter items (viennoiserie, cakes, bread, savory, holiday items and the base creams) marked in gray as a proposal: check each one against your actual recipe and your suppliers' spec sheets, record the source and date it; until you do, the status column says DO NOT PUBLISH. The customer-facing allergen chart fills itself in from the matrix, and the workbook adds a sign for the bakery case and cut-out case labels with price and abbreviated allergens. It covers the 9 major US allergens (milk, eggs, wheat, soy, peanuts, tree nuts, sesame, fish and shellfish, under FALCPA and the FASTER Act), sulfites (declared from 10 ppm) and the UK's other four (celery, mustard, lupin and mollusks), so the UK's 14 are there too. For unpackaged items, the information has to be in writing before purchase where your state has adopted the FDA Food Code 2022 (3-602.12(C)); a \"may contain\" statement is voluntary and must be true.",
    },
    {
      q: 'Does it include a food temperature log and a receiving log?',
      a: "Yes. The temperature log is one sheet per month with morning and afternoon readings for the walk-in cooler (32–41 °F), the dough retarder in retard mode (36–41 °F), the freezer (0 °F or below), two bakery cases (32–41 °F) and the blast chiller (135 → 70 °F in 2 hours and 41 °F within 4 more), with a corrective action column; readings out of range turn red on their own. The receiving log has one line per delivery (supplier, invoice, product, lot, expiration date, temperature at delivery, vehicle and packaging, accepted or rejected) and the rejection criteria: refrigerated TCS food above 41 °F, shell eggs in a truck with air above 45 °F, milk and cream above 45 °F (between 41 and 45 °F only where dairy law allows it, then cooled to 41 °F within 4 hours), frozen food showing signs of thawing, torn packaging or a dirty, warm truck. The workbook adds prep labels (item, made, use by, batch) and a shelf-life chart in °F.",
    },
    {
      q: 'What temperatures does a pastry shop need to log?',
      a: "The bakery cases, the walk-in and anything custard-, cream- or cheese-filled at 41 °F or below (the FDA Food Code limit for TCS food such as pastry cream, whipped cream, cheesecake and custard pies), and perishable savory items such as quiche, empanadas and ham & cheese croissants in the refrigerated case too, the dough retarder at 36–41 °F, the freezer at 0 °F or below, and creams cooled from 135 °F to 70 °F within 2 hours and to 41 °F within 4 more. Ready-to-eat TCS food carries a date mark of 7 days at most at 41 °F; for anything made with eggs, the kit's quality target is 24 hours. If TCS food has been above 41 °F for more than 2 hours, or nobody knows for how long, the kit says throw it out. Thermometers and probes are calibrated every month in ice water (32 °F), and the shop is kept at 68–72 °F for chocolate and puff pastry.",
    },
    {
      q: 'Does it cover doughs, creams and decorating?',
      a: 'Yes. The production workbook has a sheet for each station, with a Target / Spec column for the key parameters. Doughs and fermentation: the sourdough starter, croissant dough mixed short and checked at 72–75 °F, chilled before laminating (3 single or 2 double folds), shaped for a second bake and for tomorrow, proofed at no more than 82 °F and baked at 375–400 °F; artisan bread divided, shaped, proofed in bannetons, scored and baked with steam; sweet and savory tart bases blind-baked at 350 °F. Creams and fillings: pastry cream cooled fast and labeled, buttercream, ganache, diplomat cream, curds, mousses with cooked meringue or pasteurized whites, entremets frozen for glazing, mirror glaze, fondant, Italian meringue and caramel. Decorating and finishing: glazing, decorating, custom cakes from their order form and the bakery case, restocked every 2 hours.',
    },
    {
      q: 'How does the production schedule and waste log work?',
      a: 'The weekly plan lists 32 US bakery items in 5 categories (viennoiserie, cakes and pastries, bread, savory, cookies and small cakes), each with free rows for your own items: you enter the planned units for each day and it adds up the week. On "Made vs Sold" you log what was made and sold at closing, and the leftover, waste % and waste cost calculate themselves (enter the unit cost from your recipe costing). An action column says what to do with leftovers, each option with its condition: product that has been on display is not frozen to sell later. The weekly summary by category compares waste against a target you set (5% to start; the kit\'s guideline is 3–8% in an artisan pastry shop).',
    },
    {
      q: 'Does it include holidays and celebration cakes?',
      a: "Yes, with US dates. The holiday season checklist runs from November to January: cookie tins and trays, Yule logs, stollen and panettone, gift boxes, pickup slots for December 22–24, New Year's Eve orders and Three Kings Day (Three Kings bread or rosca de Reyes for January 6, the big day, and King cake until Mardi Gras, with the baby figurine packed separately because it is a choking hazard). Seasonal hires come with the federal rules for minors: 16- and 17-year-olds don't run or clean dough or batter mixers, sheeters, dividers or rounders (portable countertop mixers of 5 quarts and ½ hp or less excepted), and 14- and 15-year-olds don't run power-driven machinery or bake, and work no earlier than 7 AM or later than 7 PM during the school year. Valentine's Day, Easter (hot cross buns, Easter breads, carrot cake, chocolate eggs) and Mother's & Father's Day have their own checklists, as do celebration cakes for First Communions, graduations and showers (consultation, written quote, tasting, deposit, tiered cake assembly and delivery with cream-filled items at 41 °F) and Thanksgiving pies (pre-orders, pickup slots on the Wednesday before, custard pies cooled fast and held at 41 °F, and pecan held cold unless your health department accepts it as non-TCS). Each campaign ends with a wrap-up of what sold and what was wasted, and the bonus calendar adds 17 key dates and occasions.",
    },
    {
      q: 'What should a bakery cleaning schedule include?',
      a: "Daily cleaning belongs in the closing checklists. On top of that, the kit schedules a weekly deep clean by area: inside the ovens, the spiral and planetary mixers taken apart, the dough sheeter, marble benches with a dedicated cleaner, the hood filters (and, if you cook with grease, the ducts by a certified company under NFPA 96), walls and floors, the walk-ins with a full FIFO review and the freezer contents, dry storage, the bakery cases, register, scale and the packaging area. Monthly equipment maintenance covers the ovens (gaskets, thermostats, steam system), the walk-in coils, gaskets and drains, the probe checked against the display, mixer gears, sheeter belts and rollers, pans, piping tips and the scale.",
    },
    {
      q: 'Is there a free bakery checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 413 pastry shop tasks already written in 9 Excel checklists and a pre-shift huddle, sorted by shift, area and role, 4 logs ready to fill in (production and waste, cake orders, allergens, temperatures), °F temperatures under the FDA Food Code and a cash count in US dollars. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a pastry shop?',
      a: "The 9 checklists come with the real tasks of a pastry shop already written: you adjust them to your shop, delete the ones that don't apply and add your own. The 4 logs (production and waste, cake orders, allergens and temperatures) are ready to fill in with your data; the allergen matrix comes with 43 starter items that you must check against your recipes and suppliers. The editable cells are green.",
    },
    {
      q: 'Does it work for a small pastry shop and a large production bakery?',
      a: 'Yes. The templates scale. A small pastry shop can use the kitchen and bakery case tasks. A large production kitchen can use every production station, the cake order form, order log and pickup schedule, and the weekly production schedule.',
    },
    {
      q: 'How does the sign-off work?',
      a: 'Each checklist has columns for the area, who does it, a due-by time, ✓ Done (a drop-down with ✓, — for not done, or N/A) and initials, with who does it and the due-by time already filled in on the task checklists, a done counter and a "Verified by" line at the bottom. The shift lead prints the checklist and hands it out, each person checks off their tasks, and at the end of the shift the shift lead checks it and signs.',
    },
    {
      q: 'How is it different from checklist apps like Trail?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $19, a one-time payment. What it is not: there are no reminders, photos or notifications on your staff's phones.",
    },
    {
      q: 'Can I use it in several pastry shops or bakeries?',
      a: "Yes. One purchase covers one business with all of its shops, which makes it a good fit for pastry shop chains. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change (no sheet is protected). The kit is set up for the US: temperatures in °F under the FDA Food Code (41 °F cold holding, 0 °F frozen), the 9 major allergens and a cash count in US bills and coins. In the UK, chilled food such as cream-filled pastries is kept at 8 °C or below, frozen food at −18 °C, and allergen information covers 14 allergens under the Food Information Regulations 2014: the allergen chart already has the UK's four extra columns. In Canada and Australia, check your provincial or state food safety rules and allergen list, and type them into the tasks. For pounds, Canadian or Australian dollars, change the label and value of each bill and coin in the cash count. The holiday calendar has a UK note (Mothering Sunday, bank holidays and Boxing Day). Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
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
    heading: 'Stop Repeating the Same Instructions Every Day',
    subtitle: "13 templates + 3 bonuses for your pastry shop for less than one hour of a consultant's time.",
    items: [
      'Opening and closing checklists for the kitchen and the shop',
      'Production stations: doughs, fermentation, creams, mousse, decorating',
      'Production control: temperatures, times, FIFO',
      'Manager checklists: daily, weekly and monthly',
      'Tasks by role: head pastry chef, pastry cook, assistant, counter associate',
      "Holidays and events: the holiday season with Three Kings Day, Valentine's Day, Easter, celebration cakes, Thanksgiving",
      'Weekly production schedule with a waste log',
      'Cake order form and custom order log',
      'Bakery allergen chart (9 major allergens, UK 14) with case sign and labels',
      'Food temperature log and receiving log',
      'BONUS: Pastry Shop Pre-Shift Meeting Template',
      'BONUS: Pastry Shop Holiday & Events Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PASTRY SHOP CHECKLISTS KIT — $19',
  },

  // Testimonios: traducción fiel de los del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Pastelería / Obrador, la edición española de este kit: por eso conservan sus nombres, negocios y cifras, y el subtítulo
  // lo dice. Solo se pintan: NO alimentan el JSON-LD. La ficha ES de Astro ya trae neutralizadas las marcas reales del
  // marquee de la SPA (ver cabecera); ninguno choca con el kit EN: ninguna frase cambiada.
  testimonials: {
    subtitle:
      'Pastry chefs, shift leads and bakery owners who already run their operations with Kit de Tareas Recurrentes: Pastelería / Obrador, the Spanish edition of this kit',
    items: [
      {
        name: 'Marc Vidal',
        role: 'Head Pastry Chef, Obrador Sant Jordi',
        text: 'The fermentation and lamination checklist saved us. Every pastry cook used to laminate their own way and our viennoiserie was inconsistent. Now we all follow the same protocol and the croissants come out perfect every day.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Pablo Roca',
        role: 'Owner, Pastelería La Miga de Oro',
        text: 'I opened my pastry shop a year ago and I forgot everything: turning the ovens on in time, taking the doughs out of the proofer, checking the cases. These checklists got me organized from the first week.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Manager, Dulce Tradición Obrador',
        text: 'Running a kitchen that makes viennoiserie, bread and pastries was chaotic. The checklists by area and by role brought order. Onboarding new assistants went from 2 weeks to 4 days.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Carlos Martín',
        role: 'Pastry Chef, boutique hotel in Valencia',
        text: 'In a hotel with a breakfast buffet and afternoon pastries, everything has to be ready on time. The opening checklists by shift put an end to the night team forgetting things.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Ana Belén Torres',
        role: 'Owner, Macarons & Co',
        text: 'The bakery case and allergen labeling tasks are gold. Having the signed record every day brought order to how we control the case and label our products.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Javier Molina',
        role: 'Master Pastry Chef, Obrador Artesano BCN',
        text: "The monthly maintenance tasks for the ovens and mixers are exactly what we needed. We had no routine before, and our equipment broke down for lack of preventive maintenance.",
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Isabel García',
        role: 'General Manager, Pastelería Familiar El Rincón Dulce',
        text: "The yearly calendar of special tasks is incredible. Christmas, Three Kings Day, Valentine's Day, Mother's Day... now we plan production weeks ahead instead of improvising.",
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Diego Alonso',
        role: 'Pastry Assistant, industrial bakery in Barcelona',
        text: "As an assistant, the checklist for my role tells me exactly what's expected of me every shift. I don't have to keep asking what to do. It gives me independence.",
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Raquel Sánchez',
        role: 'Bakery Consultant',
        text: 'The first thing I do with every new client is hand them these checklists. They bring order from day one. Production, cases, cleaning, inventory... they cover 95% of what any pastry kitchen needs.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Fernando López',
        role: 'Pastry Instructor, pastry school in Barcelona',
        text: 'I recommend this kit to every student who is about to open their own pastry kitchen. The production tasks are perfectly structured by station. It is the standard every pastry shop should have.',
        avatar: '/avatars/chef-avatar-3.jpg',
      },
    ],
  },

  pricing: {
    price: '$19',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    // D4: obligatorio en KitTareasPricing; sin «valor total» ni ahorro (FTC).
    bonusTotalLabel: 'Everything included: 13 templates + 3 bonuses',
  },

  // Como el ES (que enlaza «Cómo Montar una Pastelería»), su gemelo EN How to Open a Pastry Shop en el pie; saliente extra
  // (como el Ghost Kitchen y el Ice Cream Shop): el caso de uso EN de panaderías y pastelerías, que a su vez lista este kit
  // (products-catalog.ts urlByLang.en).
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/how-to-open-a-pastry-shop', label: 'How to Open a Pastry Shop' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/bar-checklist-templates', label: 'Bar Checklists Kit Pro' },
    { href: '/en/digital-products/coffee-shop-checklist-templates', label: 'Coffee Shop Checklists Kit Pro' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
    { href: '/en/digital-products/ghost-kitchen-checklist-templates', label: 'Ghost Kitchen Checklists Kit Pro' },
    { href: '/en/digital-products/ice-cream-shop-checklist-templates', label: 'Ice Cream Shop Checklists Kit Pro' },
    { href: '/en/digital-products/chocolate-shop-checklist-templates', label: 'Chocolate Shop Checklists Kit Pro' },
    { href: '/en/digital-products/hotel-checklist-templates', label: 'Hotel Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: '/en/use-cases/concept/bakery-pastry-shop', label: 'AI for Bakeries & Pastry Shops' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'pastry-shop-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
