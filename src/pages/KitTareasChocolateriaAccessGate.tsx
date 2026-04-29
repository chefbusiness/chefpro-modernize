import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasChocolateriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-chocolateria"
      storageKey="kit-tareas-chocolateria-jwt"
      dashboardPath="/kit-tareas-chocolateria-library"
      landingPath="/kit-tareas-chocolateria"
      productLabel="Kit de Tareas Chocolatería"
    />
  );
}
