import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioFoodTruckAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-food-truck"
      storageKey="plan-negocio-food-truck-jwt"
      dashboardPath="/plan-negocio-food-truck-library"
      landingPath="/plan-negocio-food-truck"
      productLabel="Plan de Negocio Food Truck"
    />
  );
}
