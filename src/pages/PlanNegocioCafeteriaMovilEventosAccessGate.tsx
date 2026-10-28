import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioCafeteriaMovilEventosAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-cafeteria-movil-eventos"
      storageKey="plan-negocio-cafeteria-movil-eventos-jwt"
      dashboardPath="/plan-negocio-cafeteria-movil-eventos-library"
      landingPath="/plan-negocio-cafeteria-movil-eventos"
      productLabel="Plan de Negocio: Cafetería Móvil para Eventos"
    />
  );
}
