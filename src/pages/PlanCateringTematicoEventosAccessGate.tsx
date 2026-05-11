import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanCateringTematicoEventosAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-catering-tematico-eventos"
      storageKey="plan-catering-tematico-eventos-jwt"
      dashboardPath="/plan-catering-tematico-eventos-library"
      landingPath="/plan-catering-tematico-eventos"
      productLabel="Plan de Negocio para Catering & Kit Temático para Eventos"
    />
  );
}
