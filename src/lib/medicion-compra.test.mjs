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

test('Ads usa el label real; GA4 está activo y Meta sigue apagado', () => {
  assert.equal(GOOGLE_ADS_PURCHASE_LABEL, 'ARzvCKiTuq8dELTL67VC');
  assert.equal(`${GOOGLE_ADS_ID}/${GOOGLE_ADS_PURCHASE_LABEL}`, 'AW-17829651892/ARzvCKiTuq8dELTL67VC');
  assert.equal(adsLabelActivo(GOOGLE_ADS_PURCHASE_LABEL), true);
  assert.equal(adsLabelActivo('PENDIENTE_LABEL'), false);
  assert.equal(adsLabelActivo(''), false);
  assert.equal(adsLabelActivo('AbCdEf'), true);
  assert.equal(GA4_MEASUREMENT_ID, 'G-7SWN171DEX');
  assert.equal(ga4Activo(GA4_MEASUREMENT_ID), true);
  assert.equal(ga4Activo(''), false);
  assert.equal(ga4Activo('AW-17829651892'), false);
  assert.equal(ga4Activo('G-ABC123XYZ'), true);
  assert.equal(META_PIXEL_ID, '');
  assert.equal(metaActivo(META_PIXEL_ID), false);
  assert.equal(metaActivo(''), false);
  assert.equal(metaActivo('123456789012345'), true);
});

test('la cuenta de Ads es la de GoogleTag.astro', () => {
  const tag = readFileSync(new URL('../../astro-site/src/components/GoogleTag.astro', import.meta.url), 'utf8');
  assert.match(tag, new RegExp(GOOGLE_ADS_ID));
});

test('GA4 de GoogleTag es la misma propiedad y no carga otro G-', () => {
  const tag = readFileSync(new URL('../../astro-site/src/components/GoogleTag.astro', import.meta.url), 'utf8');
  assert.match(tag, new RegExp(`const GA4_MEASUREMENT_ID = '${GA4_MEASUREMENT_ID}'`));
  assert.match(tag, /gtag\('config', GA4_MEASUREMENT_ID\)/);
  assert.match(tag, /gtag\/js\?id=\$\{GOOGLE_ADS_ID\}/);
  assert.equal(tag.match(/googletagmanager\.com\/gtag\/js/g)?.length, 1);
  assert.doesNotMatch(tag, /G-KVMQGZ1PH4|G-J88H8YLR8P|G-LE6385H6SF/);
  const src = readFileSync(new URL('./medicion-compra.ts', import.meta.url), 'utf8');
  assert.doesNotMatch(src, /G-KVMQGZ1PH4|G-J88H8YLR8P|G-LE6385H6SF/);
});

test('la conversión de Ads manda value, currency y transaction_id', () => {
  const src = readFileSync(new URL('./medicion-compra.ts', import.meta.url), 'utf8');
  assert.match(src, /send_to: `\$\{GOOGLE_ADS_ID\}\/\$\{GOOGLE_ADS_PURCHASE_LABEL\}`/);
  assert.match(src, /value: compra\.value/);
  assert.match(src, /currency: compra\.currency/);
  assert.match(src, /transaction_id: compra\.transactionId/);
});

test('el purchase de GA4 manda value, currency, transaction_id e items', () => {
  const src = readFileSync(new URL('./medicion-compra.ts', import.meta.url), 'utf8');
  assert.match(src, /send_to: GA4_MEASUREMENT_ID/);
  assert.match(src, /gtag\('event', 'purchase'/);
  assert.match(src, /item_id: compra\.productId/);
  assert.match(src, /item_name: itemName/);
  assert.match(src, /price: compra\.value/);
  assert.match(src, /quantity: 1/);
  assert.match(src, /send_page_view: false/);
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
