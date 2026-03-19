import { useEffect, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { Loader2, ShieldCheck, AlertCircle } from 'lucide-react';

export default function KitTareasHamburguseriaAccessGate() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const [status, setStatus] = useState<'loading' | 'success' | 'error'>('loading');
  const [errorMsg, setErrorMsg] = useState('');

  useEffect(() => {
    const sessionId = searchParams.get('session_id');
    if (!sessionId) {
      setStatus('error');
      setErrorMsg('No se encontró la sesión de pago.');
      return;
    }

    fetch('/.netlify/functions/verify-purchase', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sessionId, product: 'kit-tareas-hamburgueseria' }),
    })
      .then((r) => r.json())
      .then((data) => {
        if (data.token) {
          localStorage.setItem('kit-tareas-hamburgueseria-jwt', data.token);
          setStatus('success');
          setTimeout(() => navigate('/kit-tareas-hamburgueseria-library'), 1500);
        } else {
          setStatus('error');
          setErrorMsg(data.error || 'Error al verificar la compra.');
        }
      })
      .catch(() => {
        setStatus('error');
        setErrorMsg('Error de conexión. Inténtalo de nuevo.');
      });
  }, [searchParams, navigate]);

  return (
    <div className="min-h-screen bg-[#0a0a0a] flex items-center justify-center px-4">
      <div className="max-w-md mx-auto text-center">
        {status === 'loading' && (
          <>
            <Loader2 className="w-12 h-12 text-[#FFD700] animate-spin mx-auto mb-4" />
            <h1 className="text-xl font-bold text-white mb-2">Verificando tu compra del Kit de Tareas Hamburguesería...</h1>
            <p className="text-gray-400">Esto solo tarda unos segundos</p>
          </>
        )}
        {status === 'success' && (
          <>
            <ShieldCheck className="w-12 h-12 text-[#FFD700] mx-auto mb-4" />
            <h1 className="text-xl font-bold text-white mb-2">¡Compra verificada!</h1>
            <p className="text-gray-400">Redirigiendo a tu dashboard...</p>
          </>
        )}
        {status === 'error' && (
          <>
            <AlertCircle className="w-12 h-12 text-red-400 mx-auto mb-4" />
            <h1 className="text-xl font-bold text-white mb-2">Error</h1>
            <p className="text-gray-400 mb-4">{errorMsg}</p>
            <a href="/kit-tareas-hamburgueseria" className="text-[#FFD700] hover:underline">
              Volver al Kit de Tareas Hamburguesería
            </a>
          </>
        )}
      </div>
    </div>
  );
}
