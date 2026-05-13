import ProductAccessGate from '@/components/shared/ProductAccessGate';

export default function GuiaPanaderiaObradorAccessGate() {
  return (
    <ProductAccessGate
      productId="guia-panaderia-obrador"
      storageKey="guia-panaderia-obrador-jwt"
      dashboardPath="/guia-panaderia-obrador-library"
      landingPath="/guia-panaderia-obrador"
      productLabel="Guía Panadería con Obrador"
    />
  );
}
