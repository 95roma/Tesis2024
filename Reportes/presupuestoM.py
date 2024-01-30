from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from PresupuestoApp.models import *


class presupuestoMj(FPDF):
    
    def presupuestoM(request, id ):

        try:
            presupuesto_datos_generales = Presupuestodg.objects.get(id=id)
        except Presupuestodg.DoesNotExist:
            presupuesto_datos_generales = ""

        try:
            pre = Presupuesto.objects.get(idp=presupuesto_datos_generales.id)
        except:
            pre = ""

        try:
            s = solicitud.objects.get(id=presupuesto_datos_generales.ids.id)
        except solicitud.DoesNotExist:
            s = ""
        try:
            do = datosObra.objects.get(
                idSolicitud=presupuesto_datos_generales.ids.id)
        except datosObra.DoesNotExist:
            do = ""
        try:
            listam = Materiales.objects.filter(estado="activo")
        except Materiales.DoesNotExist:
            listam = ""

        try:
            lista_materiales = PresupuestoMateriales.objects.filter(
                idp=presupuesto_datos_generales.id)
            datos_materiales = []
            for item in lista_materiales:
                datos_materiales.append({'id': item.id, 'precio': item.preciouni, 'cantida': item.cantidad, 'total': item.subtotal,
                            "nombre": item.idm.nombre, "descripcion": item.idm.descripcion, "unidad": item.idm.unidad, "idm": item.idm.id})
         
        except PresupuestoMateriales.DoesNotExist:
            None

        try:
            lista_mano_obra = PresupuestoManoObra.objects.filter(
                idp=presupuesto_datos_generales.id)
            datos_mano_obra = []
            for item in lista_mano_obra:
                datos_mano_obra.append({
                    "id": item.id,
                    "descripcion": item.descripcion,
                    "unidad": item.unidad,
                    "preciouni": item.preciouni,
                    "cantidad": item.cantidad,
                    "total": item.subtotal,
                })
        except PresupuestoManoObra.DoesNotExist:
            lista_mano_obra = ""
  

        try:
            lista_otros = PresupuestoOtros.objects.filter(
                idp=presupuesto_datos_generales.id)
            datos_otros = []
            for item in lista_otros:
                datos_otros.append({
                    "id": item.id,
                    "descripcion": item.descripcion,
                    "unidad": item.unidad,
                    "preciouni": item.preciouni,
                    "cantidad": item.cantidad,
                    "total": item.subtotal,
                })
        except PresupuestoOtros.DoesNotExist:
            lista_otros = ""


        

        r=59
        g=93
        b=149
        aux=[0, 1, 2, 3]
        aux2=[0, 1, 2]    
        totalmt=0
        totalmo=0
        totalot=0
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        
        pdf.image('TesisApp\static\TesisApp\images\logohabitat.jpg', x=20, y=4, w=40, h=25)    
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=9,txt='', border=0, align='C', fill=False)
        pdf.cell(w=0,h=9,txt=' PRESUPUESTO DE MEJORAMIENTO DE VIVIENDA', border=1,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=7,txt='', border='',  align='C', fill=False, ln=1)

        pdf.set_font('Arial', '', 10)
        pdf.set_fill_color(166,166,166)
        pdf.cell(w=65,h=6,txt='Nombre del Cliente:', border=1, align='C', fill=True)
        pdf.cell(w=55,h=6,txt='Municipio del mejoramiento:', border=1, align='C', fill=True)
        pdf.cell(w=20,h=6,txt='Agencia:', border=1, align='C', fill=True)
        pdf.cell(w=0,h=6,txt=s.perfil.Agencia.nombre, border=1 if hasattr(s, 'perfil') else '', align='C', fill=False, ln=1)
        pdf.cell(w=65,h=5,txt=(s.perfil.nombres if hasattr(s.perfil, 'nombres') else '') +' '+ (s.perfil.apellidos if hasattr(s.perfil, 'apellidos') else ''), border=1,  align='C', fill=False)
        pdf.cell(w=55,h=5,txt=s.perfil.municipio.distri if hasattr(s, 'perfil') else '', border=1, align='C', fill=False)
        pdf.cell(w=20,h=5,txt='Fecha', border=1, align='C', fill=True)
        x=pdf.get_x()
        pdf.cell(w=0,h=5,txt=presupuesto_datos_generales.fecha.strftime("%d/%m/%Y") if hasattr(presupuesto_datos_generales, 'fecha') else '', border=1, align='C', fill=False, ln=1)
        pdf.cell(w=65,h=10,txt='Dirección del proyecto:', border=1, align='C', fill=True)
        #pdf.set_font('Arial', '', 10)
        y=pdf.get_y()
        pdf.multi_cell(w=75,h=5,txt=str(do.direExacta) if hasattr(do, 'DireExacta') else '', border='TLR',  align='C', fill=False)
        pdf.set_xy(x, y)
        pdf.multi_cell(w=0,h=5,txt='Dias estimados para la construcción de la obra:', border=1, align='C', fill=True)
        pdf.cell(w=65,h=6,txt='Mejora a realizar:', border=1, align='C', fill=True)
        pdf.cell(w=75,h=6,txt=presupuesto_datos_generales.mejorarea if hasattr(presupuesto_datos_generales, 'mejorarea') else '' , border=1,  align='C', fill=False)
        pdf.cell(w=0,h=6,txt=presupuesto_datos_generales.diasestimadosc if hasattr(presupuesto_datos_generales, 'diasestimadosc') else '', border=1, align='C', fill=False, ln=1)
        pdf.cell(w=0,h=2,txt='', border='',  align='C', fill=False, ln=1)

        pdf.set_font('Arial', '', 7)
        pdf.cell(w=5,h=10,txt='N°', border=1, align='C', fill=False)
        pdf.cell(w=81,h=10,txt='DESCRIPCION', border=1, align='C', fill=False)
        pdf.cell(w=19,h=10,txt='UNIDAD', border=1,  align='C', fill=False)
        x=pdf.get_x()
        
        pdf.multi_cell(w=0,h=5,txt='PRESUPUESTO', border=1,  align='C', fill=False)
        y=pdf.get_y()
        pdf.set_xy(x, y)
        pdf.cell(w=20,h=5,txt='P.U.', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='CANT', border=1,  align='C', fill=False)
        pdf.multi_cell(w=0,h=5,txt='SUBTOTAL', border=1,  align='C', fill=False)
        
        #### Tabla de materiales
        pdf.cell(w=5,h=5,txt='1.0', border=1, align='C', fill=True)
        pdf.cell(w=81,h=5,txt='MATERIALES', border=1, align='L', fill=True)
        pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=True, ln=1)
         
        if datos_materiales !='' and len(datos_materiales):
            for mat in datos_materiales:
                nmat = mat["nombre"]
                umat = mat["unidad"]
                pumat = mat["precio"]
                cmat = mat["cantida"]
                stmat = mat["total"]
                totalmt=totalmt +stmat
                pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt=nmat, border=1, align='L', fill=False)
                pdf.cell(w=19,h=5,txt=umat, border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='$  '+str(pumat) or '', border=1,  align='R', fill=False)
                pdf.cell(w=15,h=5,txt='$  '+str(cmat) or '', border=1,  align='R', fill=False)
                pdf.cell(w=0,h=5,txt='$  '+str(stmat) or '', border=1,  align='R', fill=False, ln=1)
               
        else:
            
            for i in aux:
                pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)

        pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=135,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)

        pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=False)
        pdf.set_font('Arial', 'B', 5)
        pdf.cell(w=35,h=5,txt='SUB-TOTAL MATERIALES', border=1,  align='C', fill=False)
        pdf.set_font('Arial', '', 7)
        pdf.cell(w=0,h=5,txt='$  '+str(totalmt) or '', border=1,  align='R', fill=False, ln=1)

        #### Tabla de mano de obra
        pdf.cell(w=5,h=5,txt='2.0', border=1, align='C', fill=True)
        pdf.cell(w=81,h=5,txt='MANO DE OBRA', border=1, align='L', fill=True)
        pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=True, ln=1)
         
        if datos_mano_obra !='' and len(datos_mano_obra):
            for mo in datos_mano_obra:
                dmo = mo["descripcion"]
                umo = mo["unidad"] 
                pumo = mo["preciouni"] 
                cmo = mo["cantidad"]
                stmo = mo["total"]
                totalmo=totalmo +stmo
                pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt=dmo, border=1, align='L', fill=False)
                pdf.cell(w=19,h=5,txt=umo, border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='$  '+str(pumo) or '', border=1,  align='R', fill=False)
                pdf.cell(w=15,h=5,txt='$  '+str(cmo) or '', border=1,  align='R', fill=False)
                pdf.cell(w=0,h=5,txt='$  '+str(stmo) or '', border=1,  align='R', fill=False, ln=1)
               
        else:
            
            for i in aux:
                pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)

        pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=135,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)

        pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=False)
        pdf.set_font('Arial', 'B', 5)
        pdf.cell(w=35,h=5,txt='SUB-TOTAL MANO DE OBRA', border=1,  align='C', fill=False)
        pdf.set_font('Arial', '', 7)
        pdf.cell(w=0,h=5,txt='$  '+str(totalmo) or '', border=1,  align='R', fill=False, ln=1)

        #### Tabla de mano de obra
        pdf.cell(w=5,h=5,txt='2.0', border=1, align='C', fill=True)
        pdf.cell(w=81,h=5,txt='MANO DE OBRA', border=1, align='L', fill=True)
        pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=True, ln=1)
         
        if datos_otros !='' and len(datos_otros):
            for ot in datos_otros:
                dot = ot["descripcion"]
                uot = ot["unidad"] 
                puot = ot["preciouni"] 
                cot = ot["cantidad"]
                stot = ot["total"]
                totalot=totalot +stot
                pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt=dot, border=1, align='L', fill=False)
                pdf.cell(w=19,h=5,txt=uot, border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='$  '+str(puot) or '', border=1,  align='R', fill=False)
                pdf.cell(w=15,h=5,txt='$  '+str(cot) or '', border=1,  align='R', fill=False)
                pdf.cell(w=0,h=5,txt='$  '+str(stot) or '', border=1,  align='R', fill=False, ln=1)
               
        else:
            
            for i in aux:
                pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)

        pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=135,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)

        pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=19,h=5,txt='', border=1,  align='C', fill=False)
        pdf.set_font('Arial', 'B', 5)
        pdf.cell(w=35,h=5,txt='SUB-TOTAL OTROS', border=1,  align='C', fill=False)
        pdf.set_font('Arial', '', 7)
        pdf.cell(w=0,h=5,txt='$  '+str(totalot) or '', border=1,  align='R', fill=False, ln=1)
        
        pdf.multi_cell(w=0,h=5,txt='NOTAS:', border=0,  align='L', fill=False)
        y=pdf.get_y()
        pdf.multi_cell(w=80,h=5,txt=pre.notas if hasattr(pre, 'notas') else '', border=0,  align='L', fill=False)
        x=pdf.get_x()
        pdf.set_font('Arial', '', 5.5)
        pdf.set_xy(95, y)
        pdf.set_x(95)
        pdf.cell(w=54,h=5,txt='SUB-TOTAL', border=1,  align='C', fill=False)
        pdf.multi_cell(w=56,h=5,txt='$  '+str(pre.subtotal) if hasattr(pre, 'subtotal') else '', border=1,  align='R', fill=False)
        pdf.set_x(95)
        pdf.cell(w=39,h=5,txt='ASISTENCIA TECNICA CONSTRUCTIVA', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.multi_cell(w=56,h=5,txt='$  '+str(pre.asistenciatecn) if hasattr(pre, 'asistenciatecn') else '', border=1,  align='C', fill=False)
        pdf.set_x(95)
        pdf.cell(w=39,h=5,txt='COMISIÓN POR OTORGAMIENTO', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.multi_cell(w=56,h=5,txt='$  '+str(pre.comisionporot) if hasattr(pre, 'comisionporot') else '', border=1,  align='C', fill=False)
        pdf.set_x(95)
        pdf.cell(w=54,h=5,txt='CONSULTA BURÓ DE CREDITOS', border=1,  align='C', fill=False)
        pdf.multi_cell(w=56,h=5,txt='$  '+str(pre.consultabcredoto) if hasattr(pre, 'consultabcredoto') else '', border=1,  align='C', fill=False)
        pdf.set_x(95)
        pdf.cell(w=54,h=5,txt='CANC. SALDO PENDIENTE', border=1,  align='C', fill=False)
        pdf.multi_cell(w=56,h=5,txt='$  '+str(pre.cansaldopend) if hasattr(pre, 'cansaldopend') else '', border=1,  align='C', fill=False)
        pdf.set_x(95)
        pdf.cell(w=54,h=5,txt='1o. CUOTA', border=1,  align='C', fill=False)
        pdf.multi_cell(w=56,h=5,txt='$  '+str(pre.pcuota) if hasattr(pre, 'pcuota') else '', border=1,  align='C', fill=False)
        pdf.set_x(95)
        pdf.set_font('Arial', 'B', 5.5)
        pdf.cell(w=54,h=5,txt='TOTAL', border=1,  align='C', fill=False)
        pdf.multi_cell(w=56,h=5,txt='$  '+str(pre.total) if hasattr(pre, 'total') else '', border=1,  align='C', fill=False)

        y=pdf.get_y()
        pdf.text(x=20, y=y+13, txt='F')
        pdf.line(20, y+15, 80, y+15)
        pdf.text(x=20, y=y+20, txt='ELABORO ')
        pdf.text(x=20, y=y+25, txt='Nombre. ')
        pdf.text(x=20, y=y+30, txt='Dui')

        pdf.output('presupuestoMej.pdf', 'F')
        return FileResponse(open('presupuestoMej.pdf', 'rb'), as_attachment=True, content_type='application/pdf')