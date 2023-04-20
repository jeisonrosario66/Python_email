"""
Ciclo 2: Tienes un mensaje

sendMail: Objeto creado para la resolucion de ciclo. Se compon de :
  def __init__(self, email, password):
    constructor, define la informacion minima para crear dicho objeto
    correo y contraseña en este caso

  def send_mail(self, df):
    Metodo, encargado del mecanimos de envio la plantilla html por correo
"""


import pandas as pd
import smtplib
from email.message import EmailMessage
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from templetehtml import cuerpo_html # Templete

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

    def send_mail(self, df):
        """_summary_
        Metodo para realizar el envio de correo
        Args:
            df (dataframe): Archivo csv con la informacion
        """
        remitente = self.email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
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

# Instanciamos la clase sendMain
send_mail = sendMail('jeisonrosario.reto3@gmail.com', os.environ['RETO3'])
send_mail.send_mail(df)