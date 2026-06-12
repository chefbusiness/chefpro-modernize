# -*- coding: utf-8 -*-
"""Migración usos→créditos 2026-06-12.

Conversión por plan (captura del user, app.aichef.pro):
  Miembro Gratis   : 20 usos/mes  -> 10.000 créditos/mes
  Premium Pro 25€  : 150 usos/mes -> 85.000 créditos/mes
  Premium Plus 50€ : 350 usos/mes -> 175.000 créditos/mes
  Premium Max 95€  : ilimitado    -> créditos ilimitados
  Plus Anual 950€  : ilimitado    -> créditos ilimitados
CTAs gratis "5 usos al mes" -> "10.000 créditos al mes".
Reemplazo por cadena exacta; reporta conteo por par y avisa si 0.
"""
import sys

BASE = '/Users/johnguerrero/chefpro-modernize/'

# (archivo, [(viejo, nuevo), ...])
JOBS = []

# ──────────────────────────── es.json ────────────────────────────
JOBS.append(('src/i18n/locales/es.json', [
    ('"uses_label": "USOS"', '"uses_label": "CRÉDITOS"'),
    ('"unlimited_badge": "Uso Ilimitado"', '"unlimited_badge": "Créditos Ilimitados"'),
    ('"uses": "20/mes"', '"uses": "10.000/mes"'),
    ('"uses": "150/mes"', '"uses": "85.000/mes"'),
    ('"uses": "350/mes"', '"uses": "175.000/mes"'),
    ('"20 usos mensuales"', '"10.000 créditos mensuales"'),
    ('"150 usos mensuales"', '"85.000 créditos mensuales"'),
    ('"350 usos mensuales"', '"175.000 créditos mensuales"'),
    ('"Uso ilimitado mensual para profesionales exigentes"', '"Créditos ilimitados mensuales para profesionales exigentes"'),
    ('"Uso ilimitado mensual"', '"Créditos ilimitados mensuales"'),
    ('"Uso ilimitado durante todo el año"', '"Créditos ilimitados durante todo el año"'),
    ('20 usos/mes', '10.000 créditos/mes'),
    ('150 usos/mes', '85.000 créditos/mes'),
    ('350 usos/mes', '175.000 créditos/mes'),
    ('20 menús/mes', '10.000 créditos/mes'),
    ('150 menús/mes', '85.000 créditos/mes'),
    ('350 menús/mes', '175.000 créditos/mes'),
    ('Incluye 20 usos al mes', 'Incluye 10.000 créditos al mes'),
    ('con 20 usos al mes', 'con 10.000 créditos al mes'),
    (', 150 usos)', ', 85.000 créditos)'),
    ('para uso ilimitado', 'para créditos ilimitados'),
    ('hasta el uso ilimitado', 'hasta los créditos ilimitados'),
    ('hasta uso ilimitado', 'hasta créditos ilimitados'),
]))

# ──────────────────────────── en.json ────────────────────────────
JOBS.append(('src/i18n/locales/en.json', [
    ('"uses_label": "USES"', '"uses_label": "CREDITS"'),
    ('"unlimited_badge": "Unlimited Usage"', '"unlimited_badge": "Unlimited Credits"'),
    ('"uses": "20/month"', '"uses": "10,000/month"'),
    ('"uses": "150/month"', '"uses": "85,000/month"'),
    ('"uses": "350/month"', '"uses": "175,000/month"'),
    ('"20 monthly uses"', '"10,000 monthly credits"'),
    ('"150 monthly uses"', '"85,000 monthly credits"'),
    ('"350 monthly uses"', '"175,000 monthly credits"'),
    ('"Unlimited monthly use for demanding professionals"', '"Unlimited monthly credits for demanding professionals"'),
    ('"Unlimited monthly use"', '"Unlimited monthly credits"'),
    ('"Unlimited use throughout the year"', '"Unlimited credits throughout the year"'),
    ('20 uses/month', '10,000 credits/month'),
    ('150 uses/month', '85,000 credits/month'),
    ('350 uses/month', '175,000 credits/month'),
    ('20 menus/mo', '10,000 credits/mo'),
    ('150 menus/mo', '85,000 credits/mo'),
    ('350 menus/mo', '175,000 credits/mo'),
    ('It includes 20 uses per month', 'It includes 10,000 credits per month'),
    ('with 20 uses per month', 'with 10,000 credits per month'),
    (', 150 uses)', ', 85,000 credits)'),
    ('for unlimited use', 'for unlimited credits'),
    ('to unlimited use', 'to unlimited credits'),
]))

