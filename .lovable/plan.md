

# Plan: Traducir el Tooltip del Widget de WhatsApp

## Problema

El texto "Contacta con nosotros en WhatsApp" y el `aria-label` del boton flotante de WhatsApp estan escritos directamente en espanol (hardcoded). No cambian cuando el usuario selecciona otro idioma.

## Cambios

### 1. Agregar clave de traduccion en los 7 archivos de idiomas

Agregar la clave `whatsapp.tooltip` en cada archivo de locale:

- **es.json**: "Contacta con nosotros en WhatsApp"
- **en.json**: "Contact us on WhatsApp"
- **fr.json**: "Contactez-nous sur WhatsApp"
- **de.json**: "Kontaktieren Sie uns auf WhatsApp"
- **it.json**: "Contattaci su WhatsApp"
- **pt.json**: "Contacte-nos no WhatsApp"
- **nl.json**: "Neem contact met ons op via WhatsApp"

### 2. Actualizar `WhatsAppFloatingButton.tsx`

- Importar `useTranslation` de `react-i18next`
- Llamar a `const { t } = useTranslation()` dentro del componente
- Reemplazar el texto hardcoded del tooltip y el `aria-label` por `t('whatsapp.tooltip')`

Resultado: el tooltip mostrara el texto en el idioma activo del usuario.
