from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from SolicitudesApp.models import *
from InspeccionLoteApp.models import *
from InspeccionMejViviendaApp.models import *
from HistorialApp.models import *


class solDen(FPDF):
    
    def solicitudesDen(request, id ):

        try:
            s=  solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s=""
        try:
            d=  domicilio.objects.get(idSolicitud=id, tipo="Solicitante")
        except domicilio.DoesNotExist:
            d=""
        try:
            do=  datosObra.objects.get(idSolicitud=id)
        except datosObra.DoesNotExist:
            do=""
        try:
            dt=  detalle.objects.get(idSolicitud=id)
        except detalle.DoesNotExist:
            dt=""
        
        try:
            rh=  RegHis.objects.get(idsolicitud=id)
        except RegHis.DoesNotExist:
            rh=""
        
        if s.tipoobra=='mejora':
            try:
                inspm=InspeccionM.objects.get(ids=s.id)  
                ft=Factibilidadipm.objects.get(idip=inspm.id) 
            except InspeccionM.DoesNotExist:
                inspm=""   
                
        else:
            try:
                inspl=Inspeccionl.objects.get(ids=s.id) 
                ft=Factibilidadipl.objects.get(idipl=inspl.id)   
            except Inspeccionl.DoesNotExist:
                inspl=""
                  
        
        locale.setlocale(locale.LC_TIME, 'es_ES')
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()      

        pdf.set_font('Arial', 'B', 12)
        pdf.set_y(20)
        pdf.set_left_margin(20)
        pdf.cell(w=0,h=5,txt='ASOCIACIÓN HPH EL SALVADOR ', border='',  align='C', fill=False, ln=1)  
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=0,h=5,txt=s.perfil.Agencia.departamento if hasattr(s, 'perfil') else '', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=0,h=5,txt="Datos de Solicitud Denegada ", border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 9)
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=15, y=15, w=55, h=20)
        pdf.cell(w=0,h=10,txt='', border='',  align='C', fill=False, ln=1)

        pdf.cell(w=0,h=5,txt=s.fecha.strftime("%A, %d de %B de %Y") if hasattr(s, 'fecha') else '', border='', align='R', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=190,h=5,txt='Datos del Solicitante:', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=60,h=6,txt='DUI:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=s.perfil.dui if hasattr(s, 'perfil') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Nombre del Cliente:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=s.perfil.nombres +' '+ s.perfil.apellidos, border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Dirección:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=d.direccion if hasattr(d, 'direccion') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Teléfono:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=s.perfil.telefono if hasattr(s, 'perfil') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Profesión u oficio:', border=0, align='L', fill=False)
        pdf.set_font('Arial', '', 7)
        pdf.cell(w=110,h=6,txt=s.perfil.idocu.ocupacion if hasattr(s, 'perfil') else '', border=0, align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=60,h=6,txt='Ingresos:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt='$   '+ str(d.salarioIngreso) if hasattr(d, 'salarioIngreso') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Puntaje DICOM:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt= str(rh.puntaje) if hasattr(rh, 'puntaje') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=6,txt='', border=0, align='L', fill=False, ln=1)

        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=190,h=5,txt='Datos de la Obra a Realizar:', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=60,h=6,txt='Destino del Credito:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=do.destino.alternativa if hasattr(do, 'destino') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Detalle de la Obra:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=do.detalle.topovivienda  if hasattr(do, 'detalle') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Presupuesto de la Obra:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt='$   '+ str(do.presupuesto) if hasattr(do, 'presupuesto') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=6,txt='', border=0, align='L', fill=False, ln=1)

        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=190,h=5,txt='Detalle de la Solicitud:', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=60,h=6,txt='Monto a Solicitar:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt='$   '+ str(dt.monto) if hasattr(dt, 'monto') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Plazo solicitado:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=dt.plazo if hasattr(dt, 'plazo') else '' , border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Cuota:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt='$   '+ str(dt.cuota) if hasattr(dt, 'cuota') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=60,h=6,txt='Fecha que Solicita Pagar:', border=0, align='L', fill=False)
        pdf.cell(w=110,h=6,txt=dt.fechaPago if hasattr(dt, 'fechaPago') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=6,txt='', border=0, align='L', fill=False, ln=1)

        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=190,h=5,txt='Observaciones:', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=6,txt=s.observaciones if hasattr(s, 'observaciones') else '', border=0, align='L', fill=False, ln=1)

    
        pdf.output('solicitudesDenegadas.pdf', 'F')
        return FileResponse(open('solicitudesDenegadas.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
