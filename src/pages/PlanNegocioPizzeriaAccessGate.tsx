import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioPizzeriaAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-pizzeria"
      storageKey="plan-negocio-pizzeria-jwt"
      dashboardPath="/plan-negocio-pizzeria-library"
      landingPath="/plan-negocio-pizzeria"
      productLabel="Plan de Negocio Pizzería Napolitana"
    />
  );
}
