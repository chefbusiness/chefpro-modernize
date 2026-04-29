import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasHeladeriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-heladeria"
      storageKey="kit-tareas-heladeria-jwt"
      dashboardPath="/kit-tareas-heladeria-library"
      landingPath="/kit-tareas-heladeria"
      productLabel="Kit de Tareas Heladería"
    />
  );
}
