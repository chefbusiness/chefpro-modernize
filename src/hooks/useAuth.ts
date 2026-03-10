export function useAuth() {
  const token = sessionStorage.getItem('pro-prompts-jwt');
  if (!token) return { isAuthenticated: false, email: null, token: null };

  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    if (payload.exp < Date.now() / 1000) {
      sessionStorage.removeItem('pro-prompts-jwt');
      return { isAuthenticated: false, email: null, token: null };
    }
    return { isAuthenticated: true, email: payload.email as string, token };
  } catch {
    return { isAuthenticated: false, email: null, token: null };
  }
}
