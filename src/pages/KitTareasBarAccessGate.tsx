import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasBarAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-bar"
      storageKey="kit-tareas-bar-jwt"
      dashboardPath="/kit-tareas-bar-library"
      landingPath="/kit-tareas-bar"
      productLabel="Kit de Tareas Bar"
    />
  );
}
