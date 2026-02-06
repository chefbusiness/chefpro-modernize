

# Plan: Arreglar NH Hotels + Agregar 6 Nuevos Logos

## Problema Identificado

El archivo `nh-hotels.png` parece estar corrupto o no se copió correctamente. La solución es usar el archivo alternativo `nh-hotels-2.png` que proporcionaste.

---

## Logos a Agregar

| # | Archivo | Nombre de marca |
|---|---------|-----------------|
| 1 | `fierro.png` | Fierro by Carito y Germán |
| 2 | `stillroom.png` | Stillroom - El Arte de lo Invisible |
| 3 | `qatar-arways.png` | Qatar Airways |
| 4 | `singapore-airlines.png` | Singapore Airlines |
| 5 | `wyndham-hotels.png` | Wyndham Hotels & Resorts |
| 6 | `accor-hotels.png` | Accor Hotels |

---

## Archivos a Copiar

Copiar a `public/logos/`:

1. `nh-hotels-2.png` → Reemplazar `nh-hotels.png` (o usar nombre nuevo)
2. `fierro.png`
3. `stillroom.png`
4. `qatar-airways.png` (corregir nombre del typo)
5. `singapore-airlines.png`
6. `wyndham-hotels.png`
7. `accor-hotels.png`

---

## Actualización del Componente

**Archivo:** `src/components/TrustedByLogos.tsx`

Actualizar el array de logos:

```tsx
const logos = [
  // Hoteles
  { src: '/logos/melia-hotels.png', alt: 'Meliá Hotels International' },
  { src: '/logos/nh-hotels.png', alt: 'NH Hotels' },  // Arreglado
  { src: '/logos/marriot-hotels.png', alt: 'Marriott International' },
  { src: '/logos/intercontinental-hotels.png', alt: 'InterContinental Hotels & Resorts' },
  { src: '/logos/wyndham-hotels.png', alt: 'Wyndham Hotels & Resorts' },
  { src: '/logos/accor-hotels.png', alt: 'Accor Hotels' },
  
  // Aerolíneas
  { src: '/logos/qatar-airways.png', alt: 'Qatar Airways' },
  { src: '/logos/singapore-airlines.png', alt: 'Singapore Airlines' },
  
  // Restaurantes/Bares
  { src: '/logos/fierro.png', alt: 'Fierro by Carito y Germán' },
  { src: '/logos/stillroom.png', alt: 'Stillroom - El Arte de lo Invisible' },
];
```

---

## Total de Logos Después del Cambio

- **Antes:** 4 logos (con 1 roto)
- **Después:** 10 logos funcionando

---

## Resumen de Cambios

| Tipo | Archivo |
|------|---------|
| Copiar | 7 archivos a `public/logos/` |
| Modificar | `src/components/TrustedByLogos.tsx` |

