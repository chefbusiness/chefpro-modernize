import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioTapasBarAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-tapas-bar"
      storageKey="plan-negocio-tapas-bar-jwt"
      dashboardPath="/plan-negocio-tapas-bar-library"
      landingPath="/plan-negocio-tapas-bar"
      productLabel="Plan de Negocio Tapas Bar"
    />
  );
}
