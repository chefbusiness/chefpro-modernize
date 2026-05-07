import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasPanaderiaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-panaderia"
      storageKey="kit-tareas-panaderia-jwt"
      dashboardPath="/kit-tareas-panaderia-library"
      landingPath="/kit-tareas-panaderia"
      productLabel="Kit de Tareas Panadería"
    />
  );
}
