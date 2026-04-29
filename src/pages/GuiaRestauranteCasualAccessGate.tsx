import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaRestauranteCasualAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-restaurante-casual"
      storageKey="guia-restaurante-casual-jwt"
      dashboardPath="/guia-restaurante-casual-library"
      landingPath="/guia-restaurante-casual"
      productLabel="Guía Restaurante Casual"
    />
  );
}
