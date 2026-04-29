import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaRestauranteGastronomicoAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-restaurante-gastronomico"
      storageKey="guia-restaurante-gastronomico-jwt"
      dashboardPath="/guia-restaurante-gastronomico-library"
      landingPath="/guia-restaurante-gastronomico"
      productLabel="Guía Restaurante Gastronómico"
    />
  );
}
