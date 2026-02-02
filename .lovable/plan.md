

# Plan: Corregir Etiqueta "USOS" Hardcodeada

## Problema Identificado

La palabra **"USOS:"** está hardcodeada en español en el componente `ModernPricing.tsx` (línea 193):

```tsx
<span className="font-semibold uppercase tracking-wide">USOS: </span>
```

Esto hace que aparezca "USOS:" en todos los idiomas en lugar de traducirse correctamente.

---

## Solución

### 1. Agregar clave de traducción en los 7 idiomas

Añadir `pricing.uses_label` en cada archivo de idioma:

| Idioma | Archivo | Traducción |
|--------|---------|------------|
| Español | `es.json` | "USOS" |
| English | `en.json` | "USES" |
| Français | `fr.json` | "UTILISATIONS" |
| Deutsch | `de.json` | "NUTZUNGEN" |
| Italiano | `it.json` | "UTILIZZI" |
| Português | `pt.json` | "USOS" |
| Nederlands | `nl.json` | "GEBRUIK" |

### 2. Actualizar el componente

**Archivo:** `src/components/ModernPricing.tsx`

Cambiar de:
```tsx
<span className="font-semibold uppercase tracking-wide">USOS: </span>
```

A:
```tsx
<span className="font-semibold uppercase tracking-wide">{t('pricing.uses_label')}: </span>
```

---

## Archivos a Modificar

1. `src/components/ModernPricing.tsx` - Usar traducción en lugar de texto hardcodeado
2. `src/i18n/locales/es.json` - Añadir `"uses_label": "USOS"`
3. `src/i18n/locales/en.json` - Añadir `"uses_label": "USES"`
4. `src/i18n/locales/fr.json` - Añadir `"uses_label": "UTILISATIONS"`
5. `src/i18n/locales/de.json` - Añadir `"uses_label": "NUTZUNGEN"`
6. `src/i18n/locales/it.json` - Añadir `"uses_label": "UTILIZZI"`
7. `src/i18n/locales/pt.json` - Añadir `"uses_label": "USOS"`
8. `src/i18n/locales/nl.json` - Añadir `"uses_label": "GEBRUIK"`

---

## Resultado Esperado

- En español: "USOS: 150/mes"
- En inglés: "USES: 150/month"
- En francés: "UTILISATIONS: 150/mois"
- En alemán: "NUTZUNGEN: 150/Monat"
- En italiano: "UTILIZZI: 150/mese"
- En portugués: "USOS: 150/mês"
- En neerlandés: "GEBRUIK: 150/maand"

