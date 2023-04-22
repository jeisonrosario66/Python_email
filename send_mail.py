"""
Ciclo 2: Tienes un mensaje

sendMail: Objeto creado para la resolución de ciclo. Se compone de :
  def __init__(self, email, password):
    constructor, define la información mínima para crear dicho objeto
    correo y contraseña en este caso

  def send_mail(self, df):
    Método, encargado del mecanismo de envió la plantilla html por correo
"""

import os
import time
import smtplib, ssl
import pandas as pd
from email import encoders
from datetime import datetime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from create_pdfFile import PdfTools
from templetehtml import cuerpo_html # Templete
from dateutil.relativedelta import relativedelta
df = pd.read_csv('contactos.csv')

#instancia de clase PdfTools
class SendMail:
    """_summary_
    Envia correo electronicos perzonalidos
    """
    def __init__(self, email, password):
        """_summary_
        Constructor
        Args:
            email (mail): Direccion email del remitente
            password (pass): Contraseña para aplicaciones
        """
        self.email = email
        self.password = password
        self.cuerpo_html = cuerpo_html
        self.context = ssl.create_default_context()
        # Hora-Fecha - Informacion adicional
        named_tuple = time.localtime() # get struct_time
        self.time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    def send_mail_html(self, df):
        """_summary_
        Metodo para realizar el envio de correo
        Args:
            df (dataframe): Archivo csv con la informacion
        """
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as server:
            server.login(self.email, self.password)
            # Filtramos los datos para que sólamente se envíen los correos a las personas que cumplen años en el día de hoy
            # hoy = datetime.now().strftime('%d/%m') # La fecha del dia (Dia/Mes)
            datos_hoy = df[df['date'].apply(lambda x: datetime.strptime(f"{datetime.now().year}/{x[-2:]}/{x[:5]}", '%Y/%y/%d/%m').strftime('%d/%m') == datetime.now().strftime('%d/%m'))]

            # Recorremos el DataFrame con un ciclo for y enviamos un correo electrónico a cada destinatario
            for column, row in datos_hoy.iterrows():
                nombreDestinatario = row['nombre'].upper()
                
                # Calcular edad ['date']
                fecha_nacimiento = datetime.strptime(row['date'], "%d/%m/%Y")
                edad = relativedelta(datetime.now(), fecha_nacimiento)
                
                # plantilla html con los datos formateados | str.format(nombreDestinatario, edad.years)
                cuerpo_html = self.cuerpo_html.format(nombreDestinatario, edad.years)
                mensaje = EmailMessage()
                mensaje['From'] = self.email
                mensaje['To'] = row['mail']
                mensaje['Subject'] = 'Feliz Cumpleaños!!'
                mensaje.set_content(cuerpo_html, subtype='html')
                server.send_message(mensaje)
    
    def send_mail_text(self, df):
        
        mensaje = """\
        Subject: Prueba smtplib

        Saludos {}, Este es un mensaje automatico enviado desde python {}."""
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(self.email, self.password)
            for column, row in df.iterrows():
                destinatario = row['mail']
                nombreDestinatario = row['nombre']
                mensaje = mensaje.format(nombreDestinatario,self.time_string)
                server.sendmail(self.email, destinatario, mensaje)

    def send_mail_pdf(self, df):
        archivoPdf_pach = "tempfile.pdf"
        pdfTools = PdfTools(archivoPdf_pach) # Instancia de objeto "PdfTools"
        cuerpoTexto = "Este es el contenido en texto del mensaje"
        sender_email = self.email
        password = self.password
        # Log in to server using secure context and send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(sender_email, password)

            for column, row in df.iterrows():
                # Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = row['mail']
                message["Subject"] = "Email enviado desde python"
                message["Bcc"] = row['mail']  # Recommended for mass emails
                # Add cuerpoTexto to email
                message.attach(MIMEText(cuerpoTexto, "plain"))
                
                # Metodo para crear el pdf
                pdfTools.create_pdf(row['mail'],row['nombre'],self.time_string) 
                # Open PDF file in binary mode
                with open(archivoPdf_pach, "rb") as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                # Encode file in ASCII characters to send by email    
                encoders.encode_base64(part)
                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {archivoPdf_pach}",
                )
                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()
                server.sendmail(sender_email, row['mail'], text)
                pdfTools.delete_pdf()

# Instanciamos la clase sendMain
send_mail = SendMail(os.environ['RETO3USER'], os.environ['RETO3PASS'])

# Metodos de envio
""" 
Toda la informacion necesaria para el envio del correo se entra dentro de la clase SendMail
"""
# send_mail.send_mail_text(df)
# send_mail.send_mail_html(df)
# send_mail.send_mail_pdf(df)

