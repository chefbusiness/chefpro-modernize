import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioTaqueriaAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-taqueria"
      storageKey="plan-negocio-taqueria-jwt"
      dashboardPath="/plan-negocio-taqueria-library"
      landingPath="/plan-negocio-taqueria"
      productLabel="Plan de Negocio: Taquería"
    />
  );
}
