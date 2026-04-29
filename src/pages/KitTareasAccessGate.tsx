import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas"
      storageKey="kit-tareas-jwt"
      dashboardPath="/kit-tareas-library"
      landingPath="/kit-tareas"
      productLabel="Kit de Tareas"
    />
  );
}
