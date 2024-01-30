from fpdf import FPDF
from datetime import date
import locale
from django.http import FileResponse
from SolicitudesApp.models import *
from EvaluacionIvEFApp.models import *
from SolicitudInscripcionSApp.models import *


class hojaPN(FPDF):
    
    def hojaPreN(request, id ):

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
            med=Medio.objects.get(idSolicitud=id)                    
        except:
            med=""
        ##############################################3
        try:
            eg=  Egresosf.objects.get(idp=s.perfil.id)
        except Egresosf.DoesNotExist:
            eg=""
        try:
            ca=  Capacidadpagof.objects.get(ide=eg.id)
        except Capacidadpagof.DoesNotExist:
            ca=""

        try:
            ss=  Solicitudis.objects.get(ids=id)
        except Solicitudis.DoesNotExist:
            ss=""

        try:
            varp=(int(ss.plazo) *12)
        except :
            varp=""
                 
        locale.setlocale(locale.LC_TIME, 'es_ES')
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        
        pdf.set_margins(left=20, top=10, right=-1) # agrega el mergen a la pagina
        pdf.set_font('Arial', 'B', 10)
        #pdf.set_fill_color(r,g,b)
        #pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='         ASOCIACIÓN HPH EL SALVADOR EL SALVADOR', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='AGENCIA  '+ s.perfil.Agencia.nombre if hasattr(s, 'perfil') else '', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='HOJA DE PRE-APROBACIÓN DE CRÉDITO', border='',  align='C', fill=False, ln=1)
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=9, y=9, w=45, h=20)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)

        pdf.set_font('Arial', '', 9)
        pdf.cell(w=30,h=5,txt=s.perfil.Agencia.departamento if hasattr(s, 'perfil') else '', border=0, align='L', fill=False)
        pdf.cell(w=0,h=5,txt=s.fecha.strftime("%A, %d de %B de %Y") if hasattr(s, 'fecha') else '', border='', align='L', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        
        pdf.cell(w=30,h=5,txt='Comunidad:', border=0, align='L', fill=False)
        pdf.set_font('Arial', 'B', 9)
        pdf.cell(w=60,h=5,txt=s.comunidad if hasattr(s, 'comunidad') else '', border='B', align='C', fill=False)
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=25,h=5,txt='Municipio:', border=0, align='L', fill=False)
        pdf.set_font('Arial', 'B', 9)
        pdf.cell(w=45,h=5,txt=s.perfil.municipio.distri if hasattr(s, 'perfil') else '', border='B', align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='Destino de la Solicitud:', border=0, align='L', fill=False)
        pdf.cell(w=45,h=5,txt='Mejora de Vivienda', border='', align='L', fill=False)
        pdf.cell(w=12,h=5,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'MEJORAMIENTO' else '', border=1, align='C', fill=False)
        pdf.cell(w=45,h=5,txt='Lote + Vivienda', border='', align='L', fill=False)
        pdf.cell(w=12,h=5,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'LOTE MAS VIVIENDA' else '', border=1, align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border=0, align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='L', fill=False)
        pdf.cell(w=45,h=5,txt='Vivienda In Situ', border='', align='L', fill=False)
        pdf.cell(w=12,h=5,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'CONSTRUCCION VIVIENDA IN SITU' else '', border=1, align='C', fill=False)
        pdf.cell(w=45,h=5,txt='Vivienda Usada', border='', align='L', fill=False)
        pdf.cell(w=12,h=5,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'VIVIENDA USADA' else '', border=1, align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border=0, align='C', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=45,h=5,txt='', border='',  align='C', fill=False)
        pdf.cell(w=100,h=5,txt='Datos del Solicitante', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=4,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=30,h=8,txt='Nombre:', border=0, align='L', fill=False)
        pdf.set_font('Arial', 'B', 9)
        pdf.cell(w=116,h=8,txt= (s.perfil.nombres if hasattr(s, 'perfil') else '') +' '+ (s.perfil.apellidos if hasattr(s, 'perfil') else '') , border='B', align='C', fill=False)
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=0,h=8,txt='', border='', align='R', fill=False, ln=1)
        pdf.cell(w=30,h=8,txt='Dirección:', border=0, align='L', fill=False)
        pdf.set_font('Arial', 'B', 9)
        pdf.cell(w=0,h=8,txt=(d.direccion if hasattr(d, 'direccion') else '') +' '+ (d.referencia if hasattr(d, 'referencia') else ''), border='B', align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=30,h=8,txt='Teléfono:', border=0, align='L', fill=False)
        pdf.set_font('Arial', 'B', 9)
        pdf.cell(w=60,h=8,txt=s.perfil.telefono if hasattr(s, 'perfil') else '', border='B', align='C', fill=False)
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=0,h=8,txt='', border='', align='R', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)
        if s.tipoobra =='mejora':
            pdf.cell(w=45,h=5,txt='', border='',  align='C', fill=False)
            pdf.cell(w=100,h=5,txt='Mejoramiento de Vivienda', border=1,  align='C', fill=False)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.cell(w=45,h=8,txt='Tipo de Mejoramiento:', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=0,h=8,txt=(do.detalle.topovivienda if hasattr(do, 'detalle') else '')+''+ (do.detalleadic if hasattr(do, 'detalleadic') else ''), border='B', align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=45,h=8,txt='Monto Solicitado:', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=25,h=8,txt=str(do.presupuesto) if hasattr(do, 'presupuesto') else '', border='B', align='C', fill=False)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=25,h=8,txt='Plazo (meses):', border=0, align='C', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=35,h=8,txt=str(varp) if hasattr(ss, 'plazo') else '', border='B', align='C', fill=False)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=27,h=8,txt='Cuota Solicitada:', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=0,h=8,txt=str(ca.cuota) if hasattr(ca, 'cuota') else '', border='B', align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=0,h=6,txt='', border='',  align='C', fill=False, ln=1)
        else:
            pdf.cell(w=45,h=5,txt='', border='',  align='C', fill=False)
            pdf.cell(w=100,h=5,txt='Mejoramiento de Vivienda', border=1,  align='C', fill=False)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.cell(w=45,h=8,txt='Tipo de Mejoramiento:', border=0, align='L', fill=False)
            pdf.cell(w=0,h=8,txt='', border='B', align='R', fill=False, ln=1)
            pdf.cell(w=45,h=8,txt='Monto Solicitado:', border=0, align='L', fill=False)
            pdf.cell(w=25,h=8,txt='', border='B', align='C', fill=False)
            pdf.cell(w=25,h=8,txt='Plazo (meses):', border=0, align='L', fill=False)
            pdf.cell(w=35,h=8,txt='', border='B', align='R', fill=False)
            pdf.cell(w=27,h=8,txt='Cuota Solicitada:', border=0, align='L', fill=False)
            pdf.cell(w=0,h=8,txt='', border='B', align='C', fill=False, ln=1)
            pdf.cell(w=0,h=6,txt='', border='',  align='C', fill=False, ln=1)

        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)
        if s.tipoobra =='vivienda':
            pdf.cell(w=45,h=5,txt='', border='',  align='C', fill=False)
            pdf.cell(w=100,h=5,txt='Vivienda', border=1,  align='C', fill=False)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.cell(w=45,h=8,txt='Modelo de Vivienda:', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=0,h=8,txt=do.detalle.topovivienda if hasattr(do, 'detalle') else '', border='B', align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=45,h=8,txt='Dirección de la Obra:', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=0,h=8,txt=do.direExacta if hasattr(do, 'direExacta') else '', border='B', align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=45,h=8,txt='Monto Propuesto:', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=25,h=8,txt=str(do.presupuesto) if hasattr(do, 'presupuesto') else '', border='B', align='C', fill=False)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=25,h=8,txt='Plazo (meses):', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=35,h=8,txt=str(varp) if hasattr(ss, 'plazo') else '', border='B', align='C', fill=False)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=27,h=8,txt='Cuota Solicitada:', border=0, align='L', fill=False)
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(w=0,h=8,txt=str(ca.cuota) if hasattr(ca, 'cuota') else '', border='B', align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=0,h=3,txt='', border='', align='R', fill=False, ln=1)
        else:
            pdf.cell(w=45,h=5,txt='', border='',  align='C', fill=False)
            pdf.cell(w=100,h=5,txt='Vivienda', border=1,  align='C', fill=False)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.set_font('Arial', '', 9)
            pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
            pdf.cell(w=45,h=8,txt='Modelo de Vivienda:', border=0, align='L', fill=False)
            pdf.cell(w=0,h=8,txt='', border='B', align='R', fill=False, ln=1)
            pdf.cell(w=45,h=8,txt='Dirección de la Obra:', border=0, align='L', fill=False)
            pdf.cell(w=0,h=8,txt='', border='B', align='C', fill=False, ln=1)
            pdf.cell(w=45,h=8,txt='Monto Propuesto:', border=0, align='L', fill=False)
            pdf.cell(w=25,h=8,txt='', border='B', align='C', fill=False)
            pdf.cell(w=25,h=8,txt='Plazo (meses):', border=0, align='L', fill=False)
            pdf.cell(w=35,h=8,txt='', border='B', align='R', fill=False)
            pdf.cell(w=27,h=8,txt='Cuota Solicitada:', border=0, align='L', fill=False)
            pdf.cell(w=0,h=8,txt='', border='B', align='C', fill=False, ln=1)
            pdf.cell(w=0,h=3,txt='', border='', align='R', fill=False, ln=1)

        pdf.cell(w=25,h=5,txt='Aprobado:', border='', align='L', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=25,h=8,txt='', border='', align='R', fill=False)
        pdf.cell(w=25,h=5,txt='Observado:', border='', align='L', fill=False)
        pdf.cell(w=12,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=25,h=8,txt='', border='', align='R', fill=False)
        pdf.cell(w=25,h=5,txt='Denegado:', border='', align='L', fill=False)
        pdf.cell(w=12,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=0,h=8,txt='', border='', align='R', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)

        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=45,h=5,txt='', border='',  align='C', fill=False)
        pdf.cell(w=100,h=5,txt='Estrategia de Colocación', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 9)
        pdf.cell(w=0,h=8,txt=(med.referenciado or '') + (med.campanap or '') + (med.redes or '') + (med.pvv or '') + (med.feriav or '') + (med.perifoneo or '') + (med.radio or '') +(med.especifique or ''), border='B', align='L', fill=False, ln=1)
        pdf.cell(w=0,h=4,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=8,txt='Observaciones:', border=0, align='L', fill=False)
        pdf.cell(w=0,h=8,txt='', border='B', align='R', fill=False, ln=1)
        pdf.cell(w=45,h=8,txt='', border=0, align='L', fill=False)
        pdf.cell(w=0,h=8,txt='', border='B', align='R', fill=False, ln=1)
        pdf.cell(w=0,h=22,txt='', border='', align='R', fill=False, ln=1)

        pdf.cell(w=40,h=5,txt='', border='B', align='L', fill=False)
        pdf.cell(w=25,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=40,h=5,txt='', border='B', align='L', fill=False)
        pdf.cell(w=25,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=40,h=5,txt='', border='B', align='L', fill=False, ln=1)
        pdf.cell(w=40,h=5,txt='Gerente de Agencia', border='', align='L', fill=False)
        pdf.cell(w=25,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=40,h=5,txt='Oficial de Créditos', border='', align='L', fill=False)
        pdf.cell(w=25,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=40,h=5,txt='Oficial de Créditos', border='', align='L', fill=False, ln=1)
        pdf.cell(w=40,h=5,txt='Martin Barrillas', border='', align='L', fill=False)
        pdf.cell(w=25,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=40,h=5,txt='Fernando Díaz', border='', align='L', fill=False)
        pdf.cell(w=25,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=40,h=5,txt='Presenta a Cómite', border='', align='L', fill=False, ln=1)

        

        pdf.output('hojaPreAprobacionNatural.pdf', 'F')
        return FileResponse(open('hojaPreAprobacionNatural.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
