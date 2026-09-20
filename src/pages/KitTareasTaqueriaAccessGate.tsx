import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitTareasTaqueriaAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-tareas-taqueria"
      storageKey="kit-tareas-taqueria-jwt"
      dashboardPath="/kit-tareas-taqueria-library"
      landingPath="/kit-tareas-taqueria"
      productLabel="Kit de Tareas Taquería Mexicana"
    />
  );
}
