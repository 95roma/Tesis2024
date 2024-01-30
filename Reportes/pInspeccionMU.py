from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from InspeccionMejViviendaApp.models import *
from PresupuestoVApp.models import *


class pinspmu(FPDF):
    
    def pInspeccionMU(request, id ):
        try:
            pim=pInspeccionm.objects.get(id=id)
        except pInspeccionm.DoesNotExist:
            pim=""
        try:
            inspeccionm=InspeccionM.objects.get(id=pim.idim.id)
        except InspeccionM.DoesNotExist:
            inspeccionm=""
        try:
            do= datosObra.objects.get(idSolicitud=inspeccionm.ids.id)
        except datosObra.DoesNotExist:
            do=""    
        try:
            DMipm = DMejoramientoipm.objects.get(idip=pim.id)
        except DMejoramientoipm.DoesNotExist:
            DMipm=""   



        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
   
        #Margenes de la pagina

        pdf.rect(10, 55,196,177)
        pdf.set_line_width(0.1)
        
        
        try:  
            # Agregar la imagen desde la instancia pil
            img_path = pim.esquema.path  # Asumiendo que es un campo FileField o ImageField
            x = 11  # Coordenada horizontal 
            y = 70  # Coordenada vertical... arriba
            w = 194 # Ancho de la imagen en puntos
            h = 127  # Altura de la imagen en puntos
            pdf.image(img_path , x=x, y=y, w=w, h=h)
        except:
            pass

        pdf.image('TesisApp\static\TesisApp\images\logohabitat.jpg', x=20, y=4, w=40, h=25)    
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=9,txt='', border=0, align='C', fill=False)
        pdf.cell(w=0,h=9,txt=pim.ninspeccion + ' INSPECCIÓN', border=1,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=7,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 8)
        pdf.text(x=15, y=60, txt='UBICACIÓN DEL MEJORAMIENTO ')

        pdf.set_font('Arial', '', 10)
        pdf.set_fill_color(166,166,166)
        pdf.cell(w=65,h=6,txt='Nombre del Cliente:', border=1, align='C', fill=True)
        pdf.cell(w=50,h=6,txt='Municipio del mejoramiento:', border=1, align='C', fill=True)
        pdf.cell(w=20,h=6,txt='Agencia:', border=1, align='C', fill=True)
        pdf.cell(w=0,h=6,txt=inspeccionm.ids.perfil.Agencia.nombre if hasattr(inspeccionm, 'ids') else '', border=1, align='C', fill=False, ln=1)
        pdf.cell(w=65,h=5,txt=(inspeccionm.ids.perfil.nombres if hasattr(inspeccionm, 'ids') else '') +' '+ (inspeccionm.ids.perfil.apellidos if hasattr(inspeccionm, 'ids') else '' ), border=1,  align='C', fill=False)
        pdf.cell(w=50,h=5,txt=inspeccionm.ids.perfil.municipio.distri if hasattr(inspeccionm, 'ids') else '', border=1, align='C', fill=False)
        pdf.cell(w=20,h=5,txt='Fecha', border=1, align='C', fill=True)
        x=pdf.get_x()
        pdf.cell(w=0,h=5,txt=pim.fecha.strftime("%d/%m/%Y") if hasattr(pim, 'fecha') else '', border=1, align='C', fill=False, ln=1)
        pdf.cell(w=65,h=10,txt='Dirección del proyecto:', border=1, align='C', fill=True)
        y=pdf.get_y()
        pdf.multi_cell(w=70,h=5,txt=str(do.direExacta) if hasattr(do, 'direExacta') else '', border='TLR',  align='C', fill=False)
        pdf.set_xy(x, y)
        pdf.multi_cell(w=0,h=5,txt='Dias estimados para la construcción de la obra:', border=1, align='C', fill=True)
        
        pdf.cell(w=65,h=6,txt='Mejora a realizar:', border=1, align='C', fill=True)
        pdf.cell(w=70,h=6,txt=DMipm.descripcion if hasattr(DMipm, 'descripcion') else '', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=6,txt=str(DMipm.diasestimados) if hasattr(DMipm, 'diasestimado') else '', border=1, align='C', fill=False, ln=1)

        pdf.text(x=20, y=249, txt='F. ')
        pdf.line(20, 250, 60, 250)
        pdf.text(x=20, y=255, txt='Nombre. ')
        pdf.text(x=20, y=259, txt='Tec. de Construcción ')
       

        pdf.output('pInspeccionmUbi.pdf', 'F')
        return FileResponse(open('pInspeccionmUbi.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
