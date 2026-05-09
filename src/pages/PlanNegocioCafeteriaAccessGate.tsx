import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioCafeteriaAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-cafeteria"
      storageKey="plan-negocio-cafeteria-jwt"
      dashboardPath="/plan-negocio-cafeteria-library"
      landingPath="/plan-negocio-cafeteria"
      productLabel="Plan de Negocio Cafetería"
    />
  );
}
