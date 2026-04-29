import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitPlanFinancieroAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-plan-financiero"
      storageKey="kit-plan-financiero-jwt"
      dashboardPath="/kit-plan-financiero-library"
      landingPath="/kit-plan-financiero"
      productLabel="Kit Plan Financiero"
    />
  );
}
