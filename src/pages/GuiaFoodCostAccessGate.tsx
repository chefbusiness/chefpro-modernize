import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaFoodCostAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-food-cost-ingenieria-menu"
      storageKey="guia-food-cost-ingenieria-menu-jwt"
      dashboardPath="/guia-food-cost-ingenieria-menu-library"
      landingPath="/guia-food-cost-ingenieria-menu"
      productLabel="Guía Food Cost + Ingeniería de Menú"
    />
  );
}
