import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaDarkKitchenAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-dark-kitchen"
      storageKey="guia-dark-kitchen-jwt"
      dashboardPath="/guia-dark-kitchen-library"
      landingPath="/guia-dark-kitchen"
      productLabel="Guía Dark Kitchen"
    />
  );
}
