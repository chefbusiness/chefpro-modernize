import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaChocolateriaAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-chocolateria-obrador"
      storageKey="guia-chocolateria-obrador-jwt"
      dashboardPath="/guia-chocolateria-obrador-library"
      landingPath="/guia-chocolateria-obrador"
      productLabel="Cómo Montar una Chocolatería Boutique & Atelier"
    />
  );
}
