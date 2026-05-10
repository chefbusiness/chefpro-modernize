import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioParrilleroAsadorEventosAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-parrillero-asador-eventos"
      storageKey="plan-negocio-parrillero-asador-eventos-jwt"
      dashboardPath="/plan-negocio-parrillero-asador-eventos-library"
      landingPath="/plan-negocio-parrillero-asador-eventos"
      productLabel="Plan de Negocio Parrillero / Asador Eventos"
    />
  );
}
