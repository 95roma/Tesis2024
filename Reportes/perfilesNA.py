from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from ClienteApp.models import *



class perN(FPDF):
    
    def perfilesNA(request, id ):

        try:
            p=  Perfilna.objects.get(id=id)
        except Perfilna.DoesNotExist:
            p=""
     
        
        locale.setlocale(locale.LC_TIME, 'es_ES')
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()      

        pdf.set_font('Arial', 'B', 12)
        pdf.set_y(20)
        pdf.set_left_margin(20)
        pdf.cell(w=0,h=5,txt='ASOCIACIÓN HPH EL SALVADOR ', border='',  align='C', fill=False, ln=1)  
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=0,h=5,txt=p.Agencia.departamento if hasattr(p, 'Agencia') else '', border='',  align='C', fill=False, ln=1)
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=15, y=15, w=55, h=20)
        pdf.cell(w=0,h=5,txt='Datos del Solicitante que No Aplica', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=10,txt='', border='',  align='C', fill=False, ln=1)

        #pdf.cell(w=0,h=5,txt=s.fecha.strftime("%A, %d de %B de %Y"), border='', align='R', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=190,h=5,txt='Datos del Solicitante:', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=60,h=6,txt='Fecha de Registro:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.fechaR.strftime("%d/%m/%Y") if hasattr(p, 'fechaR') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='DUI:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.dui if hasattr(p, 'dui') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Nombre del Cliente:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.nombres +' '+ p.apellidos, border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Dirección:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.direccion if hasattr(p, 'direccion') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Teléfono:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.telefono if hasattr(p, 'telefono') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Nacionalidad:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.nacionalidad if hasattr(p, 'nacionalidad') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Fecha de Nacimiento:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.fecha.strftime("%d/%m/%Y") if hasattr(p, 'fecha') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Edad:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=str(p.edad) if hasattr(p, 'edad') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Salario:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=str(p.salario) if hasattr(p, 'salario') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Observaciones:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=p.observaciones if hasattr(p, 'observaciones') else '', border=0, align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        
    
        pdf.output('perfilesNoAplic.pdf', 'F')
        return FileResponse(open('perfilesNoAplic.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
