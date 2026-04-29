import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasRestauranteCreativoAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-restaurante-creativo"
      storageKey="kit-tareas-restaurante-creativo-jwt"
      dashboardPath="/kit-tareas-restaurante-creativo-library"
      landingPath="/kit-tareas-restaurante-creativo"
      productLabel="Kit de Tareas Restaurante Creativo"
    />
  );
}