# ──────────────────────────── fr.json ────────────────────────────
JOBS.append(('src/i18n/locales/fr.json', [
    ('"uses_label": "UTILISATIONS"', '"uses_label": "CRÉDITS"'),
    ('"unlimited_badge": "Usage Illimité"', '"unlimited_badge": "Crédits Illimités"'),
    ('"uses": "20/mois"', '"uses": "10 000/mois"'),
    ('"uses": "150/mois"', '"uses": "85 000/mois"'),
    ('"uses": "350/mois"', '"uses": "175 000/mois"'),
    ('"20 utilisations mensuelles"', '"10 000 crédits mensuels"'),
    ('"150 utilisations mensuelles"', '"85 000 crédits mensuels"'),
    ('"350 utilisations mensuelles"', '"175 000 crédits mensuels"'),
    ('"Usage illimité mensuel pour les professionnels exigeants"', '"Crédits mensuels illimités pour les professionnels exigeants"'),
    ('"Usage illimité mensuel"', '"Crédits mensuels illimités"'),
    ("\"Usage illimité toute l'année\"", "\"Crédits illimités toute l'année\""),
    ('20 utilisations/mois', '10 000 crédits/mois'),
    ('150 utilisations/mois', '85 000 crédits/mois'),
    ('350 utilisations/mois', '175 000 crédits/mois'),
    ('20 menus/mois', '10 000 crédits/mois'),
    ('150 menus/mois', '85 000 crédits/mois'),
    ('350 menus/mois', '175 000 crédits/mois'),
    ('Il comprend 20 utilisations par mois', 'Il comprend 10 000 crédits par mois'),
    ('avec 20 utilisations par mois', 'avec 10 000 crédits par mois'),
    (', 150 utilisations)', ', 85 000 crédits)'),
    ('pour un usage illimité', 'pour des crédits illimités'),
    ("à l'usage illimité", 'aux crédits illimités'),
    ("à l'utilisation illimitée", 'aux crédits illimités'),
]))

# ──────────────────────────── de.json ────────────────────────────
JOBS.append(('src/i18n/locales/de.json', [
    ('"uses_label": "NUTZUNGEN"', '"uses_label": "CREDITS"'),
    ('"unlimited_badge": "Unbegrenzte Nutzung"', '"unlimited_badge": "Unbegrenzte Credits"'),
    ('"uses": "20/Monat"', '"uses": "10.000/Monat"'),
    ('"uses": "150/Monat"', '"uses": "85.000/Monat"'),
    ('"uses": "350/Monat"', '"uses": "175.000/Monat"'),
    ('"20 monatliche Nutzungen"', '"10.000 monatliche Credits"'),
    ('"150 monatliche Nutzungen"', '"85.000 monatliche Credits"'),
    ('"350 monatliche Nutzungen"', '"175.000 monatliche Credits"'),
    ('"Unbegrenzte monatliche Nutzung für anspruchsvolle Profis"', '"Unbegrenzte monatliche Credits für anspruchsvolle Profis"'),
    ('"Unbegrenzte monatliche Nutzung"', '"Unbegrenzte monatliche Credits"'),
    ('"Unbegrenzte Nutzung das ganze Jahr"', '"Unbegrenzte Credits das ganze Jahr"'),
    ('20 Nutzungen/Monat', '10.000 Credits/Monat'),
    ('150 Nutzungen/Monat', '85.000 Credits/Monat'),
    ('350 Nutzungen/Monat', '175.000 Credits/Monat'),
    ('10 Menüs/Monat', '10.000 Credits/Monat'),
    ('150 Menüs/Monat', '85.000 Credits/Monat'),
    ('350 Menüs/Monat', '175.000 Credits/Monat'),
    ('Er umfasst 20 Nutzungen pro Monat', 'Er umfasst 10.000 Credits pro Monat'),
    ('mit 20 Nutzungen pro Monat', 'mit 10.000 Credits pro Monat'),
    (', 150 Nutzungen)', ', 85.000 Credits)'),
    ('für unbegrenzte Nutzung', 'für unbegrenzte Credits'),
]))

