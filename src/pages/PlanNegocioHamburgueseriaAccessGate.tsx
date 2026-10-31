import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioHamburgueseriaAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-hamburgueseria"
      storageKey="plan-negocio-hamburgueseria-jwt"
      dashboardPath="/plan-negocio-hamburgueseria-library"
      landingPath="/plan-negocio-hamburgueseria"
      productLabel="Plan de Negocio: Hamburguesería Smash"
    />
  );
}
