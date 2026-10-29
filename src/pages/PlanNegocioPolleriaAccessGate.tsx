import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioPolleriaAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-polleria"
      storageKey="plan-negocio-polleria-jwt"
      dashboardPath="/plan-negocio-polleria-library"
      landingPath="/plan-negocio-polleria"
      productLabel="Plan de Negocio: Pollería y Asador de Pollos"
    />
  );
}
