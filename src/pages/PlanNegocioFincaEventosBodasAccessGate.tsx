import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanNegocioFincaEventosBodasAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-negocio-finca-eventos-bodas"
      storageKey="plan-negocio-finca-eventos-bodas-jwt"
      dashboardPath="/plan-negocio-finca-eventos-bodas-library"
      landingPath="/plan-negocio-finca-eventos-bodas"
      productLabel="Plan de Negocio Finca de Eventos y Bodas"
    />
  );
}
