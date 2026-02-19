

# Fix: Header Sticky No Funciona

## Problema

El contenedor padre en `Index.tsx` tiene la clase `overflow-x-hidden`:

```
<div className="min-h-screen bg-background overflow-x-hidden">
```

En los navegadores, `position: sticky` deja de funcionar cuando cualquier elemento ancestro tiene `overflow` distinto de `visible`. Esto anula por completo el comportamiento sticky del header.

## Solucion

Cambiar la estrategia para evitar el desbordamiento horizontal sin romper el sticky:

**Archivo: `src/pages/Index.tsx` (linea 29)**

Reemplazar `overflow-x-hidden` en el div principal por `overflow-x-clip`. La propiedad `overflow-x: clip` recorta el contenido desbordante igual que `hidden`, pero **no crea un contexto de scroll**, por lo que no interfiere con `position: sticky`.

```
// Antes
<div className="min-h-screen bg-background overflow-x-hidden">

// Despues  
<div className="min-h-screen bg-background overflow-x-clip">
```

Es un cambio de una sola clase en una sola linea. No se requieren cambios en ningun otro archivo.

