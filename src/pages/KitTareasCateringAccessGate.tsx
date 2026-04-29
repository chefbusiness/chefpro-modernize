import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasCateringAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-catering"
      storageKey="kit-tareas-catering-jwt"
      dashboardPath="/kit-tareas-catering-library"
      landingPath="/kit-tareas-catering"
      productLabel="Kit de Tareas Catering"
    />
  );
}
