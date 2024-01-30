from fpdf import FPDF
from datetime import date
import locale
from ConozcaClienteApp.models import Clientedg
from HistorialApp.models import RegHis
from django.http import FileResponse
from SolicitudesApp.models import *
from EvaluacionIvEFApp.models import *
from SolicitudInscripcionSApp.models import *


class formularioCN(FPDF):
    
    def formComiteN(request, id ):

        try:
            s=  solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s=""
        try:    
            cdg=  Clientedg.objects.get(ids=s.id)
        except Clientedg.DoesNotExist:
            cdg="" 
        try:
            d=  domicilio.objects.get(idSolicitud=id, tipo="Solicitante")
        except domicilio.DoesNotExist:
            d=""
        try:
            df=  domicilio.objects.get(idSolicitud=id, tipo="codeudor")
        except domicilio.DoesNotExist:
            df=""
            
        try:
            dpf=  DatosPersonalesF.objects.get(idSolicitud=id)
        except DatosPersonalesF.DoesNotExist:
            dpf=""
        try:
            do=  datosObra.objects.get(idSolicitud=id)
        except datosObra.DoesNotExist:
            do=""
        try:
            dt=  detalle.objects.get(idSolicitud=id)
        except detalle.DoesNotExist:
            dt=""
        try:
            rh=  RegHis.objects.get(idsolicitud=s.id)
        except RegHis.DoesNotExist:
            rh=""
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
            ssd=  Solicitudisdadf.objects.get(idsis=ss.id)
        except Solicitudisdadf.DoesNotExist:
            ssd=""
                  
        # para calcular el plazo en meses          
        try:
            varp=(int(ss.plazo) *12)
        except :
            varp=""

        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()      

        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=0,h=5,txt='ASOCIACIÓN HPH EL SALVADOR ', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(w=0,h=5,txt='Formulario de Comite de Crédito', border='',  align='C', fill=False, ln=1)
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=9, y=6, w=55, h=20)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        
        pdf.cell(w=98,h=5,txt='     Datos del Solicitante:', border=0, align='L', fill=False)
        pdf.cell(w=98,h=5,txt='     Datos Actividad Economica Solicitante', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=38,h=6,txt='Codigo de Cliente:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=cdg.codigo if hasattr(cdg, 'codigo') else '', border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Sector Productivo:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt='', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=38,h=6,txt='Nombre del Cliente:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=(s.perfil.nombres if hasattr(s.perfil, 'nombres') else '') +' '+ (s.perfil.apellidos if hasattr(s.perfil, 'apellidos') else ''), border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Dirección Actividad', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=d.direccionTrabMicro if hasattr(d, 'direccionTrabMicro') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=38,h=6,txt='Dirección:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=d.direccion if hasattr(d, 'direccion') else '', border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Teléfono:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=d.telefonoTrabMicro if hasattr(d, 'telefonoTrabMicro') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=38,h=6,txt='Teléfono:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=s.perfil.telefono if hasattr(s, 'perfil') else '', border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Tiempo de Servicio:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=d.tiempEmptiempFun if hasattr(d, 'tiempEmptiempFun') else '', border=0, align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=98,h=5,txt='     Datos del Codeudor:', border=0, align='L', fill=False)
        pdf.cell(w=98,h=5,txt='     Datos Actividad Economica Codeudor', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=38,h=6,txt='Codigo de Codeudor:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt='', border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Sector Productivo:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt='', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=38,h=6,txt='Nombre del Codeudor:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=(dpf.nombrefia if hasattr(dpf, 'nombrefia') else '' ) +' '+ (dpf.apellidofia if hasattr(dpf, 'apellidofia') else '' ) , border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Dirección Actividad', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=df.direccionTrabMicro if hasattr(df, 'direccionTrabMicro') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=38,h=6,txt='Dirección:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=df.direccion  if hasattr(df, 'direccion') else '', border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Teléfono:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=df.telefonoTrabMicro if hasattr(df, 'telefonoTrabMicro') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=38,h=6,txt='Teléfono:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=df.telefono if hasattr(df, 'telefono') else '', border=0, align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Tiempo de Servicio:', border=0, align='L', fill=False)
        pdf.cell(w=60,h=6,txt=df.tiempEmptiempFun if hasattr(df, 'tiempEmptiempFun') else '', border=0, align='L', fill=False, ln=1)

        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(w=0,h=5,txt='CREDITO SOLICITADO ', border='',  align='C', fill=False, ln=1)   
        pdf.cell(w=0,h=2,txt='', border=0, align='C', fill=False, ln=1)   
        pdf.cell(w=98,h=6,txt='Cuenta Número:', border=0, align='R', fill=False)
        pdf.cell(w=98,h=6,txt='', border=0, align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 8)

        pdf.cell(w=0,h=3,txt='', border=0, align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='Linea de Financiamiento:', border=0, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=7,h=3,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'CONSTRUCCION VIVIENDA IN SITU' else '', border=1, align='C', fill=False)
        pdf.cell(w=30,h=5,txt='Const. Vivienda', border='', align='C', fill=False)
        pdf.cell(w=7,h=3,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'MEJORAMIENTO' else '', border=1, align='C', fill=False)
        pdf.cell(w=30,h=5,txt='Mejoramiento', border='', align='C', fill=False)
        pdf.cell(w=7,h=3,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'VIVIENDA USADA' else '', border=1, align='C', fill=False)
        pdf.cell(w=20,h=5,txt='V. Usada', border='', align='C', fill=False)
        pdf.cell(w=7,h=3,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'VIVIENDA NUEVA' else '', border=1, align='C', fill=False)
        pdf.cell(w=20,h=5,txt='V. Nueva', border='', align='C', fill=False, ln=1)
        pdf.cell(w=0,h=3,txt='', border=0, align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=7,h=3,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'LOTE MAS VIVIENDA' else '', border=1, align='C', fill=False)
        pdf.cell(w=30,h=5,txt='Lote + Vivienda', border='', align='C', fill=False)
        pdf.cell(w=7,h=3,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'CORPORATIVO' else '', border=1, align='C', fill=False)
        pdf.cell(w=30,h=5,txt='Coorporativo', border='', align='C', fill=False)
        pdf.cell(w=7,h=3,txt='X' if hasattr(do.destino, 'alternativa') and do.destino.alternativa == 'PROYECTO ESPECIAL' else '', border=1, align='C', fill=False)
        pdf.cell(w=35,h=5,txt='Proyecto Especial', border='', align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border='', align='C', fill=False, ln=1)

        pdf.cell(w=0,h=5,txt='', border=0, align='C', fill=False, ln=1)
        pdf.cell(w=32,h=6,txt='', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Monto', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Cuota', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Plazo (Meses)', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Forma de Pago:', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='No Cuotas', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=32,h=6,txt='Solicitado:', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt=str(dt.monto) if hasattr(dt, 'monto') else '', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='0', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='0 ', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='0', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='0', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=32,h=6,txt='Sugerido:', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt=str(do.presupuesto) if hasattr(do, 'presupuesto') else '', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt=str(ca.cuota) if hasattr(ca, 'cuota') else '', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt=str(varp) if hasattr(ss, 'plazo') else '', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Mensual', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt=str(varp) if hasattr(ss, 'plazo') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=32,h=6,txt='Prima:', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='0', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Analista', border=0, align='L', fill=False)
        pdf.cell(w=0,h=6,txt='  ', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=32,h=6,txt='Subsidio:', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='0', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Puntuación Dicom', border=0, align='L', fill=False)
        pdf.cell(w=64,h=6,txt= str(rh.puntaje) if hasattr(rh, 'puntaje') else '', border='B', align='L', fill=False)
        pdf.cell(w=0,h=6,txt='', border=0, align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 8)                    
        pdf.cell(w=64,h=7,txt='Destino del Financiamiento:', border=0, align='L', fill=False)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=64,h=6,txt=do.destino.alternativa if hasattr(do, 'destino') else '', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=32,h=6,txt='Garantía:', border=0, align='L', fill=False)
        pdf.cell(w=64,h=6,txt=ss.garantia if hasattr(ss, 'garantia') else '', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='', border=0, align='L', fill=False)
        pdf.cell(w=32,h=6,txt='Tasa de Interes:', border=0, align='R', fill=False)
        pdf.cell(w=32,h=6,txt=(str(do.destino.interes.interes) if hasattr(do, 'destino') else '') +'%', border=0, align='L', fill=False, ln=1)
        pdf.cell(w=64,h=6,txt='Nombre de Línea de Financiamiento:', border=0, align='L', fill=False)
        pdf.cell(w=64,h=6,txt=str(do.destino.alternativa) +" "+ (str(do.destino.interes.interes)) + '%', border=0, align='L', fill=False, ln=1)

        pdf.set_font('Arial', 'B', 8)
        pdf.cell(w=0,h=5,txt='CHEQUEO DE RELACIONES INTERNAS ', border='',  align='C', fill=False, ln=1)   
        pdf.cell(w=0,h=7,txt='', border=0, align='C', fill=False, ln=1)  

        pdf.cell(w=0,h=5,txt='RESOLUCION DEL COMITE DE CREDITO ', border='',  align='C', fill=False, ln=1)   
        pdf.cell(w=0,h=3,txt='', border=0, align='C', fill=False, ln=1)  
        pdf.cell(w=35,h=5,txt='', border=0, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=7,h=3,txt='', border=1, align='C', fill=False)
        pdf.cell(w=45,h=5,txt='    Aprobado', border='', align='L', fill=False)
        pdf.cell(w=7,h=3,txt='', border=1, align='C', fill=False)
        pdf.cell(w=45,h=5,txt='    Denegado', border='', align='L', fill=False)
        pdf.cell(w=7,h=3,txt='', border=1, align='C', fill=False)
        pdf.cell(w=45,h=5,txt='    Observado', border='', align='L', fill=False, ln=1 )
        pdf.set_font('Arial', '', 8)

        pdf.cell(w=0,h=3,txt='', border='', align='C', fill=False, ln=1 )
        pdf.cell(w=28,h=6,txt='Monto Aprob. $:', border=0, align='L', fill=False)
        pdf.cell(w=27,h=6,txt='', border='B', align='L', fill=False)
        pdf.cell(w=12,h=6,txt='Plazo:', border=0, align='L', fill=False)
        pdf.cell(w=12,h=6,txt='', border='B', align='L', fill=False)
        pdf.cell(w=20,h=6,txt='Nro. Cuota:', border=0, align='L', fill=False)
        pdf.cell(w=12,h=6,txt='', border='B', align='L', fill=False)
        pdf.cell(w=27,h=6,txt='Forma de Pago:', border=0, align='L', fill=False)
        pdf.cell(w=15,h=6,txt='', border='B', align='L', fill=False)
        pdf.cell(w=25,h=6,txt='Tasa Inflación:', border=0, align='L', fill=False)
        pdf.cell(w=0,h=6,txt='', border='B', align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='', align='L', fill=False, ln=1)
        pdf.cell(w=42,h=6,txt='Aplica a Seguro de Desempleo:', border=0, align='L', fill=False)
        pdf.cell(w=8,h=6,txt=ssd.segurodd if hasattr(ssd, 'segurodd') else '', border='B', align='L', fill=False)
        pdf.cell(w=0,h=6,txt='', border='', align='L', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='', align='C', fill=False, ln=1 )
        pdf.cell(w=38,h=6,txt='Fecha del Cómite:', border=0, align='L', fill=False)
        pdf.cell(w=35,h=7,txt='', border='B', align='L', fill=False)
        pdf.cell(w=38,h=6,txt='Fuente de Fondos.', border=0, align='C', fill=False)
        pdf.cell(w=35,h=6,txt='F..', border=0, align='L', fill=False)
        pdf.cell(w=0,h=6,txt='', border=0, align='L', fill=False, ln=1)

        pdf.cell(w=38,h=6,txt='Observaciones:', border=0, align='L', fill=False)
        pdf.cell(w=0,h=6,txt='', border='B', align='R', fill=False, ln=1)
        pdf.cell(w=38,h=6,txt='', border=0, align='L', fill=False)
        pdf.cell(w=0,h=6,txt='', border='B', align='R', fill=False, ln=1)
        pdf.cell(w=0,h=6,txt='', border='', align='R', fill=False, ln=1)

        pdf.cell(w=35,h=5,txt='', border='B', align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='', border='B', align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='', border='B', align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='', border='B', align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='', border='B', align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=35,h=5,txt='Gerente de Créditos', border='', align='C', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='Gerencia de Operaciones', border='', align='C', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='Gerencia de Admón. y finanzas', border='', align='C', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='Supervisor de Construcción', border='', align='C', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='R', fill=False)
        pdf.cell(w=35,h=5,txt='Superv. de Créditos', border='', align='C', fill=False, ln=1)



        pdf.output('formularioComiteNatural.pdf', 'F')
        return FileResponse(open('formularioComiteNatural.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
