/**
 * Registro de la zona app post-pago (Fase 5) — 44 productos.
 *
 * Extraído VERBATIM de la SPA el 2026-07-19 (censo con verificación cruzada
 * 44/44: storageKey gate == ProtectedRoute, dashboardPath == ruta -library,
 * productIds 1:1 con el mapa PRODUCTS de netlify/functions/verify-purchase.ts).
 *
 * ⚠️ IMPORTANTE — qué es y qué NO es este fichero:
 *  - ES el índice para generar las páginas .astro (-access y -library) y sus
 *    <title>, y para gates de verificación (conteos, QA de rutas).
 *  - NO es fuente de configuración de dinero: las 5 props de cada gate
 *    (productId, storageKey, dashboardPath, landingPath, productLabel) viven
 *    hardcodeadas en los wrappers de la SPA (src/pages/*AccessGate.tsx), que
 *    los islands importan TAL CUAL. Si esto divergiera de la SPA, el island
 *    seguiría comportándose como la SPA — el drift solo rompería títulos o
 *    generación de páginas, nunca el flujo de verificación de compra.
 *
 * Quirks heredados de la SPA (NO "corregir" — paridad D6):
 *  - kit-tareas-hotel: accessPath lleva "-completo-" extra (App.tsx:548;
 *    verify-purchase.ts:91 genera el email con ese mismo path).
 *  - kit-tareas-hamburgueseria: el fichero/componente del gate tiene typo
 *    "Hamburguseria" (sin la e) — App.tsx:67. Props internas correctas.
 *  - pro-prompts: gate vanilla AccessGate.tsx sin campo `product` en el body
 *    (cae al fallback legacy 'pro-prompts-ebook' de verify-purchase.ts:340-346);
 *    ProtectedRoute sin props (defaults 'pro-prompts-jwt' / '/pro-prompts-ebook');
 *    el "dashboard" es ProPromptsLibrary.tsx (único sin sufijo Dashboard).
 *  - kit-escandallos: gate vanilla con valores hardcodeados consistentes.
 */

export interface ProductoZonaApp {
  productId: string;
  accessPath: string;
  libraryPath: string;
  landingPath: string;
  storageKey: string;
  productLabel: string;
  /** Nombre de fichero (sin .tsx) en src/pages/ de la SPA. */
  gateComponent: string;
  /** Nombre de fichero (sin .tsx) en src/pages/ de la SPA. */
  dashboardComponent: string;
  /** <title> verbatim del Helmet del dashboard (se rellena en S2 con byte-verify). */
  libraryTitle?: string;
  vanilla?: boolean;
  notas?: string;
}

/** Título compartido por los 44 gates (verbatim de ProductAccessGate.tsx:68,
 *  AccessGate.tsx y KitEscandallosAccessGate.tsx — idéntico en los 3). */
export const ACCESS_TITLE = 'Verificando acceso... | AI Chef Pro';

