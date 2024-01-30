from fpdf import FPDF
from datetime import date
import locale
from termcolor import colored
from django.http import FileResponse
from PresupuestoVApp.models import *

from ClienteApp.models import *

from django.db.models import Q


class presupuestoVv(FPDF):
    
    def presupuestoV(request, id ):

        try:
            pvdg=  Presupuestovdg.objects.get(ids=id)
        except Presupuestovdg.DoesNotExist:
            pvdg=""
        try:
            s=  solicitud.objects.get(id=pvdg.ids.id)
        except solicitud.DoesNotExist:
            s=""

        try:
            do= datosObra.objects.get(idSolicitud=pvdg.ids.id)
        except datosObra.DoesNotExist:
            do=""
        
        try:
            d=  detalle.objects.get(idSolicitud=pvdg.ids.id)
        except detalle.DoesNotExist:
            d=""
        
        try:
            listam=Materiales.objects.filter(estado="activo")
        except Materiales.DoesNotExist:
            listam=""
        try:
            pvt=  PresupuestovTotal.objects.get(idp=pvdg.id)
        except PresupuestovTotal.DoesNotExist:
            pvt=""

        try:
            lista_materiales= PresupuestovMateriales.objects.filter(idp=pvdg.id)
            datos_materiales=[]
            for item in lista_materiales:
                datos_materiales.append ( {'id': item.id, 'precio':item.preciouni,'cantida': item.cantidad,'total':item.subtotal,
                "nombre":item.idm.nombre,"descripcion":item.idm.descripcion,"unidad":item.idm.unidad,"idm":item.idm.id })
        except PresupuestovMateriales.DoesNotExist:
            lista_materiales=""

        try:
            lista_mano_obra= PresupuestovManoObra.objects.filter(idp=pvdg.id)
            datos_mano_obra=[]
            for item in lista_mano_obra:
                datos_mano_obra.append({
                    "id":item.id,
                    "descripcion":item.descripcion,
                    "unidad":item.unidad,
                    "preciouni":item.preciouni,
                    "cantidad":item.cantidad,
                    "total":item.subtotal,
                })
        except PresupuestovManoObra.DoesNotExist:
            lista_mano_obra=""
    

        r=59
        g=93
        b=149
        aux=[0, 1, 2, 3]
        aux2=[0, 1, 2]    
        subtot=0
        subtotmo=0
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=10, y=12, w=55, h=30)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=0,h=8,txt='PRESUPUESTO DE VIVIENDA HABITAT', border=1,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_font('Arial', '', 7)
        pdf.cell(w=96,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=25,h=5,txt='AGENCIA:', border=1,  align='L', fill=False)
        pdf.cell(w=30,h=5,txt=s.perfil.Agencia.nombre if hasattr(s, 'perfil') else '', border='LR',  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='COSTO TOTAL=', border=1,  align='L', fill=False)
        pdf.cell(w=20,h=5,txt='$      ' + str(d.monto) if hasattr(d, 'monto') else '', border='L',  align='R', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=96,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=25,h=5,txt='FECHA:', border=1,  align='L', fill=False)
        pdf.cell(w=30,h=5,txt=pvdg.fecha.strftime("%d/%m/%Y") if hasattr(pvdg, 'fecha') else '', border='LR',  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='CANT. VIVIENDA=', border=1,  align='L', fill=False)
        pdf.cell(w=20,h=5,txt=str(pvdg.cantidadvivienda) if hasattr(pvdg, 'cantidadvivienda') else '', border='L',  align='R', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=96,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=40,h=5,txt='TIEMPO DE CONSTRUCCION:', border=1,  align='L', fill=False)
        pdf.cell(w=15,h=5,txt=pvdg.tiempoconstruccion if hasattr(pvdg, 'tiempoconstruccion') else '', border='LR',  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='COSTO TOTAL=', border=1,  align='L', fill=False)
        pdf.cell(w=20,h=5,txt='$      '+ str(pvdg.costototalv) if hasattr(pvdg, 'costototalv') else '', border='L',  align='R', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.set_fill_color(217,217,217)
        pdf.cell(w=96,h=5,txt='CLIENTE', border=1, align='C', fill=False)
        pdf.cell(w=100,h=5,txt=(s.perfil.nombres if hasattr(s.perfil, 'nombres') else '') +' '+ (s.perfil.apellidos if hasattr(s.perfil, 'apellidos') else ''), border=1, align='C', fill=True, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=15,h=5,txt='MODELO:', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='TIPO   '+ pvdg.modelo if hasattr(pvdg, 'modelo') else '', border=1, align='L', fill=True)
        pdf.cell(w=40,h=5,txt='DIMENSION DE VIVIENDA:', border=1,  align='L', fill=False)
        pdf.cell(w=0,h=5,txt=pvdg.dimensionviv if hasattr(pvdg, 'dimensionviv') else '', border=1, align='C', fill=True, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=96,h=5,txt='DIRECCIÓN DEL INMUEBLE:', border=1, align='L', fill=False)
        pdf.cell(w=100,h=5,txt=str(do.direExacta) if hasattr(do, 'direExacta') else '', border=1, align='C', fill=True, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)

        pdf.cell(w=15,h=5,txt='COD', border=1, align='C', fill=True)
        pdf.cell(w=81,h=5,txt='DESCRIPCION', border=1, align='C', fill=True)
        pdf.cell(w=20,h=5,txt='UNIDAD', border=1,  align='C', fill=True)
        pdf.cell(w=20,h=5,txt='P.U.', border=1,  align='C', fill=True)
        pdf.cell(w=15,h=5,txt='CANT', border=1,  align='C', fill=True)
        pdf.cell(w=25,h=5,txt='CANTIDAD TOTAL', border=1,  align='C', fill=True)
        pdf.cell(w=0,h=5,txt='SubTotal', border=1,  align='C', fill=True, ln=1)

        pdf.cell(w=15,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=161,h=5,txt='', border=1, align='C', fill=False)
        for mat in datos_materiales:
                stmat = mat["total"]
                subtot=subtot+stmat
        tot=pdf.cell(w=0,h=5,txt='$  '+str(subtot) or '', border=1,  align='R', fill=False, ln=1)

        #### Tabla de materiales
        if datos_materiales !='' and len(datos_materiales):
            for mat in datos_materiales:
                nmat = mat["nombre"]
                umat = mat["unidad"]
                pumat = mat["precio"]
                cmat = mat["cantida"]
                stmat = mat["total"]
                pdf.cell(w=15,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt=nmat, border=1, align='L', fill=False)
                pdf.cell(w=20,h=5,txt=umat, border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='$  '+str(pumat) or '', border=1,  align='R', fill=False)
                pdf.cell(w=15,h=5,txt='$  '+str(cmat) or '', border=1,  align='R', fill=False)
                pdf.cell(w=25,h=5,txt='$  '+str(stmat) or '', border=1,  align='R', fill=False)
                pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)
               
        else:
            
            for i in aux:
                pdf.cell(w=15,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)

        
        #### Tabla de mano de obra
        pdf.cell(w=15,h=5,txt='MO', border=1, align='C', fill=False)
        pdf.cell(w=161,h=5,txt='MANO DE OBRA', border=1, align='L', fill=False)
        for mo in datos_mano_obra:
                stmo = mo["total"]
                subtotmo=subtotmo+stmo
        tot=pdf.cell(w=0,h=5,txt='$  '+str(subtotmo) or '', border=1,  align='R', fill=False, ln=1)

        if datos_mano_obra !='' and len(datos_mano_obra):
            for mo in datos_mano_obra:
                dmo = mo["descripcion"]
                umo = mo["unidad"]
                pumo = mo["preciouni"]
                cmo = mo["cantidad"]
                stmo = mo["total"]
                pdf.cell(w=15,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt=dmo, border=1, align='L', fill=False)
                pdf.cell(w=20,h=5,txt=umo, border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='$  '+str(pumo) or '', border=1,  align='R', fill=False)
                pdf.cell(w=15,h=5,txt='$  '+str(cmo) or '', border=1,  align='R', fill=False)
                pdf.cell(w=25,h=5,txt='$  '+str(stmo) or '', border=1,  align='R', fill=False)
                pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)
                
        else:
            
            for i in aux:
                pdf.cell(w=15,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=81,h=5,txt='', border=1, align='C', fill=False)
                pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
                pdf.cell(w=0,h=5,txt='', border=1,  align='C', fill=False, ln=1)
        
        pdf.cell(w=15,h=5,txt='A', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='MATERIALES', border=1, align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=5,txt='$  '+ str(pvt.materiales) if hasattr(pvt, 'materiales') else '', border=1,  align='R', fill=False, ln=1)
        pdf.cell(w=15,h=5,txt='B', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='MANO DE OBRA', border=1, align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=5,txt='$  '+str(pvt.manoobra) if hasattr(pvt, 'manoobra') else '', border=1,  align='R', fill=False, ln=1)
        pdf.cell(w=15,h=5,txt='C', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='TRANSPORTE', border=1, align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=5,txt='$  '+str(pvt.transporte) if hasattr(pvt, 'transporte') else '', border=1,  align='R', fill=False, ln=1)
        pdf.cell(w=15,h=5,txt='D', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='SOLUCIÓN SANITARIA', border=1, align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=5,txt='$  '+str(pvt.solucionsanit) if hasattr(pvt, 'solucionsanit') else '', border=1,  align='R', fill=False, ln=1)
        pdf.cell(w=15,h=5,txt='E', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='KIT DE EMERGENCIA', border=1, align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=5,txt='$  '+str(pvt.kitemerg) if hasattr(pvt, 'kitemerg') else '', border=1,  align='R', fill=False, ln=1)
        pdf.cell(w=15,h=5,txt='F', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='HERRAMIENTAS', border=1, align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=False)
        pdf.cell(w=0,h=5,txt='$  '+str(pvt.herramientas) if hasattr(pvt, 'herramientas') else '', border=1,  align='R', fill=False, ln=1)
        pdf.cell(w=15,h=5,txt='', border=1, align='L', fill=False)
        pdf.cell(w=81,h=5,txt='TOTAL COSTOS DIRECTOS', border=1, align='L', fill=True)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=20,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=15,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=25,h=5,txt='', border=1,  align='C', fill=True)
        pdf.cell(w=0,h=5,txt='$  '+str(pvt.totalcostosd) if hasattr(pvt, 'totalcostosd') else '', border=1,  align='R', fill=True, ln=1)
        y=pdf.get_y()
        pdf.cell(w=0,h=70,txt='', border=1,  align='C', fill=False)


        pdf.text(x=20, y=y+13, txt='F')
        pdf.line(20, y+15, 80, y+15)
        pdf.text(x=20, y=y+20, txt='ELABORO ')
        pdf.text(x=20, y=y+25, txt='Nombre. ')
        pdf.text(x=20, y=y+30, txt='Dui')

        pdf.text(x=130, y=y+13, txt='F')
        pdf.line(130, y+15, 190, y+15)
        pdf.text(x=130, y=y+20, txt='AUTORIZO ')
        pdf.text(x=130, y=y+25, txt='Nombre. ')
        pdf.text(x=130, y=y+30, txt='Dui')

        #y=pdf.get_y()
        pdf.text(x=20, y=y+43, txt='F')
        pdf.line(20, y+45, 80, y+45)
        pdf.text(x=20, y=y+50, txt='REVISADO')
        pdf.text(x=20, y=y+55, txt='Nombre. ')
        pdf.text(x=20, y=y+60, txt='Admin ')
        pdf.text(x=20, y=y+65, txt='Dui')

        #tot.txt=str('10')
        pdf.output('presupuestoViv.pdf', 'F')
        return FileResponse(open('presupuestoViv.pdf', 'rb'), as_attachment=True, content_type='application/pdf')