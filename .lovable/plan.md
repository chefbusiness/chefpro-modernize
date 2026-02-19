

# Plan: Banner de Anuncio en la Parte Superior del Header

## Descripcion

Agregar una cinta/banner de anuncio moderno (announcement bar) por encima del header principal, al estilo de Vercel/Framer, que promocione el articulo "30 hacks con IA para mejorar la eficiencia en tu cocina". El banner enlazara a `https://blog.aichef.pro/30-hacks-con-inteligencia-artificial-de-ai-chef-pro-para-mejorar-la-eficiencia-en-tu-cocina/` y sera visible en todos los idiomas.

## Diseno Visual

- Fondo oscuro (negro/gris muy oscuro) con texto claro y un toque dorado (acorde a la marca)
- Icono de rayo o chispa para llamar la atencion
- Texto breve + enlace "Leer mas" con flecha
- Boton de cerrar (X) para que el usuario pueda ocultarlo
- Altura compacta (~36px)
- Responsive: texto abreviado en movil

## Cambios

### 1. Crear componente `src/components/AnnouncementBar.tsx`

Componente nuevo con:
- Estado local para mostrar/ocultar (con localStorage para recordar si el usuario lo cerro)
- Enlace externo al articulo del blog
- Texto traducido via i18next
- Icono Zap o Sparkles de lucide-react
- Boton X para cerrar

### 2. Modificar `src/components/ModernHeader.tsx`

Importar y renderizar `AnnouncementBar` justo encima del `<header>` actual, envolviendo ambos en un fragmento.

### 3. Agregar traducciones en los 7 archivos de idioma

Agregar clave `announcement_bar` en cada locale:

| Idioma | Texto |
|--------|-------|
| ES | "30 hacks con IA para mejorar la eficiencia en tu cocina" |
| EN | "30 AI hacks to boost efficiency in your kitchen" |
| FR | "30 astuces IA pour ameliorer l'efficacite en cuisine" |
| DE | "30 KI-Hacks fur mehr Effizienz in deiner Kuche" |
| IT | "30 hack IA per migliorare l'efficienza in cucina" |
| PT | "30 hacks de IA para melhorar a eficiencia na cozinha" |
| NL | "30 AI-hacks om de efficientie in je keuken te verbeteren" |

Cada idioma tambien tendra una clave `"cta"` con "Leer mas" / "Read more" / etc.

### 4. Archivos a crear/modificar

| Archivo | Accion |
|---------|--------|
| `src/components/AnnouncementBar.tsx` | Crear nuevo |
| `src/components/ModernHeader.tsx` | Importar y renderizar AnnouncementBar encima del header |
| `src/i18n/locales/es.json` | Agregar `announcement_bar` |
| `src/i18n/locales/en.json` | Agregar `announcement_bar` |
| `src/i18n/locales/fr.json` | Agregar `announcement_bar` |
| `src/i18n/locales/de.json` | Agregar `announcement_bar` |
| `src/i18n/locales/it.json` | Agregar `announcement_bar` |
| `src/i18n/locales/pt.json` | Agregar `announcement_bar` |
| `src/i18n/locales/nl.json` | Agregar `announcement_bar` |

### Seccion Tecnica

```typescript
// AnnouncementBar.tsx - estructura basica
const AnnouncementBar = () => {
  const [visible, setVisible] = useState(() => {
    return localStorage.getItem('announcement-dismissed') !== 'true';
  });

  const dismiss = () => {
    setVisible(false);
    localStorage.setItem('announcement-dismissed', 'true');
  };

  if (!visible) return null;

  return (
    <div className="bg-primary text-primary-foreground text-center text-sm py-2 px-4 relative">
      <a href="https://blog.aichef.pro/30-hacks-con-inteligencia-artificial-de-ai-chef-pro-para-mejorar-la-eficiencia-en-tu-cocina/"
         target="_blank" rel="noopener noreferrer"
         className="inline-flex items-center gap-2 hover:underline">
        <Sparkles className="h-4 w-4" />
        {t('announcement_bar.text')}
        <span className="font-semibold">{t('announcement_bar.cta')} →</span>
      </a>
      <button onClick={dismiss} className="absolute right-2 top-1/2 -translate-y-1/2">
        <X className="h-4 w-4" />
      </button>
    </div>
  );
};
```

El header sticky actual ajustara su `top` automaticamente ya que el banner estara fuera del sticky container.

