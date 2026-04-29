import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasDarkKitchenAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-dark-kitchen"
      storageKey="kit-tareas-dark-kitchen-jwt"
      dashboardPath="/kit-tareas-dark-kitchen-library"
      landingPath="/kit-tareas-dark-kitchen"
      productLabel="Kit de Tareas Dark Kitchen"
    />
  );
}
