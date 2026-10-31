import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import {
  GA4_MEASUREMENT_ID,
  GOOGLE_ADS_ID,
  GOOGLE_ADS_PURCHASE_LABEL,
  META_PIXEL_ID,
  adsLabelActivo,
  compraDesdeRespuesta,
  ga4Activo,
  metaActivo,
} from './medicion-compra.ts';

const SESION = 'cs_test_a1b2c3d4e5f6';
const PAGO = 'pi_3Abcdefghijk1234';

const compra = {
  value: 18.5,
  currency: 'EUR',
  transactionId: PAGO,
  sessionId: SESION,
  paymentId: PAGO,
  productId: 'kit-tareas-hotel',
};

test('los marcadores de esta cuenta no disparan todavía', () => {
  assert.equal(adsLabelActivo(GOOGLE_ADS_PURCHASE_LABEL), false);
  assert.equal(adsLabelActivo('PENDIENTE_LABEL'), false);
  assert.equal(adsLabelActivo(''), false);
  assert.equal(adsLabelActivo('AbCdEf'), true);
  assert.equal(ga4Activo(GA4_MEASUREMENT_ID), false);
  assert.equal(ga4Activo('AW-17829651892'), false);
  assert.equal(ga4Activo('G-ABC123XYZ'), true);
  assert.equal(metaActivo(META_PIXEL_ID), false);
  assert.equal(metaActivo(''), false);
  assert.equal(metaActivo('123456789012345'), true);
});

test('la cuenta de Ads es la de GoogleTag.astro', () => {
  const tag = readFileSync(new URL('../../astro-site/src/components/GoogleTag.astro', import.meta.url), 'utf8');
  assert.match(tag, new RegExp(GOOGLE_ADS_ID));
});

test('solo pasa una compra con la forma de verify-purchase', () => {
  assert.deepEqual(compraDesdeRespuesta(compra), compra);
  assert.equal(compraDesdeRespuesta(null), null);
  assert.equal(compraDesdeRespuesta({ ...compra, value: 999999 }), null);
  assert.equal(compraDesdeRespuesta({ ...compra, currency: 'euro' }), null);
  assert.equal(compraDesdeRespuesta({ ...compra, transactionId: 'pedido-cripto' }), null);
  assert.equal(compraDesdeRespuesta({ ...compra, sessionId: '{CHECKOUT_SESSION_ID}' }), null);
  assert.equal(compraDesdeRespuesta({ ...compra, paymentId: null, transactionId: SESION }).transactionId, SESION);
  assert.equal(compraDesdeRespuesta({ ...compra, paymentId: null, transactionId: PAGO }), null);
});
