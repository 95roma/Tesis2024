from fpdf import FPDF
from ClienteApp.models import *

from django.http import FileResponse

class HistorialC(FPDF):
   pass

   def historialC(request, id):

   # idSolicitud=request.POST['idSoli']
    per=Perfil.objects.get(id=id)
    
    pdf=FPDF(orientation='P', unit='mm', format='Letter')
    pdf.add_page()
    pdf.image('TesisApp\static\TesisApp\images\Equifax_logo.png', x=20, y=10, w=40, h=10)#, link=url)

    pdf.set_font('Arial', 'B', 12)
    #pdf.text(x=40, y=30, txt='AUTORIZACIÓN PARA CONSULTAR Y COMPARTIR INFORMACIÓN.')
    

    pdf.set_font('Arial', 'B', 12)
    pdf.text(x=40, y=30, txt='AUTORIZACIÓN PARA CONSULTAR Y COMPARTIR INFORMACIÓN.')
    pdf.text(x=90, y=35, txt='(Historial Crediticio)')
    pdf.set_font('Arial', '', 11)
    pdf.set_y(50)
    pdf.set_left_margin(20)
    #pdf.add_page
    texto="Yo, "+ per.nombres +" " + per.apellidos +", de conformidad a los articulos 14 literal d) y 15 de la Ley de Regulación de los Servicios de Información sobre el Historial de Crédito de las personas y articulo 18 literal g) de la Ley de Protección al Consumidor, por este medio, "+"SI__ NO__ AUTORIZO Y CONSIENTO para que, ASOCIACIÓN HPH EL SALVADOR recopile, transmita, comparte, acceda, consulte y verifique mi informacion personal y crediticia, para análisis presente y futuros relacionados con la contratación de servicios. Expreso en realación a la autorización y consentimiento consignado en este documento, que tengo pleno conocimiento y, por lo tanto, SI__ NO__ AUTORIZO Y CONSIENTO: a) Que ASOCIACIÓN HPH EL SALVADOR podra acceder, consultar y verificar mi informacion personal y crediticia que estuviere contenida en las bases de datos de Equifax, TransUnion y/o Infored, con las que ASOCIACIÓN HPH EL SALVADOR tuviere acuerdos de carácter comercial y/o contractual; b) Que ASOCIACIÓN HPH EL SALVADOR podra recopiilar, transmitir y compartir mi información personal y crediticia, con Equifax, TransUnion e Infored, a fin de tales datos pasen a formar parte de mi historial crediticio en las bases de datos que al efecto lleva Equifax, TransUnion e Infored; c) Que ASOCIACION HPH EL SALVADOR podra adicionar, modificar y/o actualizar, cualquier informacion personal y crediticia proporcionada por mi persona, incluyendo los de esta solicitud y cualquier otra información que ASOCIACION HPH EL SALVADOR requiera en un futuro tanto de caracter personal como crediticio; y d) Que la presente autorización y consentimiento tendra una vigencia igual al plazo que perdure la relacion contractual entre el suscrito y ASOCIACION HPH EL SALVADOR, o en su defecto que la ley establece para la duracion de las autorizaciones. Conozco y admito que la presente autorizacion no afecta ni afectara en modo alguno las condiciones juridicas y económicas del credito que eventualmente me otorgue ASOCIACION HPH EL SALVADOR"
    pdf.multi_cell(w=175, h=5, txt=texto, border=0, align= 'J', fill=0)
    pdf.text(x=20, y=200, txt='Firma: ')
    pdf.line(40, 200, 100, 200)
    pdf.text(x=20, y=215, txt='DUI: ')
    pdf.line(40, 215, 100, 215)
    pdf.text(x=20, y=230, txt='Fecha: ')
    pdf.line(40, 230, 100, 230)
    pdf.output('historial.pdf', 'F')
    return FileResponse(open('historial.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
    

