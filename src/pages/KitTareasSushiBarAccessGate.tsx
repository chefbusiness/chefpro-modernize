import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasSushiBarAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-sushi-bar"
      storageKey="kit-tareas-sushi-bar-jwt"
      dashboardPath="/kit-tareas-sushi-bar-library"
      landingPath="/kit-tareas-sushi-bar"
      productLabel="Kit de Tareas Sushi Bar"
    />
  );
}