export const PRODUCTOS_ZONA_APP: ProductoZonaApp[] = [
  { productId: 'kit-escandallos', accessPath: '/kit-escandallos-access', libraryPath: '/kit-escandallos-library', landingPath: '/kit-escandallos', storageKey: 'kit-escandallos-jwt', productLabel: 'Kit de Escandallos', gateComponent: 'KitEscandallosAccessGate', dashboardComponent: 'KitEscandallosDashboard', vanilla: true, notas: 'Gate vanilla: props hardcodeadas inline (src/pages/KitEscandallosAccessGate.tsx)' },
  { productId: 'pack-appcc', accessPath: '/pack-appcc-access', libraryPath: '/pack-appcc-library', landingPath: '/pack-appcc', storageKey: 'pack-appcc-jwt', productLabel: 'Pack APPCC', gateComponent: 'PackAppccAccessGate', dashboardComponent: 'PackAppccDashboard' },
  { productId: 'kit-tareas', accessPath: '/kit-tareas-access', libraryPath: '/kit-tareas-library', landingPath: '/kit-tareas', storageKey: 'kit-tareas-jwt', productLabel: 'Kit de Tareas', gateComponent: 'KitTareasAccessGate', dashboardComponent: 'KitTareasDashboard' },
  { productId: 'kit-tareas-cafeteria', accessPath: '/kit-tareas-cafeteria-access', libraryPath: '/kit-tareas-cafeteria-library', landingPath: '/kit-tareas-cafeteria', storageKey: 'kit-tareas-cafeteria-jwt', productLabel: 'Kit de Tareas Cafetería', gateComponent: 'KitTareasCafeteriaAccessGate', dashboardComponent: 'KitTareasCafeteriaDashboard' },
  { productId: 'kit-tareas-pizzeria', accessPath: '/kit-tareas-pizzeria-access', libraryPath: '/kit-tareas-pizzeria-library', landingPath: '/kit-tareas-pizzeria', storageKey: 'kit-tareas-pizzeria-jwt', productLabel: 'Kit de Tareas Pizzería', gateComponent: 'KitTareasPizzeriaAccessGate', dashboardComponent: 'KitTareasPizzeriaDashboard' },
  { productId: 'kit-tareas-hamburgueseria', accessPath: '/kit-tareas-hamburgueseria-access', libraryPath: '/kit-tareas-hamburgueseria-library', landingPath: '/kit-tareas-hamburgueseria', storageKey: 'kit-tareas-hamburgueseria-jwt', productLabel: 'Kit de Tareas Hamburguesería', gateComponent: 'KitTareasHamburguseriaAccessGate', dashboardComponent: 'KitTareasHamburgueseriaDashboard', notas: 'QUIRK: gateComponent con typo "Hamburguseria" (sin la e) — así en la SPA (App.tsx:67). NO corregir.' },
  { productId: 'kit-tareas-dark-kitchen', accessPath: '/kit-tareas-dark-kitchen-access', libraryPath: '/kit-tareas-dark-kitchen-library', landingPath: '/kit-tareas-dark-kitchen', storageKey: 'kit-tareas-dark-kitchen-jwt', productLabel: 'Kit de Tareas Dark Kitchen', gateComponent: 'KitTareasDarkKitchenAccessGate', dashboardComponent: 'KitTareasDarkKitchenDashboard' },
  { productId: 'kit-tareas-pasteleria', accessPath: '/kit-tareas-pasteleria-access', libraryPath: '/kit-tareas-pasteleria-library', landingPath: '/kit-tareas-pasteleria', storageKey: 'kit-tareas-pasteleria-jwt', productLabel: 'Kit de Tareas Pastelería', gateComponent: 'KitTareasPasteleriaAccessGate', dashboardComponent: 'KitTareasPasteleriaDashboard' },
  { productId: 'kit-tareas-bar', accessPath: '/kit-tareas-bar-access', libraryPath: '/kit-tareas-bar-library', landingPath: '/kit-tareas-bar', storageKey: 'kit-tareas-bar-jwt', productLabel: 'Kit de Tareas Bar', gateComponent: 'KitTareasBarAccessGate', dashboardComponent: 'KitTareasBarDashboard' },
  { productId: 'kit-tareas-catering', accessPath: '/kit-tareas-catering-access', libraryPath: '/kit-tareas-catering-library', landingPath: '/kit-tareas-catering', storageKey: 'kit-tareas-catering-jwt', productLabel: 'Kit de Tareas Catering', gateComponent: 'KitTareasCateringAccessGate', dashboardComponent: 'KitTareasCateringDashboard' },
  { productId: 'kit-tareas-hotel', accessPath: '/kit-tareas-hotel-completo-access', libraryPath: '/kit-tareas-hotel-library', landingPath: '/kit-tareas-hotel', storageKey: 'kit-tareas-hotel-jwt', productLabel: 'Kit de Tareas Hotel', gateComponent: 'KitTareasHotelAccessGate', dashboardComponent: 'KitTareasHotelDashboard', notas: 'QUIRK: accessPath con "-completo-" extra (App.tsx:548; verify-purchase.ts:91). NO regularizar.' },
  { productId: 'kit-tareas-heladeria', accessPath: '/kit-tareas-heladeria-access', libraryPath: '/kit-tareas-heladeria-library', landingPath: '/kit-tareas-heladeria', storageKey: 'kit-tareas-heladeria-jwt', productLabel: 'Kit de Tareas Heladería', gateComponent: 'KitTareasHeladeriaAccessGate', dashboardComponent: 'KitTareasHeladeriaDashboard' },
  { productId: 'kit-tareas-chocolateria', accessPath: '/kit-tareas-chocolateria-access', libraryPath: '/kit-tareas-chocolateria-library', landingPath: '/kit-tareas-chocolateria', storageKey: 'kit-tareas-chocolateria-jwt', productLabel: 'Kit de Tareas Chocolatería', gateComponent: 'KitTareasChocolateriaAccessGate', dashboardComponent: 'KitTareasChocolateriaDashboard' },
  { productId: 'kit-tareas-restaurante-creativo', accessPath: '/kit-tareas-restaurante-creativo-access', libraryPath: '/kit-tareas-restaurante-creativo-library', landingPath: '/kit-tareas-restaurante-creativo', storageKey: 'kit-tareas-restaurante-creativo-jwt', productLabel: 'Kit de Tareas Restaurante Creativo', gateComponent: 'KitTareasRestauranteCreativoAccessGate', dashboardComponent: 'KitTareasRestauranteCreativoDashboard' },
  { productId: 'kit-tareas-chef-privado', accessPath: '/kit-tareas-chef-privado-access', libraryPath: '/kit-tareas-chef-privado-library', landingPath: '/kit-tareas-chef-privado', storageKey: 'kit-tareas-chef-privado-jwt', productLabel: 'Kit de Tareas Chef Privado', gateComponent: 'KitTareasChefPrivadoAccessGate', dashboardComponent: 'KitTareasChefPrivadoDashboard' },
  { productId: 'kit-tareas-sushi-bar', accessPath: '/kit-tareas-sushi-bar-access', libraryPath: '/kit-tareas-sushi-bar-library', landingPath: '/kit-tareas-sushi-bar', storageKey: 'kit-tareas-sushi-bar-jwt', productLabel: 'Kit de Tareas Sushi Bar', gateComponent: 'KitTareasSushiBarAccessGate', dashboardComponent: 'KitTareasSushiBarDashboard' },
  { productId: 'plan-negocio-bar-restaurante', accessPath: '/plan-negocio-bar-restaurante-access', libraryPath: '/plan-negocio-bar-restaurante-library', landingPath: '/plan-negocio-bar-restaurante', storageKey: 'plan-negocio-bar-restaurante-jwt', productLabel: 'Plan de Negocio Bar-Restaurante', gateComponent: 'PlanNegocioBarRestauranteAccessGate', dashboardComponent: 'PlanNegocioBarRestauranteDashboard' },
  { productId: 'plan-negocio-tapas-bar', accessPath: '/plan-negocio-tapas-bar-access', libraryPath: '/plan-negocio-tapas-bar-library', landingPath: '/plan-negocio-tapas-bar', storageKey: 'plan-negocio-tapas-bar-jwt', productLabel: 'Plan de Negocio Tapas Bar', gateComponent: 'PlanNegocioTapasBarAccessGate', dashboardComponent: 'PlanNegocioTapasBarDashboard' },
  { productId: 'plan-negocio-cafeteria', accessPath: '/plan-negocio-cafeteria-access', libraryPath: '/plan-negocio-cafeteria-library', landingPath: '/plan-negocio-cafeteria', storageKey: 'plan-negocio-cafeteria-jwt', productLabel: 'Plan de Negocio Cafetería', gateComponent: 'PlanNegocioCafeteriaAccessGate', dashboardComponent: 'PlanNegocioCafeteriaDashboard' },
  { productId: 'plan-negocio-panaderia', accessPath: '/plan-negocio-panaderia-access', libraryPath: '/plan-negocio-panaderia-library', landingPath: '/plan-negocio-panaderia', storageKey: 'plan-negocio-panaderia-jwt', productLabel: 'Plan de Negocio Panadería', gateComponent: 'PlanNegocioPanaderiaAccessGate', dashboardComponent: 'PlanNegocioPanaderiaDashboard' },
  { productId: 'plan-negocio-food-truck', accessPath: '/plan-negocio-food-truck-access', libraryPath: '/plan-negocio-food-truck-library', landingPath: '/plan-negocio-food-truck', storageKey: 'plan-negocio-food-truck-jwt', productLabel: 'Plan de Negocio Food Truck', gateComponent: 'PlanNegocioFoodTruckAccessGate', dashboardComponent: 'PlanNegocioFoodTruckDashboard' },
  { productId: 'plan-negocio-cocteleria-eventos', accessPath: '/plan-negocio-cocteleria-eventos-access', libraryPath: '/plan-negocio-cocteleria-eventos-library', landingPath: '/plan-negocio-cocteleria-eventos', storageKey: 'plan-negocio-cocteleria-eventos-jwt', productLabel: 'Plan de Negocio Coctelería de Eventos', gateComponent: 'PlanNegocioCocteleriaEventosAccessGate', dashboardComponent: 'PlanNegocioCocteleriaEventosDashboard' },
  { productId: 'plan-negocio-parrillero-asador-eventos', accessPath: '/plan-negocio-parrillero-asador-eventos-access', libraryPath: '/plan-negocio-parrillero-asador-eventos-library', landingPath: '/plan-negocio-parrillero-asador-eventos', storageKey: 'plan-negocio-parrillero-asador-eventos-jwt', productLabel: 'Plan de Negocio Parrillero / Asador Eventos', gateComponent: 'PlanNegocioParrilleroAsadorEventosAccessGate', dashboardComponent: 'PlanNegocioParrilleroAsadorEventosDashboard' },
  { productId: 'plan-negocio-paellero-eventos', accessPath: '/plan-negocio-paellero-eventos-access', libraryPath: '/plan-negocio-paellero-eventos-library', landingPath: '/plan-negocio-paellero-eventos', storageKey: 'plan-negocio-paellero-eventos-jwt', productLabel: 'Plan de Negocio Paellero / Paella Eventos', gateComponent: 'PlanNegocioPaelleroEventosAccessGate', dashboardComponent: 'PlanNegocioPaelleroEventosDashboard' },
  { productId: 'plan-chef-privado-showcooking-eventos', accessPath: '/plan-chef-privado-showcooking-eventos-access', libraryPath: '/plan-chef-privado-showcooking-eventos-library', landingPath: '/plan-chef-privado-showcooking-eventos', storageKey: 'plan-chef-privado-showcooking-eventos-jwt', productLabel: 'Plan de Negocio Chef Privado / Showcooking a Domicilio', gateComponent: 'PlanChefPrivadoShowcookingEventosAccessGate', dashboardComponent: 'PlanChefPrivadoShowcookingEventosDashboard' },
  { productId: 'plan-catering-tematico-eventos', accessPath: '/plan-catering-tematico-eventos-access', libraryPath: '/plan-catering-tematico-eventos-library', landingPath: '/plan-catering-tematico-eventos', storageKey: 'plan-catering-tematico-eventos-jwt', productLabel: 'Plan de Negocio para Catering & Kit Temático para Eventos', gateComponent: 'PlanCateringTematicoEventosAccessGate', dashboardComponent: 'PlanCateringTematicoEventosDashboard' },
  { productId: 'kit-tareas-asador', accessPath: '/kit-tareas-asador-access', libraryPath: '/kit-tareas-asador-library', landingPath: '/kit-tareas-asador', storageKey: 'kit-tareas-asador-jwt', productLabel: 'Kit de Tareas Asador', gateComponent: 'KitTareasAsadorAccessGate', dashboardComponent: 'KitTareasAsadorDashboard', libraryTitle: 'Kit de Tareas Asador — Dashboard | AI Chef Pro' },
  { productId: 'kit-tareas-marisqueria', accessPath: '/kit-tareas-marisqueria-access', libraryPath: '/kit-tareas-marisqueria-library', landingPath: '/kit-tareas-marisqueria', storageKey: 'kit-tareas-marisqueria-jwt', productLabel: 'Kit de Tareas Marisquería', gateComponent: 'KitTareasMarisqueriaAccessGate', dashboardComponent: 'KitTareasMarisqueriaDashboard' },
  { productId: 'kit-tareas-tapas-bar', accessPath: '/kit-tareas-tapas-bar-access', libraryPath: '/kit-tareas-tapas-bar-library', landingPath: '/kit-tareas-tapas-bar', storageKey: 'kit-tareas-tapas-bar-jwt', productLabel: 'Kit de Tareas Tapas Bar', gateComponent: 'KitTareasTapasBarAccessGate', dashboardComponent: 'KitTareasTapasBarDashboard' },
  { productId: 'kit-tareas-food-truck', accessPath: '/kit-tareas-food-truck-access', libraryPath: '/kit-tareas-food-truck-library', landingPath: '/kit-tareas-food-truck', storageKey: 'kit-tareas-food-truck-jwt', productLabel: 'Kit de Tareas Food Truck', gateComponent: 'KitTareasFoodTruckAccessGate', dashboardComponent: 'KitTareasFoodTruckDashboard' },
  { productId: 'kit-tareas-panaderia', accessPath: '/kit-tareas-panaderia-access', libraryPath: '/kit-tareas-panaderia-library', landingPath: '/kit-tareas-panaderia', storageKey: 'kit-tareas-panaderia-jwt', productLabel: 'Kit de Tareas Panadería', gateComponent: 'KitTareasPanaderiaAccessGate', dashboardComponent: 'KitTareasPanaderiaDashboard' },
  { productId: 'kit-gestion-personal', accessPath: '/kit-gestion-personal-access', libraryPath: '/kit-gestion-personal-library', landingPath: '/kit-gestion-personal', storageKey: 'kit-gestion-personal-jwt', productLabel: 'Kit de Gestión de Personal', gateComponent: 'KitGestionPersonalAccessGate', dashboardComponent: 'KitGestionPersonalDashboard' },
  { productId: 'kit-inventario', accessPath: '/kit-inventario-access', libraryPath: '/kit-inventario-library', landingPath: '/kit-inventario', storageKey: 'kit-inventario-jwt', productLabel: 'Kit de Inventario', gateComponent: 'KitInventarioAccessGate', dashboardComponent: 'KitInventarioDashboard' },
  { productId: 'guia-dark-kitchen', accessPath: '/guia-dark-kitchen-access', libraryPath: '/guia-dark-kitchen-library', landingPath: '/guia-dark-kitchen', storageKey: 'guia-dark-kitchen-jwt', productLabel: 'Guía Dark Kitchen', gateComponent: 'GuiaDarkKitchenAccessGate', dashboardComponent: 'GuiaDarkKitchenDashboard' },
  { productId: 'guia-restaurante-gastronomico', accessPath: '/guia-restaurante-gastronomico-access', libraryPath: '/guia-restaurante-gastronomico-library', landingPath: '/guia-restaurante-gastronomico', storageKey: 'guia-restaurante-gastronomico-jwt', productLabel: 'Guía Restaurante Gastronómico', gateComponent: 'GuiaRestauranteGastronomicoAccessGate', dashboardComponent: 'GuiaRestauranteGastronomicoDashboard' },
  { productId: 'guia-restaurante-casual', accessPath: '/guia-restaurante-casual-access', libraryPath: '/guia-restaurante-casual-library', landingPath: '/guia-restaurante-casual', storageKey: 'guia-restaurante-casual-jwt', productLabel: 'Guía Restaurante Casual', gateComponent: 'GuiaRestauranteCasualAccessGate', dashboardComponent: 'GuiaRestauranteCasualDashboard' },
  { productId: 'guia-panaderia-obrador', accessPath: '/guia-panaderia-obrador-access', libraryPath: '/guia-panaderia-obrador-library', landingPath: '/guia-panaderia-obrador', storageKey: 'guia-panaderia-obrador-jwt', productLabel: 'Guía Panadería con Obrador', gateComponent: 'GuiaPanaderiaObradorAccessGate', dashboardComponent: 'GuiaPanaderiaObradorDashboard' },
  { productId: 'guia-restaurante-mexicano', accessPath: '/guia-restaurante-mexicano-access', libraryPath: '/guia-restaurante-mexicano-library', landingPath: '/guia-restaurante-mexicano', storageKey: 'guia-restaurante-mexicano-jwt', productLabel: 'Guía Restaurante Mexicano', gateComponent: 'GuiaRestauranteMexicanoAccessGate', dashboardComponent: 'GuiaRestauranteMexicanoDashboard' },
  { productId: 'guia-restaurante-peruano', accessPath: '/guia-restaurante-peruano-access', libraryPath: '/guia-restaurante-peruano-library', landingPath: '/guia-restaurante-peruano', storageKey: 'guia-restaurante-peruano-jwt', productLabel: 'Guía Restaurante Peruano', gateComponent: 'GuiaRestaurantePeruanoAccessGate', dashboardComponent: 'GuiaRestaurantePeruanoDashboard' },
  { productId: 'guia-restaurante-japones', accessPath: '/guia-restaurante-japones-access', libraryPath: '/guia-restaurante-japones-library', landingPath: '/guia-restaurante-japones', storageKey: 'guia-restaurante-japones-jwt', productLabel: 'Guía Restaurante Japonés', gateComponent: 'GuiaRestauranteJaponesAccessGate', dashboardComponent: 'GuiaRestauranteJaponesDashboard' },
  { productId: 'guia-restaurante-nikkei', accessPath: '/guia-restaurante-nikkei-access', libraryPath: '/guia-restaurante-nikkei-library', landingPath: '/guia-restaurante-nikkei', storageKey: 'guia-restaurante-nikkei-jwt', productLabel: 'Guía Restaurante Nikkei', gateComponent: 'GuiaRestauranteNikkeiAccessGate', dashboardComponent: 'GuiaRestauranteNikkeiDashboard' },
  { productId: 'mega-pack-tareas', accessPath: '/mega-pack-tareas-access', libraryPath: '/mega-pack-tareas-library', landingPath: '/mega-pack-tareas', storageKey: 'mega-pack-tareas-jwt', productLabel: 'Mega Pack Tareas', gateComponent: 'MegaPackTareasAccessGate', dashboardComponent: 'MegaPackTareasDashboard' },
  { productId: 'kit-plan-financiero', accessPath: '/kit-plan-financiero-access', libraryPath: '/kit-plan-financiero-library', landingPath: '/kit-plan-financiero', storageKey: 'kit-plan-financiero-jwt', productLabel: 'Kit Plan Financiero', gateComponent: 'KitPlanFinancieroAccessGate', dashboardComponent: 'KitPlanFinancieroDashboard' },
  { productId: 'pro-prompts-ebook', accessPath: '/pro-prompts-library-access', libraryPath: '/pro-prompts-library', landingPath: '/pro-prompts-ebook', storageKey: 'pro-prompts-jwt', productLabel: 'Pro Prompts Library', gateComponent: 'AccessGate', dashboardComponent: 'ProPromptsLibrary', vanilla: true, notas: 'Vanilla total: sin campo `product` en el body (fallback legacy pro-prompts-ebook, verify-purchase.ts:340-346); ProtectedRoute usa defaults; dashboard sin sufijo Dashboard.' },
];
