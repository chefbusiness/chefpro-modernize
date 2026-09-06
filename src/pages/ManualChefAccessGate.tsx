import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function ManualChefAccessGate() {
  return (
    <ProductAccessGate
      productId="manual-chef-ejecutivo"
      storageKey="manual-chef-ejecutivo-jwt"
      dashboardPath="/manual-chef-ejecutivo-library"
      landingPath="/manual-chef-ejecutivo"
      productLabel="Manual del Chef Ejecutivo"
    />
  );
}
