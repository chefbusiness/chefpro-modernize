import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function KitGestionPersonalAccessGate() {
  return (
    <ProductAccessGate
      productId="kit-gestion-personal"
      storageKey="kit-gestion-personal-jwt"
      dashboardPath="/kit-gestion-personal-library"
      landingPath="/kit-gestion-personal"
      productLabel="Kit de Gestión de Personal"
    />
  );
}
