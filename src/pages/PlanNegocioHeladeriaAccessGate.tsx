import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioHeladeriaAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-heladeria"
      storageKey="plan-negocio-heladeria-jwt"
      dashboardPath="/plan-negocio-heladeria-library"
      landingPath="/plan-negocio-heladeria"
      productLabel="Plan de Negocio Heladería"
    />
  );
}
