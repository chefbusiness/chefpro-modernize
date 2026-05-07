import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasFoodTruckAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-food-truck"
      storageKey="kit-tareas-food-truck-jwt"
      dashboardPath="/kit-tareas-food-truck-library"
      landingPath="/kit-tareas-food-truck"
      productLabel="Kit de Tareas Food Truck"
    />
  );
}
