import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioSushiBarAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-sushi-bar"
      storageKey="plan-negocio-sushi-bar-jwt"
      dashboardPath="/plan-negocio-sushi-bar-library"
      landingPath="/plan-negocio-sushi-bar"
      productLabel="Plan de Negocio: Sushi Bar"
    />
  );
}
