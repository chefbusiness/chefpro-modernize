import assert from 'node:assert/strict';
import test from 'node:test';
import { purchaseFromSession } from './purchase-measurement.ts';

const SESION = 'cs_live_a1b2c3d4e5f6';
const PAGO = 'pi_3Abcdefghijk1234';

test('una sesión pagada en EUR devuelve euros y el payment_intent', () => {
  const compra = purchaseFromSession({
    id: SESION,
    amount_total: 1850,
    currency: 'eur',
    payment_intent: PAGO,
    payment_status: 'paid',
  }, 'kit-tareas-hotel');
  assert.deepEqual(compra, {
    value: 18.5,
    currency: 'EUR',
    transactionId: PAGO,
    sessionId: SESION,
    paymentId: PAGO,
    productId: 'kit-tareas-hotel',
  });
});

test('sin payment_intent el id de transacción es la sesión', () => {
  const compra = purchaseFromSession({
    id: SESION,
    amount_total: 1400,
    currency: 'usd',
    payment_intent: null,
    payment_status: 'paid',
  }, 'food-cost-templates');
  assert.equal(compra.transactionId, SESION);
  assert.equal(compra.paymentId, null);
  assert.equal(compra.value, 14);
  assert.equal(compra.currency, 'USD');
});

test('un payment_intent expandido también vale', () => {
  const compra = purchaseFromSession({
    id: SESION,
    amount_total: 900,
    currency: 'eur',
    payment_intent: { id: PAGO },
    payment_status: 'paid',
  }, 'pro-prompts-ebook');
  assert.equal(compra.paymentId, PAGO);
  assert.equal(compra.value, 9);
});

test('no mide una sesión sin pagar, cripto o sin importe', () => {
  assert.equal(purchaseFromSession({
    id: SESION,
    amount_total: 1400,
    currency: 'eur',
    payment_status: 'unpaid',
  }, 'kit-escandallos'), null);
  assert.equal(purchaseFromSession({
    id: 'orden-cripto-123',
    amount_total: 1400,
    currency: 'eur',
    payment_status: 'paid',
  }, 'kit-escandallos'), null);
  assert.equal(purchaseFromSession({
    id: SESION,
    amount_total: null,
    currency: 'eur',
    payment_status: 'paid',
  }, 'kit-escandallos'), null);
  assert.equal(purchaseFromSession({
    id: SESION,
    amount_total: 1400,
    currency: '',
    payment_status: 'paid',
  }, 'kit-escandallos'), null);
});

test('el yen no se divide entre 100', () => {
  const compra = purchaseFromSession({
    id: SESION,
    amount_total: 1500,
    currency: 'jpy',
    payment_status: 'paid',
  }, 'kit-escandallos');
  assert.equal(compra.value, 1500);
  assert.equal(compra.currency, 'JPY');
});
