

# Plan: Logo Carousel "Trusted By" - Profesionales de Hostelería

## Resumen

Crear un nuevo componente de carrusel de logos en movimiento (infinite scroll ticker) que se ubicará entre el Hero y la sección ScreenshotSection. Mostrará logos de empresas/marcas reconocidas de la industria hotelera y gastronómica.

---

## Diseño Visual

```text
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│      USADO POR LOS MEJORES PROFESIONALES DE HOSTELERÍA             │
│              QUE DESTACAN ALREDEDOR DEL MUNDO                       │
│                                                                     │
│  ←── [Logo1] [Logo2] [Logo3] [Logo4] ... [LogoN] [Logo1] ... ──→   │
│              (cinta en movimiento continuo)                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Estructura del Componente

### Nuevo archivo: `src/components/TrustedByLogos.tsx`

**Características técnicas:**
- H2 con texto traducido en los 7 idiomas
- Carrusel CSS puro (sin dependencias extras) con animación `infinite scroll`
- Los logos se duplican para crear efecto de loop infinito
- Pausa al hover para que el usuario pueda ver los logos
- Tamaño de logos responsive:
  - Móvil: 80px de ancho
  - Tablet: 100px de ancho  
  - Desktop: 120px de ancho
- Fondo sutil para destacar la sección

---

## Traducciones a Agregar (7 idiomas)

Nueva clave: `trusted_by`

| Idioma | H2 Título |
|--------|-----------|
| ES | "Usado por los mejores profesionales de hostelería que destacan alrededor del mundo" |
| EN | "Used by the best hospitality professionals who excel around the world" |
| FR | "Utilisé par les meilleurs professionnels de l'hôtellerie qui excellent dans le monde" |
| DE | "Genutzt von den besten Hotellerie-Profis, die weltweit herausragen" |
| IT | "Utilizzato dai migliori professionisti dell'ospitalità che eccellono nel mondo" |
| PT | "Usado pelos melhores profissionais de hotelaria que se destacam no mundo" |
| NL | "Gebruikt door de beste horecaprofessionals die wereldwijd uitblinken" |

---

## Logos a Integrar

Primeros 4 logos (proporcionados):
1. `melia-hotels.png` - Meliá Hotels International
2. `nh-hotels.png` - NH Hoteles
3. `marriot-hotels.png` - Marriott
4. `intercontinental-hotels.png` - InterContinental Hotels & Resorts

**Nota:** El usuario indicó que compartirá 24 logos en total. El componente estará preparado para agregar más logos fácilmente.

Ubicación de assets: `public/logos/` (para acceso directo sin importaciones)

---

## CSS Animation (Infinite Scroll)

```css
@keyframes scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

.logo-track {
  animation: scroll 30s linear infinite;
}

.logo-track:hover {
  animation-play-state: paused;
}
```

---

## Archivos a Crear/Modificar

### Crear:
1. `src/components/TrustedByLogos.tsx` - Nuevo componente
2. `public/logos/melia-hotels.png` - Copiar logo
3. `public/logos/nh-hotels.png` - Copiar logo
4. `public/logos/marriot-hotels.png` - Copiar logo
5. `public/logos/intercontinental-hotels.png` - Copiar logo

### Modificar:
1. `src/pages/Index.tsx` - Agregar componente entre Hero y ScreenshotSection
2. `src/index.css` - Agregar animación keyframes
3. `src/i18n/locales/es.json` - Agregar traducciones
4. `src/i18n/locales/en.json` - Agregar traducciones
5. `src/i18n/locales/fr.json` - Agregar traducciones
6. `src/i18n/locales/de.json` - Agregar traducciones
7. `src/i18n/locales/it.json` - Agregar traducciones
8. `src/i18n/locales/pt.json` - Agregar traducciones
9. `src/i18n/locales/nl.json` - Agregar traducciones

---

## Código del Componente

```tsx
// src/components/TrustedByLogos.tsx
export default function TrustedByLogos() {
  const { t } = useLanguage();
  
  const logos = [
    { src: '/logos/melia-hotels.png', alt: 'Meliá Hotels' },
    { src: '/logos/nh-hotels.png', alt: 'NH Hotels' },
    { src: '/logos/marriot-hotels.png', alt: 'Marriott' },
    { src: '/logos/intercontinental-hotels.png', alt: 'InterContinental' },
    // ... más logos cuando se agreguen
  ];

  return (
    <section className="py-12 bg-muted/30 overflow-hidden">
      <div className="container">
        <h2 className="text-center text-lg md:text-xl font-semibold text-muted-foreground mb-8 uppercase tracking-wide">
          {t('trusted_by.title')}
        </h2>
      </div>
      
      <div className="relative">
        <div className="logo-track flex items-center gap-12">
          {/* Logos duplicados para loop infinito */}
          {[...logos, ...logos].map((logo, i) => (
            <img 
              key={i}
              src={logo.src} 
              alt={logo.alt}
              className="h-12 md:h-16 lg:h-20 w-auto opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0"
            />
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Orden en Index.tsx

```tsx
<main>
  <ModernHero />
  <TrustedByLogos />       {/* ← NUEVO COMPONENTE AQUÍ */}
  <ScreenshotSection />
  <SocialProofStrip />
  ...
</main>
```

---

## Resultado Visual Esperado

El componente mostrará:
- H2 centrado con texto en mayúsculas y color sutil
- Fila de logos en movimiento continuo de derecha a izquierda
- Logos en escala de grises que se colorean al hover
- Animación que pausa cuando el usuario pasa el cursor
- Espacio preparado para recibir los 24 logos totales

---

## Notas Importantes

- Los logos se guardan en `public/logos/` para acceso directo via URL
- El array de logos es fácil de expandir cuando lleguen los 20 logos restantes
- La animación CSS es ligera y no requiere JavaScript adicional
- El efecto grayscale da uniformidad visual a logos de diferentes colores

