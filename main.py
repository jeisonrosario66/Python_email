import pandas as pd
from smtp import send_email

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