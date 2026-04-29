import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasPasteleriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-pasteleria"
      storageKey="kit-tareas-pasteleria-jwt"
      dashboardPath="/kit-tareas-pasteleria-library"
      landingPath="/kit-tareas-pasteleria"
      productLabel="Kit de Tareas Pastelería"
    />
  );
}
