import type { Handler } from '@netlify/functions';
import { validatePurchase } from '../shared/purchase-validation';
import { abrirLibro, listOrdersByEmail, maskEmail } from '../shared/crypto-orders';
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

const PRODUCTS: Record<string, ProductConfig> = {
  'pro-prompts-ebook': {
    accessPath: '/pro-prompts-library-access',
    emailSubject: 'Tu acceso a Pro Prompts Library',
    emailTitle: 'Accede a tu Pro Prompts Library',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard con todos los prompts y descargas:',
    emailCta: 'Acceder a mi Library',
  },
  // Tienda EN (2026-10-03): gemelo de pro-prompts-ebook (ver verify-purchase.ts).
  'ai-prompts-for-restaurants': {
    accessPath: '/en/digital-products/ai-prompts-for-restaurants/access',
    emailSubject: 'Your access to the Gastro Pro Prompts eBook',
    emailTitle: 'Access your Pro Prompts Library',
    emailBody: 'Click the button to open your dashboard with all the prompts and downloads:',
    emailCta: 'Open my Library',
    lang: 'en',
  },
  'kit-escandallos': {
    accessPath: '/kit-escandallos-access',
    emailSubject: 'Tu acceso al Kit de Escandallos Pro',
    emailTitle: 'Accede a tu Kit de Escandallos Pro',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 13 plantillas Excel + 2 bonus:',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-09-24): gemelo de kit-escandallos (ver verify-purchase.ts).
  'food-cost-templates': {
    accessPath: '/en/digital-products/food-cost-templates/access',
    emailSubject: 'Your access to Food Cost Kit Pro',
    emailTitle: 'Access your Food Cost Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 13 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'pack-appcc': {
    accessPath: '/pack-appcc-access',
    emailSubject: 'Tu acceso al Pack de Plantillas APPCC',
    emailTitle: 'Accede a tu Pack de Plantillas APPCC',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 19 registros + 2 bonus de seguridad alimentaria:',
    emailCta: 'Acceder a mis Plantillas APPCC',
  },
  // Tienda EN (2026-10-03): gemelo de pack-appcc (ver verify-purchase.ts).
  'haccp-templates': {
    accessPath: '/en/digital-products/haccp-templates/access',
    emailSubject: 'Your access to HACCP Food Safety Kit Pro',
    emailTitle: 'Access your HACCP Food Safety Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 19 food safety templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'kit-tareas': {
    accessPath: '/kit-tareas-access',
    emailSubject: 'Tu acceso al Kit de Tareas Recurrentes',
    emailTitle: 'Accede a tu Kit de Tareas Recurrentes',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-cafeteria': {
    accessPath: '/kit-tareas-cafeteria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Cafetería / Brunch',
    emailTitle: 'Accede a tu Kit de Tareas: Cafetería / Brunch',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pizzeria': {
    accessPath: '/kit-tareas-pizzeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pizzería',
    emailTitle: 'Accede a tu Kit de Tareas: Pizzería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hamburgueseria': {
    accessPath: '/kit-tareas-hamburgueseria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Hamburguesería',
    emailTitle: 'Accede a tu Kit de Tareas: Hamburguesería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-dark-kitchen': {
    accessPath: '/kit-tareas-dark-kitchen-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Dark Kitchen',
    emailTitle: 'Accede a tu Kit de Tareas: Dark Kitchen',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pasteleria': {
    accessPath: '/kit-tareas-pasteleria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pastelería / Obrador',
    emailTitle: 'Accede a tu Kit de Tareas: Pastelería / Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 13 checklists operativos + 2 bonus (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-bar': {
    accessPath: '/kit-tareas-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Bar / Cocktails',
    emailTitle: 'Accede a tu Kit de Tareas: Bar / Cocktails',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-catering': {
    accessPath: '/kit-tareas-catering-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Catering / Eventos',
    emailTitle: 'Accede a tu Kit de Tareas: Catering / Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hotel': {
    accessPath: '/kit-tareas-hotel-completo-access',
    emailSubject: 'Tu acceso al Kit Tareas Recurrentes: Hotel Completo — 53 Checklists',
    emailTitle: 'Accede a tu Kit Tareas: Hotel Completo',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 19 ficheros con 53 checklists operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-heladeria': {
    accessPath: '/kit-tareas-heladeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Heladería Artesanal',
    emailTitle: 'Accede a tu Kit de Tareas: Heladería Artesanal',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chocolateria': {
    accessPath: '/kit-tareas-chocolateria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chocolatería / Obrador de Chocolate',
    emailTitle: 'Accede a tu Kit de Tareas: Chocolatería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas + 2 bonus (11 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-restaurante-creativo': {
    accessPath: '/kit-tareas-restaurante-creativo-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Restaurante Creativo / De Autor',
    emailTitle: 'Accede a tu Kit de Tareas: Restaurante Creativo',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 11 plantillas + 2 bonus (13 ficheros) operativos (v2.0):',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chef-privado': {
    accessPath: '/kit-tareas-chef-privado-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chef Privado / Personal Chef',
    emailTitle: 'Accede a tu Kit de Tareas: Chef Privado',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists profesionales:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-gestion-personal': {
    accessPath: '/kit-gestion-personal-access',
    emailSubject: 'Tu acceso al Kit de Gestión de Personal y Turnos',
    emailTitle: 'Accede a tu Kit de Gestión de Personal',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de gestión de personal:',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-10-03): gemelo de kit-gestion-personal (ver verify-purchase.ts).
  'restaurant-schedule-templates': {
    accessPath: '/en/digital-products/restaurant-schedule-templates/access',
    emailSubject: 'Your access to Restaurant Staff Scheduling Kit Pro',
    emailTitle: 'Access your Restaurant Staff Scheduling Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 7 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'kit-inventario': {
    accessPath: '/kit-inventario-access',
    emailSubject: 'Tu acceso al Kit Control de Inventario y Compras',
    emailTitle: 'Accede a tu Kit Control de Inventario',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de control de inventario:',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-09-25): gemelo de kit-inventario (ver verify-purchase.ts).
  'restaurant-inventory-templates': {
    accessPath: '/en/digital-products/restaurant-inventory-templates/access',
    emailSubject: 'Your access to Restaurant Inventory Kit Pro',
    emailTitle: 'Access your Restaurant Inventory Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 7 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'guia-dark-kitchen': {
    accessPath: '/guia-dark-kitchen-access',
    emailSubject: 'Tu acceso a la Guía: Cómo Montar una Dark Kitchen',
    emailTitle: 'Accede a tu Guía Dark Kitchen',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 3 checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-gastronomico': {
    accessPath: '/guia-restaurante-gastronomico-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Gastronómico 65 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Gastronómico',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 20 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-food-cost-ingenieria-menu': {
    accessPath: '/guia-food-cost-ingenieria-menu-access',
    emailSubject: 'Tu acceso a la Guía Food Cost + Ingeniería de Menú',
    emailTitle: 'Accede a tu Guía Food Cost + Ingeniería de Menú',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX, 8 herramientas Excel y el bonus de ejercicios:',
    emailCta: 'Acceder a mi Guía',
  },
  'manual-manager-restaurante': {
    accessPath: '/manual-manager-restaurante-access',
    emailSubject: 'Tu acceso al Manual del Manager de Restaurante',
    emailTitle: 'Accede a tu Manual del Manager de Restaurante',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el manual PDF + DOCX, 7 herramientas Excel y el bonus de 12 situaciones resueltas:',
    emailCta: 'Acceder a mi Manual',
  },
  'manual-chef-ejecutivo': {
    accessPath: '/manual-chef-ejecutivo-access',
    emailSubject: 'Tu acceso al Manual del Chef Ejecutivo',
    emailTitle: 'Accede a tu Manual del Chef Ejecutivo',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el manual PDF + DOCX, 7 herramientas Excel y el bonus de 12 situaciones resueltas en cocina:<br /><br />Si además diriges el negocio —no sólo la cocina—, el <a href="https://aichef.pro/manual-manager-restaurante?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Manual del Manager de Restaurante</a> es su hermano: si llevas las dos cosas, necesitas los dos.',
    emailCta: 'Acceder a mi Manual',
  },
  'guia-pasteleria-obrador': {
    accessPath: '/guia-pasteleria-obrador-access',
    emailSubject: 'Tu acceso a Cómo Montar una Pastelería',
    emailTitle: 'Accede a tu guía Cómo Montar una Pastelería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX (20 capítulos y anexo normativo, 103 páginas), las 8 herramientas Excel con fórmulas vivas, el business plan modelo relleno y las 12 decisiones de apertura resueltas:<br /><br />El día que abras, lo que vas a usar cada mañana es el <a href="https://aichef.pro/kit-tareas-pasteleria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Pastelería</a> (producción, encargos, alérgenos de vitrina y temperaturas). Para el papeleo diario de seguridad alimentaria está el <a href="https://aichef.pro/pack-appcc?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Pack de Plantillas APPCC</a>, para escandallar por formato el <a href="https://aichef.pro/kit-escandallos?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Escandallos Pro</a>, y cuando ya estés vendiendo y toque revisar precios y carta, la <a href="https://aichef.pro/guia-food-cost-ingenieria-menu?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Guía Food Cost + Ingeniería de Menú</a>.',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-chocolateria-obrador': {
    accessPath: '/guia-chocolateria-obrador-access',
    emailSubject: 'Tu acceso a Cómo Montar una Chocolatería Boutique & Atelier',
    emailTitle: 'Accede a tu guía Cómo Montar una Chocolatería Boutique &amp; Atelier',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX (20 capítulos y anexo normativo, 111 páginas), los 9 libros de Excel con fórmulas vivas, el business plan modelo relleno y las 12 decisiones de apertura resueltas (34 páginas):<br /><br />El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes.<br /><br />Cuando abras, lo que vas a usar cada mañana es el <a href="https://aichef.pro/kit-tareas-chocolateria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Chocolatería</a> (templado, moldeado, vitrina y temperaturas). Para el papeleo diario de seguridad alimentaria está el <a href="https://aichef.pro/pack-appcc?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Pack de Plantillas APPCC</a>, para escandallar por formato el <a href="https://aichef.pro/kit-escandallos?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Escandallos Pro</a>, y cuando ya estés vendiendo y toque revisar precios y carta, la <a href="https://aichef.pro/guia-food-cost-ingenieria-menu?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Guía Food Cost + Ingeniería de Menú</a>.',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-churreria-chocolateria': {
    accessPath: '/guia-churreria-chocolateria-access',
    emailSubject: 'Tu acceso a Cómo Montar una Churrería-Chocolatería',
    emailTitle: 'Accede a tu guía Cómo Montar una Churrería-Chocolatería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX (16 capítulos y anexo normativo, 95 páginas), los 8 libros de Excel con fórmulas vivas, el business plan modelo relleno y las 12 decisiones de apertura resueltas (21 páginas):<br /><br />Esta guía es todo lo que hay que decidir antes de abrir.<br /><br />Cuando ya estés trabajando, el registro diario del aceite de fritura va en el <a href="https://aichef.pro/pack-appcc?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Pack de Plantillas APPCC</a>, el cuadrante semana a semana en el <a href="https://aichef.pro/kit-gestion-personal?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit Gestión de Personal y Turnos</a> y el escandallo del resto de tu carta en el <a href="https://aichef.pro/kit-escandallos?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Escandallos Pro</a>. Y si tu plan incluye salir a ferias con un vehículo, tienes el <a href="https://aichef.pro/plan-negocio-food-truck?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Plan de Negocio: Food Truck</a>; si vas a servir churros dentro de una cafetería, el <a href="https://aichef.pro/plan-negocio-cafeteria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Plan de Negocio: Cafetería</a>; y si también te atrae la bombonería, que es otro negocio, la guía <a href="https://aichef.pro/guia-chocolateria-obrador?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Cómo Montar una Chocolatería Boutique &amp; Atelier</a>.',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-casual': {
    accessPath: '/guia-restaurante-casual-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Casual 80 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Casual',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 16 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-mexicano': {
    accessPath: '/guia-restaurante-mexicano-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Mexicano 80 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Mexicano',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-peruano': {
    accessPath: '/guia-restaurante-peruano-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Peruano 80 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Peruano',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-japones': {
    accessPath: '/guia-restaurante-japones-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Japonés 60 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Japonés',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-nikkei': {
    accessPath: '/guia-restaurante-nikkei-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Nikkei 60 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Nikkei',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'mega-pack-tareas': {
    accessPath: '/mega-pack-tareas-access',
    emailSubject: 'Tu acceso al Mega Pack Tareas Recurrentes — 13 Kits',
    emailTitle: 'Accede a tu Mega Pack Tareas Recurrentes',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 151 plantillas:',
    emailCta: 'Acceder a mis 13 Kits',
  },
  'kit-plan-financiero': {
    accessPath: '/kit-plan-financiero-access',
    emailSubject: 'Tu acceso al Kit Plan Financiero para Restaurantes',
    emailTitle: 'Accede a tu Kit Plan Financiero',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 10 plantillas financieras (8 + 2 bonus):',
    emailCta: 'Acceder a mis Plantillas',
  },
  // Tienda EN (2026-10-03): gemelo de kit-plan-financiero (ver verify-purchase.ts).
  'restaurant-financial-plan-templates': {
    accessPath: '/en/digital-products/restaurant-financial-plan-templates/access',
    emailSubject: 'Your access to Restaurant Financial Plan Kit Pro',
    emailTitle: 'Access your Restaurant Financial Plan Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 8 Excel templates + 2 bonuses:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-food-truck (ver verify-purchase.ts).
  'food-truck-business-plan': {
    accessPath: '/en/digital-products/food-truck-business-plan/access',
    emailSubject: 'Your access to Food Truck Business Plan Kit',
    emailTitle: 'Access your Food Truck Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-cafeteria (ver verify-purchase.ts).
  'coffee-shop-business-plan': {
    accessPath: '/en/digital-products/coffee-shop-business-plan/access',
    emailSubject: 'Your access to Coffee Shop Business Plan Kit',
    emailTitle: 'Access your Coffee Shop Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 75-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-bar-restaurante (ver verify-purchase.ts).
  'restaurant-business-plan': {
    accessPath: '/en/digital-products/restaurant-business-plan/access',
    emailSubject: 'Your access to Restaurant Business Plan Kit',
    emailTitle: 'Access your Restaurant Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 64-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-04): gemelo de plan-negocio-panaderia (ver verify-purchase.ts).
  'bakery-business-plan': {
    accessPath: '/en/digital-products/bakery-business-plan/access',
    emailSubject: 'Your access to Bakery Business Plan Kit',
    emailTitle: 'Access your Bakery Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 66-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-11): gemelo de plan-negocio-tapas-bar (ver verify-purchase.ts).
  'bar-business-plan': {
    accessPath: '/en/digital-products/bar-business-plan/access',
    emailSubject: 'Your access to Bar Business Plan Kit',
    emailTitle: 'Access your Bar Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 73-task opening checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-11): gemelo de plan-catering-tematico-eventos (ver verify-purchase.ts).
  'catering-business-plan': {
    accessPath: '/en/digital-products/catering-business-plan/access',
    emailSubject: 'Your access to Catering Business Plan Kit',
    emailTitle: 'Access your Catering Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-13): gemelo de plan-negocio-cocteleria-eventos (ver verify-purchase.ts).
  'mobile-bar-business-plan': {
    accessPath: '/en/digital-products/mobile-bar-business-plan/access',
    emailSubject: 'Your access to Mobile Bar Business Plan Kit',
    emailTitle: 'Access your Mobile Bar Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator with a shopping list for the host and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de plan-negocio-parrillero-asador-eventos (ver verify-purchase.ts).
  'bbq-catering-business-plan': {
    accessPath: '/en/digital-products/bbq-catering-business-plan/access',
    emailSubject: 'Your access to BBQ Catering Business Plan Kit',
    emailTitle: 'Access your BBQ Catering Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator with a smoke schedule and a shopping list by guest count and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de plan-negocio-paellero-eventos (ver verify-purchase.ts).
  'paella-catering-business-plan': {
    accessPath: '/en/digital-products/paella-catering-business-plan/access',
    emailSubject: 'Your access to Paella Catering Business Plan Kit',
    emailTitle: 'Access your Paella Catering Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator with a paella yield and pan sizing table and a shopping list by guest count and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-25): gemelo de plan-negocio-pizzeria (ver verify-purchase.ts).
  'pizza-shop-business-plan': {
    accessPath: '/en/digital-products/pizza-shop-business-plan/access',
    emailSubject: 'Your access to Pizza Shop Business Plan Kit',
    emailTitle: 'Access your Pizza Shop Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pizza dough and food cost calculator and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-27): gemelo de plan-negocio-heladeria (ver verify-purchase.ts).
  'ice-cream-shop-business-plan': {
    accessPath: '/en/digital-products/ice-cream-shop-business-plan/access',
    emailSubject: 'Your access to Ice Cream Shop Business Plan Kit',
    emailTitle: 'Access your Ice Cream Shop Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-27): gemelo de plan-negocio-finca-eventos-bodas (ver verify-purchase.ts).
  'wedding-venue-business-plan': {
    accessPath: '/en/digital-products/wedding-venue-business-plan/access',
    emailSubject: 'Your access to Wedding Venue Business Plan Kit',
    emailTitle: 'Access your Wedding Venue Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing and quote calculator, the venue rental agreement templates and the 84-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-28): gemelo de plan-negocio-cafeteria-movil-eventos (ver verify-purchase.ts).
  'coffee-cart-business-plan': {
    accessPath: '/en/digital-products/coffee-cart-business-plan/access',
    emailSubject: 'Your access to Coffee Cart Business Plan Kit',
    emailTitle: 'Access your Coffee Cart Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the pricing calculator, the coffee catering service agreement template and the 68-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-29): gemelo de plan-negocio-taqueria (ver verify-purchase.ts).
  'taco-shop-business-plan': {
    accessPath: '/en/digital-products/taco-shop-business-plan/access',
    emailSubject: 'Your access to Taco Shop Business Plan Kit',
    emailTitle: 'Access your Taco Shop Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the taco cost and trompo yield calculator and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-29): gemelo de plan-negocio-polleria (ver verify-purchase.ts).
  'rotisserie-chicken-restaurant-business-plan': {
    accessPath: '/en/digital-products/rotisserie-chicken-restaurant-business-plan/access',
    emailSubject: 'Your access to Rotisserie Chicken Restaurant Business Plan Kit',
    emailTitle: 'Access your Rotisserie Chicken Restaurant Business Plan Kit',
    emailBody: 'Click the button to open your dashboard and download the 10-section Word business plan, the Excel financial projections, the chicken yield, rotisserie and costing calculator and the 80-task startup checklist:',
    emailCta: 'Access my business plan',
    lang: 'en',
  },
  // Tienda EN (2026-10-15): gemelo de guia-food-cost-ingenieria-menu (ver verify-purchase.ts).
  'food-cost-menu-engineering-guide': {
    accessPath: '/en/digital-products/food-cost-menu-engineering-guide/access',
    emailSubject: 'Your access to the Food Cost + Menu Engineering Guide',
    emailTitle: 'Access your Food Cost + Menu Engineering Guide',
    emailBody: 'Click the button to open your dashboard and download the guide in PDF + DOCX, the 8 Excel tools, the 12 solved exercises and the Equivalents Guide:',
    emailCta: 'Access my guide',
    lang: 'en',
  },
  // Tienda EN (2026-10-17): gemelo de guia-pasteleria-obrador (ver verify-purchase.ts).
  'how-to-open-a-pastry-shop': {
    accessPath: '/en/digital-products/how-to-open-a-pastry-shop/access',
    emailSubject: 'Your access to How to Open a Pastry Shop',
    emailTitle: 'Access your guide: How to Open a Pastry Shop',
    emailBody: 'Click the button to open your dashboard and download the guide in PDF + DOCX, the 8 Excel tools, the sample business plan, the 12 opening decisions and the Equivalents Guide:',
    emailCta: 'Access my guide',
    lang: 'en',
  },
  // Tienda EN (2026-10-17): gemelo de kit-tareas (ver verify-purchase.ts).
  'restaurant-checklist-templates': {
    accessPath: '/en/digital-products/restaurant-checklist-templates/access',
    emailSubject: 'Your access to Restaurant Checklists Kit Pro',
    emailTitle: 'Access your Restaurant Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-bar (ver verify-purchase.ts).
  'bar-checklist-templates': {
    accessPath: '/en/digital-products/bar-checklist-templates/access',
    emailSubject: 'Your access to Bar Checklists Kit Pro',
    emailTitle: 'Access your Bar Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-cafeteria (ver verify-purchase.ts).
  'coffee-shop-checklist-templates': {
    accessPath: '/en/digital-products/coffee-shop-checklist-templates/access',
    emailSubject: 'Your access to Coffee Shop Checklists Kit Pro',
    emailTitle: 'Access your Coffee Shop Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-catering (ver verify-purchase.ts).
  'catering-checklist-templates': {
    accessPath: '/en/digital-products/catering-checklist-templates/access',
    emailSubject: 'Your access to Catering Checklists Kit Pro',
    emailTitle: 'Access your Catering Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-pizzeria (ver verify-purchase.ts).
  'pizza-shop-checklist-templates': {
    accessPath: '/en/digital-products/pizza-shop-checklist-templates/access',
    emailSubject: 'Your access to Pizza Shop Checklists Kit Pro',
    emailTitle: 'Access your Pizza Shop Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-hamburgueseria (ver verify-purchase.ts).
  'burger-joint-checklist-templates': {
    accessPath: '/en/digital-products/burger-joint-checklist-templates/access',
    emailSubject: 'Your access to Burger Joint Checklists Kit Pro',
    emailTitle: 'Access your Burger Joint Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-18): gemelo de kit-tareas-dark-kitchen (ver verify-purchase.ts).
  'ghost-kitchen-checklist-templates': {
    accessPath: '/en/digital-products/ghost-kitchen-checklist-templates/access',
    emailSubject: 'Your access to Ghost Kitchen Checklists Kit Pro',
    emailTitle: 'Access your Ghost Kitchen Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de kit-tareas-heladeria (ver verify-purchase.ts).
  'ice-cream-shop-checklist-templates': {
    accessPath: '/en/digital-products/ice-cream-shop-checklist-templates/access',
    emailSubject: 'Your access to Ice Cream Shop Checklists Kit Pro',
    emailTitle: 'Access your Ice Cream Shop Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-27): gemelo de kit-tareas-hotel (ver verify-purchase.ts).
  'hotel-checklist-templates': {
    accessPath: '/en/digital-products/hotel-checklist-templates/access',
    emailSubject: 'Your access to Hotel Checklists Kit Pro',
    emailTitle: 'Access your Hotel Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 17 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-31): gemelo de kit-tareas-taqueria (ver verify-purchase.ts).
  'taco-shop-checklist-templates': {
    accessPath: '/en/digital-products/taco-shop-checklist-templates/access',
    emailSubject: 'Your access to Taco Shop Checklists Kit Pro',
    emailTitle: 'Access your Taco Shop Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-31): gemelo de kit-tareas-food-truck (ver verify-purchase.ts).
  'food-truck-checklist-templates': {
    accessPath: '/en/digital-products/food-truck-checklist-templates/access',
    emailSubject: 'Your access to Food Truck Checklists Kit Pro',
    emailTitle: 'Access your Food Truck Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-31): gemelo de kit-tareas-panaderia (ver verify-purchase.ts).
  'bakery-checklist-templates': {
    accessPath: '/en/digital-products/bakery-checklist-templates/access',
    emailSubject: 'Your access to Bakery Checklists Kit Pro',
    emailTitle: 'Access your Bakery Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de kit-tareas-chocolateria (ver verify-purchase.ts).
  'chocolate-shop-checklist-templates': {
    accessPath: '/en/digital-products/chocolate-shop-checklist-templates/access',
    emailSubject: 'Your access to Chocolate Shop Checklists Kit Pro',
    emailTitle: 'Access your Chocolate Shop Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 9 Excel checklist templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  // Tienda EN (2026-10-24): gemelo de kit-tareas-pasteleria (ver verify-purchase.ts).
  'pastry-shop-checklist-templates': {
    accessPath: '/en/digital-products/pastry-shop-checklist-templates/access',
    emailSubject: 'Your access to Pastry Shop Checklists Kit Pro',
    emailTitle: 'Access your Pastry Shop Checklists Kit Pro',
    emailBody: 'Click the button to open your dashboard and download the 13 Excel templates, the 2 bonus templates and the Equivalents Guide:',
    emailCta: 'Access my templates',
    lang: 'en',
  },
  'kit-tareas-sushi-bar': {
    accessPath: '/kit-tareas-sushi-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Sushi Bar',
    emailTitle: 'Accede a tu Kit de Tareas: Sushi Bar',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos con protocolo anisakis APPCC:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-taqueria': {
    accessPath: '/kit-tareas-taqueria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Taquería Mexicana',
    emailTitle: 'Accede a tu Kit de Tareas: Taquería Mexicana',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos con trompo, nixtamal y tortillería, barra de salsas y APPCC:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-asador': {
    accessPath: '/kit-tareas-asador-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Asador / Parrilla y Josper',
    emailTitle: 'Accede a tu Kit de Tareas: Asador / Parrilla y Josper',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos del horno Josper, brasas y maduración:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-marisqueria': {
    accessPath: '/kit-tareas-marisqueria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Marisquería con Vivero y APPCC',
    emailTitle: 'Accede a tu Kit de Tareas: Marisquería con Vivero y APPCC',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos del vivero, expositor de hielo y trazabilidad APPCC marisco:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-tapas-bar': {
    accessPath: '/kit-tareas-tapas-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Tapas Bar / Gastrobar',
    emailTitle: 'Accede a tu Kit de Tareas: Tapas Bar / Gastrobar',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos de barra de pinchos, cocina de raciones, cerveza grifo, vinos por copa y vermut:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-food-truck': {
    accessPath: '/kit-tareas-food-truck-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Food Truck',
    emailTitle: 'Accede a tu Kit de Tareas: Food Truck',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos de setup, teardown, APPCC móvil, permisos y eventos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-panaderia': {
    accessPath: '/kit-tareas-panaderia-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Panadería / Obrador',
    emailTitle: 'Accede a tu Kit de Tareas: Panadería / Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos de turno madrugada, masas madre, hornos, expositor y campañas estacionales:',
    emailCta: 'Acceder a mis Checklists',
  },
  'guia-panaderia-obrador': {
    accessPath: '/guia-panaderia-obrador-access',
    emailSubject: 'Tu acceso a la Guía: Panadería con Obrador',
    emailTitle: 'Accede a tu Guía Panadería con Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel + manual del obrador:',
    emailCta: 'Acceder a mi Guía',
  },
  'plan-negocio-bar-restaurante': {
    accessPath: '/plan-negocio-bar-restaurante-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Bar-Restaurante',
    emailTitle: 'Accede a tu Plan de Negocio: Bar-Restaurante',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-tapas-bar': {
    accessPath: '/plan-negocio-tapas-bar-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Tapas Bar / Gastrobar',
    emailTitle: 'Accede a tu Plan de Negocio: Tapas Bar / Gastrobar',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el documento DOCX, el plan financiero Excel y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cafeteria': {
    accessPath: '/plan-negocio-cafeteria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Cafetería / Brunch',
    emailTitle: 'Accede a tu Plan de Negocio: Cafetería / Brunch',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-panaderia': {
    accessPath: '/plan-negocio-panaderia-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Panadería / Obrador',
    emailTitle: 'Accede a tu Plan de Negocio: Panadería / Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-heladeria': {
    accessPath: '/plan-negocio-heladeria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Heladería Artesanal',
    emailTitle: 'Accede a tu Plan de Negocio: Heladería Artesanal',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word (10 secciones), el plan financiero en Excel (9 hojas con fórmulas vivas), el checklist de apertura (80 tareas en 6 fases) y la Guía de Equivalencias para Latinoamérica:<br /><br />Para el día a día del obrador y el mostrador, el <a href="https://aichef.pro/kit-tareas-heladeria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Heladería</a> es su hermano: el plan te dice cómo abrir, el kit cómo operar cada jornada.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-finca-eventos-bodas': {
    accessPath: '/plan-negocio-finca-eventos-bodas-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Finca de Eventos y Bodas',
    emailTitle: 'Accede a tu Plan de Negocio: Finca de Eventos y Bodas',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word (10 secciones), el plan financiero en Excel (9 hojas con fórmulas vivas), el checklist de apertura (84 tareas en 6 fases), la calculadora de presupuesto del espacio, los modelos de contrato y la Guía de Equivalencias para Latinoamérica:<br /><br />Para el día a día del servicio de tu catering, el <a href="https://aichef.pro/kit-tareas-catering?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Catering</a> es su hermano: el plan te dice cómo abrir la finca, el kit cómo operar cada evento.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cafeteria-movil-eventos': {
    accessPath: '/plan-negocio-cafeteria-movil-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Cafetería Móvil para Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Cafetería Móvil para Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas en 6 fases, calculadora de escandallo y presupuesto por evento, modelo de contrato de servicio (particular y anexo para empresas y ferias) y guía de equivalencias para 21 países:<br /><br />Para el día a día de la barra y el servicio, el <a href="https://aichef.pro/kit-tareas-cafeteria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Cafetería</a> es su hermano: el plan te dice cómo montar el negocio, el kit cómo operar cada turno.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-pizzeria': {
    accessPath: '/plan-negocio-pizzeria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Pizzería Napolitana',
    emailTitle: 'Accede a tu Plan de Negocio: Pizzería Napolitana',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas, calculadora de masa y escandallo por pizza y guía de equivalencias para Hispanoamérica:<br /><br />Para el día a día del horno y el servicio, el <a href="https://aichef.pro/kit-tareas-pizzeria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Pizzería</a> es su hermano: el plan te dice cómo abrir, el kit cómo operar cada turno.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-taqueria': {
    accessPath: '/plan-negocio-taqueria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Taquería',
    emailTitle: 'Accede a tu Plan de Negocio: Taquería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas en 6 fases, calculadora del trompo y escandallo por taco de 4 hojas y guía de equivalencias para Hispanoamérica:<br /><br />Para el día a día del trompo y el servicio, el <a href="https://aichef.pro/kit-tareas-taqueria?utm_source=email&amp;utm_medium=postpago&amp;utm_campaign=cross-sell" style="color: #b8860b;">Kit de Tareas Taquería Mexicana</a> es su hermano: el plan te dice cómo abrir, el kit cómo operar cada turno.',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-polleria': {
    accessPath: '/plan-negocio-polleria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Pollería y Asador de Pollos',
    emailTitle: 'Accede a tu Plan de Negocio: Pollería y Asador de Pollos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan de negocio en Word de 10 secciones con las cinco corrientes del pollo asado, plan financiero en Excel de 9 hojas, checklist de apertura de 80 tareas en 6 fases, calculadora del pollo, el asador y el escandallo de 4 hojas y guía de equivalencias para Hispanoamérica:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-food-truck': {
    accessPath: '/plan-negocio-food-truck-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Food Truck',
    emailTitle: 'Accede a tu Plan de Negocio: Food Truck',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el documento DOCX, el plan financiero Excel y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cocteleria-eventos': {
    accessPath: '/plan-negocio-cocteleria-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Coctelería de Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Coctelería de Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 10 entregables del kit de coctelería de eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-parrillero-asador-eventos': {
    accessPath: '/plan-negocio-parrillero-asador-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Parrillero / Asador para Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Parrillero / Asador para Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables del kit de parrillero / asador para eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-paellero-eventos': {
    accessPath: '/plan-negocio-paellero-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Paellero / Paella para Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Paellero / Paella para Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables del kit de paellero / paella para eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-chef-privado-showcooking-eventos': {
    accessPath: '/plan-chef-privado-showcooking-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Chef Privado / Showcooking a Domicilio',
    emailTitle: 'Accede a tu Plan de Negocio: Chef Privado / Showcooking a Domicilio',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables del kit de chef privado y showcooking a domicilio:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-catering-tematico-eventos': {
    accessPath: '/plan-catering-tematico-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Catering & Kit Temático para Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Catering & Kit Temático para Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 12 entregables del kit de catering temático multi-concepto para eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
};

// ── Envío del magic link ────────────────────────────────────────
// Extraído del handler (2026-09-05) para que la ruta cripto reutilice EXACTAMENTE
// el mismo email que la de Stripe. El HTML no se ha tocado ni un byte: es el
// que había en línea en el handler, movido tal cual.
async function enviarEmailAcceso(
  emailNorm: string,
  token: string,
  config: ProductConfig,
): Promise<{ ok: true } | { ok: false; status: number }> {
  const magicLink = `https://aichef.pro${config.accessPath}?jwt=${token}`;

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
    },
    body: JSON.stringify({
      from: 'AI Chef Pro <noreply@contact.aichef.pro>',
      to: emailNorm,
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
            </div>
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
    return { ok: false, status: res.status };
  }
  return { ok: true };
}

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
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    const { email, product } = JSON.parse(event.body || '{}');
    if (!email) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'Email required' }) };
    }

    // Reject an explicitly-provided but unknown product (avoid silent fallback to pro-prompts-ebook).
    // Legacy callers that omit `product` (undefined/null) keep the pro-prompts-ebook fallback.
    if (product != null && !PRODUCTS[product]) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'unknown_product' }) };
    }

    const productId = product && PRODUCTS[product] ? product : 'pro-prompts-ebook';
    const config = PRODUCTS[productId];

    // El cliente teclea el email a mano en "¿Ya compraste?": normalizar espacios/mayúsculas.
    const emailNorm = String(email).trim().toLowerCase();

    // ── Ruta CRIPTO, primero (2026-09-05) ─────────────────────────────────
    // Se consulta el libro de pedidos ANTES que Stripe y sin depender de
    // PURCHASE_VALIDATION (spec PAGOS_CRYPTO_NOWPAYMENTS.md:176): quien pagó en
    // cripto no tiene ninguna sesión de Stripe, así que la ruta de abajo le
    // devolvería «No purchase found» aunque su compra esté entregada y cobrada.
    // FAIL-SOFT a propósito: si Blobs no responde se sigue con Stripe — un
    // comprador de tarjeta no puede quedarse sin su enlace porque falle el
    // libro cripto, que es la vía minoritaria.
    try {
      const store = await abrirLibro(event);
      const pedidos = await listOrdersByEmail(store, emailNorm);
      const servido = pedidos.find((o) => o.delivered && o.productId === productId);
      if (servido) {
        const jwt = (await import('jsonwebtoken')).default;
        const token = jwt.sign({ email: emailNorm, product: productId }, process.env.JWT_SECRET!, {
          expiresIn: '365d',
        });
        const envio = await enviarEmailAcceso(emailNorm, token, config);
        if (!envio.ok) {
          return { statusCode: 500, headers, body: JSON.stringify({ error: `Email send failed: ${envio.status}` }) };
        }
        console.log(`[resend-access] reenvío CRIPTO: ${productId} → ${maskEmail(emailNorm)} (pedido ${servido.orderId})`);
        return { statusCode: 200, headers, body: JSON.stringify({ sent: true, via: 'crypto' }) };
      }
    } catch (err) {
      console.error('[resend-access] libro cripto no consultable (se sigue con Stripe):', err);
    }

    // Search Stripe for completed checkout sessions with this email
    const Stripe = (await import('stripe')).default;
    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, { apiVersion: '2024-12-18.acacia' });

    // Se consulta Stripe con la variante normalizada Y la literal (bug "email case-sensitive",
    // catalogado en CB PRODUCTOS-DIGITALES-ROADMAP §2). Se conserva la literal para no romper
    // a quien pagó con mayúsculas si el filtro de Stripe resultara sensible a ellas.
    // (`emailNorm` se calcula arriba: lo necesita también la ruta cripto.)
    const variants = emailNorm === email ? [email] : [emailNorm, email];
    const results = await Promise.all(
      variants.map((e) => stripe.checkout.sessions.list({ customer_details: { email: e }, limit: 100 }))
    );
    const allSessions = results.flatMap((r) => r.data);

    const paidSessions = allSessions.filter((s) => s.payment_status === 'paid');

    if (!paidSessions.length) {
      return { statusCode: 404, headers, body: JSON.stringify({ error: 'No purchase found' }) };
    }

    // Elegir la sesión que pagó ESTE producto (no cualquier compra del email):
    // ver netlify/shared/purchase-validation.ts. En modo soft, si ninguna coincide se concede
    // igualmente (y se loguea); en strict es 404 para este producto.
    let paidSession: (typeof paidSessions)[number] | null = null;
    let mode: 'off' | 'soft' | 'strict' = 'soft';
    for (const s of paidSessions) {
      const v = await validatePurchase(stripe, s, productId, 'resend-access');
      mode = v.mode;
      if (v.verdict === 'match' || v.verdict === 'unknown' || mode === 'off') {
        paidSession = s;
        break;
      }
    }
    if (!paidSession) {
      console.warn(`[purchase-validation] resend-access: ${emailNorm} tiene ${paidSessions.length} compra(s) pero ninguna de ${productId} (modo ${mode})`);
      if (mode === 'strict') {
        return { statusCode: 404, headers, body: JSON.stringify({ error: 'No purchase found for this product' }) };
      }
      paidSession = paidSessions[0];
    }

    // Generate new JWT and send email
    const jwt = (await import('jsonwebtoken')).default;
    const token = jwt.sign(
      { email: emailNorm, product: productId },
      process.env.JWT_SECRET!,
      { expiresIn: '365d' }
    );

    const envio = await enviarEmailAcceso(emailNorm, token, config);
    if (!envio.ok) {
      return { statusCode: 500, headers, body: JSON.stringify({ error: `Email send failed: ${envio.status}` }) };
    }

    console.log('Resend-access email sent to:', email);
    return { statusCode: 200, headers, body: JSON.stringify({ sent: true }) };
  } catch (err) {
    console.error('resend-access error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ error: 'Server error' }) };
  }
};
