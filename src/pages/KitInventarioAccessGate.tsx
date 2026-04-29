import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitInventarioAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-inventario"
      storageKey="kit-inventario-jwt"
      dashboardPath="/kit-inventario-library"
      landingPath="/kit-inventario"
      productLabel="Kit de Inventario"
    />
  );
}