# ──────────────────────────── it.json ────────────────────────────
JOBS.append(('src/i18n/locales/it.json', [
    ('"uses_label": "UTILIZZI"', '"uses_label": "CREDITI"'),
    ('"unlimited_badge": "Uso Illimitato"', '"unlimited_badge": "Crediti Illimitati"'),
    ('"uses": "20/mese"', '"uses": "10.000/mese"'),
    ('"uses": "150/mese"', '"uses": "85.000/mese"'),
    ('"uses": "350/mese"', '"uses": "175.000/mese"'),
    ('"20 utilizzi mensili"', '"10.000 crediti mensili"'),
    ('"150 utilizzi mensili"', '"85.000 crediti mensili"'),
    ('"350 utilizzi mensili"', '"175.000 crediti mensili"'),
    ('"Uso illimitato mensile per professionisti esigenti"', '"Crediti illimitati mensili per professionisti esigenti"'),
    ('"Uso illimitato mensile"', '"Crediti illimitati mensili"'),
    ("\"Uso illimitato per tutto l'anno\"", "\"Crediti illimitati per tutto l'anno\""),
    ('20 utilizzi/mese', '10.000 crediti/mese'),
    ('150 utilizzi/mese', '85.000 crediti/mese'),
    ('350 utilizzi/mese', '175.000 crediti/mese'),
    ('"10 menu/mese"', '"10.000 crediti/mese"'),
    ('"150 menu/mese"', '"85.000 crediti/mese"'),
    ('"350 menu/mese"', '"175.000 crediti/mese"'),
    ('Include 20 utilizzi al mese', 'Include 10.000 crediti al mese'),
    ('con 20 utilizzi al mese', 'con 10.000 crediti al mese'),
    (', 150 utilizzi)', ', 85.000 crediti)'),
    ('per uso illimitato', 'per crediti illimitati'),
    ("all'utilizzo illimitato", 'ai crediti illimitati'),
]))

# ──────────────────────────── pt.json ────────────────────────────
JOBS.append(('src/i18n/locales/pt.json', [
    ('"uses_label": "USOS"', '"uses_label": "CRÉDITOS"'),
    ('"unlimited_badge": "Uso Ilimitado"', '"unlimited_badge": "Créditos Ilimitados"'),
    ('"uses": "20/mês"', '"uses": "10.000/mês"'),
    ('"uses": "150/mês"', '"uses": "85.000/mês"'),
    ('"uses": "350/mês"', '"uses": "175.000/mês"'),
    ('"20 usos mensais"', '"10.000 créditos mensais"'),
    ('"150 usos mensais"', '"85.000 créditos mensais"'),
    ('"350 usos mensais"', '"175.000 créditos mensais"'),
    ('"Uso ilimitado mensal para profissionais exigentes"', '"Créditos ilimitados mensais para profissionais exigentes"'),
    ('"Uso ilimitado mensal"', '"Créditos ilimitados mensais"'),
    ('"Uso ilimitado durante todo o ano"', '"Créditos ilimitados durante todo o ano"'),
    ('20 utilizações/mês', '10.000 créditos/mês'),
    ('150 utilizações/mês', '85.000 créditos/mês'),
    ('350 utilizações/mês', '175.000 créditos/mês'),
    ('20 menus/mês', '10.000 créditos/mês'),
    ('150 menus/mês', '85.000 créditos/mês'),
    ('350 menus/mês', '175.000 créditos/mês'),
    ('20 usos por mês', '10.000 créditos por mês'),
    (', 150 usos)', ', 85.000 créditos)'),
    ('para uso ilimitado', 'para créditos ilimitados'),
    ('ao uso ilimitado', 'aos créditos ilimitados'),
    ('até o uso ilimitado', 'até os créditos ilimitados'),
]))

