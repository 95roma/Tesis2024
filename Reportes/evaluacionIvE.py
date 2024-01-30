from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from EvaluacionIvEFApp.models import *


class evaluacionIvEF(FPDF):
    
    def evaluacionIvE(request, id ):
        locale.setlocale(locale.LC_TIME, 'es_ES')
        fecha=date.today()

        ide=int(id)
        try:    
            egf=  Egresosf.objects.get(id=ide)
        except Egresosf.DoesNotExist:
            egf="" 
        try: 
            cliente = Perfil.objects.get(id=egf.idp.id)
        except Perfil.DoesNotExist:
            cliente=""        
        try:    
            igf=  Ingresosf.objects.get(ide=ide)
        except Ingresosf.DoesNotExist:
            igf="" 
        try:    
            cpf=  Capacidadpagof.objects.get(ide=ide)
        except Capacidadpagof.DoesNotExist:
            cpf="" 
        try:
            bns=Bienesh.objects.filter(ide=ide)
        except bns.DoesNotExist:
            bns=""

        r=59
        g=93
        b=149
        aux=[0, 1, 2, 3, 4]
        aux2=[0, 1, 2]    
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        #pdf.multi_cell(w=0, h=40, txt='', border=1)
        
        pdf.set_font('Arial', 'B', 12)
        #pdf.set_fill_color(r,g,b)
        #pdf.set_text_color(255,255,255)
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=8, y=7, w=45, h=30)#, link=url) 
        pdf.set_font('Arial', 'B', 12)
        pdf.set_y(30)
        pdf.set_left_margin(10)       
        pdf.cell(w=142,h=8,txt='EVALUACIÓN PERSONAL', border=1,  align='C', fill=False, ln=1)
        pdf.cell(w=142,h=6,txt='', border='T',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=20,h=6,txt='Solicitante: ' , border='', align='L', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=122,h=6,txt= (cliente.nombres if hasattr(cliente, 'nombres') else '') +' '+ (cliente.apellidos if hasattr(cliente, 'apellidos') else '') , border='', align='L', fill=True, ln=1)
        pdf.cell(w=0,h=5,txt='', border='', align='L', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='Descripción de los bienes del hogar encontrados en la vivienda', border='', align='L', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='', align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='No.', border=1, align='C', fill=False)
        pdf.cell(w=50,h=5,txt='Descripcioón del bien', border=1, align='C', fill=False)
        pdf.cell(w=32,h=5,txt='Precio de Compra', border=1, align='C', fill=False)
        pdf.cell(w=30,h=5,txt='Cuota mensual', border=1, align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)

        if bns!='' and len(bns)>0:
            for i in bns:
                pdf.cell(w=30,h=5,txt=i.numero, border=1, align='L', fill=False)
                pdf.cell(w=50,h=5,txt=i.descripcionbien, border=1, align='L', fill=False)
                pdf.cell(w=32,h=5,txt='$ '+str(i.preciocompra), border=1, align='R', fill=False)
                pdf.cell(w=30,h=5,txt='$ '+str(i.cuotamensual), border=1, align='R', fill=False)
                pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        else:
            
            for i in aux:
                pdf.cell(w=30,h=5,txt='', border=1, align='L', fill=False)
                pdf.cell(w=50,h=5,txt='', border=1, align='L', fill=False)
                pdf.cell(w=32,h=5,txt='', border=1, align='L', fill=False)
                pdf.cell(w=30,h=5,txt='', border=1, align='L', fill=False)
                pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)

               
        pdf.cell(w=170,h=10,txt='', border='B',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=170,h=6,txt='EVALUACIÓN DE INGRESOS VRS. EGRESOS FAMILIARES', border=1,  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=170,h=5,txt='', border='TB',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.set_fill_color(191,191,191)
        pdf.cell(w=170,h=6,txt='Flujo de Caja', border=1,  align='C', fill=True, ln=1)
        pdf.cell(w=105,h=6,txt='Egresos', border=1,  align='C', fill=True)
        pdf.cell(w=65,h=6,txt='Ingresos', border=1,  align='C', fill=True)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=6,txt='', border='L',  align='C', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='Alimentación del grupo familiar', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.alimentacion) if hasattr(egf, 'alimentacion') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=40,h=5,txt='Familiar', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(igf.familiar) if hasattr(igf, 'familiar') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='Educación del grupo familiar', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.educacion) if hasattr(egf, 'educacion') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=40,h=5,txt='Otros ingresos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(igf.otrosingres)if hasattr(igf, 'otrosingres') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='Transporte', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.transporte) if hasattr(egf, 'transporte') else '0', border='RBT',  align='R', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=5,txt='Total(2)', border=1,  align='L', fill=False)      
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(igf.totali) if hasattr(igf, 'totali') else '0', border='RBT',  align='R', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='Salud / ISSS / ISBM / Otros gastos de salud', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.salud) if hasattr(egf, 'salud') else '0', border='RBT',  align='R', fill=False)
        pdf.set_fill_color(191,191,191)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=5,txt='Análisis de Capacidad de Pago', border=1,  align='C', fill=True)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt='Porcentajes', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='AFP / IPSFA / IRS / Otros', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.AFP) if hasattr(egf, 'AFP') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=65,h=5,txt='Endeudamiento Actual:', border=1,  align='C', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=0,h=5,txt=str(cpf.porcentajee) if hasattr(cpf, 'porcentajee') else '0.0%', border=1,  align='C', fill=True, ln=1)
        pdf.cell(w=80,h=5,txt='Servicios', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.servicios) if hasattr(egf, 'servicios') else '0', border='RBT',  align='R', fill=False)
        pdf.set_fill_color(191,191,191)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=5,txt='Disponible = 2-1', border=1,  align='C', fill=True)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=25,h=5,txt='', border='LRT',  align='L', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=0,h=5,txt='', border='LRT',  align='L', fill=True, ln=1)
        pdf.cell(w=80,h=5,txt='Alquiler', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.alquiler) if hasattr(egf, 'alquiler') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=40,h=5,txt='Ingresos - Egresos', border=1,  align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='B',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(cpf.disponible) if hasattr(cpf, 'disponible') else '0', border='RB',  align='R', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=0,h=5,txt=str(cpf.porcentajedis) if hasattr(cpf, 'porcentajedis') else '0', border='LRB',  align='C', fill=True, ln=1)
        pdf.cell(w=35,h=5,txt='', border='LRT',  align='L', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=45,h=5,txt='En Planilla', border=1,  align='L', fill=True)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=True)
        pdf.cell(w=20,h=5,txt=str(egf.pplanilla) if hasattr(egf, 'pplanilla') else '0', border='RBT',  align='R', fill=True)
        pdf.cell(w=40,h=5,txt='Cuota', border=1,  align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(cpf.cuota) if hasattr(cpf, 'cuota') else '0', border='RBT',  align='R', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=0,h=5,txt=str(cpf.porcentajecuot) if hasattr(cpf, 'porcentajecuot') else '0', border=1,  align='C', fill=True, ln=1)
        pdf.cell(w=35,h=5,txt='Préstamos Actuales', border='LR',  align='C', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=45,h=5,txt='En Ventanilla', border=1,  align='L', fill=True)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=True)
        pdf.cell(w=20,h=5,txt=str(egf.pventanilla) if hasattr(egf, 'pventanilla') else '0', border='RBT',  align='R', fill=True)
        pdf.cell(w=40,h=5,txt='Superávit', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(cpf.superavit) if hasattr(cpf, 'superavit') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=35,h=5,txt='', border='LRB',  align='L', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=45,h=5,txt='HPH EL SALVADOR', border=1,  align='L', fill=True)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=True)
        pdf.cell(w=20,h=5,txt=str(egf.phplhes) if hasattr(egf, 'phplhes') else '0', border='RBT',  align='R', fill=True)
        pdf.cell(w=40,h=5,txt='Deficit', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(cpf.deficit) if hasattr(cpf, 'deficit') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='Otros descuentos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.otrosdesc) if hasattr(egf, 'otrosdesc') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='Recreación', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.recreacion) if hasattr(egf, 'recreacion') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='Imprevistos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.imprevistos) if hasattr(egf, 'imprevistos') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=80,h=5,txt='Total(1)', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(egf.total) if hasattr(egf, 'total') else '0', border='RBT',  align='R', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='', align='L', fill=False, ln=1)

        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=80,h=7,txt='Crédito presentado por:', border='',  align='L', fill=False)
        pdf.cell(w=60,h=7,txt='', border='B',  align='L', fill=False)
        pdf.cell(w=0,h=7,txt='', border='',  align='L', fill=False, ln=1)
        pdf.cell(w=80,h=7,txt='Cargo:', border='',  align='L', fill=False)
        pdf.cell(w=60,h=7,txt='', border='B',  align='L', fill=False)
        pdf.cell(w=0,h=7,txt='', border='',  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=25,txt='', border='', align='L', fill=False, ln=1)
        pdf.cell(w=80,h=7,txt='Firma:', border='',  align='L', fill=False)
        pdf.cell(w=60,h=7,txt='', border='B',  align='L', fill=False)
        pdf.cell(w=0,h=7,txt='', border='',  align='L', fill=False, ln=1)
  
     
        pdf.output('evaluacionIvEF.pdf', 'F')
        return FileResponse(open('evaluacionIvEF.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

