""" 
********************************************************************
Scrip: Creador de pdf con texto simple y personalizable
Para posterior envio por smtplib
Reto 3 Ciclo 3: Tienes un mensaje
********************************************************************
"""
from os import remove
from templatepdf import templatePdf
from reportlab.lib.pagesizes import A6
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate

class PdfTools:
    """Clase encargada de Crear archivo pdf y eliminar dicho archivo
    """
    def __init__(self,filename):
        self.pagesize = A6
        self.X = 8
        self.Y = 400
        self.filename = filename
        self.templatePdf = templatePdf


    def create_pdf(self,r_mail,r_name,date):
        """_summary_
        Crea archivo pdf recibiendo los siguientes parametros

        Args:
            r_mail (str): Email de quien recible el correo
            r_name (str): Nombre de quien recibe el correo
            date (str): hora y fecha actual al momento de crear el archvo
        """
        doc = SimpleDocTemplate(
            self.filename,
            pagesize = self.pagesize
        )
        
        paragraph = Paragraph(
            self.templatePdf.format(r_mail,r_name,date),
            ParagraphStyle(
                "ps1",
                fontName="Times-Roman",
                fontSize=11
            )
        )
        
        doc.build([paragraph]) 
        
    def delete_pdf(self):
        remove(self.filename)
        
#instancia
#obj = PdfTools("1.pdf")
#obj.create_pdf()
#obj.create_pdf("bolas@adentro.com","sin sonia","ahora mismo perro")