import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasCafeteriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-cafeteria"
      storageKey="kit-tareas-cafeteria-jwt"
      dashboardPath="/kit-tareas-cafeteria-library"
      landingPath="/kit-tareas-cafeteria"
      productLabel="Kit de Tareas Cafetería"
    />
  );
}
