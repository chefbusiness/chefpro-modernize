#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mailing del hito «1.000.000 de consultas» (2026-09-21) — monta un HTML por idioma.

    python3 build.py            # los 7 idiomas que tengan copy/<lang>.json
    python3 build.py --lang es

Entradas:
  copy/<lang>.json  — la prosa (el ES lo escribe una persona; el resto sale de traducir.py)
  datos.json        — lo que NO se traduce: enlaces, nombres de agentes tal como están en
                      cada workspace de Pickaxe, remitente y segmento de Resend.
Salida: ../broadcast-hito-1m-<lang>.html (misma plantilla que broadcast-integraciones-agentes-*.html).

Los bloques se montan sólo si el idioma tiene datos: NL no tiene sección de modelos (su
workspace sólo tiene ChatGPT 5) ni post en el blog; «35 agentes afinados» sólo en ES.
"""
import argparse, json, html
from pathlib import Path

DIR = Path(__file__).resolve().parent
OUT = DIR.parent
IMG = 'https://aichef.pro/blog-assets/2026/09/un-millon-destacada.jpg'
CAMP = 'hito-1m'


def utm(url, lang, slot):
    sep = '&amp;' if '?' in url else '?'
    return '%s%sutm_source=resend&amp;utm_medium=email&amp;utm_campaign=%s&amp;utm_content=%s-%s-%s' % (
        url, sep, CAMP, CAMP, lang, slot)


def lista_inline(nombres, conj):
    n = [html.escape(x) for x in nombres]
    if len(n) == 1:
        return n[0]
    return ', '.join(n[:-1]) + ' ' + conj + ' ' + n[-1]


def monta(lang):
    t = json.loads((DIR / 'copy' / ('%s.json' % lang)).read_text(encoding='utf-8'))
    d = json.loads((DIR / 'datos.json').read_text(encoding='utf-8'))[lang]
    # El traductor deja «Modelos IA + LLM» sin traducir; aquí entra el nombre real de la carpeta.
    if d.get('seccion'):
        t = {k: (v.replace('Modelos IA + LLM', d['seccion']) if isinstance(v, str) else v) for k, v in t.items()}
    P = 'style="margin:0 0 16px;"'
    H = 'style="margin:24px 0 10px;font-family:Arial,Helvetica,sans-serif;font-size:18px;line-height:1.3;color:#111111;"'
    LI = 'style="margin:0 0 8px;"'
    destino_img = d['post'] or d['app']

    partes = []
    partes.append('<p style="margin:0 0 4px;font-family:Arial,Helvetica,sans-serif;font-size:13px;letter-spacing:1px;'
                  'text-transform:uppercase;color:#111111;font-weight:bold;border-bottom:3px solid #FFD700;'
                  'display:inline-block;padding-bottom:3px;">%s</p>' % html.escape(t['label']))
    partes.append('<p style="margin:16px 0 20px;">%s</p>' % t['saludo'])
    partes.append('<p %s>%s</p>' % (P, t['p_hito']))
    partes.append('<a href="%s" style="display:block;margin:4px 0 20px;"><img src="%s" width="536" alt="%s" '
                  'style="display:block;width:100%%;max-width:536px;height:auto;border-radius:8px;border:0;" /></a>'
                  % (utm(destino_img, lang, 'imagen'), IMG, html.escape(t['alt_imagen'])))
    partes.append('<p %s>%s</p>' % (P, t['p_gracias']))

    if d['modelos']:
        partes.append('<h2 %s>%s</h2>' % (H, html.escape(t['h_modelos'])))
        partes.append('<p style="margin:0 0 10px;">%s</p>' % t['p_modelos'])
        items = []
        for nombre, url, tag in d['modelos']:
            etiqueta = ''
            if tag:
                etiqueta = (' <span style="font-family:Arial,Helvetica,sans-serif;font-size:11px;letter-spacing:1px;'
                            'text-transform:uppercase;color:#111111;background:#FFD700;border-radius:4px;padding:1px 6px;">'
                            '%s</span>' % html.escape(t['tag_' + tag]))
            items.append('<li %s><a href="%s" style="color:#2b2620;font-weight:bold;">%s</a>%s</li>'
                         % (LI, utm(url, lang, 'modelo'), html.escape(nombre), etiqueta))
        partes.append('<ul style="margin:0 0 16px;padding-left:20px;">%s</ul>' % ''.join(items))
        partes.append('<p %s>%s</p>' % (P, t['p_modelos_prueba']))

    if d['afinados']:
        partes.append('<h2 %s>%s</h2>' % (H, html.escape(t['h_afinados'])))
        partes.append('<p %s>%s</p>' % (P, t['p_afinados']))

    if d['top']:
        partes.append('<h2 %s>%s</h2>' % (H, html.escape(t['h_top'])))
        partes.append('<p %s>%s <strong>%s</strong>.</p>' % (P, t['p_top'], lista_inline(d['top'], t['conj'])))

    partes.append('<h2 %s>%s</h2>' % (H, html.escape(t['h_feedback'])))
    partes.append('<p style="margin:0 0 24px;">%s</p>' % t['p_feedback'])

    partes.append('<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto 24px;"><tr>'
                  '<td style="border-radius:8px;background:#111111;"><a href="%s" style="display:inline-block;'
                  'padding:13px 30px;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;'
                  'color:#FFD700;text-decoration:none;">%s</a></td></tr></table>'
                  % (utm(d['app'], lang, 'cta'), html.escape(t['cta'])))

    if d['post']:
        partes.append('<p %s>%s<a href="%s" style="color:#2b2620;">%s</a>.</p>'
                      % (P, t['p_blog_antes'], utm(d['post'], lang, 'blog'), html.escape(t['p_blog_enlace'])))
    partes.append('<p style="margin:0 0 20px;">%s</p>' % t['p_no_usuario'])
    partes.append('<p style="margin:0;">%s<br />%s</p>' % (t['despedida'], html.escape(t['firma'])))

    cuerpo = '\n'.join(partes)
    doc = '''<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width" />
<title>%(subject)s</title>
</head>
<body style="margin:0;padding:0;background:#f6f4ef;">
<div style="display:none;max-height:0;overflow:hidden;">
%(preheader)s
</div>
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" style="background:#f6f4ef;padding:24px 0;">
<tr>
<td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%%;background:#ffffff;border-radius:12px;padding:32px;font-family:Georgia,'Times New Roman',serif;color:#2b2620;font-size:16px;line-height:1.6;">
<tr>
<td>
%(cuerpo)s
</td>
</tr>
<tr>
<td style="padding-top:28px;border-top:1px solid #eee6da;margin-top:20px;">
<p style="margin:16px 0 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#9a8f80;">
AI Chef Pro · aichef.pro<br />
%(footer)s<br />
<a href="{{{RESEND_UNSUBSCRIBE_URL}}}" style="color:#9a8f80;">%(baja)s</a>
</p>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>
''' % dict(lang=lang, subject=html.escape(t['subject']), preheader=html.escape(t['preheader']),
           cuerpo=cuerpo, footer=html.escape(t['footer_por_que']), baja=html.escape(t['baja']))
    out = OUT / ('broadcast-hito-1m-%s.html' % lang)
    out.write_text(doc, encoding='utf-8')
    print('%s → %s (%d bytes) · asunto: %s' % (lang, out.name, len(doc.encode('utf-8')), t['subject']))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default=None)
    a = ap.parse_args()
    langs = [a.lang] if a.lang else [p.stem for p in sorted((DIR / 'copy').glob('*.json'))]
    for l in langs:
        monta(l)
