# -*- coding: utf-8 -*-
"""Migración usos→créditos — fase 2 (residuales tras la pasada principal).

Cubre: ConsultoriaGastroProHub.tsx (UI 7 idiomas con variantes propias),
PSeoCityPage.tsx (CTA hardcoded), SEOHead.tsx (2ª description JSON-LD),
it.json (2 subtítulos "all'uso illimitato").
"""
import sys

BASE = '/Users/johnguerrero/chefpro-modernize/'

JOBS = [
    ('src/components/SEOHead.tsx', [
        ('Uso ilimitado mensual para profesionales exigentes.',
         'Créditos ilimitados mensuales para profesionales exigentes.'),
    ]),
    ('src/i18n/locales/it.json', [
        ("all'uso illimitato", 'ai crediti illimitati'),
    ]),
    ('src/pages/PSeoCityPage.tsx', [
        ('5 usos gratis al mes · Sin tarjeta', '10.000 créditos gratis al mes · Sin tarjeta'),
    ]),
    ('src/pages/ConsultoriaGastroProHub.tsx', [
        # ES
        ('5 usos gratis al mes · Sin tarjeta', '10.000 créditos gratis al mes · Sin tarjeta'),
        # EN
        ('5 free uses per month · No credit card', '10,000 free credits per month · No credit card'),
        ('5 uses per month', '10,000 credits per month'),
        # FR
        ('5 usages gratuits/mois · Sans carte bancaire', '10 000 crédits gratuits/mois · Sans carte bancaire'),
        ('5 usages par mois', '10 000 crédits par mois'),
        ('5 utilisations par mois', '10 000 crédits par mois'),
        # DE
        ('5 kostenlose Anwendungen/Monat · Keine Kreditkarte', '10.000 kostenlose Credits/Monat · Keine Kreditkarte'),
        ('5 Nutzungen pro Monat', '10.000 Credits pro Monat'),
        # IT
        ('5 utilizzi gratis/mese · Senza carta', '10.000 crediti gratis/mese · Senza carta'),
        ('5 utilizzi al mese', '10.000 crediti al mese'),
        # PT
        ('5 usos grátis/mês · Sem cartão', '10.000 créditos grátis/mês · Sem cartão'),
        ('5 usos por mês', '10.000 créditos por mês'),
        ('5 utilizações por mês', '10.000 créditos por mês'),
        # NL (la forma "5 gratis gebruiken per maand" antes que "5 gebruiken per maand" no se solapa)
        ('5 gratis gebruiken/maand · Geen creditcard', '10.000 gratis credits/maand · Geen creditcard'),
        ('5 gratis gebruiken per maand', '10.000 gratis credits per maand'),
        ('5 gebruiken per maand', '10.000 credits per maand'),
    ]),
]


def main():
    total, zeros = 0, []
    for relpath, pairs in JOBS:
        path = BASE + relpath
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        hits = 0
        for old, new in pairs:
            n = text.count(old)
            if n == 0:
                zeros.append('%s :: %r' % (relpath, old))
            text = text.replace(old, new)
            hits += n
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        total += hits
        print('%-50s %3d reemplazos' % (relpath, hits))
    print('\nTOTAL fase 2: %d' % total)
    if zeros:
        print('\n⚠️  SIN COINCIDENCIA (%d):' % len(zeros))
        for z in zeros:
            print('   -', z)
        sys.exit(1)


if __name__ == '__main__':
    main()
