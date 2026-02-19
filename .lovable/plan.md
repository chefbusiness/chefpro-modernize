
# Plan: Header y Announcement Bar Flotantes al Hacer Scroll

## Problema

Actualmente el `AnnouncementBar` y el `<header>` son elementos hermanos dentro de un fragmento (`<>`). Solo el `<header>` tiene `sticky top-0`, por lo que el banner de anuncio desaparece al hacer scroll y el header se queda pegado solo.

## Solucion

Envolver ambos elementos (AnnouncementBar + header) en un unico contenedor `<div>` con `sticky top-0 z-50`, y quitar el sticky del `<header>` interno.

## Cambios

### Archivo: `src/components/ModernHeader.tsx`

1. Reemplazar el fragmento `<>...</>` por un `<div className="sticky top-0 z-50">`
2. Quitar las clases `sticky top-0 z-50` del `<header>` interno (dejar solo las de fondo, borde y backdrop-blur)

Resultado:

```
<div className="sticky top-0 z-50">        <!-- contenedor sticky -->
  <AnnouncementBar />                       <!-- se queda visible -->
  <header className="w-full border-b bg-background/95 backdrop-blur ...">
    ...                                     <!-- contenido del header -->
  </header>
</div>
```

Con este cambio, tanto el banner de anuncio como el header completo permanecen visibles ("flotando") al hacer scroll, en desktop y mobile. Cuando el usuario cierre el banner con la X, solo se mostrara el header.

No se requieren cambios en ningun otro archivo.
