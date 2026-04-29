import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaRestaurantePeruanoAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-restaurante-peruano"
      storageKey="guia-restaurante-peruano-jwt"
      dashboardPath="/guia-restaurante-peruano-library"
      landingPath="/guia-restaurante-peruano"
      productLabel="Guía Restaurante Peruano"
    />
  );
}
