import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasHotelAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-hotel"
      storageKey="kit-tareas-hotel-jwt"
      dashboardPath="/kit-tareas-hotel-library"
      landingPath="/kit-tareas-hotel"
      productLabel="Kit de Tareas Hotel"
    />
  );
}
