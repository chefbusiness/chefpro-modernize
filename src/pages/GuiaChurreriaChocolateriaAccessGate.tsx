import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaChurreriaChocolateriaAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-churreria-chocolateria"
      storageKey="guia-churreria-chocolateria-jwt"
      dashboardPath="/guia-churreria-chocolateria-library"
      landingPath="/guia-churreria-chocolateria"
      productLabel="Cómo Montar una Churrería-Chocolatería"
    />
  );
}
