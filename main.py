"""
Ciclo 1: Tienes un mensaje
Script: Itera sobre las filas del archivo cvs, enviando un correo sencillo por cada iteracion
"""

import pandas as pd
from send_mail_text import send_email

df = pd.read_csv("contactos.csv")
for column, row in df.iterrows():
    send_email(row['nombre'],row['mail'])






































"""import csv

# lee el archivo csv
with open('ej.csv', mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(', '.join(row))
        
    
"""