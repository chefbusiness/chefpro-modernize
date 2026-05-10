import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioCocteleriaEventosAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-cocteleria-eventos"
      storageKey="plan-negocio-cocteleria-eventos-jwt"
      dashboardPath="/plan-negocio-cocteleria-eventos-library"
      landingPath="/plan-negocio-cocteleria-eventos"
      productLabel="Plan de Negocio Coctelería de Eventos"
    />
  );
}
