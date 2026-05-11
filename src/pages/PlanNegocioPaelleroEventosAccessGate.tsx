import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioPaelleroEventosAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-paellero-eventos"
      storageKey="plan-negocio-paellero-eventos-jwt"
      dashboardPath="/plan-negocio-paellero-eventos-library"
      landingPath="/plan-negocio-paellero-eventos"
      productLabel="Plan de Negocio Paellero / Paella Eventos"
    />
  );
}
