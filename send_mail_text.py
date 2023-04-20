"""
Ciclo 1: Tienes un mensaje
Script: Itera sobre las filas del archivo cvs, enviando un correo sencillo por cada iteracion
"""

import smtplib, ssl
import time
import os

def send_email(nombre,mail):
    """_summary_
    Envia correos de texto plano
    args:
        nombre (str): Nombre del destinatario
        email (str): correo del detinatario
    """
 
    # Hora-Fecha - Informacion adicional
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = os.environ['RETO3'] # Variable de entorno

    sender_email = "jeisonrosario.reto3@gmail.com"  # Correo propio
    receiver_email = [mail]  # Lista de contactos a enviar correos
    
    mensaje = """\
    Subject: Prueba smtplib

    Saludos {}, Este es un mensaje automatico enviado desde python {}.""".format(nombre,time_string) 

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, mensaje)