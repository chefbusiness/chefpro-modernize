
# Plan: Rediseño Visual del Componente TrustedByLogos

## Objetivo

Transformar la sección "Trusted By" de un componente discreto a uno visualmente impactante que transmita confianza y prestigio.

## Cambios Principales

### 1. Fondo Oscuro Premium

Cambiar de `bg-muted/30` (gris claro sutil) a un fondo oscuro elegante que haga resaltar los logos y transmita profesionalismo.

```
Antes:  bg-muted/30
Ahora:  bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900
```

### 2. Header con Contador Visual

Agregar un badge contador dorado junto al título para destacar la cantidad de marcas:

```
[23+ marcas de elite]

LA ELECCION DE LOS PROFESIONALES DE HOSTELERIA DE CLASE MUNDIAL

───────────────────────
```

Incluye:
- Badge dorado con contador animado
- Título más grande y en color claro
- Línea decorativa dorada debajo

### 3. Logos Luminosos a Todo Color

Eliminar el efecto grayscale y añadir efectos de brillo:

```
Antes:  grayscale opacity-70
Ahora:  brightness-110 drop-shadow-glow
```

Los logos se mostrarán a color completo con un sutil efecto de brillo que los haga "pop" sobre el fondo oscuro.

### 4. Efecto Hover "Spotlight"

Al pasar el mouse sobre un logo:
- Aumenta de tamaño (scale-110)
- Brillo adicional
- Sombra dorada suave

### 5. Bordes Decorativos Dorados

Añadir líneas doradas sutiles arriba y abajo de la sección para enmarcarla como una zona premium.

## Archivos a Modificar

| Archivo | Cambios |
|---------|---------|
| `src/components/TrustedByLogos.tsx` | Rediseño completo del componente |
| `src/index.css` | Añadir nuevas clases de utilidad (glow effects) |
| `src/i18n/locales/es.json` | Añadir texto del badge "23+ marcas de elite" |
| `src/i18n/locales/en.json` | Añadir traducción inglés |
| `src/i18n/locales/fr.json` | Añadir traducción francés |
| `src/i18n/locales/de.json` | Añadir traducción alemán |
| `src/i18n/locales/it.json` | Añadir traducción italiano |
| `src/i18n/locales/pt.json` | Añadir traducción portugués |
| `src/i18n/locales/nl.json` | Añadir traducción holandés |

## Estructura Visual Final

```text
┌─────────────────────────────────────────────────────────────┐
│ ════════════════════ BORDE DORADO ═══════════════════════   │
│                                                             │
│              ╔═══════════════════════╗                      │
│              ║  23+ marcas de elite  ║  ← Badge dorado      │
│              ╚═══════════════════════╝                      │
│                                                             │
│   LA ELECCION DE LOS PROFESIONALES DE HOSTELERIA           │
│              DE CLASE MUNDIAL                               │
│                                                             │
│              ─────── ✦ ───────  ← Separador dorado          │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Logo1] [Logo2] [Logo3] [Logo4] [Logo5] [Logo6] ... │   │
│  │           ← Carrusel infinito a color →               │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│ ════════════════════ BORDE DORADO ═══════════════════════   │
└─────────────────────────────────────────────────────────────┘
          Fondo: Gradiente oscuro (slate-900 → slate-800)
```

## Detalles Técnicos

### Nuevas clases CSS en index.css

```css
/* Logo glow effect para fondo oscuro */
.logo-glow {
  filter: brightness(1.1) drop-shadow(0 0 8px rgba(255, 255, 255, 0.3));
}

.logo-glow:hover {
  filter: brightness(1.2) drop-shadow(0 0 15px rgba(251, 191, 36, 0.5));
  transform: scale(1.1);
}
```

### Nuevas traducciones

```json
"trusted_by": {
  "title": "La elección de los profesionales de hostelería de clase mundial",
  "badge": "23+ marcas de elite"
}
```

## Beneficios del Rediseño

1. **Contraste visual**: El fondo oscuro hace que los logos destaquen inmediatamente
2. **Social proof reforzado**: El badge "23+ marcas de elite" cuantifica la confianza
3. **Sensación premium**: Los efectos de brillo y bordes dorados elevan la percepción de calidad
4. **Coherencia con la marca**: Usa los colores dorados de AI Chef Pro
5. **Atención capturada**: Los logos a color llaman más la atención que los grises
