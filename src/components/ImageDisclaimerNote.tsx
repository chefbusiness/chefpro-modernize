import { Camera, FileDown, Sparkles } from 'lucide-react';
import { Card, CardContent } from '@/components/ui/card';

type Variant = 'apps' | 'gallery';
type Lang = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

interface ImageDisclaimerNoteProps {
  variant?: Variant;
  lang?: Lang;
}

const COPY: Record<Lang, {
  galleryTitle: string;
  appsTitle: string;
  bodyPrefix: string;
  bodyIllustrate: string;
  bodyMiddle: string;
  bodyDefinitive: string;
  bodySuffix: string;
  point1Bold: string;
  point1Rest: string;
  point2Prefix: string;
  point2Bold: string;
  point2Suffix: string;
}> = {
  es: {
    galleryTitle: 'Sobre estas imágenes: son ilustrativas, no fotos finales del escandallo',
    appsTitle: 'Cómo funciona la imagen en cada app: es una referencia visual, no la foto final',
    bodyPrefix: 'Cuando una app genera una imagen, sirve para ',
    bodyIllustrate: 'ilustrar la idea',
    bodyMiddle: ' del plato, bebida, postre o pre-elaboración: te ayuda a contrastar volumen, textura, emplatado, vajilla y la matemática visual del concepto. La ',
    bodyDefinitive: 'foto definitiva del escandallo o ficha técnica',
    bodySuffix: ' es la que tú haces de tu plato real, ya emplatado en tu cocina.',
    point1Bold: 'Todas las apps de recetas y contenido creativo',
    point1Rest: ' ofrecen al final del flujo generar una imagen con Nano Banana 2 (la app dedicada a imágenes parte de cero con sus propios pasos). Puedes generar la primera y luego tantas variantes como quieras, incluidas pre-elaboraciones, no solo el plato final.',
    point2Prefix: 'Después de generar una receta, escandallo o cualquier contenido, puedes ',
    point2Bold: 'descargar el resultado en CSV, PDF o Word',
    point2Suffix: ' e incorporar tu foto real cuando ejecutes el plato en cocina.',
  },
  en: {
    galleryTitle: 'About these images: they are visual references, not the final hero photos',
    appsTitle: 'How images work in each app: a visual reference, not the final photo',
    bodyPrefix: 'When an app generates an image, it serves to ',
    bodyIllustrate: 'illustrate the idea',
    bodyMiddle: ' of the dish, drink, dessert or sub-prep: it helps you sense check volume, texture, plating, tableware and the visual math of the concept. The ',
    bodyDefinitive: 'definitive photo of the recipe cost card or tech sheet',
    bodySuffix: ' is the one you take of your real dish, plated in your own kitchen.',
    point1Bold: 'Every recipe and creative-content app',
    point1Rest: ' offers an option at the end of the workflow to generate an image with Nano Banana 2 (the dedicated image app starts from scratch with its own steps). You can generate the first one and then as many variants as you need, including sub-preps — not just the final plate.',
    point2Prefix: 'After generating a recipe, cost card or any content, you can ',
    point2Bold: 'download the output as CSV, PDF or Word',
    point2Suffix: ' and add your real photo when you cook the dish in service.',
  },
  // Other languages fall back to Spanish content for now (matches use-case content fallback policy)
  fr: {} as never,
  de: {} as never,
  it: {} as never,
  pt: {} as never,
  nl: {} as never,
};

export default function ImageDisclaimerNote({ variant = 'apps', lang = 'es' }: ImageDisclaimerNoteProps) {
  const t = COPY[lang] && Object.keys(COPY[lang]).length > 0 ? COPY[lang] : COPY.es;
  return (
    <div className="container mx-auto px-4 mt-10">
      <Card className="max-w-4xl mx-auto border-dashed bg-card">
        <CardContent className="py-6 px-6 md:px-8">
          <div className="flex items-start gap-3 mb-4">
            <Sparkles className="h-5 w-5 text-primary flex-shrink-0 mt-0.5" />
            <div>
              <h3 className="font-semibold text-foreground text-base mb-1">
                {variant === 'gallery' ? t.galleryTitle : t.appsTitle}
              </h3>
              <p className="text-sm text-muted-foreground leading-relaxed">
                {t.bodyPrefix}
                <strong className="text-foreground">{t.bodyIllustrate}</strong>
                {t.bodyMiddle}
                <strong className="text-foreground">{t.bodyDefinitive}</strong>
                {t.bodySuffix}
              </p>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pl-8">
            <div className="flex items-start gap-2">
              <Camera className="h-4 w-4 text-primary flex-shrink-0 mt-0.5" />
              <p className="text-xs text-muted-foreground leading-snug">
                <strong className="text-foreground">{t.point1Bold}</strong>
                {t.point1Rest}
              </p>
            </div>
            <div className="flex items-start gap-2">
              <FileDown className="h-4 w-4 text-primary flex-shrink-0 mt-0.5" />
              <p className="text-xs text-muted-foreground leading-snug">
                {t.point2Prefix}
                <strong className="text-foreground">{t.point2Bold}</strong>
                {t.point2Suffix}
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
