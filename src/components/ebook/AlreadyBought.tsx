import { useState } from 'react';
import { Mail, Loader2, CheckCircle } from 'lucide-react';

interface Props {
  product?: 'pro-prompts-ebook' | 'kit-escandallos';
  label?: string;
}

export default function AlreadyBought({
  product = 'pro-prompts-ebook',
  label = '¿Ya compraste el eBook? Vuelve a entrar al dashboard',
}: Props) {
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.trim()) return;

    setStatus('loading');
    try {
      const res = await fetch('/.netlify/functions/resend-access', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email.trim(), product }),
      });

      if (res.ok) {
        setStatus('success');
      } else {
        setStatus('error');
      }
    } catch {
      setStatus('error');
    }
  };

  return (
    <div className="border-t border-white/10 pt-8 mt-4">
      <div className="text-center">
        <p className="text-white font-semibold text-sm mb-1">
          {label}
        </p>
        <p className="text-gray-500 text-xs mb-3">
          Introduce tu email de compra y te enviaremos el enlace de acceso
        </p>
        {status === 'success' ? (
          <div className="flex items-center justify-center gap-2 text-emerald-400 text-sm">
            <CheckCircle className="w-4 h-4" />
            <span>Enlace de acceso enviado a tu email</span>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="flex items-center justify-center gap-2 max-w-sm mx-auto">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Tu email de compra"
              required
              className="flex-1 px-4 py-2 bg-white/5 border border-white/10 rounded-lg text-white text-sm placeholder:text-gray-500 focus:outline-none focus:border-[#FFD700]/40"
            />
            <button
              type="submit"
              disabled={status === 'loading'}
              className="px-4 py-2 bg-white/10 border border-white/10 text-gray-300 text-sm font-medium rounded-lg hover:bg-white/15 hover:text-white transition-all disabled:opacity-50 flex items-center gap-2"
            >
              {status === 'loading' ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <Mail className="w-4 h-4" />
              )}
              Reenviar acceso
            </button>
          </form>
        )}
        {status === 'error' && (
          <p className="text-red-400 text-xs mt-2">
            No encontramos una compra con ese email. ¿Usaste otro?
          </p>
        )}
      </div>
    </div>
  );
}
