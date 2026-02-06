

# Plan: Aumentar Tamaño del H1 en Móvil y Tablet

## Problema Actual

El H1 del Hero tiene tamaños que se ven pequeños en móvil y tablet:

| Breakpoint | Clase Actual | Tamaño |
|------------|--------------|--------|
| Móvil (<640px) | `text-3xl` | 30px |
| Tablet (≥768px) | `md:text-5xl` | 48px |
| Desktop (≥1024px) | `lg:text-6xl` | 60px |

## Propuesta de Nuevos Tamaños

| Breakpoint | Nueva Clase | Nuevo Tamaño |
|------------|-------------|--------------|
| Móvil (<640px) | `text-4xl` | 36px (+6px) |
| Tablet (≥768px) | `md:text-5xl` | 48px (sin cambio) |
| Tablet/Desktop intermedio (≥768px) | `md:text-6xl` | 60px (+12px) |
| Desktop (≥1024px) | `lg:text-7xl` | 72px (+12px) |

---

## Cambio en ModernHero.tsx

### Antes (línea 37):
```tsx
<h1 className="text-center text-3xl font-bold leading-tight tracking-tighter md:text-5xl lg:text-6xl lg:leading-[1.1] text-balance">
```

### Después:
```tsx
<h1 className="text-center text-4xl font-bold leading-tight tracking-tighter md:text-6xl lg:text-7xl lg:leading-[1.1] text-balance">
```

---

## Resultado Visual Esperado

### Móvil (antes → después)
```
30px → 36px (+20% más grande)
```

### Tablet (antes → después)
```
48px → 60px (+25% más grande)
```

### Desktop (se mantiene bien, pero crece proporcionalmente)
```
60px → 72px (+20% más grande)
```

---

## Archivo a Modificar

1. `src/components/ModernHero.tsx` - Línea 37: Actualizar clases del H1

---

## Notas Técnicas

- Se usa la escala de Tailwind: `text-4xl` (2.25rem), `text-6xl` (3.75rem), `text-7xl` (4.5rem)
- El `leading-tight` y `tracking-tighter` se mantienen para legibilidad
- El `text-balance` ayuda a distribuir el texto uniformemente

