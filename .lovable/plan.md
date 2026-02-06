

# Plan: Agregar 4 Nuevos Logos al Carrusel

## Logos Recibidos

| # | Archivo | Nombre de marca | Categoría |
|---|---------|-----------------|-----------|
| 1 | `albi-alimentación.png` | Albi Alimentación & Bienestar | Alimentación |
| 2 | `amrest-group.png` | AmRest Group | Grupo Hostelería |
| 3 | `restaurant-brands-europe.png` | Restaurant Brands Europe | Grupo Restauración |
| 4 | `grupo-dani-garcia.png` | Grupo Dani García | Chef/Restaurantes |

---

## Archivos a Copiar

Copiar a `public/logos/`:

1. `albi-alimentacion.png` (normalizar nombre sin tilde)
2. `amrest-group.png`
3. `restaurant-brands-europe.png`
4. `grupo-dani-garcia.png`

---

## Actualización del Componente

**Archivo:** `src/components/TrustedByLogos.tsx`

Agregar al array de logos en las categorías correspondientes:

```tsx
const logos = [
  // Hoteles (existentes)
  { src: '/logos/melia-hotels.png', alt: 'Meliá Hotels International' },
  { src: '/logos/marriot-hotels.png', alt: 'Marriott International' },
  { src: '/logos/intercontinental-hotels.png', alt: 'InterContinental Hotels & Resorts' },
  { src: '/logos/wyndham-hotels.png', alt: 'Wyndham Hotels & Resorts' },
  { src: '/logos/accor-hotels.png', alt: 'Accor Hotels' },
  { src: '/logos/villa-cortes-hotel.png', alt: 'Villa Cortés Deluxe Hotel' },
  
  // Aerolíneas (existentes)
  { src: '/logos/qatar-airways.png', alt: 'Qatar Airways' },
  { src: '/logos/singapore-airlines.png', alt: 'Singapore Airlines' },
  
  // Restaurantes/Bares (existentes + nuevos)
  { src: '/logos/fierro.png', alt: 'Fierro by Carito y Germán' },
  { src: '/logos/stillroom.png', alt: 'Stillroom - El Arte de lo Invisible' },
  { src: '/logos/taste-1973.png', alt: '1973 Taste Restaurant' },
  { src: '/logos/grupo-dani-garcia.png', alt: 'Grupo Dani García' },  // NUEVO
  
  // Grupos Hostelería & Restauración (NUEVA CATEGORÍA)
  { src: '/logos/amrest-group.png', alt: 'AmRest Group' },
  { src: '/logos/restaurant-brands-europe.png', alt: 'Restaurant Brands Europe' },
  
  // Escuelas & Formación (existentes)
  { src: '/logos/hecansa-canarias.png', alt: 'Hecansa Hoteles Escuela de Canarias' },
  { src: '/logos/basque-culinary-center.png', alt: 'Basque Culinary Center' },
  
  // Alimentación & Proveedores (NUEVA CATEGORÍA)
  { src: '/logos/albi-alimentacion.png', alt: 'Albi Alimentación & Bienestar' },
  
  // Grupos Empresariales & Innovación (existentes)
  { src: '/logos/venture-group-tenerife.png', alt: 'Venture Group Tenerife' },
  { src: '/logos/labe.png', alt: 'Lab-e' },
];
```

---

## Total de Logos Después del Cambio

- **Antes:** 15 logos
- **Después:** 19 logos

---

## Categorías Actualizadas

| Categoría | Cantidad |
|-----------|----------|
| Hoteles | 6 |
| Aerolíneas | 2 |
| Restaurantes/Bares/Chefs | 4 |
| Grupos Hostelería | 2 |
| Escuelas & Formación | 2 |
| Alimentación & Proveedores | 1 |
| Innovación & Empresas | 2 |

---

## Resumen de Cambios

| Tipo | Archivo |
|------|---------|
| Copiar | 4 archivos nuevos a `public/logos/` |
| Modificar | `src/components/TrustedByLogos.tsx` |