# ──────────────────────────── nl.json ────────────────────────────
JOBS.append(('src/i18n/locales/nl.json', [
    ('"uses_label": "GEBRUIK"', '"uses_label": "CREDITS"'),
    ('"unlimited_badge": "Onbeperkt Gebruik"', '"unlimited_badge": "Onbeperkte Credits"'),
    ('"uses": "20/maand"', '"uses": "10.000/maand"'),
    ('"uses": "150/maand"', '"uses": "85.000/maand"'),
    ('"uses": "350/maand"', '"uses": "175.000/maand"'),
    ('"20 maandelijkse gebruiken"', '"10.000 maandelijkse credits"'),
    ('"150 maandelijkse gebruiken"', '"85.000 maandelijkse credits"'),
    ('"350 maandelijkse gebruiken"', '"175.000 maandelijkse credits"'),
    ('"Onbeperkt maandelijks gebruik voor veeleisende professionals"', '"Onbeperkte maandelijkse credits voor veeleisende professionals"'),
    ('"Onbeperkt maandelijks gebruik"', '"Onbeperkte maandelijkse credits"'),
    ('"Onbeperkt gebruik het hele jaar"', '"Onbeperkte credits het hele jaar"'),
    ('20 gebruiken/maand', '10.000 credits/maand'),
    ('150 gebruiken/maand', '85.000 credits/maand'),
    ('350 gebruiken/maand', '175.000 credits/maand'),
    ('20 gebruik/maand', '10.000 credits/maand'),
    ('150 gebruik/maand', '85.000 credits/maand'),
    ('350 gebruik/maand', '175.000 credits/maand'),
    ("20 menu's/maand", '10.000 credits/maand'),
    ("150 menu's/maand", '85.000 credits/maand'),
    ("350 menu's/maand", '175.000 credits/maand'),
    ('Het omvat 20 gebruiken per maand', 'Het omvat 10.000 credits per maand'),
    ('met 20 gebruiken per maand', 'met 10.000 credits per maand'),
    (', 150 gebruiken)', ', 85.000 credits)'),
    ('voor onbeperkt gebruik', 'voor onbeperkte credits'),
    ('tot onbeperkt gebruik', 'tot onbeperkte credits'),
]))

# ─────────────────────── SEOHead.tsx (JSON-LD) ───────────────────────
JOBS.append(('src/components/SEOHead.tsx', [
    ('5 usos/mes.', '10.000 créditos/mes.'),
    ('150 usos/mes.', '85.000 créditos/mes.'),
    ('350 usos/mes.', '175.000 créditos/mes.'),
]))

