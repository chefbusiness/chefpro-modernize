import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasChefPrivadoAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-chef-privado"
      storageKey="kit-tareas-chef-privado-jwt"
      dashboardPath="/kit-tareas-chef-privado-library"
      landingPath="/kit-tareas-chef-privado"
      productLabel="Kit de Tareas Chef Privado"
    />
  );
}
