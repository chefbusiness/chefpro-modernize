import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasMarisqueriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-marisqueria"
      storageKey="kit-tareas-marisqueria-jwt"
      dashboardPath="/kit-tareas-marisqueria-library"
      landingPath="/kit-tareas-marisqueria"
      productLabel="Kit de Tareas Marisquería"
    />
  );
}
