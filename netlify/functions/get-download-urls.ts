import type { Handler } from '@netlify/functions';

// ── File maps per product (no env vars needed) ──────────────────
const PRODUCT_FILES: Record<string, Record<string, string>> = {
  'kit-escandallos': {
    'estandar': '/dl/kit-escandallos/01-escandallo-estandar.xlsx',
    'degustacion': '/dl/kit-escandallos/02-menu-degustacion.xlsx',
    'menu-dia': '/dl/kit-escandallos/03-menu-del-dia.xlsx',
    'cocktails': '/dl/kit-escandallos/04-cocktails-bebidas.xlsx',
    'pasteleria': '/dl/kit-escandallos/05-pasteleria.xlsx',
    'catering': '/dl/kit-escandallos/06-catering.xlsx',
    'cafeteria': '/dl/kit-escandallos/07-cafeteria-brunch.xlsx',
    'food-truck': '/dl/kit-escandallos/08-food-truck.xlsx',
    'mermas': '/dl/kit-escandallos/09-control-mermas.xlsx',
    'calculadora-pvp': '/dl/kit-escandallos/10-calculadora-pvp.xlsx',
    'dashboard': '/dl/kit-escandallos/11-dashboard-food-cost.xlsx',
    'bonus-mermas': '/dl/kit-escandallos/BONUS-mermas-inventario.xlsx',
  },
  'pack-appcc': {
    'temp-diario': '/dl/pack-appcc/01-registro-temperaturas-diario.xlsx',
    'temp-recepcion': '/dl/pack-appcc/02-temperaturas-recepcion.xlsx',
    'plan-limpieza': '/dl/pack-appcc/03-plan-limpieza-desinfeccion.xlsx',
    'registro-limpieza': '/dl/pack-appcc/04-registro-limpieza-diaria.xlsx',
    'recepcion': '/dl/pack-appcc/05-checklist-recepcion-mercancias.xlsx',
    'trazabilidad': '/dl/pack-appcc/06-registro-trazabilidad.xlsx',
    'plagas': '/dl/pack-appcc/07-control-plagas-ddd.xlsx',
    'alergenos': '/dl/pack-appcc/08-matriz-alergenos.xlsx',
    'aceite': '/dl/pack-appcc/09-control-aceite-fritura.xlsx',
    'agua': '/dl/pack-appcc/10-control-agua-potable.xlsx',
    'acciones': '/dl/pack-appcc/11-acciones-correctivas.xlsx',
    'haccp': '/dl/pack-appcc/12-analisis-peligros-haccp.xlsx',
    'higiene': '/dl/pack-appcc/13-checklist-higiene-personal.xlsx',
    'fichas-alergenos': '/dl/pack-appcc/14-fichas-14-alergenos.xlsx',
    'guia-inspeccion': '/dl/pack-appcc/15-guia-inspeccion-sanidad.xlsx',
    'bonus-formacion': '/dl/pack-appcc/BONUS-01-registro-formacion.xlsx',
    'bonus-protocolo': '/dl/pack-appcc/BONUS-02-protocolo-alerta.xlsx',
  },
  'kit-tareas': {
    'apertura-cierre': '/dl/kit-tareas/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-cafeteria': {
    'apertura-cierre': '/dl/kit-tareas-cafeteria/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-cafeteria/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas-cafeteria/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-cafeteria/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-cafeteria/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-cafeteria/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas-cafeteria/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-cafeteria/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-cafeteria/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-cafeteria/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-cafeteria/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-pizzeria': {
    'apertura-cierre': '/dl/kit-tareas-pizzeria/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-pizzeria/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas-pizzeria/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-pizzeria/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-pizzeria/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-pizzeria/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas-pizzeria/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-pizzeria/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-pizzeria/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-pizzeria/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-pizzeria/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-hamburgueseria': {
    'apertura-cierre': '/dl/kit-tareas-hamburgueseria/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-hamburgueseria/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas-hamburgueseria/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-hamburgueseria/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-hamburgueseria/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-hamburgueseria/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas-hamburgueseria/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-hamburgueseria/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-hamburgueseria/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-hamburgueseria/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-hamburgueseria/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-dark-kitchen': {
    'apertura-cierre': '/dl/kit-tareas-dark-kitchen/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-dark-kitchen/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas-dark-kitchen/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-dark-kitchen/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-dark-kitchen/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-dark-kitchen/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas-dark-kitchen/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-dark-kitchen/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-dark-kitchen/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-dark-kitchen/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-dark-kitchen/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-pasteleria': {
    'apertura-cierre': '/dl/kit-tareas-pasteleria/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-pasteleria/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas-pasteleria/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-pasteleria/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-pasteleria/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-pasteleria/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas-pasteleria/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-pasteleria/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-pasteleria/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-pasteleria/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-pasteleria/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-bar': {
    'apertura-cierre': '/dl/kit-tareas-bar/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-bar/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas-bar/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-bar/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-bar/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-bar/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas-bar/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-bar/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-bar/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-bar/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-bar/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-catering': {
    'apertura-cierre': '/dl/kit-tareas-catering/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-catering/02-partidas-cocina.xlsx',
    'manager': '/dl/kit-tareas-catering/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-catering/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-catering/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-catering/06-eventos-festivos.xlsx',
    'personalizable': '/dl/kit-tareas-catering/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-catering/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-catering/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-catering/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-catering/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-hotel': {
    'fb-buffet-desayuno': '/dl/kit-tareas-hotel/01-fb-buffet-desayuno.xlsx',
    'fb-buffet-comida-cena': '/dl/kit-tareas-hotel/02-fb-buffet-comida-cena.xlsx',
    'fb-restaurante-carte': '/dl/kit-tareas-hotel/03-fb-restaurante-carte.xlsx',
    'fb-outlets': '/dl/kit-tareas-hotel/04-fb-outlets.xlsx',
    'fb-room-service-minibar': '/dl/kit-tareas-hotel/05-fb-room-service-minibar.xlsx',
    'fb-banquetes-eventos': '/dl/kit-tareas-hotel/06-fb-banquetes-eventos.xlsx',
    'recepcion-turnos': '/dl/kit-tareas-hotel/07-recepcion-turnos.xlsx',
    'guest-services': '/dl/kit-tareas-hotel/08-guest-services.xlsx',
    'housekeeping': '/dl/kit-tareas-hotel/09-housekeeping.xlsx',
    'areas-publicas': '/dl/kit-tareas-hotel/10-areas-publicas.xlsx',
    'piscina': '/dl/kit-tareas-hotel/11-piscina.xlsx',
    'terraza': '/dl/kit-tareas-hotel/12-terraza.xlsx',
    'mantenimiento': '/dl/kit-tareas-hotel/13-mantenimiento.xlsx',
    'administracion': '/dl/kit-tareas-hotel/14-administracion.xlsx',
    'spa-wellness': '/dl/kit-tareas-hotel/15-spa-wellness.xlsx',
    'apertura-negocio': '/dl/kit-tareas-hotel/18-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-hotel/19-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-hotel/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-hotel/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-heladeria': {
    'apertura-cierre': '/dl/kit-tareas-heladeria/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-heladeria/02-partidas-produccion.xlsx',
    'manager': '/dl/kit-tareas-heladeria/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-heladeria/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-heladeria/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-heladeria/06-eventos-temporada.xlsx',
    'personalizable': '/dl/kit-tareas-heladeria/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-heladeria/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-heladeria/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-heladeria/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-heladeria/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-chocolateria': {
    'apertura-cierre': '/dl/kit-tareas-chocolateria/01-apertura-cierre.xlsx',
    'partidas': '/dl/kit-tareas-chocolateria/02-partidas-produccion.xlsx',
    'manager': '/dl/kit-tareas-chocolateria/03-tareas-manager.xlsx',
    'perfiles': '/dl/kit-tareas-chocolateria/04-tareas-perfiles.xlsx',
    'periodicas': '/dl/kit-tareas-chocolateria/05-tareas-semanales-mensuales.xlsx',
    'eventos': '/dl/kit-tareas-chocolateria/06-eventos-temporada.xlsx',
    'personalizable': '/dl/kit-tareas-chocolateria/07-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-chocolateria/08-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-chocolateria/09-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-chocolateria/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-chocolateria/BONUS-02-calendario-anual-tareas.xlsx',
  },
  'kit-tareas-restaurante-creativo': {
    'apertura-cierre': '/dl/kit-tareas-restaurante-creativo/01-apertura-cierre.xlsx',
    'mise-en-place': '/dl/kit-tareas-restaurante-creativo/02-mise-en-place-degustacion.xlsx',
    'id-menu': '/dl/kit-tareas-restaurante-creativo/03-id-desarrollo-menu.xlsx',
    'brigada': '/dl/kit-tareas-restaurante-creativo/04-tareas-brigada-creativa.xlsx',
    'periodicas': '/dl/kit-tareas-restaurante-creativo/05-tareas-semanales-mensuales.xlsx',
    'sumiller': '/dl/kit-tareas-restaurante-creativo/06-sumiller-maridajes.xlsx',
    'eventos': '/dl/kit-tareas-restaurante-creativo/07-chefs-table-eventos.xlsx',
    'fotografia': '/dl/kit-tareas-restaurante-creativo/08-fotografia-storytelling.xlsx',
    'personalizable': '/dl/kit-tareas-restaurante-creativo/09-plantilla-personalizable.xlsx',
    'apertura-negocio': '/dl/kit-tareas-restaurante-creativo/10-apertura-cierre-negocio.xlsx',
    'apertura-caja': '/dl/kit-tareas-restaurante-creativo/11-apertura-cierre-caja.xlsx',
    'bonus-briefing': '/dl/kit-tareas-restaurante-creativo/BONUS-01-briefing-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-restaurante-creativo/BONUS-02-calendario-anual.xlsx',
  },
  'kit-tareas-chef-privado': {
    'ficha-cliente': '/dl/kit-tareas-chef-privado/01-ficha-cliente-consulta.xlsx',
    'menu-compras': '/dl/kit-tareas-chef-privado/02-planificacion-menu-compras.xlsx',
    'equipo-transporte': '/dl/kit-tareas-chef-privado/03-equipo-transporte.xlsx',
    'appcc': '/dl/kit-tareas-chef-privado/04-seguridad-alimentaria-appcc.xlsx',
    'servicio': '/dl/kit-tareas-chef-privado/05-checklist-servicio.xlsx',
    'fidelizacion': '/dl/kit-tareas-chef-privado/06-seguimiento-fidelizacion.xlsx',
    'admin': '/dl/kit-tareas-chef-privado/07-administracion-autonomo.xlsx',
    'bonus-briefing': '/dl/kit-tareas-chef-privado/BONUS-01-briefing-pre-servicio.xlsx',
    'bonus-calendario': '/dl/kit-tareas-chef-privado/BONUS-02-calendario-anual-demanda.xlsx',
  },
  'kit-gestion-personal': {
    'cuadrante': '/dl/kit-gestion-personal/01-cuadrante-turnos-semanal.xlsx',
    'horas-extra': '/dl/kit-gestion-personal/02-control-horas-extras.xlsx',
    'coste-laboral': '/dl/kit-gestion-personal/03-coste-laboral-mensual.xlsx',
    'onboarding': '/dl/kit-gestion-personal/04-onboarding-nuevo-empleado.xlsx',
    'vacaciones': '/dl/kit-gestion-personal/05-planificacion-vacaciones.xlsx',
    'evaluacion': '/dl/kit-gestion-personal/06-evaluacion-desempeno.xlsx',
    'directorio': '/dl/kit-gestion-personal/07-directorio-plantilla.xlsx',
    'bonus-briefing': '/dl/kit-gestion-personal/BONUS-01-briefing-cambio-turno.xlsx',
    'bonus-calculadora': '/dl/kit-gestion-personal/BONUS-02-calculadora-plantilla-optima.xlsx',
  },
  'kit-inventario': {
    'stock': '/dl/kit-inventario/01-inventario-stock-diario.xlsx',
    'proveedores': '/dl/kit-inventario/02-fichas-proveedores.xlsx',
    'pedidos': '/dl/kit-inventario/03-pedidos-compra.xlsx',
    'recepcion': '/dl/kit-inventario/04-recepcion-mercancias.xlsx',
    'mermas': '/dl/kit-inventario/05-control-mermas.xlsx',
    'fifo': '/dl/kit-inventario/06-fifo-caducidades.xlsx',
    'costes': '/dl/kit-inventario/07-analisis-costes-compras.xlsx',
    'bonus-inventario-rapido': '/dl/kit-inventario/BONUS-08-inventario-rapido-mensual.xlsx',
    'bonus-calculadora': '/dl/kit-inventario/BONUS-09-calculadora-punto-pedido.xlsx',
  },
  'kit-plan-financiero': {
    'plan-previsional': '/dl/kit-plan-financiero/01-plan-financiero-previsional.xlsx',
    'plan-previsional-5': '/dl/kit-plan-financiero/01b-plan-financiero-previsional-5-anos.xlsx',
    'break-even': '/dl/kit-plan-financiero/02-calculadora-punto-equilibrio.xlsx',
    'cash-flow': '/dl/kit-plan-financiero/03-cash-flow-forecast.xlsx',
    'capex': '/dl/kit-plan-financiero/04-presupuesto-inversion-capex.xlsx',
    'pyl': '/dl/kit-plan-financiero/05-pyl-mensual-real-vs-presupuesto.xlsx',
    'ratios': '/dl/kit-plan-financiero/06-dashboard-ratios-financieros.xlsx',
    'viabilidad': '/dl/kit-plan-financiero/07-informe-viabilidad-bancos.xlsx',
    'bonus-simulador': '/dl/kit-plan-financiero/BONUS-08-simulador-escenarios.xlsx',
    'bonus-checklist': '/dl/kit-plan-financiero/BONUS-09-checklist-pre-apertura.xlsx',
  },
};

export const handler: Handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }

  if (event.httpMethod !== 'GET') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  const authHeader = event.headers.authorization || event.headers.Authorization;
  if (!authHeader?.startsWith('Bearer ')) {
    return { statusCode: 401, headers, body: JSON.stringify({ error: 'Unauthorized' }) };
  }

  try {
    const jwt = (await import('jsonwebtoken')).default;
    const token = authHeader.split(' ')[1];
    const payload = jwt.verify(token, process.env.JWT_SECRET!) as { product?: string };

    const product = payload.product || 'pro-prompts-ebook';

    // ── Pro Prompts eBook (special: PDF downloads from env vars) ──
    if (product === 'pro-prompts-ebook') {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          product: 'pro-prompts-ebook',
          ebook: process.env.PDF_EBOOK_URL || null,
          bonus1: process.env.PDF_BONUS1_URL || null,
          bonus23: process.env.PDF_BONUS23_URL || null,
        }),
      };
    }

    // ── All other products: use hardcoded file maps ──
    const files = PRODUCT_FILES[product];
    if (files) {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({ product, files }),
      };
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ product, error: 'Unknown product' }),
    };
  } catch {
    return { statusCode: 403, headers, body: JSON.stringify({ error: 'Invalid token' }) };
  }
};
