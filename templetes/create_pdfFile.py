""" 
********************************************************************
Scrip: Creador de pdf con texto simple y personalizable
Para posterior envio por smtplib
Reto 3 Ciclo 3: Tienes un mensaje
********************************************************************
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A6
from os import remove
from templatepdf import templatePdf
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph

class PdfTools:
    def __init__(self,filename):
        self.pagesize = A6
        self.X = 8
        self.Y = 400
        self.filename = filename
        self.templatePdf = templatePdf
        self.stylesheet = stylesheet=getSampleStyleSheet()
        self.normalStyle = normalStyle = stylesheet['Normal']


    def create_pdf(self):
        c = canvas.Canvas(self.filename, self.pagesize)
        c.drawString(self.X, self.Y,self.templatePdf.format("remitente","receptor","fecha"))
        c.showPage()
        c.save()
        
    def delete_pdf(self):
        remove(self.filename)
        
    def pdf_format_str(self):
        pass
#instancia
obj = PdfTools("1.pdf")
#obj.create_pdf()
obj.create_pdf()