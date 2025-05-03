<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/bloglist">
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
                                <div class="main-body-container">
                                    <div class="window-title">Teminal - All Blog Entries</div>
                                    <div class="main-body">

                                            <xsl:copy-of select="content"/>

                                    </div>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="navigation">
        <div class="window-title">Navigation</div>
        <div class="cde-menu">
            <xsl:copy-of select="content"/>
        </div>
    </xsl:template>
</xsl:stylesheet>
