from fpdf import FPDF
from datetime import date
import locale
from ClienteApp.models import *

from django.http import FileResponse
from SolicitudesApp.models import *
from django.db.models import Q
from DeclaracionJurClienteApp.models import *



class Declaracion(FPDF):
    
    def declaJur(request,id,idp):

        locale.setlocale(locale.LC_TIME, 'es_ES')
        fecha=date.today()
        
        print(fecha)
        try:
            dj=Declaracionjc.objects.get(iddj=id)
        except Declaracionjc.DoesNotExist:
            dj=''
        idsl=dj.ids.id
        try:
            sol=solicitud.objects.get(id=idsl)
        except solicitud.DoesNotExist: 
            sol=''
        try:
            d=  detalle.objects.get(idSolicitud=idsl)
        except detalle.DoesNotExist:
            d=""

        try:
            per=Perfil.objects.get(id=idp)
        except Perfil.DoesNotExist:
            per=''

        try:
            djnm=  Declaracionjcjnm.objects.get(idjn=id)
        except Declaracionjcjnm.DoesNotExist:
            djnm=""

        try:
            dja=  Declaracionjcaern.objects.get(idae=id)
        except Declaracionjcaern.DoesNotExist:
            dja=""
        

        
        r=0
        g=102
        b=153
        aux=[0, 1, 2, 3]
        aux2=[0, 1, 2]    
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        pdf.set_draw_color(r,g,b)
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=8, y=5, w=40, h=30)#, link=url)

        
        
        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=0, h=30, txt='', border='TRL')
        pdf.text(x=80, y=20, txt='ASOCIACIÓN HPH EL SALVADOR.')
        pdf.text(x=80, y=25, txt='DECLARACIÓN JURADA CLIENTES')
        pdf.set_font('Arial', 'B', 10)
        pdf.set_xy(40,25)
        pdf.multi_cell(w=165,h=5,txt='(Según Acuerdo No.85, Instructivo de la Unidad de Investigacion Financiera para la prevencion de lavado de Dinero y de activos en las instituciones de Intermediación Financiera).', border=0, align='C', fill=False)    
        pdf.set_font('Arial', '', 10)
        pdf.set_y(40)
        pdf.set_left_margin(10)
        pdf.cell(w=10,h=5,txt='Yo:', border='L', align='L', fill=False)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=120,h=5,txt=(per.nombres if hasattr(per, 'nombres') else '') +' '+ (per.apellidos if hasattr(per, 'apellidos') else ''), border='B', align='L', fill=False)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=0,h=5,txt='actuando en mi calidad personal y/o de ', border='R', align='L', fill=False)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=125,h=4,txt='(Nombre de la Persona Natural o Representante Legal)', border='L', align='C', fill=False)
        pdf.multi_cell(w=0,h=4,txt='', border='R', align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=40,h=5,txt='Representante Legal de:', border='L', align='L', fill=False)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=150,h=5,txt='', border='B', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='R', align='L', fill=False)
        pdf.set_text_color(r,g,b)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=180,h=4,txt='(Nombre de la Persona o de la Empresa que Representa)', border='L', align='C', fill=False)
        pdf.multi_cell(w=0,h=4,txt='', border='R', align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border='RL',  align='L', ln=1, fill=0)
        pdf.set_font('Arial', '', 10)
        pdf.set_y(60)
        pdf.set_left_margin(10)
        pdf.set_fill_color(r,g,b)
        pdf.cell(w=0,h=5,txt='', border='RLB',  align='L', ln=1, fill=0)
        pdf.multi_cell(w=110,h=5,txt='DOCUMENTO(S) DE IDENTIFICACION DE PERSONA NATURAL O APODERADO LEGAL', border=1, align='C', fill=False)
        pdf.set_xy(120,65)
        pdf.multi_cell(w=0,h=5,txt='DOCUMENTO(s) DE IDENTIFICACION DE LA PERSONA REPRESENTADA', border=1,  align='C', fill=False)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=30,h=5,txt='Nombre:', border='TL', align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=(per.nombres if hasattr(per, 'nombres') else '') +' '+ (per.apellidos if hasattr(per, 'apellidos') else ''), border='TR', align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=0,h=5,txt='No. NIT:', border='TLR',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=110,h=5,txt='', border='LRB',  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='', border='BLR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=25,h=10,txt='DUI NÚMERO:', border='LTB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=25,h=10,txt=per.dui if hasattr(per, 'dui') else '', border='RTB',  align='L', fill=0)
        #pdf.cell(w=80,h=5,txt='per.apellidos', border=1,  align='L', fill=0)
       
           # pdf.multi_cell(w=0, h=10, border='R')
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=40,h=10,txt='No. de Registro Fiscal:', border='TLB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=10,txt="", border='TRB',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=35,h=5,txt='NIT NÚMERO:', border='TBL',  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='TIPO DE OPERACIÓN:', border='TBL',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=dj.toperacion.nombre if hasattr(dj, 'toperacion') else '', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=20,h=5,txt='Crédito N°', border='TL',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=40,h=5,txt=dj.ncredito if hasattr(dj, 'ncredito') else '', border='TB',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=15,h=5,txt='Monto $', border='T',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=60,h=5,txt=str(d.monto) if hasattr(d, 'monto') else '', border='TB',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=15,h=5,txt='Plazo', border='T',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=30,h=5,txt=dj.plazo if hasattr(dj, 'plazo') else '', border='TB',  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.set_font('Arial', '', 8)
        pdf.multi_cell(w=0,h=5,txt='(Espacio Reservado para Asociacion HPH El Salvador)', border='RL',  align='C', fill=0)
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=0,h=5,border='LR')
        pdf.multi_cell(w=0,h=5,txt='Declaro bajo Juramento que:', border='LR',  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='a) Los fondos que utilizaré para cancelar el crédito, que este día me otorga Asociación HPH El Salvador procedera de:', border='BLR',  align='L', fill=0)
        pdf.multi_cell(w=50,h=5,txt='ACTIVIDAD ECONÓMICA (PARA PERSONA NATURAL)', border='BLT',  align='L', fill=0)
        pdf.set_xy(60, 130)
        pdf.multi_cell(w=50,h=10,border='RTB')
        pdf.set_xy(110, 130)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=0,h=10,txt='GIRO DEL NEGOCIO AL QUE SE DEDICA', border='LTBR',  align='L', fill=0)
      
        pdf.set_text_color(r,g,b)
        pdf.cell(w=25,h=5,txt='-Empleado en:', border='TLB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=75,h=5,txt=dja.empleadoen if hasattr(dja, 'empleadoen') else '', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=25,h=5,txt='-Empresa de: ', border='TLB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt= djnm.empresa if hasattr(djnm, 'empresa') else '', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        #pdf.cell(w=50,h=5,txt='', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='-Profesional Independiente en:', border='TLB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=50,h=5,txt=dja.profecinalind if hasattr(dja, 'profecinalind') else '', border='TBR',  align='L', fill=0)
        #pdf.multi_cell(w=0,h=5,txt='', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=25,h=5,txt='-Industria de:', border='TLB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt= djnm.industriade if hasattr(djnm, 'industriade') else '', border='TBR',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        #pdf.multi_cell(w=0,h=5,txt='', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=30,h=5,txt='-Conocimiento en:', border='LTB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=dja.conocimientoen if hasattr(dja, 'conocimientoen') else '', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=25,h=5,txt='-Comercio de:', border='LTB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt= djnm.comercio if hasattr(djnm, 'comercio') else '', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=30,h=5,txt='-Empresario en:', border='LTB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=dja.empresarioen if hasattr(dja, 'empresarioen') else '', border='RTB',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=35,h=5,txt='-Otros, especifique:', border='LTB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=djnm.especificarot if hasattr(djnm, 'especificarot') else '', border='TBR',  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=35,h=5,txt='-Otros, especifique:', border='LTB',  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=65,h=5,txt=dja.especificaro if hasattr(dja, 'especificaro') else '', border='TBR',  align='L', fill=0)
        pdf.multi_cell(w=0,h=5, border=1)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=0,h=8,txt='b) Este crédito será cancelado de acuerdo a las cuotas y plazos establecidos por Asociacion HPH El Salvador.', border='TRL', align='C', fill=0)
        pdf.cell(w=120,h=8,txt='   c) Tengo proyectado realizar pagos adicionales a las cuotas establecidas ',border='LB', align='C', fill=0)
        if dj.rpagosa =='Si':            
            pdf.cell(w=5,h=8,txt='Si', border='B',  align='C', fill=False)
            pdf.cell(w=5,h=6,txt='X', border='B',  align='C', fill=False )
            pdf.cell(w=5,h=8,txt='No', border='B',  align='C', fill=False)
            pdf.cell(w=5,h=6,txt='', border='B',  align='C', fill=False)      
        else:
            pdf.cell(w=5,h=8,txt='Si', border=0,  align='C', fill=False)
            pdf.cell(w=5,h=6,txt='', border='B',  align='C', fill=False)
            pdf.cell(w=5,h=8,txt='No', border=0,  align='C', fill=False)
            pdf.cell(w=5,h=6,txt='X', border='B',  align='C', fill=False)
        pdf.multi_cell(w=0,h=8,txt=', con fondos procedentes de:',border='RB', align='L', fill=0)
        
        #pdf.cell(w=60,h=5,txt='Nombre', border=1,  align='C', fill=1)
        pdf.multi_cell(w=0,h=10,txt='(Especifique procedencia de fondos de las cuotas adicionales).', border='LTR',  align='C', fill=0)
        pdf.multi_cell(w=0,h=5,txt='La informacion procedente en este instrumento, es veridica y puede ser comprobada en cualquier momento po Asociacion HPH El Salvador. Ademas pueden solicitar otros documentos para la aprobacion de fondos.', border='LR',  align='L', fill=0)
        pdf.cell(w=25,h=5,txt='Lugar y fecha:', border='L',  align='L', fill=0)
        pdf.cell(w=50,h=5, txt='',border='B', align='C', fill=0)
        pdf.cell(w=3,h=5,txt=',',border=0)
        pdf.cell(w=30,h=5,txt='',border='B')
        pdf.cell(w=8,h=5,txt=', de',border=0)
        pdf.cell(w=20,h=5,txt='',border='B')
        pdf.cell(w=8,h=5,txt='de',border=0)
        pdf.cell(w=20,h=5,txt='',border='B')
        pdf.cell(w=1,h=5,txt='',border=0)
        pdf.cell(w=10,h=5,txt='',border='B')
        pdf.multi_cell(w=0,h=5,txt=', sello.', border='R',  align='L', fill=0)
        pdf.multi_cell(w=0,h=8,txt='ESPACIO RESERVADO PARA ASOCIACIÓN HPH EL SALVADOR.', border='BLR',  align='C', fill=0)
        pdf.multi_cell(w=0,h=35,txt='', border='LTR',  align='L', fill=0)
        pdf.set_xy(85, 217)
        #pdf.cell(w=30,h=10,txt='Ventanilla', border=0,  align='L', fill=0)
        #pdf.set_xy(105, 32)
        pdf.cell(w=25,h=28,txt='', border=1,  align='L', fill=0)
        #pdf.set_xy(140, 30)
        pdf.cell(w=10,h=5,txt='', border=0,  align='L', fill=0)
        #pdf.set_xy(150, 32)
        pdf.cell(w=25,h=28,txt='', border=1,  align='L', fill=0)
        
        pdf.set_xy(10, 247)
        pdf.cell(w=25, h=5, txt='Firma Cliente:', border='L', align='L', fill=0)
        pdf.cell(w=40, h=5, txt='', border='B', align='L', fill=0)
        pdf.cell(w=9, h=5, txt='', border=0, align='L', fill=0)
        pdf.cell(w=30, h=5, txt='Pulgar Izquierdo', border=0, align='L', fill=0)
        pdf.cell(w=7, h=5, txt='', border=0, align='L', fill=0)
        pdf.cell(w=30, h=5, txt='Pulgar Derecho', border=0, align='L', fill=0)
        pdf.multi_cell(w=0, h=5, txt='', border='R', align='L', fill=0)
        pdf.multi_cell(w=0, h=7, txt='SE FIRMA ÚNICAMENTE EN PRESENCIA DE UN FUNCIONARIO DE LA ASOCIACIÓN.', border='LBR', align='C', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.set_text_color(0,0,0)
        
        pdf.output('declaracionJur.pdf', 'F')
        return FileResponse(open('declaracionJur.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
