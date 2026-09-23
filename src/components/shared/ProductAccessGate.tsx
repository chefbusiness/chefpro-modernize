import { useEffect, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { Loader2 } from 'lucide-react';

interface Props {
  productId: string;
  storageKey: string;
  dashboardPath: string;
  landingPath: string;
  productLabel: string;
  /** Idioma de la tienda (2026-09-23). Ausente = 'es': los 50 productos españoles
   *  no lo pasan y se pintan exactamente igual que antes. */
  lang?: 'es' | 'en';
}

// Textos visibles del gate por idioma. El `es` es el literal que había en el JSX
// (JSX colapsa el salto de línea del párrafo de error en un espacio: aquí ya va así).
const COPY = {
  es: {
    title: 'Verificando acceso... | AI Chef Pro',
    loading: 'Verificando tu compra...',
    loadingSub: 'Un momento por favor',
    errorTitle: 'No hemos podido verificar tu acceso',
    errorBody: 'Si acabas de comprar, revisa tu email para el enlace de acceso. ¿Problemas? Contáctanos en',
    backTo: 'Volver a ',
  },
  en: {
    title: 'Verifying access... | AI Chef Pro',
    loading: 'Verifying your purchase...',
    loadingSub: 'Just a moment, please',
    errorTitle: "We couldn't verify your access",
    errorBody: "If you just purchased, check your email for your access link. Having trouble? Contact us at",
    backTo: 'Back to ',
  },
} as const;

type Status = 'loading' | 'error';

export default function ProductAccessGate({
  productId,
  storageKey,
  dashboardPath,
  landingPath,
  productLabel,
  lang = 'es',
}: Props) {
  const t = COPY[lang === 'en' ? 'en' : 'es'];
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
          ? { checkoutSessionId: checkoutToken, product: productId }
          : { existingJwt: jwtToken, product: productId };

        const res = await fetch('/.netlify/functions/verify-purchase', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        });

        const data = await res.json();

        if (data.valid && data.jwt) {
          localStorage.setItem(storageKey, data.jwt);
          navigate(dashboardPath, { replace: true });
        } else {
          setStatus('error');
        }
      } catch {
        setStatus('error');
      }
    };

    verify();
  }, [params, navigate, productId, storageKey, dashboardPath]);

  return (
    <>
      <Helmet>
        <meta name="robots" content="noindex, nofollow" />
        <title>{t.title}</title>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a] flex items-center justify-center px-4">
        {status === 'loading' ? (
          <div className="text-center">
            <Loader2 className="w-10 h-10 text-[#FFD700] animate-spin mx-auto mb-4" />
            <p className="text-white text-lg font-medium">{t.loading}</p>
            <p className="text-gray-400 text-sm mt-1">{t.loadingSub}</p>
          </div>
        ) : (
          <div className="text-center max-w-md">
            <div className="w-16 h-16 rounded-full bg-red-500/10 flex items-center justify-center mx-auto mb-4">
              <span className="text-red-400 text-2xl">!</span>
            </div>
            <h1 className="text-white text-xl font-bold mb-3">
              {t.errorTitle}
            </h1>
            <p className="text-gray-400 mb-6 leading-relaxed">
              {t.errorBody}{' '}
              <a href="mailto:info@aichef.pro" className="text-[#FFD700] underline">
                info@aichef.pro
              </a>
            </p>
            <a
              href={landingPath}
              className="inline-block px-6 py-3 bg-[#FFD700] text-black font-bold rounded-xl hover:bg-[#FFD700]/90 transition-all"
            >
              {t.backTo}{productLabel}
            </a>
          </div>
        )}
      </div>
    </>
  );
}
