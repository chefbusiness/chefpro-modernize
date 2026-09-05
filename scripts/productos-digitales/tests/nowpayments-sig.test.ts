// ════════════════════════════════════════════════════════════════════════════
// Test de la firma del IPN de NOWPayments — sin red, sin Blobs, sin build.
//
//   node --experimental-strip-types scripts/productos-digitales/tests/nowpayments-sig.test.ts
//
// POR QUÉ EXISTE: la firma es lo único que separa un pago real de un POST
// cualquiera contra `nowpayments-ipn`, y se calcula sobre el JSON con las
// claves ORDENADAS RECURSIVAMENTE — no sobre el cuerpo crudo (eso es Stripe).
// Un fallo aquí no da error: da «invalid_signature» en TODOS los pagos, o —peor—
// acepta firmas que no debería. Se prueba en local porque `netlify/shared/
// nowpayments.ts` sólo usa `node:crypto` (nada de Blobs, nada de Astro: cero
// builds, regla térmica del Mac).
//
// LA FIRMA ESPERADA SE CALCULA APARTE, con la implementación de referencia del
// SDK oficial (`sort` + `reduce` + `createHmac`), escrita a mano en este
// fichero. Si el test importara la misma función que prueba, sólo comprobaría
// que una función es igual a sí misma.
// ════════════════════════════════════════════════════════════════════════════

import { createHmac } from 'node:crypto';
import {
  computeIpnSignature,
  isKnownStatus,
  PAYMENT_STATUSES,
  readRawBody,
  sortObjectDeep,
  verifyIpnSignature,
  computeIpnSignatureLegacy,
  sortObjectLegacy,
} from '../../../netlify/shared/nowpayments.ts';

// ── Implementación de referencia (SDK oficial, forma reduce + sort) ─────────
// El `sortObject` publicado por NOWPayments es exactamente este `reduce`. Se le
// añade la rama explícita de arrays porque el contrato acordado
// (PAGOS_CRYPTO_NOWPAYMENTS.md:149) dice «respeta arrays», y porque la versión
// en PHP —donde `ksort` sobre una lista deja los índices 0..n y `json_encode`
// sigue emitiendo un array— se comporta así. La variante SIN esa rama convierte
// `[1,2]` en `{"0":1,"1":2}`; abajo se mide esa divergencia explícitamente.
function sortObjectRef(obj: unknown): unknown {
  if (Array.isArray(obj)) return obj.map((v) => sortObjectRef(v));
  if (obj === null || typeof obj !== 'object') return obj;
  const o = obj as Record<string, unknown>;
  return Object.keys(o)
    .sort()
    .reduce((acc: Record<string, unknown>, key: string) => {
      acc[key] = o[key] && typeof o[key] === 'object' ? sortObjectRef(o[key]) : o[key];
      return acc;
    }, {});
}

/** La misma sin la rama de arrays: el `sortObject` literal del SDK de Node. */
function sortObjectRefIngenuo(obj: unknown): unknown {
  if (obj === null || typeof obj !== 'object') return obj;
  const o = obj as Record<string, unknown>;
  return Object.keys(o)
    .sort()
    .reduce((acc: Record<string, unknown>, key: string) => {
      acc[key] = o[key] && typeof o[key] === 'object' ? sortObjectRefIngenuo(o[key]) : o[key];
      return acc;
    }, {});
}

function firmaRef(payload: unknown, secret: string): string {
  return createHmac('sha512', secret.trim()).update(JSON.stringify(sortObjectRef(payload))).digest('hex');
}

// ── Arnés ───────────────────────────────────────────────────────────────────
let total = 0;
let ok = 0;
const fallos: string[] = [];

function comprueba(nombre: string, condicion: boolean, detalle = ''): void {
  total += 1;
  if (condicion) {
    ok += 1;
    console.log(`  ok   ${nombre}`);
  } else {
    fallos.push(nombre);
    console.log(`  FALLO ${nombre}${detalle ? ` — ${detalle}` : ''}`);
  }
}

// ── Payload de prueba ───────────────────────────────────────────────────────
// Claves DESORDENADAS a propósito (el orden de un IPN real no está garantizado)
// y con los campos de la colección Postman oficial. `fee` es el objeto anidado
// que NOWPayments manda en los pagos con conversión.
const SECRETO = 'un-ipn-secret-de-prueba-1234567890';
const PAYLOAD = {
  payment_status: 'finished',
  pay_currency: 'usdttrc20',
  order_id: 'a1b2c3d4e5f60718293a4b5c6d7e8f90',
  payment_id: 5745459419,
  actually_paid: 12.04,
  price_amount: 12,
  fee: {
    withdrawalFee: 0,
    depositFee: 0.12,
    serviceFee: 0.06,
    currency: 'usdttrc20',
  },
  price_currency: 'eur',
  pay_amount: 12.03,
  outcome_currency: 'usdttrc20',
  order_description: 'Kit de Tareas: Cafetería / Brunch',
  invoice_id: 4522625843,
  purchase_id: '5077125051',
  pay_address: 'TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE',
  outcome_amount: 11.86,
  created_at: '2026-09-05T10:12:04.000Z',
  updated_at: '2026-09-05T10:19:41.000Z',
  // Un array para fijar el comportamiento acordado: se respeta tal cual.
  historial: ['waiting', 'confirming', 'confirmed', 'sending', 'finished'],
};

