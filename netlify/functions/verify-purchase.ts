import type { Handler } from '@netlify/functions';
import { validatePurchase } from '../shared/purchase-validation';
import { emailI18n, type TiendaLang } from '../shared/email-i18n';

// ── Product config ──────────────────────────────────────────────
interface ProductConfig {
  accessPath: string;
  emailSubject: string;
  emailTitle: string;
  emailBody: string;
  emailCta: string;
  /** Idioma de la tienda (2026-09-23). Ausente = 'es'. Elige los textos fijos del
   *  email (netlify/shared/email-i18n.ts); los de arriba ya van en ese idioma. */
  lang?: TiendaLang;
}

export const PRODUCTS: Record<string, ProductConfig> = {
  'pro-prompts-ebook': {
    accessPath: '/pro-prompts-library-access',
    emailSubject: 'Tu acceso a Pro Prompts Library',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Pro Prompts Library</strong> está listo. Haz clic en el botón para acceder a tus prompts y descargas:',
    emailCta: 'Acceder a mi Library',
  },
  // Tienda EN (2026-10-03): gemelo de pro-prompts-ebook, producto independiente con su propio acceso
  // (mismo patrón que food-cost-templates; NO hereda el fallback legacy del ES: su gate manda
  // `product`). `lang: 'en'` elige los textos fijos del email (netlify/shared/email-i18n.ts) y la
  // página de estado cripto /en/crypto-payment; precio en USD (product-prices.ts). El asunto
  // empieza por «Your access to» para productoLabel().
  'ai-prompts-for-restaurants': {
    accessPath: '/en/digital-products/ai-prompts-for-restaurants/access',
    emailSubject: 'Your access to the Gastro Pro Prompts eBook',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to the <strong>Gastro Pro Prompts eBook</strong> is ready. Click the button to open your Pro Prompts Library with all the prompts and downloads:',
    emailCta: 'Open my Library',
    lang: 'en',
  },
  'kit-escandallos': {
    accessPath: '/kit-escandallos-access',
    emailSubject: 'Tu acceso al Kit de Escandallos Pro',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Escandallos Pro</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 13 plantillas Excel + 2 bonus:',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-09-24): gemelo de kit-escandallos, producto independiente con su propio
  // acceso. `lang: 'en'` elige los textos fijos del email (netlify/shared/email-i18n.ts) y la
  // página de estado cripto /en/crypto-payment (crypto-checkout.ts); precio en USD
  // (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'food-cost-templates': {
    accessPath: '/en/digital-products/food-cost-templates/access',
    emailSubject: 'Your access to Food Cost Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Food Cost Kit Pro</strong> is ready. Click the button to open your dashboard and download the 13 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'pack-appcc': {
    accessPath: '/pack-appcc-access',
    emailSubject: 'Tu acceso al Pack de Plantillas APPCC',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Pack de Plantillas APPCC</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 19 registros + 2 bonus de seguridad alimentaria:',
    emailCta: 'Acceder a mis Plantillas APPCC',
  },
  // Tienda EN (2026-10-03): gemelo de pack-appcc, producto independiente con su propio acceso
  // (mismo patrón que food-cost-templates y restaurant-inventory-templates). `lang: 'en'` elige los
  // textos fijos del email (netlify/shared/email-i18n.ts) y la página de estado cripto
  // /en/crypto-payment; precio en USD (product-prices.ts). El asunto empieza por «Your access to»
  // para productoLabel().
  'haccp-templates': {
    accessPath: '/en/digital-products/haccp-templates/access',
    emailSubject: 'Your access to HACCP Food Safety Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>HACCP Food Safety Kit Pro</strong> is ready. Click the button to open your dashboard and download the 19 food safety templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'kit-tareas': {
    accessPath: '/kit-tareas-access',
    emailSubject: 'Tu acceso al Kit de Tareas Recurrentes',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes Pro</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-cafeteria': {
    accessPath: '/kit-tareas-cafeteria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Cafetería / Brunch',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Cafetería / Brunch</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pizzeria': {
    accessPath: '/kit-tareas-pizzeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pizzería',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Pizzería</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hamburgueseria': {
    accessPath: '/kit-tareas-hamburgueseria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Hamburguesería',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Hamburguesería</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-dark-kitchen': {
    accessPath: '/kit-tareas-dark-kitchen-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Dark Kitchen',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Dark Kitchen</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pasteleria': {
    accessPath: '/kit-tareas-pasteleria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pastelería / Obrador',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Pastelería / Obrador</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 13 checklists operativos + 2 bonus (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-bar': {
    accessPath: '/kit-tareas-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Bar / Cocktails',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Bar / Cocktails</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-catering': {
    accessPath: '/kit-tareas-catering-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Catering / Eventos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Catering / Eventos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hotel': {
    accessPath: '/kit-tareas-hotel-completo-access',
    emailSubject: 'Tu acceso al Kit Tareas Recurrentes: Hotel Completo — 46 Checklists',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit Tareas Recurrentes: Hotel Completo — 46 Checklists</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 15 plantillas con 46 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-heladeria': {
    accessPath: '/kit-tareas-heladeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Heladería Artesanal',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Heladería Artesanal</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chocolateria': {
    accessPath: '/kit-tareas-chocolateria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chocolatería / Obrador de Chocolate',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Chocolatería / Obrador de Chocolate</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-restaurante-creativo': {
    accessPath: '/kit-tareas-restaurante-creativo-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Restaurante Creativo / De Autor',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Restaurante Creativo / De Autor</strong> esta listo. Haz clic en el boton para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chef-privado': {
    accessPath: '/kit-tareas-chef-privado-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chef Privado / Personal Chef',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Chef Privado / Personal Chef</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists profesionales:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-gestion-personal': {
    accessPath: '/kit-gestion-personal-access',
    emailSubject: 'Tu acceso al Kit de Gestión de Personal y Turnos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Gestión de Personal y Turnos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de gestión de personal:',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-10-03): gemelo de kit-gestion-personal, producto independiente con su propio
  // acceso (mismo patrón que restaurant-inventory-templates y haccp-templates). `lang: 'en'` elige
  // los textos fijos del email (netlify/shared/email-i18n.ts) y la página de estado cripto
  // /en/crypto-payment; precio en USD (product-prices.ts). El asunto empieza por «Your access to»
  // para productoLabel().
  'restaurant-schedule-templates': {
    accessPath: '/en/digital-products/restaurant-schedule-templates/access',
    emailSubject: 'Your access to Restaurant Staff Scheduling Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Restaurant Staff Scheduling Kit Pro</strong> is ready. Click the button to open your dashboard and download the 7 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'kit-inventario': {
    accessPath: '/kit-inventario-access',
    emailSubject: 'Tu acceso al Kit Control de Inventario y Compras',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit Control de Inventario y Compras</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de control de inventario:',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-09-25): gemelo de kit-inventario, producto independiente con su propio acceso
  // (mismo patrón que food-cost-templates). `lang: 'en'` elige los textos fijos del email
  // (netlify/shared/email-i18n.ts) y la página de estado cripto /en/crypto-payment; precio en USD
  // (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'restaurant-inventory-templates': {
    accessPath: '/en/digital-products/restaurant-inventory-templates/access',
    emailSubject: 'Your access to Restaurant Inventory Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Restaurant Inventory Kit Pro</strong> is ready. Click the button to open your dashboard and download the 7 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'guia-dark-kitchen': {
    accessPath: '/guia-dark-kitchen-access',
    emailSubject: 'Tu acceso a la Guía: Cómo Montar una Dark Kitchen',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar una Dark Kitchen</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 3 checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-gastronomico': {
    accessPath: '/guia-restaurante-gastronomico-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Gastronómico 65 Plazas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar un Restaurante Gastronómico</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 20 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-food-cost-ingenieria-menu': {
    accessPath: '/guia-food-cost-ingenieria-menu-access',
    emailSubject: 'Tu acceso a la Guía Food Cost + Ingeniería de Menú',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Food Cost + Ingeniería de Menú</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX, 8 herramientas Excel y el bonus de ejercicios:',
    emailCta: 'Acceder a mi Guía',
  },
  'manual-manager-restaurante': {
    accessPath: '/manual-manager-restaurante-access',
    emailSubject: 'Tu acceso al Manual del Manager de Restaurante',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Manual del Manager de Restaurante</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el manual PDF + DOCX, 7 herramientas Excel y el bonus de 12 situaciones resueltas:',
    emailCta: 'Acceder a mi Manual',
  },
  'manual-chef-ejecutivo': {
    accessPath: '/manual-chef-ejecutivo-access',
    emailSubject: 'Tu acceso al Manual del Chef Ejecutivo',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Manual del Chef Ejecutivo</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el manual PDF + DOCX, 7 herramientas Excel y el bonus de 12 situaciones resueltas en cocina:<br /><br />Si además diriges el negocio —no sólo la cocina—, el <a href="https://aichef.pro/manual-manager-restaurante?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Manual del Manager de Restaurante</a> es su hermano: si llevas las dos cosas, necesitas los dos.',
    emailCta: 'Acceder a mi Manual',
  },
  'guia-pasteleria-obrador': {
    accessPath: '/guia-pasteleria-obrador-access',
    emailSubject: 'Tu acceso a Cómo Montar una Pastelería',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a <strong>Cómo Montar una Pastelería</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX (20 capítulos y anexo normativo, 103 páginas), las 8 herramientas Excel con fórmulas vivas, el business plan modelo relleno y las 12 decisiones de apertura resueltas:<br /><br />El día que abras, lo que vas a usar cada mañana es el <a href="https://aichef.pro/kit-tareas-pasteleria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Pastelería</a> (producción, encargos, alérgenos de vitrina y temperaturas). Para el papeleo diario de seguridad alimentaria está el <a href="https://aichef.pro/pack-appcc?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Pack de Plantillas APPCC</a>, para escandallar por formato el <a href="https://aichef.pro/kit-escandallos?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Escandallos Pro</a>, y cuando ya estés vendiendo y toque revisar precios y carta, la <a href="https://aichef.pro/guia-food-cost-ingenieria-menu?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Guía Food Cost + Ingeniería de Menú</a>.',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-chocolateria-obrador': {
    accessPath: '/guia-chocolateria-obrador-access',
    emailSubject: 'Tu acceso a Cómo Montar una Chocolatería Boutique & Atelier',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a <strong>Cómo Montar una Chocolatería Boutique &amp; Atelier</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX (20 capítulos y anexo normativo, 111 páginas), los 9 libros de Excel con fórmulas vivas, el business plan modelo relleno y las 12 decisiones de apertura resueltas (34 páginas):<br /><br />El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes.<br /><br />Cuando abras, lo que vas a usar cada mañana es el <a href="https://aichef.pro/kit-tareas-chocolateria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Chocolatería</a> (templado, moldeado, vitrina y temperaturas). Para el papeleo diario de seguridad alimentaria está el <a href="https://aichef.pro/pack-appcc?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Pack de Plantillas APPCC</a>, para escandallar por formato el <a href="https://aichef.pro/kit-escandallos?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Escandallos Pro</a>, y cuando ya estés vendiendo y toque revisar precios y carta, la <a href="https://aichef.pro/guia-food-cost-ingenieria-menu?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Guía Food Cost + Ingeniería de Menú</a>.',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-churreria-chocolateria': {
    accessPath: '/guia-churreria-chocolateria-access',
    emailSubject: 'Tu acceso a Cómo Montar una Churrería-Chocolatería',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a <strong>Cómo Montar una Churrería-Chocolatería</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX (16 capítulos y anexo normativo, 95 páginas), los 8 libros de Excel con fórmulas vivas, el business plan modelo relleno y las 12 decisiones de apertura resueltas (21 páginas):<br /><br />Esta guía es todo lo que hay que decidir antes de abrir.<br /><br />Cuando ya estés trabajando, el registro diario del aceite de fritura va en el <a href="https://aichef.pro/pack-appcc?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Pack de Plantillas APPCC</a>, el cuadrante semana a semana en el <a href="https://aichef.pro/kit-gestion-personal?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit Gestión de Personal y Turnos</a> y el escandallo del resto de tu carta en el <a href="https://aichef.pro/kit-escandallos?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Escandallos Pro</a>. Y si tu plan incluye salir a ferias con un vehículo, tienes el <a href="https://aichef.pro/plan-negocio-food-truck?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Plan de Negocio: Food Truck</a>; si vas a servir churros dentro de una cafetería, el <a href="https://aichef.pro/plan-negocio-cafeteria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Plan de Negocio: Cafetería</a>; y si también te atrae la bombonería, que es otro negocio, la guía <a href="https://aichef.pro/guia-chocolateria-obrador?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Cómo Montar una Chocolatería Boutique &amp; Atelier</a>.',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-casual': {
    accessPath: '/guia-restaurante-casual-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Casual 80 Plazas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar un Restaurante Casual</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 16 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-mexicano': {
    accessPath: '/guia-restaurante-mexicano-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Mexicano 80 Plazas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar un Restaurante Mexicano</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-peruano': {
    accessPath: '/guia-restaurante-peruano-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Peruano 80 Plazas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar un Restaurante Peruano</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-japones': {
    accessPath: '/guia-restaurante-japones-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Japonés 60 Plazas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar un Restaurante Japonés</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-nikkei': {
    accessPath: '/guia-restaurante-nikkei-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Nikkei 60 Plazas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar un Restaurante Nikkei</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'mega-pack-tareas': {
    accessPath: '/mega-pack-tareas-access',
    emailSubject: 'Tu acceso al Mega Pack Tareas Recurrentes — 13 Kits',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Mega Pack Tareas Recurrentes (13 Kits)</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 151 plantillas:',
    emailCta: 'Acceder a mis 13 Kits',
  },
  'kit-plan-financiero': {
    accessPath: '/kit-plan-financiero-access',
    emailSubject: 'Tu acceso al Kit Plan Financiero para Restaurantes',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit Plan Financiero para Restaurantes</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 10 plantillas financieras (8 + 2 bonus):',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-10-03): gemelo de kit-plan-financiero, producto independiente con su propio
  // acceso (mismo patrón que restaurant-schedule-templates). `lang: 'en'` elige los textos fijos del
  // email (netlify/shared/email-i18n.ts) y la página de estado cripto /en/crypto-payment; precio en
  // USD (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'restaurant-financial-plan-templates': {
    accessPath: '/en/digital-products/restaurant-financial-plan-templates/access',
    emailSubject: 'Your access to Restaurant Financial Plan Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Restaurant Financial Plan Kit Pro</strong> is ready. Click the button to open your dashboard and download the 8 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-food-truck, producto independiente con su propio acceso
  // (mismo patrón que restaurant-financial-plan-templates). `lang: 'en'` elige los textos fijos del email
  // (netlify/shared/email-i18n.ts) y la página de estado cripto /en/crypto-payment; precio en USD
  // (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'food-truck-business-plan': {
    accessPath: '/en/digital-products/food-truck-business-plan/access',
    emailSubject: 'Your access to Food Truck Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Food Truck Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-cafeteria, producto independiente con su propio acceso
  // (mismo patrón que restaurant-financial-plan-templates). `lang: 'en'` elige los textos fijos del email
  // (netlify/shared/email-i18n.ts) y la página de estado cripto /en/crypto-payment; precio en USD
  // (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'coffee-shop-business-plan': {
    accessPath: '/en/digital-products/coffee-shop-business-plan/access',
    emailSubject: 'Your access to Coffee Shop Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Coffee Shop Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 75-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-bar-restaurante, producto independiente con su propio acceso
  // (mismo patrón que coffee-shop-business-plan). `lang: 'en'` elige los textos fijos del email
  // (netlify/shared/email-i18n.ts) y la página de estado cripto /en/crypto-payment; precio en USD
  // (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'restaurant-business-plan': {
    accessPath: '/en/digital-products/restaurant-business-plan/access',
    emailSubject: 'Your access to Restaurant Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Restaurant Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 64-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-panaderia, producto independiente con su propio acceso
  // (mismo patrón que coffee-shop-business-plan). `lang: 'en'` elige los textos fijos del email
  // (netlify/shared/email-i18n.ts) y la página de estado cripto /en/crypto-payment; precio en USD
  // (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'bakery-business-plan': {
    accessPath: '/en/digital-products/bakery-business-plan/access',
    emailSubject: 'Your access to Bakery Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Bakery Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 66-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-11): gemelo de plan-negocio-tapas-bar, producto independiente con su propio acceso
  // (mismo patrón que restaurant-business-plan). `lang: 'en'` elige los textos fijos del email
  // (netlify/shared/email-i18n.ts) y la página de estado cripto /en/crypto-payment; precio en USD
  // (product-prices.ts). El asunto empieza por «Your access to» para productoLabel().
  'bar-business-plan': {
    accessPath: '/en/digital-products/bar-business-plan/access',
    emailSubject: 'Your access to Bar Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Bar Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 73-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-11): gemelo de plan-catering-tematico-eventos, producto independiente con su propio acceso
  // (mismo patrón que bar-business-plan).
  'catering-business-plan': {
    accessPath: '/en/digital-products/catering-business-plan/access',
    emailSubject: 'Your access to Catering Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Catering Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-13): gemelo de plan-negocio-cocteleria-eventos, producto independiente con su propio acceso
  // (mismo patrón que catering-business-plan).
  'mobile-bar-business-plan': {
    accessPath: '/en/digital-products/mobile-bar-business-plan/access',
    emailSubject: 'Your access to Mobile Bar Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Mobile Bar Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator with a shopping list for the host and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de plan-negocio-parrillero-asador-eventos, producto independiente con su propio acceso
  // (mismo patrón que mobile-bar-business-plan).
  'bbq-catering-business-plan': {
    accessPath: '/en/digital-products/bbq-catering-business-plan/access',
    emailSubject: 'Your access to BBQ Catering Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>BBQ Catering Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator with a smoke schedule and a shopping list by guest count and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de plan-negocio-paellero-eventos, producto independiente con su propio acceso
  // (mismo patrón que bbq-catering-business-plan).
  'paella-catering-business-plan': {
    accessPath: '/en/digital-products/paella-catering-business-plan/access',
    emailSubject: 'Your access to Paella Catering Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Paella Catering Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator with a paella yield and pan sizing table and a shopping list by guest count and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-25): gemelo de plan-negocio-pizzeria, producto independiente con su propio acceso
  // (mismo patrón que paella-catering-business-plan).
  'pizza-shop-business-plan': {
    accessPath: '/en/digital-products/pizza-shop-business-plan/access',
    emailSubject: 'Your access to Pizza Shop Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Pizza Shop Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pizza dough and food cost calculator and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-27): gemelo de plan-negocio-heladeria, producto independiente con su propio acceso
  // (mismo patrón que pizza-shop-business-plan).
  'ice-cream-shop-business-plan': {
    accessPath: '/en/digital-products/ice-cream-shop-business-plan/access',
    emailSubject: 'Your access to Ice Cream Shop Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Ice Cream Shop Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-27): gemelo de plan-negocio-finca-eventos-bodas, producto independiente con su propio acceso
  // (mismo patrón que pizza-shop-business-plan).
  'wedding-venue-business-plan': {
    accessPath: '/en/digital-products/wedding-venue-business-plan/access',
    emailSubject: 'Your access to Wedding Venue Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Wedding Venue Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing and quote calculator, the venue rental agreement templates and the 84-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-28): gemelo de plan-negocio-cafeteria-movil-eventos, producto independiente con su propio acceso
  // (mismo patrón que wedding-venue-business-plan).
  'coffee-cart-business-plan': {
    accessPath: '/en/digital-products/coffee-cart-business-plan/access',
    emailSubject: 'Your access to Coffee Cart Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Coffee Cart Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator, the coffee catering service agreement template and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-29): gemelo de plan-negocio-taqueria, producto independiente con su propio acceso
  // (mismo patrón que coffee-cart-business-plan).
  'taco-shop-business-plan': {
    accessPath: '/en/digital-products/taco-shop-business-plan/access',
    emailSubject: 'Your access to Taco Shop Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Taco Shop Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the taco cost and trompo yield calculator and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-29): gemelo de plan-negocio-polleria, producto independiente con su propio acceso
  // (mismo patrón que coffee-cart-business-plan).
  'rotisserie-chicken-restaurant-business-plan': {
    accessPath: '/en/digital-products/rotisserie-chicken-restaurant-business-plan/access',
    emailSubject: 'Your access to Rotisserie Chicken Restaurant Business Plan Kit',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Rotisserie Chicken Restaurant Business Plan Kit</strong> is ready. Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the chicken yield, rotisserie and costing calculator and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-15): gemelo de guia-food-cost-ingenieria-menu, producto independiente con su propio acceso
  // (mismo patrón que mobile-bar-business-plan).
  'food-cost-menu-engineering-guide': {
    accessPath: '/en/digital-products/food-cost-menu-engineering-guide/access',
    emailSubject: 'Your access to the Food Cost + Menu Engineering Guide',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to the <strong>Food Cost + Menu Engineering Guide</strong> is ready. Click the button to open your dashboard and download the guide in PDF + DOCX, the 8 Excel tools, the 12 solved exercises and the Equivalents Guide:',
    emailCta: 'Access my guide',
    lang: 'en',
  },
  // Tienda EN (2026-10-17): gemelo de guia-pasteleria-obrador, producto independiente con su propio acceso
  // (mismo patrón que food-cost-menu-engineering-guide).
  'how-to-open-a-pastry-shop': {
    accessPath: '/en/digital-products/how-to-open-a-pastry-shop/access',
    emailSubject: 'Your access to How to Open a Pastry Shop',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>How to Open a Pastry Shop</strong> is ready. Click the button to open your dashboard and download the guide in PDF + DOCX, the 8 Excel tools, the sample business plan, the 12 opening decisions and the Equivalents Guide:',
    emailCta: 'Access my guide',
    lang: 'en',
  },
  // Tienda EN (2026-10-17): gemelo de kit-tareas, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'restaurant-checklist-templates': {
    accessPath: '/en/digital-products/restaurant-checklist-templates/access',
    emailSubject: 'Your access to Restaurant Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Restaurant Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-bar, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'bar-checklist-templates': {
    accessPath: '/en/digital-products/bar-checklist-templates/access',
    emailSubject: 'Your access to Bar Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Bar Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-cafeteria, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'coffee-shop-checklist-templates': {
    accessPath: '/en/digital-products/coffee-shop-checklist-templates/access',
    emailSubject: 'Your access to Coffee Shop Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Coffee Shop Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-catering, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'catering-checklist-templates': {
    accessPath: '/en/digital-products/catering-checklist-templates/access',
    emailSubject: 'Your access to Catering Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Catering Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-pizzeria, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'pizza-shop-checklist-templates': {
    accessPath: '/en/digital-products/pizza-shop-checklist-templates/access',
    emailSubject: 'Your access to Pizza Shop Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Pizza Shop Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-hamburgueseria, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'burger-joint-checklist-templates': {
    accessPath: '/en/digital-products/burger-joint-checklist-templates/access',
    emailSubject: 'Your access to Burger Joint Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Burger Joint Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-dark-kitchen, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'ghost-kitchen-checklist-templates': {
    accessPath: '/en/digital-products/ghost-kitchen-checklist-templates/access',
    emailSubject: 'Your access to Ghost Kitchen Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Ghost Kitchen Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de kit-tareas-heladeria, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'ice-cream-shop-checklist-templates': {
    accessPath: '/en/digital-products/ice-cream-shop-checklist-templates/access',
    emailSubject: 'Your access to Ice Cream Shop Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Ice Cream Shop Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-27): gemelo de kit-tareas-hotel, producto independiente con su propio acceso.
  'hotel-checklist-templates': {
    accessPath: '/en/digital-products/hotel-checklist-templates/access',
    emailSubject: 'Your access to Hotel Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Hotel Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 17 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-31): gemelo de kit-tareas-taqueria, producto independiente con su propio acceso.
  'taco-shop-checklist-templates': {
    accessPath: '/en/digital-products/taco-shop-checklist-templates/access',
    emailSubject: 'Your access to Taco Shop Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Taco Shop Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de kit-tareas-chocolateria, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'chocolate-shop-checklist-templates': {
    accessPath: '/en/digital-products/chocolate-shop-checklist-templates/access',
    emailSubject: 'Your access to Chocolate Shop Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Chocolate Shop Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de kit-tareas-pasteleria, producto independiente con su propio acceso
  // (mismo patrón que restaurant-schedule-templates).
  'pastry-shop-checklist-templates': {
    accessPath: '/en/digital-products/pastry-shop-checklist-templates/access',
    emailSubject: 'Your access to Pastry Shop Checklists Kit Pro',
    emailTitle: 'Thank you for your purchase!',
    emailBody: 'Your access to <strong>Pastry Shop Checklists Kit Pro</strong> is ready. Click the button to open your dashboard and download the 13 Excel templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'kit-tareas-sushi-bar': {
    accessPath: '/kit-tareas-sushi-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Sushi Bar',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Sushi Bar</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos con protocolo anisakis APPCC:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-taqueria': {
    accessPath: '/kit-tareas-taqueria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Taquería Mexicana',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Taquería Mexicana</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos con trompo, nixtamal y tortillería, barra de salsas y APPCC:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-asador': {
    accessPath: '/kit-tareas-asador-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Asador / Parrilla y Josper',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-marisqueria': {
    accessPath: '/kit-tareas-marisqueria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Marisquería con Vivero y APPCC',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-tapas-bar': {
    accessPath: '/kit-tareas-tapas-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Tapas Bar / Gastrobar',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Tapas Bar / Gastrobar</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-food-truck': {
    accessPath: '/kit-tareas-food-truck-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Food Truck',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Food Truck</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-panaderia': {
    accessPath: '/kit-tareas-panaderia-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Panadería / Obrador',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Panadería / Obrador</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'guia-panaderia-obrador': {
    accessPath: '/guia-panaderia-obrador-access',
    emailSubject: 'Tu acceso a la Guía: Panadería con Obrador',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar una Panadería con Obrador</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel + manual del obrador con recetario masa madre:',
    emailCta: 'Acceder a mi Guía',
  },
  'plan-negocio-bar-restaurante': {
    accessPath: '/plan-negocio-bar-restaurante-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Bar-Restaurante',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Bar-Restaurante</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura con 50+ trámites:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-tapas-bar': {
    accessPath: '/plan-negocio-tapas-bar-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Tapas Bar / Gastrobar',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Tapas Bar / Gastrobar</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el documento DOCX completo (10 secciones), el plan financiero Excel y el checklist de apertura con 63 trámites:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cafeteria': {
    accessPath: '/plan-negocio-cafeteria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Cafetería / Brunch',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Cafetería / Brunch</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura con 65+ trámites:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-panaderia': {
    accessPath: '/plan-negocio-panaderia-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Panadería / Obrador',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Panadería / Obrador</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel con estacionalidad navideña, el plan de negocio Word y el checklist de apertura con 60+ trámites RGSEAA obrador:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-heladeria': {
    accessPath: '/plan-negocio-heladeria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Heladería Artesanal',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Heladería Artesanal</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word (10 secciones), el plan financiero en Excel (9 hojas con fórmulas vivas), el checklist de apertura (80 tareas en 6 fases) y la Guía de Equivalencias para Latinoamérica:<br /><br />Para el día a día del obrador y el mostrador, el <a href="https://aichef.pro/kit-tareas-heladeria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Heladería</a> es su hermano: el plan te dice cómo abrir, el kit cómo operar cada jornada.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-finca-eventos-bodas': {
    accessPath: '/plan-negocio-finca-eventos-bodas-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Finca de Eventos y Bodas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Finca de Eventos y Bodas</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word (10 secciones), el plan financiero en Excel (9 hojas con fórmulas vivas), el checklist de apertura (84 tareas en 6 fases), la calculadora de presupuesto del espacio, los modelos de contrato y la Guía de Equivalencias para Latinoamérica:<br /><br />Para el día a día del servicio de tu catering, el <a href="https://aichef.pro/kit-tareas-catering?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Catering</a> es su hermano: el plan te dice cómo abrir la finca, el kit cómo operar cada evento.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cafeteria-movil-eventos': {
    accessPath: '/plan-negocio-cafeteria-movil-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Cafetería Móvil para Eventos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Cafetería Móvil para Eventos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas en 6 fases, calculadora de escandallo y presupuesto por evento, modelo de contrato de servicio (particular y anexo para empresas y ferias) y guía de equivalencias para 21 países:<br /><br />Para el día a día de la barra y el servicio, el <a href="https://aichef.pro/kit-tareas-cafeteria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Cafetería</a> es su hermano: el plan te dice cómo montar el negocio, el kit cómo operar cada turno.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-pizzeria': {
    accessPath: '/plan-negocio-pizzeria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Pizzería Napolitana',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Pizzería Napolitana</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas, calculadora de masa y escandallo por pizza y guía de equivalencias para Hispanoamérica:<br /><br />Para el día a día del horno y el servicio, el <a href="https://aichef.pro/kit-tareas-pizzeria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Pizzería</a> es su hermano: el plan te dice cómo abrir, el kit cómo operar cada turno.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-taqueria': {
    accessPath: '/plan-negocio-taqueria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Taquería',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Taquería</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas en 6 fases, calculadora del trompo y escandallo por taco de 4 hojas y guía de equivalencias para Hispanoamérica:<br /><br />Para el día a día del trompo y el servicio, el <a href="https://aichef.pro/kit-tareas-taqueria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Taquería Mexicana</a> es su hermano: el plan te dice cómo abrir, el kit cómo operar cada turno.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-polleria': {
    accessPath: '/plan-negocio-polleria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Pollería y Asador de Pollos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Pollería y Asador de Pollos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones con las cinco corrientes del pollo asado, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas en 6 fases, calculadora del pollo, el asador y el escandallo de 4 hojas y guía de equivalencias para Hispanoamérica:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-sushi-bar': {
    accessPath: '/plan-negocio-sushi-bar-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Sushi Bar',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Sushi Bar</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas en 6 fases, calculadora del pescado, el arroz y el escandallo de 4 hojas y guía de equivalencias para Hispanoamérica:<br /><br />Para el día a día de la barra, el arroz y el pescado, el <a href="https://aichef.pro/kit-tareas-sushi-bar?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Recurrentes: Sushi Bar</a> es su hermano: el plan te dice cómo abrir, el kit cómo operar cada turno.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-food-truck': {
    accessPath: '/plan-negocio-food-truck-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Food Truck',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio: Food Truck</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar el documento DOCX completo (10 secciones), el plan financiero Excel y el checklist de apertura con 59 trámites incluyendo licencia de venta ambulante e ITV del vehículo adaptado:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cocteleria-eventos': {
    accessPath: '/plan-negocio-cocteleria-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Coctelería de Eventos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio &amp; Kit de Coctelería de Eventos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 10 entregables: DOCX 10 secciones, Plan Financiero Excel con estacionalidad de eventos, Calculadora Pricing, plantilla de 96 proveedores, catálogo de equipamiento, carta de 15 cocktails, modelo de contrato, 10 experiencias temáticas y checklist de 71 trámites, más el bonus Guía de Equivalencias para tu país:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-parrillero-asador-eventos': {
    accessPath: '/plan-negocio-parrillero-asador-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Parrillero / Asador para Eventos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio &amp; Kit de Parrillero / Asador para Eventos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables: plan de negocio en Word de 10 secciones con anexo del fuego al aire libre, plan financiero Excel de 9 hojas, calculadora de presupuestos por evento, plantilla de 93 proveedores, catálogo equipamiento, manual técnico parrillero, carta de 12 cortes, modelos de contrato B2C+B2B, 10 experiencias temáticas, guía de 8 sistemas + roadmap food truck y checklist de apertura de 83 tareas en 6 fases, más el bonus Guía de Equivalencias para tu país:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-paellero-eventos': {
    accessPath: '/plan-negocio-paellero-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Paellero / Paella para Eventos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio &amp; Kit de Paellero / Paella para Eventos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables: plan de negocio en Word de 10 secciones con anexo del fuego al aire libre, plan financiero Excel de 9 hojas, calculadora de presupuestos por evento, plantilla de 88 proveedores DO Valencia + Calasparra, catálogo equipamiento, manual técnico paellero (fuego + socarrat), carta de 12 paellas, modelos de contrato B2C+B2B, 10 experiencias temáticas, guía de 8 sistemas + roadmap food truck arrocería y checklist de apertura de 83 tareas en 6 fases, más el bonus Guía de Equivalencias para tu país:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-chef-privado-showcooking-eventos': {
    accessPath: '/plan-chef-privado-showcooking-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Chef Privado / Showcooking a Domicilio',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio &amp; Kit de Chef Privado / Showcooking a Domicilio</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables: DOCX 60+ pp, Plan Financiero Excel con mix B2C+B2B, Calculadora Pricing dual, plantilla de 96 proveedores premium (cuchillería japonesa, vajilla Pordamsa, AOVE DO, caviar Riofrío), catálogo equipamiento + cuchillería, manual técnico servicio domicilio APPCC móvil con 7 PCC, carta de 12 menús temáticos, modelos de contrato B2C+B2B con confidencialidad y MSA, 10 experiencias temáticas, guía sistemas Chef Privado vs Personal Chef vs Caterer y checklist de apertura con anexo regulación CCAA catering itinerante, más el bonus Guía de Equivalencias para tu país:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-catering-tematico-eventos': {
    accessPath: '/plan-catering-tematico-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Catering & Kit Temático para Eventos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Plan de Negocio para Catering &amp; Kit Temático para Eventos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables de la versión 2.2: plan de negocio en Word de 10 secciones, plan financiero Excel de 9 hojas (eventos × invitados × precio por invitado, con tesorería y préstamo), calculadora de presupuestos por invitado, checklist de apertura de 82 tareas en 6 fases, plantilla de 96 proveedores de 12 cocinas del mundo, catálogo de equipamiento multi-cocina, 12 conceptos pre-empaquetados, carta de 12 menús de cocinas del mundo, manual técnico APPCC multi-concepto, modelos de contrato B2C y B2B y guía de especialización progresiva, más el bonus Guía de Equivalencias para tu país:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
};

// ── Handler ─────────────────────────────────────────────────────
export const handler: Handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ valid: false }) };
  }

  try {
    const { checkoutSessionId, existingJwt, product } = JSON.parse(event.body || '{}');
    // Reject an explicitly-provided but unknown product (avoid silent fallback to pro-prompts-ebook).
    // Legacy callers that omit `product` (undefined/null) keep the pro-prompts-ebook fallback.
    if (product != null && !PRODUCTS[product]) {
      return { statusCode: 400, headers, body: JSON.stringify({ valid: false, error: 'unknown_product' }) };
    }
    const productId = product && PRODUCTS[product] ? product : 'pro-prompts-ebook';

    // Case 1: Verify new Stripe checkout session
    if (checkoutSessionId) {
      const Stripe = (await import('stripe')).default;
      const jwt = (await import('jsonwebtoken')).default;

      const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, { apiVersion: '2024-12-18.acacia' });
      const session = await stripe.checkout.sessions.retrieve(checkoutSessionId);

      if (session.payment_status === 'paid') {
        // La sesión debe ser del producto pedido (no de cualquier compra): ver netlify/shared/purchase-validation.ts
        const { verdict, mode, resolved } = await validatePurchase(stripe, session, productId, 'verify-purchase');
        if (verdict === 'mismatch' && mode === 'strict') {
          return {
            statusCode: 403,
            headers,
            body: JSON.stringify({ valid: false, error: 'product_mismatch', paidProduct: resolved.productId }),
          };
        }
        const email = session.customer_details?.email || session.customer_email || '';
        const token = jwt.sign(
          { email, product: productId },
          process.env.JWT_SECRET!,
          { expiresIn: '365d' }
        );

        // Send access email (log errors but don't block response)
        sendAccessEmail(email, token, productId).catch((err) => {
          console.error('sendAccessEmail failed:', err);
        });

        return {
          statusCode: 200,
          headers,
          body: JSON.stringify({ valid: true, jwt: token }),
        };
      }

      return { statusCode: 403, headers, body: JSON.stringify({ valid: false }) };
    }

    // Case 2: Verify existing JWT (magic link from email)
    if (existingJwt) {
      const jwt = (await import('jsonwebtoken')).default;
      try {
        jwt.verify(existingJwt, process.env.JWT_SECRET!);
        return {
          statusCode: 200,
          headers,
          body: JSON.stringify({ valid: true, jwt: existingJwt }),
        };
      } catch {
        return { statusCode: 403, headers, body: JSON.stringify({ valid: false }) };
      }
    }

    return { statusCode: 400, headers, body: JSON.stringify({ valid: false }) };
  } catch (err) {
    console.error('verify-purchase error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ valid: false }) };
  }
};

// ── Email sender ────────────────────────────────────────────────
// `extraHtml` (2026-09-05, pagos cripto): bloque HTML opcional que se inserta
// JUSTO ANTES del párrafo «Guarda este email…». Lo usa `nowpayments-ipn.ts`
// para recordar por escrito la renuncia al desistimiento de 14 días que el
// comprador marcó al pagar en cripto. Con el argumento vacío —que es como lo
// llaman verify-purchase, stripe-webhook y admin-generate-access— el HTML
// resultante es BYTE A BYTE el de siempre: la ruta de Stripe no cambia.
export async function sendAccessEmail(email: string, token: string, productId: string, extraHtml = '') {
  if (!email || !process.env.RESEND_API_KEY) return;

  const config = PRODUCTS[productId] || PRODUCTS['pro-prompts-ebook'];
  const magicLink = `https://aichef.pro${config.accessPath}?jwt=${token}`;

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
    },
    body: JSON.stringify({
      from: 'AI Chef Pro <noreply@contact.aichef.pro>',
      to: email,
      subject: config.emailSubject,
      html: `
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
          <h1 style="color: #FFD700; font-size: 24px;">${config.emailTitle}</h1>
          <p style="color: #333; line-height: 1.6;">
            ${config.emailBody}
          </p>
          <div style="text-align: center; margin: 30px 0;">
            <a href="${magicLink}" style="background: #FFD700; color: #000; padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 16px;">
              ${config.emailCta}
            </a>
          </div>${extraHtml}
          <p style="color: #666; font-size: 14px; line-height: 1.6;">
            ${emailI18n(config.lang).guardaEmail}
          </p>
          <hr style="border: none; border-top: 1px solid #eee; margin: 30px 0;" />
          <p style="color: #999; font-size: 12px;">
            AI Chef Pro · <a href="https://aichef.pro" style="color: #FFD700;">aichef.pro</a>
          </p>
        </div>
      `,
    }),
  });

  if (!res.ok) {
    const errorBody = await res.text();
    console.error(`Resend API error (${res.status}):`, errorBody);
    throw new Error(`Resend failed: ${res.status} ${errorBody}`);
  }

  console.log('Email sent successfully to:', email);
}
