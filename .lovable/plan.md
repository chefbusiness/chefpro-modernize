
# Plan: Habilitar Subdominio Italiano (itapp.aichef.pro)

## Contexto

Toda la lógica de redirección de URLs de la aplicación pasa por la función `getAppUrl` en `src/hooks/useLanguage.ts`. Actualmente solo hay dos subdominios:

- **Español** → `https://app.aichef.pro`
- **Resto de idiomas** → `https://enapp.aichef.pro`

## Cambio

Se añade `it` como caso específico en la función `getAppUrl`, igual que ya existe para `en` y `es`.

**Archivo: `src/hooks/useLanguage.ts` (línea 57-60)**

```ts
// Antes
const getAppUrl = (language?: Language) => {
  const targetLang = language || i18n.language as Language;
  return targetLang === 'en' ? 'https://enapp.aichef.pro' : 'https://app.aichef.pro';
};

// Después
const getAppUrl = (language?: Language) => {
  const targetLang = language || i18n.language as Language;
  if (targetLang === 'en') return 'https://enapp.aichef.pro';
  if (targetLang === 'it') return 'https://itapp.aichef.pro';
  return 'https://app.aichef.pro';
};
```

## Alcance del cambio

Al ser `getAppUrl` el único punto de verdad para las URLs de la app en todo el proyecto, este cambio afecta automáticamente a **todos los botones CTA** en todas las páginas y componentes:

- Hero principal → botón "Probar gratis"
- Sección de precios → todos los planes
- ModernChefSection → botón CTA
- AIImageGallery → botón CTA
- CategoryCTAs → todos los CTAs por categoría
- Y cualquier otro componente que use `getAppUrl`

Solo se modifica un único archivo. No se requieren cambios en ningún otro componente ni en los archivos de traducción.