console.log('nowpayments-sig — firma del IPN\n');

// 1) Firma positiva contra la implementación de referencia.
const esperada = firmaRef(PAYLOAD, SECRETO);
const calculada = computeIpnSignature(PAYLOAD, SECRETO);
comprueba(
  'computeIpnSignature coincide con la referencia (claves desordenadas + objeto anidado + array)',
  calculada === esperada,
  `${calculada.slice(0, 16)}… vs ${esperada.slice(0, 16)}…`,
);
comprueba('la firma es hex de 128 caracteres (SHA-512)', /^[0-9a-f]{128}$/.test(calculada));
comprueba('verifyIpnSignature acepta la firma correcta', verifyIpnSignature(PAYLOAD, esperada, SECRETO) === true);

// 2) Firma alterada en un byte → false.
const primerDistinto = esperada[0] === 'a' ? 'b' : 'a';
const alterada = primerDistinto + esperada.slice(1);
comprueba('un byte cambiado al principio → false', verifyIpnSignature(PAYLOAD, alterada, SECRETO) === false);
const ultimo = esperada[esperada.length - 1] === 'f' ? 'e' : 'f';
const alteradaFinal = esperada.slice(0, -1) + ultimo;
comprueba('un byte cambiado al final → false', verifyIpnSignature(PAYLOAD, alteradaFinal, SECRETO) === false);

// 3) Longitudes distintas → false SIN LANZAR (`timingSafeEqual` tira RangeError
//    con buffers de distinto tamaño: si no se comprobara antes, la function
//    devolvería 500 en vez de 400 y NOWPayments reintentaría en bucle).
let lanzo = false;
let resCorta = true;
try {
  resCorta = verifyIpnSignature(PAYLOAD, esperada.slice(0, 100), SECRETO);
} catch {
  lanzo = true;
}
comprueba('firma más corta → false y sin lanzar', lanzo === false && resCorta === false);
comprueba('firma más larga → false', verifyIpnSignature(PAYLOAD, `${esperada}00`, SECRETO) === false);
comprueba('firma vacía → false', verifyIpnSignature(PAYLOAD, '', SECRETO) === false);
comprueba('firma ausente (undefined) → false', verifyIpnSignature(PAYLOAD, undefined, SECRETO) === false);
comprueba(
  'firma no-hex de la longitud correcta → false',
  verifyIpnSignature(PAYLOAD, 'z'.repeat(128), SECRETO) === false,
);

// 4) Secreto con espacios/saltos de línea: `.trim()`. Copiar la clave del panel
//    arrastra un `\n` con pasmosa facilidad, y sin trim fallarían TODOS los pagos.
comprueba(
  'secreto con espacios y \\n produce la misma firma (trim)',
  computeIpnSignature(PAYLOAD, `  ${SECRETO}\n`) === esperada,
);
comprueba(
  'verifyIpnSignature con secreto sin recortar acepta igual',
  verifyIpnSignature(PAYLOAD, esperada, `\t${SECRETO}  `) === true,
);
comprueba('otro secreto → false', verifyIpnSignature(PAYLOAD, esperada, `${SECRETO}x`) === false);

// 5) readRawBody respeta isBase64Encoded.
const cuerpo = JSON.stringify(PAYLOAD);
comprueba('readRawBody con texto plano', readRawBody({ body: cuerpo, isBase64Encoded: false }) === cuerpo);
comprueba(
  'readRawBody con base64',
  readRawBody({ body: Buffer.from(cuerpo, 'utf8').toString('base64'), isBase64Encoded: true }) === cuerpo,
);
comprueba('readRawBody sin cuerpo → cadena vacía', readRawBody({ body: null }) === '');
comprueba(
  'un IPN llegado en base64 verifica igual',
  verifyIpnSignature(
    JSON.parse(readRawBody({ body: Buffer.from(cuerpo, 'utf8').toString('base64'), isBase64Encoded: true })),
    esperada,
    SECRETO,
  ) === true,
);

