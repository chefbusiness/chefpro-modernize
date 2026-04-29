import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaRestauranteMexicanoAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-restaurante-mexicano"
      storageKey="guia-restaurante-mexicano-jwt"
      dashboardPath="/guia-restaurante-mexicano-library"
      landingPath="/guia-restaurante-mexicano"
      productLabel="Guía Restaurante Mexicano"
    />
  );
}
