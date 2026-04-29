import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaRestauranteJaponesAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-restaurante-japones"
      storageKey="guia-restaurante-japones-jwt"
      dashboardPath="/guia-restaurante-japones-library"
      landingPath="/guia-restaurante-japones"
      productLabel="Guía Restaurante Japonés"
    />
  );
}
