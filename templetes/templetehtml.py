"""
**********************************************************
Opte por guardar la plantilla en una variable de python 
para poder usar el formato de cadenas (str.format)
**********************************************************

Plantilla de correo, recibe 2 datos con (str.format)
nombre y edad del que recibe el correo para un resultado mas personalizado

https://stripo.email/: Generador de plantillas html para emails
"""

cuerpo_html = """
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<body>
    <div class="es-wrapper-color">
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="background-position: center top;">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table cellpadding="0" cellspacing="0" class="es-content esd-footer-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                            <tbody>
                                                <tr>
                                                    <td class="es-p20t es-p20r es-p20l esd-structure" align="left" background="https://demo.stripocdn.email/content/guids/3bd8ea22-deb1-43ca-a8a4-52333ae7eafd/images/template.png" style="background-image: url(https://demo.stripocdn.email/content/guids/3bd8ea22-deb1-43ca-a8a4-52333ae7eafd/images/template.png); background-repeat: no-repeat; background-position: left top;">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text">
                                                                                        <p style="text-align: center; font-family: 'comic sans ms', 'marker felt-thin', arial, sans-serif; font-size: 19px; color: #cc66cc;">CON MUCHO CARIÑO PARA {}<br>TE QUIERO:</p>
                                                                                        <p style="text-align: center; font-family: 'comic sans ms', 'marker felt-thin', arial, sans-serif; font-size: 17px;"><br></p>
                                                                                        <h1 style="text-align: center; color: #9933cc;">!TE DESEO<br>FELIZ<br>CUMPLEAÑOS¡</h1>
                                                                                        <p style="font-size: 17px;"><br style="font-size: 17px;"></p>
                                                                                        <p style="text-align: center; font-family: 'comic sans ms', 'marker felt-thin', arial, sans-serif; color: #cc66cc; font-size: 18px;">Dicen que las palabras se las lleva el tiempo..</p>
                                                                                        <p style="text-align: center; font-family: 'comic sans ms', 'marker felt-thin', arial, sans-serif; color: #cc66cc; font-size: 18px;">Pero esta imagen vale mas que mil palabras.</p>
                                                                                        <p style="text-align: center; font-family: 'comic sans ms', 'marker felt-thin', arial, sans-serif; color: #cc66cc; font-size: 18px;">Felices {} Años</p>
                                                                                        <p><br></p>
                                                                                        <p style="display: none;"><br></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
"""