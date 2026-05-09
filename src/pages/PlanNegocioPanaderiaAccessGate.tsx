import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioPanaderiaAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-panaderia"
      storageKey="plan-negocio-panaderia-jwt"
      dashboardPath="/plan-negocio-panaderia-library"
      landingPath="/plan-negocio-panaderia"
      productLabel="Plan de Negocio Panadería"
    />
  );
}
