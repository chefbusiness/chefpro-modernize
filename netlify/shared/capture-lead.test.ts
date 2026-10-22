import assert from 'node:assert/strict';
import test from 'node:test';
import {
  clearSegmentCache,
  originAllowed,
  parseCaptureBody,
  saveCapture,
} from './capture-lead.ts';

const base = {
  email: 'Chef@Restaurante.com',
  lang: 'es',
  source: 'food-cost-calculator',
  consent: true,
};

test('rechaza sin consentimiento y normaliza el email', () => {
  assert.equal(parseCaptureBody({ ...base, consent: false }).ok, false);
  const ok = parseCaptureBody(base);
  assert.equal(ok.ok, true);
  if (ok.ok && !ok.honeypot) assert.equal(ok.value.email, 'chef@restaurante.com');
});

test('el honeypot no es un error', () => {
  const parsed = parseCaptureBody({ ...base, website: 'spam' });
  assert.equal(parsed.ok && parsed.honeypot, true);
});

test('origen del site y del preview', () => {
  assert.equal(originAllowed('https://aichef.pro'), true);
  assert.equal(originAllowed('https://deploy-preview-9--aichefpro.netlify.app'), true);
  assert.equal(originAllowed('https://evil.example'), false);
  assert.equal(originAllowed(undefined), true);
});

test('crea el segmento y el contacto', async () => {
  clearSegmentCache();
  const calls: string[] = [];
  const fetchMock: typeof fetch = async (input, init) => {
    const url = String(input);
    calls.push(`${init?.method} ${url}`);
    if (url.includes('/segments?')) {
      return new Response(JSON.stringify({ data: [], has_more: false }), { status: 200 });
    }
    if (url.endsWith('/segments')) {
      return new Response(JSON.stringify({ id: 'seg-es' }), { status: 200 });
    }
    if (url.endsWith('/contacts')) {
      const body = JSON.parse(String(init?.body));
      assert.equal(body.email, 'chef@restaurante.com');
      assert.equal(body.unsubscribed, false);
      assert.equal(body.segments[0].id, 'seg-es');
      assert.equal(body.properties.capture_lang, 'es');
      return new Response(JSON.stringify({ id: 'ct_1' }), { status: 200 });
    }
    return new Response('{}', { status: 500 });
  };
  const saved = await saveCapture(
    { email: 'chef@restaurante.com', lang: 'es', source: 'footer-newsletter' },
    { fetch: fetchMock, apiKey: 're_test', env: {} },
  );
  assert.deepEqual(saved, { ok: true });
  assert.equal(calls.some((c) => c.startsWith('POST') && c.endsWith('/segments')), true);
});

test('contacto ya existente entra en el segmento', async () => {
  clearSegmentCache();
  const fetchMock: typeof fetch = async (input, init) => {
    const url = String(input);
    if (url.includes('/segments')) {
      return new Response(JSON.stringify({ data: [{ id: 'seg-en', name: 'aichef.pro captacion en' }] }), { status: 200 });
    }
    if (url.endsWith('/contacts') && init?.method === 'POST') {
      return new Response(JSON.stringify({ message: 'exists' }), { status: 409 });
    }
    if (url.includes('/segments/seg-en') && init?.method === 'POST') {
      return new Response(JSON.stringify({ id: 'seg-en' }), { status: 200 });
    }
    if (init?.method === 'PATCH') {
      return new Response(JSON.stringify({ id: 'ct' }), { status: 200 });
    }
    return new Response('{}', { status: 500 });
  };
  const saved = await saveCapture(
    { email: 'a@b.co', lang: 'en', source: 'food-cost-calculator' },
    { fetch: fetchMock, apiKey: 're_test', env: { RESEND_CAPTURE_SEGMENT_EN: 'seg-en' } },
  );
  assert.deepEqual(saved, { ok: true });
});

test('sin API key no llama a Resend', async () => {
  const saved = await saveCapture(
    { email: 'a@b.co', lang: 'fr', source: 'footer-newsletter' },
    { apiKey: undefined, fetch: async () => { throw new Error('no'); } },
  );
  assert.deepEqual(saved, { ok: false, error: 'misconfigured' });
});
