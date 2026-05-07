import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasTapasBarAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-tapas-bar"
      storageKey="kit-tareas-tapas-bar-jwt"
      dashboardPath="/kit-tareas-tapas-bar-library"
      landingPath="/kit-tareas-tapas-bar"
      productLabel="Kit de Tareas Tapas Bar"
    />
  );
}
