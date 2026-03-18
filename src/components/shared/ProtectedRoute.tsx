import { Navigate } from 'react-router-dom';
import type { ReactNode } from 'react';

interface Props {
  children: ReactNode;
  storageKey?: string;
  redirectTo?: string;
}

export default function ProtectedRoute({
  children,
  storageKey = 'pro-prompts-jwt',
  redirectTo = '/pro-prompts-ebook',
}: Props) {
  const token = localStorage.getItem(storageKey);
  if (!token) return <Navigate to={redirectTo} replace />;
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    if (payload.exp < Date.now() / 1000) {
      localStorage.removeItem(storageKey);
      return <Navigate to={redirectTo} replace />;
    }
    return <>{children}</>;
  } catch {
    return <Navigate to={redirectTo} replace />;
  }
}
