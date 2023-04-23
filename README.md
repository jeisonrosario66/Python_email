
# Python_email
Requisitos
- `panda`
- `reportlab`
- `smtplib`
- `ssl`
- `email`

Python_email: Consta de una serie de Objetos capaces de enviar correos electronicos:           
Texto plano         
Plantilla HTML  
Archivo PDF

# Instalar
```bash
  git clone https://github.com/jeisonrosario66/Python_email
  cd Python_email
  pip install -r requeriments.txt
```

# Enviar correo
`python send_mail.py` Script principal del programa
Para que el correo se envie debe activar los metodos de clase `SendMail`
- `send_mail_text(df)` Envia un texto plano `mensaje` Contiene el mensaje
- `send_mail_html(df)` Envia una plantilla HTML `cuerpo_html` Contiene la plantilla HTML
- `send_mail_pdf(df)` Envia una plantilla PDF `archivoPdf_pach` ruta del archivo a enviar

# Plantillas
Las plantillas se guardan en formato `.py` para porder formatear datos a dichas plantillas con `str.format()`

# Creador de PDF
El archivo se crea en el scrip `create_pdfFIle.py` desde la clase `PdfTools`                      
La clase `PdfTools` es auxiliar, necesaria para que funcione el metodo `send_mail_pdf(df)`
`PdfTools` cuenta con 2 metodos 
- `create_pdf(r_mail,r_name,date)`: Se ejecuta, genera el archivo y guarda su path en `archivoPdf_pach`
- `delete_pdf(self)`: Elimina el archivo creado por `create_pdf()` posterior al envio del correo

# Plantilla texto plano `mensaje`
![txt](https://user-images.githubusercontent.com/96961824/233812793-595271a3-228b-4f19-83f9-e838ea11e8f8.PNG)
# Plantilla HTML `cuerpo_html`
![correohtm,](https://user-images.githubusercontent.com/96961824/233812679-96ea3c73-c4bd-431a-b56b-20156bbe8fc1.PNG)
# Plantilla PDF `create_pdf(r_mail,r_name,date)`
![pdf1](https://user-images.githubusercontent.com/96961824/233812778-63871b39-3dd3-495e-ac3d-ad238b9f3514.PNG)
![pdf2](https://user-images.githubusercontent.com/96961824/233812787-34b42af4-052f-4b36-a5d0-390014b30796.PNG)

## Autor
- [@jeisonrosario66](https://https://github.com/jeisonrosario66)