# ─────────────────── Use-case content (CTAs gratis) ───────────────────
JOBS.append(('src/data/use-cases-content.es.ts', [
    ('5 usos al mes', '10.000 créditos al mes'),
]))
JOBS.append(('src/data/use-cases-content.es.consultor.ts', [
    ('5 usos al mes', '10.000 créditos al mes'),
]))
JOBS.append(('src/data/use-cases-content.en.ts', [
    ('5 uses per month', '10,000 credits per month'),
]))
JOBS.append(('src/data/use-cases-content.en.consultor.ts', [
    ('5 uses per month', '10,000 credits per month'),
]))
JOBS.append(('src/data/use-cases-content.fr.consultor.ts', [
    ('5 utilisations par mois', '10 000 crédits par mois'),
]))
JOBS.append(('src/data/use-cases-content.de.consultor.ts', [
    ('5 Anwendungen pro Monat', '10.000 Credits pro Monat'),
]))
JOBS.append(('src/data/use-cases-content.it.consultor.ts', [
    ('5 crediti al mese', '10.000 crediti al mese'),
]))
JOBS.append(('src/data/use-cases-content.pt.consultor.ts', [
    ('5 utilizações por mês', '10.000 créditos por mês'),
]))
JOBS.append(('src/data/use-cases-content.nl.consultor.ts', [
    ('5 keer per maand', '10.000 credits per maand'),
]))

# ─────────────────── UI use-cases (CTA notes 7 idiomas) ───────────────────
JOBS.append(('src/pages/UseCasePage.tsx', [
    ('5 usos gratis al mes · Sin tarjeta', '10.000 créditos gratis al mes · Sin tarjeta'),
    ('5 free uses per month · No credit card', '10,000 free credits per month · No credit card'),
    ('5 usages gratuits/mois · Sans carte bancaire', '10 000 crédits gratuits/mois · Sans carte bancaire'),
    ('5 kostenlose Anwendungen/Monat · Keine Kreditkarte', '10.000 kostenlose Credits/Monat · Keine Kreditkarte'),
    ('5 utilizzi gratis/mese · Senza carta', '10.000 crediti gratis/mese · Senza carta'),
    ('5 usos grátis/mês · Sem cartão', '10.000 créditos grátis/mês · Sem cartão'),
    ('5 gratis gebruiken/maand · Geen creditcard', '10.000 gratis credits/maand · Geen creditcard'),
]))
JOBS.append(('src/pages/UseCasesHub.tsx', [
    ('5 usos gratis al mes · Sin tarjeta', '10.000 créditos gratis al mes · Sin tarjeta'),
    ('5 usos al mes', '10.000 créditos al mes'),
    ('5 free uses per month · No credit card', '10,000 free credits per month · No credit card'),
    ('5 uses per month', '10,000 credits per month'),
]))
JOBS.append(('src/pages/ConsultoriaGastroProHub.tsx', [
    ('5 usos al mes', '10.000 créditos al mes'),
]))

# ─────────────────── Páginas pSEO con planes hardcoded ───────────────────
for page in ['EscandallosRestaurante', 'HerramientasIARestaurantes',
             'RecetasIARestaurantes', 'ReducirCostesRestaurante',
             'MenuRestaurante', 'ChatGPTRestaurantes',
             'SoftwareGestionCocina', 'MarketingRestaurante']:
    JOBS.append(('src/pages/%s.tsx' % page, [
        ('5 usos/mes', '10.000 créditos/mes'),
        ('150 usos/mes', '85.000 créditos/mes'),
        ('350 usos/mes', '175.000 créditos/mes'),
    ]))

# ─────────────────── pSEO ciudades ───────────────────
JOBS.append(('src/data/pseo-cities-content.es.ts', [
    ('Suscripción mensual con uso ilimitado.', 'Suscripción mensual con créditos ilimitados.'),
]))


def main():
    total, zeros = 0, []
    for relpath, pairs in JOBS:
        path = BASE + relpath
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        file_hits = 0
        for old, new in pairs:
            n = text.count(old)
            if n == 0:
                zeros.append('%s :: %r' % (relpath, old))
            text = text.replace(old, new)
            file_hits += n
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        total += file_hits
        print('%-55s %3d reemplazos' % (relpath, file_hits))
    print('\nTOTAL: %d reemplazos' % total)
    if zeros:
        print('\n⚠️  PATRONES SIN COINCIDENCIA (%d):' % len(zeros))
        for z in zeros:
            print('   -', z)
        sys.exit(1)


if __name__ == '__main__':
    main()
