from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from EvaluacionMicroApp.models import *


class evaluacionIM(FPDF):
    
    def evaluacionMc(request, id ):
        locale.setlocale(locale.LC_TIME, 'es_ES')
        fecha=date.today()

        ide=int(id)
        try:    
            egm=  Egresosm.objects.get(id=ide)
        except Egresosm.DoesNotExist:
            egm="" 
        try:    
            blm=  Balancesm.objects.get(id=egm.idb.id)
        except Balancesm.DoesNotExist:
            blm="" 

        try:    
            atm=  Activobsm.objects.get(idbs=egm.idb.id)
        except Activobsm.DoesNotExist:
            atm=""
        try:    
            psm=  Pasivobsm.objects.get(idbs=egm.idb.id)
        except Pasivobsm.DoesNotExist:
            psm=""
        try:    
            etm=  Estadorm.objects.get(idb=egm.idb.id)
        except Estadorm.DoesNotExist:
            etm="" 

        try: 
            cliente = Perfil.objects.get(id=egm.idb.idp.id)
        except Perfil.DoesNotExist:
            cliente=""        
        try:    
            igm=  Ingresosm.objects.get(ide=ide)
        except Ingresosm.DoesNotExist:
            igm="" 
        try:    
            cpm=  Capacidadpagom.objects.get(ide=ide)
        except Capacidadpagom.DoesNotExist:
            cpm="" 


        r=59
        g=93
        b=149
        aux=[0, 1, 2, 3]
        aux2=[0, 1, 2]    
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        #pdf.multi_cell(w=0, h=40, txt='', border=1)
        
        pdf.set_font('Arial', 'B', 12)
        #pdf.set_fill_color(r,g,b)
        #pdf.set_text_color(255,255,255)
        pdf.image('TesisApp\static\TesisApp\images\logohabitat.jpg', x=8, y=7, w=45, h=30)#, link=url) 
        pdf.set_font('Arial', 'B', 12)
        pdf.set_y(30)
        pdf.set_left_margin(10)       
        pdf.cell(w=184,h=8,txt='EVALUACIÓN PARA MICROEMPRESARIOS', border=1,  align='C', fill=False, ln=1)
        pdf.cell(w=184,h=4,txt='', border='TB',  align='C', fill=False, ln=1)  
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=184,h=6,txt='Tipo de Negocio: ' + blm.tiponegocio if hasattr(blm, 'tiponegocio') else '', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=184,h=4,txt='', border=1,  align='C', fill=False, ln=1)       
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=20,h=6,txt='Solicitante: ' , border='', align='L', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=164,h=6,txt= (cliente.nombres if hasattr(cliente, 'nombres') else '') +' '+ (cliente.apellidos if hasattr(cliente, 'apellidos') else '') , border='BT', align='L', fill=True, ln=1)
        pdf.cell(w=184,h=4,txt='', border=1, align='L', fill=False, ln=1)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=184,h=5,txt='Balance de Situación', border=1, align='C', fill=True, ln=1)
        pdf.cell(w=55,h=5,txt='Circulante', border=1, align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.tcirculantea) if hasattr(atm, 'tcirculantea') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Circulante', border=1, align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.tcirculantep) if hasattr(psm, 'tcirculantep') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=55,h=5,txt='Caja', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.caja) if hasattr(atm, 'caja') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Proveedores', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.proveedores) if hasattr(psm, 'proveedores') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=55,h=5,txt='Bancos', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.bancos) if hasattr(atm, 'bancos') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Cuentas por Pagar', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.cuentaspp) if hasattr(psm, 'cuentaspp') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=55,h=5,txt='Cuentas por Cobrar', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.cuentaspc) if hasattr(atm, 'cuentaspc') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Préstamos a 1 año', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.prestamoscp) if hasattr(psm, 'prestamoscp') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=55,h=5,txt='Inventarios', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.inventarios) if hasattr(atm, 'inventarios') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=55,h=5,txt='Fijo', border=1, align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.tfijoa) if hasattr(atm, 'tfijoa') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Fijo', border=1, align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.fijop) if hasattr(psm, 'fijop') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=55,h=5,txt='Mobiliario', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.mobiliario) if hasattr(atm, 'mobiliario') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Préstamos a Largo Plazo', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.prestamoslp) if hasattr(psm, 'prestamoslp') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=55,h=5,txt='Terrenos', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.terrenos) if hasattr(atm, 'terrenos') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Total Pasivo', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.totalpasivo) if hasattr(psm, 'totalpasivo') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=55,h=5,txt='Vehículos', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(atm.vehiculos) if hasattr(atm, 'vehiculos') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Patrimonio', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.patrimonio) if hasattr(psm, 'patrimonio') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=55,h=5,txt='', border='LBT', align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border='RBT',  align='R', fill=False)
        pdf.cell(w=79,h=5,txt='Capital', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(psm.capital) if hasattr(psm, 'capital') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=184,h=5,txt='', border=1, align='L', fill=False, ln=1)
        pdf.set_fill_color(191,191,191)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=55,h=5,txt='Total Activo', border='LBT', align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=True)
        pdf.cell(w=20,h=5,txt=str(atm.totalactivo) if hasattr(atm, 'totalactivo') else '0', border='RBT',  align='R', fill=True)
        pdf.cell(w=79,h=5,txt='Pasivo + Patrimpnio', border=1, align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=True)
        pdf.cell(w=20,h=5,txt=str(psm.pasivompatrim) if hasattr(psm, 'pasivompatrim') else '0', border='RBT',  align='R', fill=True)
        pdf.cell(w=0,h=5,txt='', border='L', align='L', fill=False, ln=1)
        pdf.cell(w=184,h=5,txt='', border=1, align='L', fill=False, ln=1)
        
        
        pdf.set_fill_color(191,191,191)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=48,h=6,txt='Estado de Resultados', border=1,  align='C', fill=True)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=136,h=6,txt='Flujo de Caja', border=1,  align='C', fill=True, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=30,h=5,txt='Ventas Totales', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.ventast) if hasattr(etm, 'ventast') else '0', border='RBT',  align='R', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=88,h=5,txt='Egresos', border=1,  align='C', fill=True)
        pdf.cell(w=48,h=5,txt='Ingresos', border=1,  align='C', fill=True, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=30,h=5,txt='Ventas Totales', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.ventast) if hasattr(etm, 'ventast') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='Alimentación del grupo familiar', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.alimentacion) if hasattr(egm, 'alimentacion') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='Negocio', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(igm.negocio) if hasattr(igm, 'negocio') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt='', border='RBT',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='Educación del grupo familiar', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.educacion) if hasattr(egm, 'educacion') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='Remesas', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(igm.remesas) if hasattr(igm, 'remesas') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='Costo de Ventas', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.costovent) if hasattr(etm, 'costovent') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='Transporte', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.transporte) if hasattr(egm, 'transporte') else '0', border='RBT',  align='R', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=30,h=5,txt='Total(2)', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(igm.totali) if hasattr(igm, 'totali') else '0', border='RBT',  align='R', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=30,h=5,txt='Utilidad Bruta', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.utilidadbt) if hasattr(etm, 'utilidadbt') else '0', border='RBT',  align='R', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=70,h=5,txt='Salud / ISSS / ISBM / Otros gastos de salud', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.salud) if hasattr(egm, 'salud') else '0', border='RBT',  align='R', fill=False)
        pdf.set_fill_color(191,191,191)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(w=48,h=5,txt='Análisis de Capacidad de Pago', border=1,  align='C', fill=True)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt='%', border=1,  align='C', fill=False, ln=1)
        #pdf.set_font('Arial', '', 9)
        pdf.cell(w=30,h=5,txt='Gastos Grales.', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.gastosgral) if hasattr(etm, 'gastosgral') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='AFP / IPSFA / IRS / Otros', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.AFP) if hasattr(egm, 'AFP') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=48,h=5,txt='Endeudamiento Actual:', border=1,  align='C', fill=False)
        pdf.set_fill_color(155,187,89)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=0,h=5,txt=str(cpm.porcentajee) if hasattr(cpm, 'porcentajee') else '0.0%', border=1,  align='C', fill=True, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=30,h=5,txt='Transporte', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.transporte) if hasattr(etm, 'transporte') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='Servicios', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.servicios) if hasattr(egm, 'servicios') else '0', border='RBT',  align='R', fill=False)
        pdf.set_fill_color(191,191,191)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=30,h=5,txt='Disponible = 2-1', border=1,  align='C', fill=True)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=18,h=5,txt='', border='LRT',  align='L', fill=False)
        pdf.set_fill_color(155,187,89)
        pdf.cell(w=0,h=5,txt='', border='LRT',  align='L', fill=True, ln=1)
        pdf.cell(w=30,h=5,txt='Servicios', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.servicios) if hasattr(etm, 'servicios') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='Alquiler', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.alquiler) if hasattr(egm, 'alquiler') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='Ingresos - Egresos', border=1,  align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='B',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(cpm.disponible) if hasattr(cpm, 'disponible') else '0', border='RB',  align='R', fill=False)
        pdf.set_fill_color(155,187,89)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=0,h=5,txt=str(cpm.porcentajedis) if hasattr(cpm, 'porcentajedis') else '0', border='LRB',  align='C', fill=True, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=30,h=5,txt='Impuestos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.impuestos) if hasattr(etm, 'impuestos') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=35,h=5,txt='', border='LRT',  align='L', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=35,h=5,txt='En Planilla', border=1,  align='L', fill=True)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.pplanilla) if hasattr(egm, 'pplanilla') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='Cuota', border=1,  align='C', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(cpm.cuota) if hasattr(cpm, 'cuota') else '0', border='RBT',  align='R', fill=False)
        pdf.set_fill_color(155,187,89)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=0,h=5,txt=str(cpm.porcentajecuot) if hasattr(cpm, 'porcentajecuot') else '0', border=1,  align='C', fill=True, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=30,h=5,txt='Alquiler', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.alquiler) if hasattr(etm, 'alquiler') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=35,h=5,txt='Préstamos Actuales', border='LR',  align='C', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=35,h=5,txt='En Ventanilla', border=1,  align='L', fill=True)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.pventanilla) if hasattr(egm, 'pventanilla') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='Superávit', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(cpm.superavit) if hasattr(cpm, 'superavit') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='Cuota Préstamos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.cuotaprest) if hasattr(etm, 'cuotaprest') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=35,h=5,txt='', border='LRB',  align='L', fill=False)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=35,h=5,txt='HPH EL SALVADOR', border=1,  align='L', fill=True)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.phplhes) if hasattr(egm, 'phplhes') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='Deficit', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(cpm.deficit) if hasattr(cpm, 'deficit') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='Imprevistos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.imprevistoser) if hasattr(etm, 'imprevistoser') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='Otros descuentos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.otrosdesc) if hasattr(egm, 'otrosdesc') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='Utilidad Neta', border=1,  align='L', fill=False)
        pdf.set_fill_color(191,191,191)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=True)
        pdf.cell(w=13,h=5,txt=str(etm.utilidadneta) if hasattr(etm, 'utilidadneta') else '0', border='RBT',  align='R', fill=True)
        pdf.cell(w=70,h=5,txt='Recreación', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.recreacion) if hasattr(egm, 'recreacion') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='Mensual', border='',  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(etm.mensual) if hasattr(etm, 'mensual') else '0', border='',  align='R', fill=False)
        pdf.cell(w=70,h=5,txt='Imprevistos', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.imprevistos) if hasattr(egm, 'imprevistos') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)
        pdf.cell(w=30,h=5,txt='', border='',  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='', border='',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt='', border='',  align='R', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=70,h=5,txt='Total(1)', border=1,  align='L', fill=False)
        pdf.cell(w=5,h=5,txt='$', border='LBT',  align='L', fill=False)
        pdf.cell(w=13,h=5,txt=str(egm.total) if hasattr(egm, 'total') else '0', border='RBT',  align='R', fill=False)
        pdf.cell(w=0,h=5,txt='', border='L',  align='L', fill=False, ln=1)

        pdf.cell(w=184,h=20,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=126,h=5,txt='', border='',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='Presentado por: ', border='',  align='L', fill=False)
        pdf.cell(w=0,h=5,txt='', border='B',  align='L', fill=False, ln=1)
        pdf.cell(w=126,h=5,txt='', border='',  align='R', fill=False)
        pdf.cell(w=30,h=5,txt='', border='',  align='L', fill=False)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(w=0,h=5,txt='Nombre del Oficial de Crédito', border='T',  align='L', fill=False, ln=1)


     
        pdf.output('evaluacionIM.pdf', 'F')
        return FileResponse(open('evaluacionIM.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
        #return redirect("listaSolicitud")
