import { Camera, FileDown, Sparkles } from 'lucide-react';
import { Card, CardContent } from '@/components/ui/card';

type Variant = 'apps' | 'gallery';

interface ImageDisclaimerNoteProps {
  variant?: Variant;
}

export default function ImageDisclaimerNote({ variant = 'apps' }: ImageDisclaimerNoteProps) {
  return (
    <div className="container mx-auto px-4 -mt-6 mb-12">
      <Card className="max-w-4xl mx-auto border-dashed bg-muted/30">
        <CardContent className="py-6 px-6 md:px-8">
          <div className="flex items-start gap-3 mb-4">
            <Sparkles className="h-5 w-5 text-primary flex-shrink-0 mt-0.5" />
            <div>
              <h3 className="font-semibold text-foreground text-base mb-1">
                {variant === 'gallery'
                  ? 'Sobre estas imágenes: son ilustrativas, no fotos finales del escandallo'
                  : 'Cómo funciona la imagen en cada app: es una referencia visual, no la foto final'}
              </h3>
              <p className="text-sm text-muted-foreground leading-relaxed">
                Cuando una app genera una imagen, sirve para <strong className="text-foreground">ilustrar la idea</strong> del plato, bebida, postre o
                pre-elaboración: te ayuda a contrastar volumen, textura, emplatado, vajilla y la matemática visual del concepto. La{' '}
                <strong className="text-foreground">foto definitiva del escandallo o ficha técnica</strong> es la que tú haces de tu plato real, ya
                emplatado en tu cocina.
              </p>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pl-8">
            <div className="flex items-start gap-2">
              <Camera className="h-4 w-4 text-primary flex-shrink-0 mt-0.5" />
              <p className="text-xs text-muted-foreground leading-snug">
                <strong className="text-foreground">Todas las apps de recetas y contenido creativo</strong> ofrecen al final del flujo generar una
                imagen con Nano Banana 2 (la app dedicada a imágenes parte de cero con sus propios pasos). Puedes generar la primera y luego
                tantas variantes como quieras, incluidas pre-elaboraciones, no solo el plato final.
              </p>
            </div>
            <div className="flex items-start gap-2">
              <FileDown className="h-4 w-4 text-primary flex-shrink-0 mt-0.5" />
              <p className="text-xs text-muted-foreground leading-snug">
                Después de generar una receta, escandallo o cualquier contenido, puedes <strong className="text-foreground">descargar el resultado en CSV,
                PDF o Word</strong> e incorporar tu foto real cuando ejecutes el plato en cocina.
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
