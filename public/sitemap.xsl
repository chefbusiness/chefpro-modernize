<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xhtml="http://www.w3.org/1999/xhtml"
  exclude-result-prefixes="sitemap xhtml">

  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html lang="es">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <meta name="robots" content="noindex, follow"/>
        <title>XML Sitemap — AI Chef Pro</title>
        <style>
          * { box-sizing: border-box; margin: 0; padding: 0; }
          body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f8faf8; color: #1a1a1a; }
          header { background: #166534; color: white; padding: 20px 32px; display: flex; align-items: center; gap: 16px; }
          header h1 { font-size: 1.25rem; font-weight: 600; }
          header span { font-size: 0.85rem; opacity: 0.8; }
          .meta { background: #dcfce7; border-bottom: 1px solid #bbf7d0; padding: 12px 32px; font-size: 0.85rem; color: #166534; display: flex; gap: 24px; }
          .meta strong { font-weight: 600; }
          main { max-width: 1100px; margin: 32px auto; padding: 0 16px; }
          table { width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,.08); }
          th { background: #166534; color: white; text-align: left; padding: 12px 16px; font-size: 0.8rem; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; }
          td { padding: 11px 16px; font-size: 0.875rem; border-bottom: 1px solid #f0fdf4; vertical-align: middle; }
          tr:last-child td { border-bottom: none; }
          tr:nth-child(even) td { background: #f0fdf4; }
          a { color: #166534; text-decoration: none; word-break: break-all; }
          a:hover { text-decoration: underline; }
          .lang-badge { display: inline-block; background: #dcfce7; color: #166534; border-radius: 4px; padding: 1px 6px; font-size: 0.75rem; font-weight: 600; margin-right: 4px; }
          footer { text-align: center; padding: 24px; color: #6b7280; font-size: 0.8rem; }
          footer a { color: #166534; }
        </style>
      </head>
      <body>
        <header>
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
            <circle cx="16" cy="16" r="16" fill="white" fill-opacity="0.2"/>
            <path d="M8 12h16M8 16h10M8 20h12" stroke="white" stroke-width="2" stroke-linecap="round"/>
          </svg>
          <div>
            <h1>XML Sitemap — AI Chef Pro</h1>
            <span>aichef.pro · Suite de IA para Chefs y Restaurantes</span>
          </div>
        </header>

        <div class="meta">
          <div>URLs indexadas: <strong><xsl:value-of select="count(sitemap:urlset/sitemap:url)"/></strong></div>
          <div>Última actualización: <strong><xsl:value-of select="sitemap:urlset/sitemap:url[1]/sitemap:lastmod"/></strong></div>
          <div>Generado para: <strong>Google Search Console</strong></div>
        </div>

        <main>
          <table>
            <thead>
              <tr>
                <th style="width:60%">URL</th>
                <th style="width:15%">Última modificación</th>
                <th style="width:25%">Idiomas alternativos</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="sitemap:urlset/sitemap:url">
                <tr>
                  <td>
                    <a href="{sitemap:loc}" target="_blank"><xsl:value-of select="sitemap:loc"/></a>
                  </td>
                  <td><xsl:value-of select="sitemap:lastmod"/></td>
                  <td>
                    <xsl:for-each select="xhtml:link">
                      <xsl:if test="@rel='alternate' and @hreflang != 'x-default'">
                        <span class="lang-badge"><xsl:value-of select="@hreflang"/></span>
                      </xsl:if>
                    </xsl:for-each>
                  </td>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>
        </main>

        <footer>
          <a href="https://aichef.pro">AI Chef Pro</a> · Este sitemap está generado para motores de búsqueda. ·
          <a href="https://www.sitemaps.org" target="_blank">Protocolo Sitemaps</a>
        </footer>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
