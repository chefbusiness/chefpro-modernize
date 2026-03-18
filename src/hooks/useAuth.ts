export function useAuth(storageKey = 'pro-prompts-jwt') {
  const token = localStorage.getItem(storageKey);
  if (!token) return { isAuthenticated: false, email: null, token: null, product: null };

  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    if (payload.exp < Date.now() / 1000) {
      localStorage.removeItem(storageKey);
      return { isAuthenticated: false, email: null, token: null, product: null };
    }
    return {
      isAuthenticated: true,
      email: payload.email as string,
      token,
      product: (payload.product as string) || null,
    };
  } catch {
    return { isAuthenticated: false, email: null, token: null, product: null };
  }
}
