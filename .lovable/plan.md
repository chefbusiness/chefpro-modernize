

# Plan: Añadir Esquinas Redondeadas a los Logos

## Problema Identificado

Los logos en el carrusel tienen esquinas rectas (rectangulares) que contrastan negativamente con el fondo oscuro y no mantienen la coherencia con el resto de la landing page que usa esquinas redondeadas (`rounded-*`).

## Solución

Envolver cada logo en un contenedor con fondo semitransparente y esquinas redondeadas, creando un efecto de "tarjeta" sutil que integra mejor los logos con el diseño.

## Cambios a Realizar

### Archivo: `src/components/TrustedByLogos.tsx`

**Antes (líneas 80-88):**
```jsx
<img 
  key={i}
  src={logo.src} 
  alt={logo.alt}
  loading="lazy"
  className="h-14 md:h-18 lg:h-20 w-auto flex-shrink-0 logo-glow transition-all duration-300"
/>
```

**Después:**
```jsx
<div 
  key={i}
  className="flex-shrink-0 bg-white/10 backdrop-blur-sm rounded-xl p-3 md:p-4 logo-glow transition-all duration-300"
>
  <img 
    src={logo.src} 
    alt={logo.alt}
    loading="lazy"
    className="h-10 md:h-12 lg:h-14 w-auto object-contain"
  />
</div>
```

## Detalles del Diseño

| Propiedad | Valor | Propósito |
|-----------|-------|-----------|
| `bg-white/10` | Fondo blanco 10% opacidad | Crea contraste sutil sin ser invasivo |
| `backdrop-blur-sm` | Blur sutil | Efecto glassmorphism moderno |
| `rounded-xl` | Esquinas redondeadas 12px | Coherencia con el resto del diseño |
| `p-3 md:p-4` | Padding interno | Espacio respirable alrededor del logo |

## Resultado Visual Esperado

```text
Antes:                          Después:
┌────────────┐                  ╭────────────────╮
│   LOGO     │     →            │    ╭──────╮    │
│  (rectas)  │                  │    │ LOGO │    │
└────────────┘                  │    ╰──────╯    │
                                ╰────────────────╯
                                  (redondeadas)
```

## Beneficios

1. **Coherencia visual**: Las esquinas redondeadas se alinean con el sistema de diseño
2. **Mejor integración**: Los logos flotan elegantemente sobre el fondo oscuro
3. **Efecto premium**: El glassmorphism añade profundidad y modernidad
4. **Hover mejorado**: El efecto spotlight se aplicará a toda la tarjeta

