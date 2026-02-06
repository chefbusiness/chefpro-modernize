

# Plan: Agregar 6 Nuevos Logos al Carrusel

## Logos Recibidos

| # | Archivo | Nombre de marca | Categoría |
|---|---------|-----------------|-----------|
| 1 | `taste-1973.png` | 1973 Taste Restaurant | Restaurante |
| 2 | `villa-cortes-hotel.png` | Villa Cortés Deluxe Hotel | Hotel |
| 3 | `hecanca-canarias.png` | Hecansa Hoteles Escuela de Canarias | Escuela/Hotel |
| 4 | `basque-culinary-center.png` | Basque Culinary Center | Escuela Culinaria |
| 5 | `venture-group-tenerife.png` | Venture Group Tenerife | Grupo Empresarial |
| 6 | `labe.png` | Lab-e | Laboratorio/Innovación |

---

## Archivos a Copiar

Copiar a `public/logos/`:

1. `taste-1973.png`
2. `villa-cortes-hotel.png`
3. `hecansa-canarias.png`
4. `basque-culinary-center.png`
5. `venture-group-tenerife.png`
6. `labe.png`

---

## Actualización del Componente

**Archivo:** `src/components/TrustedByLogos.tsx`

Array actualizado con categorías organizadas:

```tsx
const logos = [
  // Hoteles
  { src: '/logos/melia-hotels.png', alt: 'Meliá Hotels International' },
  { src: '/logos/marriot-hotels.png', alt: 'Marriott International' },
  { src: '/logos/intercontinental-hotels.png', alt: 'InterContinental Hotels & Resorts' },
  { src: '/logos/wyndham-hotels.png', alt: 'Wyndham Hotels & Resorts' },
  { src: '/logos/accor-hotels.png', alt: 'Accor Hotels' },
  { src: '/logos/villa-cortes-hotel.png', alt: 'Villa Cortés Deluxe Hotel' },
  
  // Aerolíneas
  { src: '/logos/qatar-airways.png', alt: 'Qatar Airways' },
  { src: '/logos/singapore-airlines.png', alt: 'Singapore Airlines' },
  
  // Restaurantes/Bares
  { src: '/logos/fierro.png', alt: 'Fierro by Carito y Germán' },
  { src: '/logos/stillroom.png', alt: 'Stillroom - El Arte de lo Invisible' },
  { src: '/logos/taste-1973.png', alt: '1973 Taste Restaurant' },
  
  // Escuelas & Formación
  { src: '/logos/hecansa-canarias.png', alt: 'Hecansa Hoteles Escuela de Canarias' },
  { src: '/logos/basque-culinary-center.png', alt: 'Basque Culinary Center' },
  
  // Grupos Empresariales & Innovación
  { src: '/logos/venture-group-tenerife.png', alt: 'Venture Group Tenerife' },
  { src: '/logos/labe.png', alt: 'Lab-e' },
];
```

---

## Total de Logos Después del Cambio

- **Antes:** 9 logos
- **Después:** 15 logos

---

## Resumen de Cambios

| Tipo | Archivo |
|------|---------|
| Copiar | 6 archivos nuevos a `public/logos/` |
| Modificar | `src/components/TrustedByLogos.tsx` |

