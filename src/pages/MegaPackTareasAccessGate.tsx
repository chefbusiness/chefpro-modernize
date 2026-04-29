import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function MegaPackTareasAccessGate() {
  return (
    <ProductAccessGate
      productId="mega-pack-tareas"
      storageKey="mega-pack-tareas-jwt"
      dashboardPath="/mega-pack-tareas-library"
      landingPath="/mega-pack-tareas"
      productLabel="Mega Pack Tareas"
    />
  );
}
