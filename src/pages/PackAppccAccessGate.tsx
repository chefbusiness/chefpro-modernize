import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PackAppccAccessGate() {
  return (
    <ProductAccessGate
      productId="pack-appcc"
      storageKey="pack-appcc-jwt"
      dashboardPath="/pack-appcc-library"
      landingPath="/pack-appcc"
      productLabel="Pack APPCC"
    />
  );
}
