import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasPizzeriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-pizzeria"
      storageKey="kit-tareas-pizzeria-jwt"
      dashboardPath="/kit-tareas-pizzeria-library"
      landingPath="/kit-tareas-pizzeria"
      productLabel="Kit de Tareas Pizzería"
    />
  );
}
