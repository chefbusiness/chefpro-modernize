

# Plan: Badge "Uso Ilimitado" + Features Adicionales para Premium Max

## Resumen

Hacer el plan Premium Max de 95€ mas atractivo visualmente con:
1. Un badge destacado "Uso Ilimitado" encima del plan
2. Dos bulletpoints adicionales (7 features vs 5 del Premium Plus)

---

## Cambios en el Componente

**Archivo:** `src/components/ModernPricing.tsx`

### 1. Agregar propiedad `unlimitedBadge` al plan premium_max

```tsx
{
  id: 'premium_max',
  // ... otras propiedades
  unlimitedBadge: t('pricing.unlimited_badge'),  // NUEVO
  features: [
    // ... 7 features en lugar de 5
  ],
  popular: false
}
```

### 2. Renderizar el badge "Uso Ilimitado"

Agregar logica condicional para mostrar el badge cuando `plan.unlimitedBadge` existe:

```tsx
{plan.unlimitedBadge && (
  <Badge 
    variant="default" 
    className="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-3 py-1 bg-purple-600 text-white border-purple-600"
  >
    ∞ {plan.unlimitedBadge}
  </Badge>
)}
```

### 3. Agregar 2 features mas al array de premium_max

Cambiar de 5 a 7 features (features.0 a features.6)

---

## Cambios en los 7 Archivos de Idiomas

### Estructura actualizada para `pricing.plans.premium_max`:

**Nuevas claves a agregar:**

1. `pricing.unlimited_badge` - Texto del badge
2. `pricing.plans.premium_max.features.5` - Feature adicional 1
3. `pricing.plans.premium_max.features.6` - Feature adicional 2

---

### Espanol (es.json)

```json
"unlimited_badge": "Uso Ilimitado",
"premium_max": {
  "features": {
    "0": "Todas las 55+ herramientas incluidas",
    "1": "Uso ilimitado mensual",
    "2": "Acceso a todas las cocinas del mundo",
    "3": "Herramientas avanzadas de negocio",
    "4": "Soporte premium 24/7",
    "5": "Acceso anticipado a nuevas funciones",    // NUEVO
    "6": "Formacion exclusiva sobre novedades"      // NUEVO
  }
}
```

### English (en.json)

```json
"unlimited_badge": "Unlimited Usage",
"premium_max": {
  "features": {
    ...
    "5": "Early access to new features",
    "6": "Exclusive training on new releases"
  }
}
```

### Francais (fr.json)

```json
"unlimited_badge": "Usage Illimite",
"premium_max": {
  "features": {
    ...
    "5": "Acces anticipe aux nouvelles fonctionnalites",
    "6": "Formation exclusive sur les nouveautes"
  }
}
```

### Deutsch (de.json)

```json
"unlimited_badge": "Unbegrenzte Nutzung",
"premium_max": {
  "features": {
    ...
    "5": "Fruher Zugang zu neuen Funktionen",
    "6": "Exklusive Schulung zu Neuheiten"
  }
}
```

### Italiano (it.json)

```json
"unlimited_badge": "Uso Illimitato",
"premium_max": {
  "features": {
    ...
    "5": "Accesso anticipato alle nuove funzionalita",
    "6": "Formazione esclusiva sulle novita"
  }
}
```

### Portugues (pt.json)

```json
"unlimited_badge": "Uso Ilimitado",
"premium_max": {
  "features": {
    ...
    "5": "Acesso antecipado a novas funcionalidades",
    "6": "Formacao exclusiva sobre novidades"
  }
}
```

### Nederlands (nl.json)

```json
"unlimited_badge": "Onbeperkt Gebruik",
"premium_max": {
  "features": {
    ...
    "5": "Vroege toegang tot nieuwe functies",
    "6": "Exclusieve training over nieuwe releases"
  }
}
```

---

## Archivos a Modificar

1. `src/components/ModernPricing.tsx` - Agregar badge y features adicionales
2. `src/i18n/locales/es.json` - Badge + 2 features nuevas
3. `src/i18n/locales/en.json` - Badge + 2 features nuevas
4. `src/i18n/locales/fr.json` - Badge + 2 features nuevas
5. `src/i18n/locales/de.json` - Badge + 2 features nuevas
6. `src/i18n/locales/it.json` - Badge + 2 features nuevas
7. `src/i18n/locales/pt.json` - Badge + 2 features nuevas
8. `src/i18n/locales/nl.json` - Badge + 2 features nuevas

---

## Resultado Visual Esperado

```text
                                                    +-----------------------+
                                                    |  ∞ USO ILIMITADO      | <- Badge morado
                                                    +-----------------------+
                                                    | AI Chef Premium Max   |
                                                    |        95€/mes        |
                                                    |      USOS: ∞          |
                                                    +-----------------------+
                                                    | ✓ 55+ herramientas    |
                                                    | ✓ Uso ilimitado       |
                                                    | ✓ Cocinas del mundo   |
                                                    | ✓ Herramientas negocio|
                                                    | ✓ Soporte 24/7        |
                                                    | ✓ Acceso anticipado   | <- NUEVO
                                                    | ✓ Formacion exclusiva | <- NUEVO
                                                    +-----------------------+
```

El plan Premium Max ahora sera visualmente mas atractivo que el Premium Plus (50€) al tener:
- Un badge distintivo "Uso Ilimitado" en morado
- 7 features en lugar de 5
- Justificacion clara del precio mas alto

