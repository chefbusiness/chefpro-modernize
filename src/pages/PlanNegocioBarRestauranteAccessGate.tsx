import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioBarRestauranteAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-bar-restaurante"
      storageKey="plan-negocio-bar-restaurante-jwt"
      dashboardPath="/plan-negocio-bar-restaurante-library"
      landingPath="/plan-negocio-bar-restaurante"
      productLabel="Plan de Negocio Bar-Restaurante"
    />
  );
}
