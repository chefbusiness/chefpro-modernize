import { Navigate } from 'react-router-dom';
import type { ReactNode } from 'react';

export default function ProtectedRoute({ children }: { children: ReactNode }) {
  const token = localStorage.getItem('pro-prompts-jwt');
  if (!token) return <Navigate to="/pro-prompts-ebook" replace />;
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    if (payload.exp < Date.now() / 1000) {
      localStorage.removeItem('pro-prompts-jwt');
      return <Navigate to="/pro-prompts-ebook" replace />;
    }
    return <>{children}</>;
  } catch {
    return <Navigate to="/pro-prompts-ebook" replace />;
  }
}
