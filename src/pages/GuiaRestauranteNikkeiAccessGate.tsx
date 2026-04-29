import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaRestauranteNikkeiAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-restaurante-nikkei"
      storageKey="guia-restaurante-nikkei-jwt"
      dashboardPath="/guia-restaurante-nikkei-library"
      landingPath="/guia-restaurante-nikkei"
      productLabel="Guía Restaurante Nikkei"
    />
  );
}