// 6) Estados oficiales: los 9 y sólo los 9.
comprueba('PAYMENT_STATUSES tiene exactamente 9 estados', PAYMENT_STATUSES.length === 9, String(PAYMENT_STATUSES.length));
for (const estado of PAYMENT_STATUSES) {
  comprueba(`isKnownStatus('${estado}')`, isKnownStatus(estado) === true);
}
comprueba("isKnownStatus('cancelled') → false (no existe en NOWPayments)", isKnownStatus('cancelled') === false);
comprueba("isKnownStatus('FINISHED') → false (distingue mayúsculas)", isKnownStatus('FINISHED') === false);
comprueba('isKnownStatus(undefined) → false', isKnownStatus(undefined) === false);

// 7) sortObjectDeep: ordena claves, NO reordena arrays.
const ordenado = sortObjectDeep({ b: 1, a: 2, c: { z: 1, y: [3, 1, 2] } }) as Record<string, unknown>;
comprueba('sortObjectDeep ordena las claves del objeto', JSON.stringify(Object.keys(ordenado)) === '["a","b","c"]');
comprueba(
  'sortObjectDeep ordena las claves anidadas',
  JSON.stringify(Object.keys(ordenado.c as Record<string, unknown>)) === '["y","z"]',
);
const arr = (ordenado.c as Record<string, unknown>).y;
comprueba('sortObjectDeep NO reordena arrays', Array.isArray(arr) && JSON.stringify(arr) === '[3,1,2]');
comprueba('sortObjectDeep respeta null', sortObjectDeep(null) === null);
comprueba(
  'sortObjectDeep respeta null dentro de un objeto',
  JSON.stringify(sortObjectDeep({ b: null, a: 1 })) === '{"a":1,"b":null}',
);
comprueba(
  'sortObjectDeep baja a los objetos dentro de un array',
  JSON.stringify(sortObjectDeep([{ b: 1, a: 2 }])) === '[{"a":2,"b":1}]',
);

// ── Aviso, no aserción: divergencia con el `sortObject` literal del SDK ─────
// El del SDK de Node no distingue arrays y los convierte en objetos indexados.
// Con los payloads reales de NOWPayments (objetos planos + `fee` anidado) las
// dos firmas coinciden; sólo divergirían si algún día mandaran un array.
// PENDIENTE DE FASE 0: contrastar con un IPN real capturado.
const firmaIngenua = createHmac('sha512', SECRETO)
  .update(JSON.stringify(sortObjectRefIngenuo(PAYLOAD)))
  .digest('hex');
const sinArray = { ...PAYLOAD } as Record<string, unknown>;
delete sinArray.historial;
const iguales = computeIpnSignature(sinArray, SECRETO) ===
  createHmac('sha512', SECRETO).update(JSON.stringify(sortObjectRefIngenuo(sinArray))).digest('hex');
console.log(
  `\n  aviso  sin arrays las dos variantes coinciden: ${iguales ? 'SÍ' : 'NO'} · ` +
    `con array divergen: ${firmaIngenua !== esperada ? 'SÍ (esperado)' : 'NO'}`,
);

// ── Resultado ───────────────────────────────────────────────────────────────
console.log('');
if (fallos.length) {
  console.log(`FALLOS ${fallos.length}/${total}: ${fallos.join(' · ')}`);
  process.exit(1);
}

// ── Doble variante (ajuste de Fable, 2026-09-06): con un array en el payload
// la verificación acepta TANTO la firma con arrays respetados COMO la del
// `sortObject` literal del SDK (arrays → objetos). Ambas son HMAC con el secreto.
comprueba('computeIpnSignatureLegacy reproduce la firma «ingenua» de referencia', computeIpnSignatureLegacy(PAYLOAD, SECRETO) === firmaIngenua);
comprueba('verifyIpnSignature acepta la firma legacy (arrays → objetos)', verifyIpnSignature(PAYLOAD, firmaIngenua, SECRETO) === true);
comprueba('verifyIpnSignature sigue aceptando la firma moderna', verifyIpnSignature(PAYLOAD, esperada, SECRETO) === true);
const legacyAlterada = (firmaIngenua[0] === 'a' ? 'b' : 'a') + firmaIngenua.slice(1);
comprueba('firma legacy alterada → false', verifyIpnSignature(PAYLOAD, legacyAlterada, SECRETO) === false);
const leg = sortObjectLegacy({ b: [3, 1], a: null }) as Record<string, unknown>;
comprueba('sortObjectLegacy convierte arrays en objetos indexados', JSON.stringify(leg) === '{"a":null,"b":{"0":3,"1":1}}');
const once = sortObjectLegacy({ x: [0,1,2,3,4,5,6,7,8,9,10] }) as Record<string, unknown>;
// Las claves enteras de un objeto JS se enumeran SIEMPRE en orden numérico
// ascendente (también en JSON.stringify), haga lo que haga el sort previo.
comprueba('sortObjectLegacy: un array de 11 elementos serializa con índices en orden numérico', JSON.stringify(once) === '{"x":{"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}}');

console.log(`OK ${ok}/${total}`);
