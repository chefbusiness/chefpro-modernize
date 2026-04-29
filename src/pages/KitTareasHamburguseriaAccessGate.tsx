import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasHamburguseriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-hamburgueseria"
      storageKey="kit-tareas-hamburgueseria-jwt"
      dashboardPath="/kit-tareas-hamburgueseria-library"
      landingPath="/kit-tareas-hamburgueseria"
      productLabel="Kit de Tareas Hamburguesería"
    />
  );
}
