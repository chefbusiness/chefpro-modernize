

# Plan: Agregar WhatsApp Flotante en la Pagina de Inicio

## Cambio

Importar y renderizar el componente `WhatsAppFloatingButton` en `src/pages/Index.tsx`, igual que ya se hace en las paginas de Mentoria Online y Formacion Presencial.

## Archivo a modificar

**`src/pages/Index.tsx`**

1. Agregar import: `import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';`
2. Renderizar `<WhatsAppFloatingButton />` dentro del componente, justo antes del cierre del `</div>` principal (despues de `<ModernFooter />`).

No se requieren cambios en ningun otro archivo. El componente ya soporta todos los idiomas y es completamente funcional.

