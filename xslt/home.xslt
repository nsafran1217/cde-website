<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/page">
        <html>
            <head>
                <title><xsl:value-of select="title"/></title>      
                <link rel="stylesheet" href="/css/main.css"/>
                <link rel="stylesheet" href="/css/default-back.css"/>
            </head>
            <body>
                <table>
                    <tbody>
                        <tr>
                            <td class="navbar">
                                <div class="navbar">
                                    <xsl:apply-templates select="document('./shared/nav.xml')/navigation"/>
                                </div>
                            </td>
                            <td>
                                <xsl:for-each select="sections/section">
                                    <div class="main-body-container">
                                        <div class="window-title"><xsl:value-of select="window-title"/></div>
                                        <div class="main-body">
                                            <xsl:copy-of select="content"/>
                                        </div>
                                    </div>
                                </xsl:for-each>
                                <xsl:apply-templates select="document('./blogspotlight.xml')/blogspotlight"/>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="blogspotlight">           
        <div class="main-body-container">
            <div class="window-title">Teminal - Recent Blog Articles</div>
            <div class="main-body">
                <xsl:copy-of select="content"/>
            </div>
        </div>
    </xsl:template>
    
    <xsl:template match="navigation">
        <div class="window-title">Navigation</div>
        <div class="cde-menu">
            <xsl:copy-of select="content"/>
        </div>
    </xsl:template>
</xsl:stylesheet>
