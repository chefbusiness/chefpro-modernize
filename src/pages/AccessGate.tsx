import { useEffect, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { Loader2 } from 'lucide-react';

type Status = 'loading' | 'error';

export default function AccessGate() {
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const [status, setStatus] = useState<Status>('loading');

  useEffect(() => {
    const checkoutToken = params.get('session_id') || params.get('token');
    const jwtToken = params.get('jwt');

    if (!checkoutToken && !jwtToken) {
      setStatus('error');
      return;
    }

    const verify = async () => {
      try {
        const body = checkoutToken
          ? { checkoutSessionId: checkoutToken }
          : { existingJwt: jwtToken };

        const res = await fetch('/.netlify/functions/verify-purchase', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        });

        const data = await res.json();

        if (data.valid && data.jwt) {
          localStorage.setItem('pro-prompts-jwt', data.jwt);
          navigate('/pro-prompts-library', { replace: true });
        } else {
          setStatus('error');
        }
      } catch {
        setStatus('error');
      }
    };

    verify();
  }, [params, navigate]);

  return (
    <>
      <Helmet>
        <meta name="robots" content="noindex, nofollow" />
        <title>Verificando acceso... | AI Chef Pro</title>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a] flex items-center justify-center px-4">
        {status === 'loading' ? (
          <div className="text-center">
            <Loader2 className="w-10 h-10 text-[#FFD700] animate-spin mx-auto mb-4" />
            <p className="text-white text-lg font-medium">Verificando tu compra...</p>
            <p className="text-gray-400 text-sm mt-1">Un momento por favor</p>
          </div>
        ) : (
          <div className="text-center max-w-md">
            <div className="w-16 h-16 rounded-full bg-red-500/10 flex items-center justify-center mx-auto mb-4">
              <span className="text-red-400 text-2xl">!</span>
            </div>
            <h1 className="text-white text-xl font-bold mb-3">
              No hemos podido verificar tu acceso
            </h1>
            <p className="text-gray-400 mb-6 leading-relaxed">
              Si acabas de comprar, revisa tu email para el enlace de acceso.
              ¿Problemas? Contáctanos en{' '}
              <a href="mailto:info@aichef.pro" className="text-[#FFD700] underline">
                info@aichef.pro
              </a>
            </p>
            <a
              href="/pro-prompts-ebook"
              className="inline-block px-6 py-3 bg-[#FFD700] text-black font-bold rounded-xl hover:bg-[#FFD700]/90 transition-all"
            >
              Volver al eBook
            </a>
          </div>
        )}
      </div>
    </>
  );
}
