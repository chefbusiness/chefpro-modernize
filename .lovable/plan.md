

# Plan: Aumentar Tamaño de Logos un 30%

## Cambios a Realizar

### Archivo: `src/components/TrustedByLogos.tsx`

**Tamaños actuales vs nuevos:**

| Breakpoint | Actual | Nuevo (+30%) |
|------------|--------|--------------|
| Mobile | `h-10` (40px) | `h-14` (56px) |
| Tablet (md) | `h-12` (48px) | `h-16` (64px) |
| Desktop (lg) | `h-14` (56px) | `h-20` (80px) |

**Padding del contenedor (proporcional):**

| Breakpoint | Actual | Nuevo |
|------------|--------|-------|
| Mobile | `p-3` | `p-4` |
| Tablet/Desktop (md) | `p-4` | `p-5` |

## Código a Modificar

**Línea ~80-87:**

```jsx
// Antes
<div className="... p-3 md:p-4 ...">
  <img className="h-10 md:h-12 lg:h-14 ..." />
</div>

// Después
<div className="... p-4 md:p-5 ...">
  <img className="h-14 md:h-16 lg:h-20 ..." />
</div>
```

## Resultado Visual

Los logos serán aproximadamente 30-40% más grandes, manteniendo proporciones elegantes con el padding aumentado del contenedor.

