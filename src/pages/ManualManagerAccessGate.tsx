import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function ManualManagerAccessGate() {
  return (
    <ProductAccessGate
      productId="manual-manager-restaurante"
      storageKey="manual-manager-restaurante-jwt"
      dashboardPath="/manual-manager-restaurante-library"
      landingPath="/manual-manager-restaurante"
      productLabel="Manual del Manager de Restaurante"
    />
  );
}
