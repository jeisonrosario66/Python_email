"""
Ciclo 2: Tienes un mensaje

sendMail: Objeto creado para la resolución de ciclo. Se compone de :
  def __init__(self, email, password):
    constructor, define la información mínima para crear dicho objeto
    correo y contraseña en este caso

  def send_mail(self, df):
    Método, encargado del mecanismo de envió la plantilla html por correo
"""

import pandas as pd
import smtplib, ssl
from email.message import EmailMessage
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import time
from templetes.templetehtml import cuerpo_html # Templete
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from reportlab.pdfgen.canvas import Canvas
df = pd.read_csv('contactos.csv')

class sendMail:
    """_summary_
    Envia correo electronicos perzonalidos
    """
    def __init__(self, email, password):
        """_summary_
        Constructor
        Args:
            email (mail): Direccion email del remitente
            password (pass): Contraseña para aplicaciones
            cuerpo_html (template): Plantilla de correo html
        """
        global cuerpo_html
        self.email = email
        self.password = password
        self.cuerpo_html = cuerpo_html
        self.context = ssl.create_default_context()
        

    def send_mail_html(self, df):
        """_summary_
        Metodo para realizar el envio de correo
        Args:
            df (dataframe): Archivo csv con la informacion
        """
        remitente = self.email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as servidor:
            servidor.login(self.email, self.password)
            
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
                destinatario = row['mail']
                mensaje = EmailMessage()
                mensaje['From'] = remitente
                mensaje['To'] = destinatario
                mensaje['Subject'] = 'Feliz Cumpleaños!!'
                mensaje.set_content(cuerpo_html, subtype='html')
                servidor.send_message(mensaje)
    
    def send_mail_text(self, df):
        # Hora-Fecha - Informacion adicional
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        mensaje = """\
        Subject: Prueba smtplib

        Saludos {}, Este es un mensaje automatico enviado desde python {}."""
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(self.email, self.password)
            for column, row in df.iterrows():
                destinatario = row['mail']
                nombreDestinatario = row['nombre']
                mensaje = mensaje.format(nombreDestinatario,time_string)
                server.sendmail(self.email, destinatario, mensaje)

    def send_mail_pdf(self, df):
        pathPdf = "ejemplo_2.pdf"
        pdfFile = Canvas(pathPdf)  # In same directory as script
        cuerpoTexto = "Este es el contenido en texto del mensaje"
        sender_email = self.email
        receiver_email = os.environ['RETO3USER']
        password = os.environ['RETO3PASS']
        # Log in to server using secure context and send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(sender_email, password)

            for column, row in df.iterrows():
                # Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = "An email with attachment from Python"
                message["Bcc"] = receiver_email  # Recommended for mass emails
                # Add cuerpoTexto to email
                message.attach(MIMEText(cuerpoTexto, "plain"))
                pdfFile.drawString(72, 72, f"Hello, World{row['nombre']}")

                # Open PDF file in binary mode
                with open(pathPdf, "rb") as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())


                # Encode file in ASCII characters to send by email    
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {pdfFile}",
                )

                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()

            
                server.sendmail(sender_email, receiver_email, text)


# Instanciamos la clase sendMain
send_mail = sendMail(os.environ['RETO3USER'], os.environ['RETO3PASS'])
send_mail.send_mail_pdf(df)