import { useState } from 'react';
import { Helmet } from 'react-helmet-async';
import { Loader2, Copy, Check, Mail, Link as LinkIcon, ShieldAlert } from 'lucide-react';
import { PRODUCTS_CONFIG, PRODUCT_IDS } from '../data/productos-digitales-config';

export default function AdminGenerateAccess() {
  const [adminPassword, setAdminPassword] = useState('');
  const [email, setEmail] = useState('');
  const [product, setProduct] = useState<string>(PRODUCT_IDS[0]);
  const [sendEmail, setSendEmail] = useState(true);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<{ magicLink: string; emailSent: boolean } | null>(null);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);
    setCopied(false);
    try {
      const res = await fetch('/.netlify/functions/admin-generate-access', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ adminPassword, email, product, sendEmail }),
      });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error || `Error ${res.status}`);
      } else {
        setResult({ magicLink: data.magicLink, emailSent: data.emailSent });
      }
    } catch {
      setError('Error de conexión');
    } finally {
      setLoading(false);
    }
  };

  const copyLink = async () => {
    if (!result) return;
    await navigator.clipboard.writeText(result.magicLink);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const whatsappShareUrl = result
    ? `https://wa.me/?text=${encodeURIComponent(
        `Hola! Aquí tienes tu enlace de acceso a tu producto AI Chef Pro:\n\n${result.magicLink}\n\nGuárdalo, es válido durante 12 meses.`
      )}`
    : '#';

  return (
    <>
      <Helmet>
        <meta name="robots" content="noindex, nofollow" />
        <title>Admin: Generar Acceso Manual | AI Chef Pro</title>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a] text-white px-4 py-12">
        <div className="max-w-2xl mx-auto">
          <div className="flex items-center gap-2 mb-2">
            <ShieldAlert className="w-6 h-6 text-[#FFD700]" />
            <h1 className="text-2xl font-bold">Generar Acceso Manual</h1>
          </div>
          <p className="text-gray-400 text-sm mb-8">
            Genera un magic link para clientes que reportan problemas de acceso después de comprar.
            Verifica el pago en Stripe antes de generar el link.
          </p>

          <form onSubmit={handleSubmit} className="space-y-5 bg-white/5 border border-white/10 rounded-xl p-6">
            <div>
              <label className="block text-sm font-semibold mb-1.5">Contraseña admin</label>
              <input
                type="password"
                required
                value={adminPassword}
                onChange={(e) => setAdminPassword(e.target.value)}
                className="w-full px-4 py-2.5 rounded-lg bg-black/40 border border-white/10 text-white placeholder-gray-500 focus:border-[#FFD700] focus:outline-none"
                placeholder="••••••••"
                autoComplete="current-password"
              />
            </div>

            <div>
              <label className="block text-sm font-semibold mb-1.5">Email del cliente</label>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-4 py-2.5 rounded-lg bg-black/40 border border-white/10 text-white placeholder-gray-500 focus:border-[#FFD700] focus:outline-none"
                placeholder="cliente@ejemplo.com"
              />
            </div>

            <div>
              <label className="block text-sm font-semibold mb-1.5">Producto</label>
              <select
                value={product}
                onChange={(e) => setProduct(e.target.value)}
                className="w-full px-4 py-2.5 rounded-lg bg-black/40 border border-white/10 text-white focus:border-[#FFD700] focus:outline-none"
              >
                {PRODUCT_IDS.map((id) => {
                  const cfg = PRODUCTS_CONFIG[id];
                  return (
                    <option key={id} value={id}>
                      {cfg.name} ({cfg.priceLabel})
                    </option>
                  );
                })}
              </select>
            </div>

            <label className="flex items-center gap-2 text-sm">
              <input
                type="checkbox"
                checked={sendEmail}
                onChange={(e) => setSendEmail(e.target.checked)}
                className="w-4 h-4 rounded accent-[#FFD700]"
              />
              <Mail className="w-4 h-4 text-gray-400" />
              También enviar el link por email al cliente
            </label>

            <button
              type="submit"
              disabled={loading}
              className="w-full px-4 py-3 rounded-lg bg-[#FFD700] text-black font-bold hover:bg-[#FFD700]/90 transition-all disabled:opacity-50 flex items-center justify-center gap-2"
            >
              {loading ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  Generando...
                </>
              ) : (
                <>
                  <LinkIcon className="w-5 h-5" />
                  Generar magic link
                </>
              )}
            </button>

            {error && (
              <div className="text-red-400 text-sm bg-red-500/10 border border-red-500/20 rounded-lg p-3">
                {error}
              </div>
            )}
          </form>

          {result && (
            <div className="mt-6 bg-emerald-500/10 border border-emerald-500/30 rounded-xl p-5">
              <h2 className="font-bold text-emerald-400 mb-3">Magic link generado</h2>

              <div className="bg-black/40 border border-white/10 rounded-lg p-3 break-all text-sm font-mono text-gray-300 mb-3">
                {result.magicLink}
              </div>

              <div className="flex flex-wrap gap-2">
                <button
                  onClick={copyLink}
                  className="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-white/10 hover:bg-white/15 text-sm transition-colors"
                >
                  {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Copy className="w-4 h-4" />}
                  {copied ? 'Copiado' : 'Copiar link'}
                </button>
                <a
                  href={whatsappShareUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 text-sm transition-colors"
                >
                  Compartir por WhatsApp
                </a>
              </div>

              <p className="text-xs text-gray-400 mt-3">
                {result.emailSent
                  ? 'Email enviado al cliente correctamente.'
                  : sendEmail
                  ? 'No se pudo enviar el email automáticamente. Comparte el link manualmente.'
                  : 'Comparte el link por email o WhatsApp.'}
              </p>
            </div>
          )}
        </div>
      </div>
    </>
  );
}
