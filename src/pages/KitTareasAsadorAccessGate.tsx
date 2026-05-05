import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasAsadorAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-asador"
      storageKey="kit-tareas-asador-jwt"
      dashboardPath="/kit-tareas-asador-library"
      landingPath="/kit-tareas-asador"
      productLabel="Kit de Tareas Asador"
    />
  );
}
