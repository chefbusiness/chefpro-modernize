

# Plan: Agregar 4 Nuevos Logos al Carrusel (Lote Final)

## Logos Recibidos

| # | Archivo | Nombre de marca | Categoría |
|---|---------|-----------------|-----------|
| 1 | `hosteleria-leioa.png` | Ostalaritza Leioa Hostelería | Escuela Culinaria |
| 2 | `shawellness.png` | SHA Masters of Longevity | Wellness Resort |
| 3 | `tragaluz.png` | Grupo Tragaluz | Grupo Restauración |
| 4 | `la-maquina.png` | La Máquina Grupo de Restauración | Grupo Restauración |

---

## Archivos a Copiar

Copiar a `public/logos/`:

1. `hosteleria-leioa.png`
2. `shawellness.png`
3. `tragaluz.png`
4. `la-maquina.png`

---

## Actualización del Componente

**Archivo:** `src/components/TrustedByLogos.tsx`

Array actualizado con los nuevos logos:

```tsx
const logos = [
  // Hoteles
  { src: '/logos/melia-hotels.png', alt: 'Meliá Hotels International' },
  { src: '/logos/marriot-hotels.png', alt: 'Marriott International' },
  { src: '/logos/intercontinental-hotels.png', alt: 'InterContinental Hotels & Resorts' },
  { src: '/logos/wyndham-hotels.png', alt: 'Wyndham Hotels & Resorts' },
  { src: '/logos/accor-hotels.png', alt: 'Accor Hotels' },
  { src: '/logos/villa-cortes-hotel.png', alt: 'Villa Cortés Deluxe Hotel' },
  { src: '/logos/shawellness.png', alt: 'SHA Masters of Longevity' },  // NUEVO
  
  // Aerolíneas
  { src: '/logos/qatar-airways.png', alt: 'Qatar Airways' },
  { src: '/logos/singapore-airlines.png', alt: 'Singapore Airlines' },
  
  // Restaurantes/Bares/Chefs
  { src: '/logos/fierro.png', alt: 'Fierro by Carito y Germán' },
  { src: '/logos/stillroom.png', alt: 'Stillroom - El Arte de lo Invisible' },
  { src: '/logos/taste-1973.png', alt: '1973 Taste Restaurant' },
  { src: '/logos/grupo-dani-garcia.png', alt: 'Grupo Dani García' },
  
  // Grupos Hostelería & Restauración
  { src: '/logos/amrest-group.png', alt: 'AmRest Group' },
  { src: '/logos/restaurant-brands-europe.png', alt: 'Restaurant Brands Europe' },
  { src: '/logos/tragaluz.png', alt: 'Grupo Tragaluz' },  // NUEVO
  { src: '/logos/la-maquina.png', alt: 'La Máquina Grupo de Restauración' },  // NUEVO
  
  // Escuelas & Formación
  { src: '/logos/hecansa-canarias.png', alt: 'Hecansa Hoteles Escuela de Canarias' },
  { src: '/logos/basque-culinary-center.png', alt: 'Basque Culinary Center' },
  { src: '/logos/hosteleria-leioa.png', alt: 'Ostalaritza Leioa Hostelería' },  // NUEVO
  
  // Alimentación & Proveedores
  { src: '/logos/albi-alimentacion.png', alt: 'Albi Alimentación & Bienestar' },
  
  // Grupos Empresariales & Innovación
  { src: '/logos/venture-group-tenerife.png', alt: 'Venture Group Tenerife' },
  { src: '/logos/labe.png', alt: 'Lab-e' },
];
```

---

## Total de Logos Después del Cambio

- **Antes:** 19 logos
- **Después:** 23 logos

---

## Categorías Finales

| Categoría | Cantidad |
|-----------|----------|
| Hoteles & Wellness | 7 |
| Aerolíneas | 2 |
| Restaurantes/Bares/Chefs | 4 |
| Grupos Hostelería & Restauración | 4 |
| Escuelas & Formación | 3 |
| Alimentación & Proveedores | 1 |
| Innovación & Empresas | 2 |

---

## Resumen de Cambios

| Tipo | Archivo |
|------|---------|
| Copiar | 4 archivos nuevos a `public/logos/` |
| Modificar | `src/components/TrustedByLogos.tsx` |

