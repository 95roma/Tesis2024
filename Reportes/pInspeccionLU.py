from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from InspeccionLoteApp.models import *
from PresupuestoVApp.models import *


class pinsplu(FPDF):
    
    def pInspeccionLU(request, id ):
        try:
            pil=pInspeccionl.objects.get(id=id)
        except pInspeccionl.DoesNotExist:
            pil=""
        try:
            inspeccionl=Inspeccionl.objects.get(id=pil.idil.id)
        except Inspeccionl.DoesNotExist:
            inspeccionl=""
        try:
            pdg= Presupuestovdg.objects.get(ids=inspeccionl.ids.id)
        except :
            pdg= ""
        try:
            do= datosObra.objects.get(idSolicitud=inspeccionl.ids.id)
        except datosObra.DoesNotExist:
            do=""       
        try:
            DPipl = DescripcionProyectoipl.objects.get(idipl=inspeccionl.id)
        except DescripcionProyectoipl.DoesNotExist:
            DPipl=""


        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        #pdf.multi_cell(w=0, h=40, txt='', border=1)
        #Margenes de la pagina
        pdf.set_auto_page_break(auto=True, margin=5)
        pdf.set_draw_color(0,0,0)
        pdf.set_line_width(0.5)
        pdf.rect(5, 3,205,260)
     
        pdf.rect(6, 4,203,50)
        pdf.set_line_width(0.1)

        pdf.rect(10, 58,196,167)
        pdf.set_line_width(0.1)
        
        
        try:  
            # Agregar la imagen desde la instancia pil
            img_path = pil.ubicacion.path  # Asumiendo que es un campo FileField o ImageField
            x = 11  # Coordenada horizontal 
            y = 75  # Coordenada vertical... arriba
            w = 194 # Ancho de la imagen en puntos
            h = 147  # Altura de la imagen en puntos
            pdf.image(img_path , x=x, y=y, w=w, h=h)
        except:
            pass

        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=7, y=6, w=43, h=28)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=45,h=8,txt='', border=0, align='C', fill=False)
        pdf.cell(w=0,h=8,txt='UBICACIÓN DE LA VIVIENDA EN EL TERRENO', border=1,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=40,h=5,txt='AGENCIA:', border=1,  align='L', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt=inspeccionl.ids.perfil.Agencia.nombre if hasattr(inspeccionl, 'ids') else '', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='C', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=5,txt='FECHA:', border=1,  align='L', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt=str(pil.fecha) if hasattr(pil, 'fecha') else '', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='C', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=5,txt='TIEMPO DE CONSTRUCCIÓN:', border=0,  align='L', fill=False)
        pdf.set_font('Arial', pdg.tiempoconstruccion if hasattr(pdg, 'tiempoconstruccion') else '', 10)
        pdf.cell(w=0,h=5,txt='', border=0,  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=5,txt='CLIENTE:', border=1, align='L', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt=(inspeccionl.ids.perfil.nombres if hasattr(inspeccionl, 'ids') else '') +' '+ (inspeccionl.ids.perfil.apellidos if hasattr(inspeccionl, 'ids') else '' ), border=1,  align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=6,txt='MODELO DE LA VIVIENDA:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=35,h=6,txt=DPipl.modeloviviedac if hasattr(DPipl, 'modeloviviedac') else '', border=1,  align='L', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=6,txt='MUNICIPIO:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=6,txt=inspeccionl.ids.perfil.municipio.distri if hasattr(inspeccionl, 'ids') else '', border=1,  align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=6,txt='DIRECCIÓN DE LA MEJORA:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=50,h=6,txt=do.direExacta if hasattr(do, 'direExacta') else '', border=1,  align='L', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=6,txt='TELEFONO:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=6,txt=inspeccionl.ids.perfil.telefono if hasattr(inspeccionl, 'ids') else '', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)

        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt='', border=0,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=162,txt='', border=0,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)

        pdf.cell(w=95,h=32,txt='', border=1, align='C', fill=False)
        pdf.cell(w=3,h=32,txt='', border=0, align='C', fill=False)
        pdf.cell(w=65,h=32,txt='', border=1, align='C', fill=False)
        pdf.cell(w=2,h=32,txt='', border=0, align='C', fill=False)
        pdf.cell(w=30,h=32,txt='', border=1, align='C', fill=False)

        pdf.text(x=109, y=234, txt='SELLO ')
        pdf.text(x=15, y=239, txt='F. ')
        pdf.line(15, 240, 90, 240)
        pdf.text(x=15, y=245, txt='TECNICO EN SERVICIOS CONSTRUCTIVOS ')
        


        pdf.output('pInspeccionlUbi.pdf', 'F')
        return FileResponse(open('pInspeccionlUbi.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
