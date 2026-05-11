import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function PlanChefPrivadoShowcookingEventosAccessGate() {
  return (
    <ProductAccessGate
      productId="plan-chef-privado-showcooking-eventos"
      storageKey="plan-chef-privado-showcooking-eventos-jwt"
      dashboardPath="/plan-chef-privado-showcooking-eventos-library"
      landingPath="/plan-chef-privado-showcooking-eventos"
      productLabel="Plan de Negocio Chef Privado / Showcooking a Domicilio"
    />
  );
}
