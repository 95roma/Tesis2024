from fpdf import FPDF
from ClienteApp.models import *

from django.http import FileResponse

class Autorizacion(FPDF):
   pass

   def autorizacionI(request, id):

   # idSolicitud=request.POST['idSoli']
    try:
      per=Perfil.objects.get(id=id)
    except:
      per=''
    
    pdf=FPDF(orientation='P', unit='mm', format='Letter')
    pdf.add_page()
    pdf.image('TesisApp\static\TesisApp\images\Equifax_logo.png', x=20, y=10, w=40, h=10)#, link=url)

    pdf.set_font('Arial', 'B', 12)
    #pdf.text(x=40, y=30, txt='AUTORIZACIÓN PARA CONSULTAR Y COMPARTIR INFORMACIÓN.')
    

    pdf.set_font('Arial', 'B', 12)
    pdf.text(x=40, y=30, txt='AUTORIZACIÓN PARA CONSULTAR Y COMPARTIR INFORMACIÓN.')
    pdf.text(x=70, y=35, txt='(Teléfono y Correo Electrónico)')
    pdf.set_font('Arial', '', 11)
    pdf.set_y(50)
    pdf.set_left_margin(20)
    #pdf.add_page
    texto="Yo, " + per.nombres + " " + per.apellidos +", de conformidad a los articulos 14 literal a) y 17 literal h) de la Ley del Historial de Crédito y artículo 16 de las Normas Técnicas para la Autorización, Registro y Funcionamiento de las Agencias de Información de DAtos y los Servicios de Informacion sobre Historial de Crédito de las Personas; " + "SI__ NO__ AUTORIZO Y CONSIENTO para que, ASOCIACIÓN HPH EL SALVADOR. recopile, transmita y comparta mi informacion personal referente a: Número de teléfono y correo electrónico, a la Agencia de Informacion de Datos Equifax, TransUnion y/o Infored con el objeto de recibir notificaciones sobre búsqueda de mi historial crediticio y respuestas ante cualquier solicitud de informacion."
    tex="Consiento además que, en caso de NO brindar mi autorizacion, no recibiré alertas mediante servicios de mensajería instantánea o por correo electrónico cuando el mismo esté siendo revisado por un agente económico, ni recibiré notificaciones relacionadas a los procesos de consulta, quejas o reclamos que realice en los puntos de consulta y/o centro de resolución de quejas."
    pdf.multi_cell(w=175, h=5, txt=texto, border=0, align= 'J', fill=0)
    pdf.ln(5)
    pdf.multi_cell(w=175, h=5, txt=tex, border=0, align= 'J', fill=0)
    pdf.text(x=20, y=150, txt='Firma: ')
    pdf.line(40, 150, 100, 150)
    pdf.text(x=20, y=165, txt='DUI: ')
    pdf.line(40, 165, 100, 165)
    pdf.text(x=20, y=180, txt='Correo electrónico: ')
    pdf.line(60, 180, 120, 180)
    pdf.text(x=20, y=195, txt='Número de teléfono: ')
    pdf.line(60, 195, 120, 195)
    pdf.text(x=20, y=210, txt='Fecha: ')
    pdf.line(40, 210, 100, 210)
    pdf.output('autorizacion.pdf', 'F')
    return FileResponse(open('autorizacion.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
    #return redirect("listaSolicitud")

