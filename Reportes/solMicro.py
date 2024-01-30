from fpdf import FPDF
from datetime import date
import locale
from ClienteApp.models import *

from django.http import FileResponse
from SolicitudesApp.models import *
from ClienteApp.models import Perfil
from django.db.models import Q



class SolicitudMicro(FPDF):
    
    def soliMicro(request, ids, idp):

        locale.setlocale(locale.LC_TIME, 'es_ES')
        fecha=date.today()
        try:
            sol=solicitud.objects.get(id=ids)
        except solicitud.DoesNotExist: 
            sol=""
        try:
            per=Perfil.objects.get(id=idp)
        except Perfil.DoesNotExist: 
            per=""
        try:
            do=datosObra.objects.get(idSolicitud=ids)
        except datosObra.DoesNotExist: 
            do=""
        try:
            gf=grupoFamiliar.objects.filter(idSolicitud=ids)         
        except grupoFamiliar.DoesNotExist: 
            gf=""  

        try:
            dps=datosPersonales.objects.get(idSolicitud=ids)
        except datosPersonales.DoesNotExist: 
            dps=""
        
        try:
            ds=domicilio.objects.get(idSolicitud=ids, tipo ='Solicitante')      
        except domicilio.DoesNotExist: 
            ds=""

        try:
            dc=domicilio.objects.get(Q(idSolicitud=ids) & Q(Q(tipo ="conyuge") | Q(tipo="codeudor")))
        except domicilio.DoesNotExist: 
            dc=""

        try:   
            dp=DatosPersonalesF.objects.get(Q(idSolicitud=ids) & Q(Q(tipo ="conyuge") | Q(tipo="codeudor")))     
        except DatosPersonalesF.DoesNotExist: 
            dp=""

        try:        
            det=detalle.objects.get(idSolicitud=ids)                
        except solicitud.DoesNotExist: 
            det=""
        try:            
            ec=experienciCrediticia.objects.filter(idSolicitud=ids)                   
        except experienciCrediticia.DoesNotExist: 
            ec=""

        try:          
            rp=referencias.objects.filter(idSolicitud=ids)                   
        except referencias.DoesNotExist: 
            rp=""

        try:           
            com=comentarios.objects.get(idSolicitud=ids)                   
        except comentarios.DoesNotExist: 
            com=""

        try:           
            med=Medio.objects.get(idSolicitud=ids)                    
        except Medio.DoesNotExist: 
            med=""
        
        
        r=0
        g=102
        b=153
        aux=[0, 1, 2, 3]
        aux2=[0, 1, 2]    
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=5, y=5, w=40, h=30)#, link=url)

        #pdf.set_font('Arial', 'B', 12)
        #pdf.text(x=40, y=30, txt='AUTORIZACIÓN PARA CONSULTAR Y COMPARTIR INFORMACIÓN.')
        
        

        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(r,g,b)
        pdf.text(x=80, y=20, txt='SOLICITUD DE CREDITO.')
        pdf.text(x=50, y=25, txt='Para familias con ingresos provenientes de Microempresas')
            
        pdf.set_font('Arial', '', 10)
        pdf.set_y(30)
        pdf.set_left_margin(10)
        pdf.cell(w=20,h=5,txt='Fecha:', border=0, align='L', fill=False)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=20,h=5,txt=fecha.strftime("%d/%m/%Y") or '', border='B', align='C', fill=False)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=20,h=5,txt='Agencia:', border=0, align='R', fill=False)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=50,h=5,txt=sol.perfil.Agencia.nombre if hasattr(sol, 'perfil') else '', border='B', align='C', fill=False)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=20,h=5,txt='Comunidad:', border=0, align='R', fill=False)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=50,h=5,txt=sol.comunidad if hasattr(sol, 'comunidad') else '', border='B', align='C', fill=False)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=20,h=5,txt='Municipio:', border=0, align='R', fill=False)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=50,h=5,txt=sol.perfil.municipio.distri if hasattr(sol, 'perfil') else '', border='B', align='C', fill=False)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=12,h=5,txt='Area: ', border=0, align='R', fill=False)
        if sol.area =="Urbana":
            pdf.cell(w=15,h=5,txt='Urbana:', border=0, align='C', fill=False)
            pdf.set_text_color(0,0,0)
            pdf.cell(w=5,h=5,txt='X', border=1, align='C', fill=False)
            pdf.set_text_color(r,g,b)
            pdf.cell(w=15,h=5,txt='Rural:', border=0, align='C', fill=False)
            pdf.multi_cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        elif sol.area == 'Rural':
            pdf.cell(w=15,h=5,txt='Urbana:', border=0, align='C', fill=False)
            pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
            pdf.cell(w=15,h=5,txt='Rural:', border=0, align='C', fill=False)
            pdf.set_text_color(0,0,0)
            pdf.multi_cell(w=5,h=5,txt='X', border=1, align='C', fill=False)
        else:
            pdf.set_text_color(r,g,b)
            pdf.cell(w=15,h=5,txt='Urbana:', border=0, align='C', fill=False)
            pdf.cell(w=5,h=5,txt='', border=1, align='C', fill=False)
            pdf.cell(w=15,h=5,txt='Rural:', border=0, align='C', fill=False)
            pdf.multi_cell(w=5,h=5,txt='', border=1, align='C', fill=False)
        
        #pdf.cell(w=0,h=5,txt='', border='B',  align='L', ln=1, fill=0)

        pdf.set_font('Arial', '', 10)
        pdf.set_y(40)
        pdf.set_left_margin(10)
        pdf.set_fill_color(r,g,b)
        #pdf.add_page
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='', border='B',  align='L', ln=1, fill=0)
        pdf.cell(w=50,h=5,txt='Identificacion', border=1, align='C', fill=True)
        pdf.cell(w=80,h=5,txt='Solicitante', border=1, align='C', fill=True)
        pdf.multi_cell(w=0,h=5,txt='Conyuge  Codeudor', border=1,  align='C', fill=True)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Nombres', border=1, align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=per.nombres if hasattr(per, 'nombres') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dp.nombrefia if hasattr(dp, 'nombrefia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Apellidos', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=per.apellidos if hasattr(per, 'apellidos') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dp.apellidofia if hasattr(dp, 'apellidofia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='DUI', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=per.dui if hasattr(per, 'dui') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dp.duifia if hasattr(dp, 'duifia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Lugar y Fecha de Expedicion', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=(dps.lugarduiC  if hasattr(dps, 'lugarduiC ') else '') +' '+dps.fechaduiC.strftime("%d/%m/%Y") if hasattr(dps, 'fechaduiC ') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=(dp.lugarduifia if hasattr(dp, 'lugarduifia ') else '') +' '+ (dp.fechaduifia.strftime("%d/%m/%Y") if hasattr(dp, 'fechaduifia ') else '') , border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Lugar y Fecha de Nacimiento', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=(dps.lugarnaciC if hasattr(dps, 'lugarnaciC') else '')  +' '+ (dps.idSolicitud.perfil.fechan .strftime("%d/%m/%Y") if hasattr(dps, 'idSolicitud') else '') , border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=(dp.lugarnacifia  if hasattr(dp, 'lugarnacifia ') else '') +' '+(dp.fechanacifia.strftime("%d/%m/%Y")  if hasattr(dp, 'fechanacifia') else ''), border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Edad', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=str(per.edad) if hasattr(per, 'edad') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=str(dp.edadfia) if hasattr(dp, 'edadfia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='NIT', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt='--------------', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='--------------', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Estado Civil', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=dps.estadocivilC if hasattr(dps, 'estadocivilC') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dp.estadocivilfia if hasattr(dp, 'estadocivilfia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Genero', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=dps.generoC if hasattr(dps, 'generoC') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dp.generofia if hasattr(dp, 'generofia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Profesión u Oficio', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=dps.profesion if hasattr(dps, 'profesion') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dp.profefia if hasattr(dp, 'profefia') else '', border=1,  align='L', fill=0)
        pdf.cell(w=0,h=5,txt='', border='TB',  align='L', ln=1, fill=0)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='Grupo Familiar', border=1, ln=1, align='C', fill=1)
        pdf.cell(w=60,h=5,txt='Nombre', border=1,  align='C', fill=1)
        pdf.cell(w=20,h=5,txt='Edad', border=1,  align='C', fill=1)
        pdf.cell(w=20,h=5,txt='Salario', border=1,  align='C', fill=1)
        pdf.cell(w=40,h=5,txt='Lugar de Trabajo', border=1,  align='C', fill=1)
        pdf.multi_cell(w=0,h=5,txt='Parentesco', border=1,  align='C', fill=1)
        pdf.set_text_color(0,0,0)
        if gf!='' and len(gf)>0:
            for i in gf:
                pdf.cell(w=60,h=5,txt=i.nombre or '', border=1,  align='L', fill=0)
                pdf.cell(w=20,h=5,txt=i.edad or '', border=1,  align='L', fill=0)
                pdf.cell(w=20,h=5,txt=str(i.salario) or '', border=1,  align='L', fill=0)
                pdf.cell(w=40,h=5,txt=i.trabajo or '', border=1,  align='L', fill=0)
                pdf.multi_cell(w=0,h=5,txt=i.parentesco or '', border=1,  align='L', fill=0)
        else:
            
            for i in aux:
                pdf.cell(w=60,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=20,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=20,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=40,h=5,txt='', border=1,  align='L', fill=0)
                pdf.multi_cell(w=0,h=5,txt='', border=1,  align='L', fill=0)
            
        pdf.cell(w=0,h=5,txt='', border='TB',  align='L', ln=1, fill=0)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='Domicilio y Lugar de Trabajo', border=1, ln=1, align='C', fill=1)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Dirección actual del domicilio', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=str(ds.direccion) if hasattr(ds, 'direccion') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=str(dc.direccion) if hasattr(dc, 'direccion') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Punto de refencia', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.referencia if hasattr(ds, 'referencia') else '', border=0,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.referencia if hasattr(dc, 'referencia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Telefóno', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.telefono if hasattr(ds, 'telefono') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.telefono if hasattr(dc, 'telefono') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Reside desde', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.resideDesde if hasattr(ds, 'resideDesde') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.resideDesde if hasattr(dc, 'resideDesde') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Condición de la vivienda', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.condVivienda if hasattr(ds, 'condVivienda') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.condVivienda if hasattr(dc, 'condVivienda') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Actividad de la microempresa', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.actividadMicro if hasattr(ds, 'actividadMicro') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.actividadMicro if hasattr(dc, 'actividadMicro') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Lugar de la microempresa', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.lugarTrabajo if hasattr(ds, 'lugarTrabajo') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.lugarTrabajo if hasattr(dc, 'lugarTrabajo') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=50,h=5,txt='Tiempo de funcionamiento de la microempresa', border=1,  align='L', fill=0)
        pdf.set_xy(60, 165)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=10,txt=ds.tiempEmptiempFun if hasattr(ds, 'tiempEmptiempFun') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=10,txt=dc.tiempEmptiempFun if hasattr(dc, 'tiempEmptiempFun') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Ingreso (Utilidad neta mensual)', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=str(ds.salarioIngreso) if hasattr(ds, 'salarioIngreso') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=str(dc.salarioIngreso) if hasattr(dc, 'salarioIngreso') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Dirección de microempresa', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.direccionTrabMicro if hasattr(ds, 'direccionTrabMicro') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.direccionTrabMicro if hasattr(dc, 'direccionTrabMicro') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Telefono de la microempresa', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.telefonoTrabMicro if hasattr(ds, 'telefonoTrabMicro') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dc.telefonoTrabMicro if hasattr(dc, 'telefonoTrabMicro') else '', border=1,  align='L', fill=0)
        pdf.cell(w=0,h=5,txt='', border='TB',  align='L', ln=1, fill=0)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='Datos de la obra a realizar', border=1, ln=1, align='C', fill=1)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Destino del credito o producto', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=do.destino.alternativa if hasattr(do, 'destino') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Nombre del dueño de la propiedad', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=do.dueno if hasattr(do, 'dueno') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Parentesco con el solicitante', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=do.parentesco if hasattr(do, 'parentesco') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Direccion exacta de donde se construira', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=do.direExacta if hasattr(do, 'direExacta') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Detalle de la obra a realizar', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=do.detalle.topovivienda if hasattr(do, 'detalle') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Presupuesto de obra', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=str(do.presupuesto) if hasattr(do, 'presupuesto') else '', border=1,  align='L', fill=0)
        pdf.add_page()
        #pdf.cell(w=0,h=20,txt='', border=0,  align='L', ln=1, fill=0)
        ##########
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='Detalle de la solicitud', border=1, ln=1, align='C', fill=1)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Monto a solicitar', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=str(det.monto) if hasattr(det, 'monto') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Plazo solicitado', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=det.plazo if hasattr(det, 'plazo') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Cuota proyectada', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=str(det.cuota) if hasattr(det, 'cuota') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=10,txt='Forma de pago', border=1,  align='L', fill=0)
        pdf.set_xy(80, 30)
        if det.formaPago=='Ventanilla':
            pdf.cell(w=30,h=10,txt='Ventanilla', border=0,  align='L', fill=0)
            pdf.set_xy(105, 32)
            pdf.cell(w=5,h=5,txt='X', border=1,  align='L', fill=0)
            pdf.set_xy(140, 30)
            pdf.cell(w=20,h=10,txt='OPI', border=0,  align='L', fill=0)
            pdf.set_xy(150, 32)
            pdf.cell(w=5,h=5,txt='', border=1,  align='L', fill=0)
            pdf.set_xy(170, 30)
            pdf.multi_cell(w=0, h=10, border='R')
        else:
            pdf.cell(w=30,h=10,txt='Ventanilla', border=0,  align='L', fill=0)
            pdf.set_xy(105, 32)
            pdf.cell(w=5,h=5,txt='', border=1,  align='L', fill=0)
            pdf.set_xy(140, 30)
            pdf.cell(w=20,h=10,txt='OPI', border=0,  align='L', fill=0)
            pdf.set_xy(150, 32)
            pdf.cell(w=5,h=5,txt='X', border=1,  align='L', fill=0)
            pdf.set_xy(170, 30)
            pdf.multi_cell(w=0, h=10, border='R')
        pdf.set_text_color(0,0,0)
        #pdf.multi_cell(w=0,h=10,txt=str(det.formaPago), border=1,  align='L', fill=0)
        pdf.set_xy(10, 40)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=70,h=5,txt='Fecha que solicita pagar', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=5,txt=str(det.fechaPago) if hasattr(det, 'fechaPago') else '', border=1,  align='L', fill=0)
        ########
        pdf.cell(w=0,h=5,txt='', border='TB',  align='L', ln=1, fill=0)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='Experiencia crediticia', border=1, ln=1, align='C', fill=1)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=10,txt='Lugar', border=1,  align='C', fill=0,)
        pdf.cell(w=30,h=10,txt='Monto', border=1,  align='C', fill=0)
        pdf.multi_cell(w=30,h=5,txt='Fecha de otorgamiento', border=1,  align='C', fill=0)
        pdf.set_xy(120, 55)
        pdf.cell(w=30,h=10,txt='Estado', border=1,  align='C', fill=0)
        pdf.multi_cell(w=0,h=10,txt='Cuota que pagaba', border=1,  align='C', fill=0)
        pdf.set_text_color(0,0,0)

        if ec!='' and len(ec)>0:
            for i in ec:
                pdf.cell(w=50,h=5,txt=i.lugar or '', border=1,  align='L', fill=0)
                pdf.cell(w=30,h=5,txt=str(i.monto) or '', border=1,  align='L', fill=0)
                pdf.cell(w=30,h=5,txt=i.fechaOtorgamiento.strftime("%d/%m/%Y") or '', border=1,  align='L', fill=0)
                pdf.cell(w=30,h=5,txt=i.estado or '', border=1,  align='L', fill=0)
                pdf.multi_cell(w=0,h=5,txt=str(i.cuota) or '', border=1,  align='L', fill=0)
        else:        
            for i in aux2:
                pdf.cell(w=50,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=30,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=30,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=30,h=5,txt='', border=1,  align='L', fill=0)
                pdf.multi_cell(w=0,h=5,txt='', border=1,  align='L', fill=0)
        ################       
        pdf.cell(w=0,h=5,txt='', border='TB',  align='L', ln=1, fill=0)
        pdf.set_text_color(255,255,255)
        pdf.cell(w=0,h=5,txt='Referencia personales y familiares', border=1, ln=1, align='C', fill=1)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=60,h=5,txt='Nombre completo', border=1,  align='C', fill=0,)
        pdf.cell(w=40,h=5,txt='Parentesco', border=1,  align='C', fill=0)
        pdf.cell(w=60,h=5,txt='Domicilio completo', border=1,  align='C', fill=0)
        pdf.multi_cell(w=0,h=5,txt='Teléfono', border=1,  align='C', fill=0)
        pdf.set_text_color(0,0,0)
        if rp!='' and len(rp)>0:
            for i in rp:
                pdf.cell(w=60,h=5,txt=i.nombre or '', border=1,  align='L', fill=0)
                pdf.cell(w=40,h=5,txt=i.parentesco or '', border=1,  align='L', fill=0)
                pdf.cell(w=60,h=5,txt=i.domicilio or '', border=1,  align='L', fill=0)
                pdf.multi_cell(w=0,h=5,txt=i.telefono or '', border=1,  align='L', fill=0)
        else:
            
            for i in aux2:
                pdf.cell(w=60,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=40,h=5,txt='', border=1,  align='L', fill=0)
                pdf.cell(w=60,h=5,txt='', border=1,  align='L', fill=0)
                pdf.multi_cell(w=0,h=5,txt='', border=1,  align='L', fill=0)
            
        ############
        
        pdf.cell(w=0,h=5,txt='', border='TB',  align='L', ln=1, fill=0)
        pdf.set_text_color(255,255,255)
        pdf.multi_cell(w=0,h=5,txt='Comentario sobre la necesidad de la vivienda o mejoramiento de vivienda', border=1, align='C', fill=1)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=15,txt=com.CSN if hasattr(com, 'CSN') else '', border=1,  align='C', fill=0)
        pdf.set_text_color(255,255,255)
        pdf.multi_cell(w=0,h=5,txt='Comentario sobre la evaluación y estabilidad de los ingresos (Capacidad de pago, actividad productiva, referencias crediticias y alternativas de pago por pérdida de fuente de ingreso actual)', border=1, align='C', fill=1)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=15,txt=com.CEE if hasattr(com, 'CEE') else '', border=1,  align='C', fill=0)
        pdf.set_text_color(255,255,255)
        pdf.multi_cell(w=0,h=5,txt='Comentario sobre la garantía ofrecida', border=1, align='C', fill=1)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=15,txt=com.CGO if hasattr(com, 'CGO') else '', border=1,  align='C', fill=0)
        ########
        pdf.ln(3)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=0,h=5,txt='Medio por el cual se infomo del servicio crediticio de HPHES', border=0,  align='C', fill=0,)
        pdf.ln(5)
        pdf.cell(w=30,h=5,txt='Redes Sociales', border=0,  align='L', fill=0)
        if med.redes=='Redes sociales':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=20,h=5,txt='PVV', border=0,  align='C', fill=0)
        if med.pvv=='PVV':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=40,h=5,txt='Referenciado', border=0,  align='C', fill=0)
        if med.referenciado=='Referenciado':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=40,h=5,txt='Perifoneo', border=0,  align='C', fill=0)
        if med.perifoneo=='Perifoneo':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=20,h=5,txt='Radio', border=0,  align='C', fill=0)
        if med.radio=='Radio':
            pdf.multi_cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.multi_cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.ln(5)
        pdf.cell(w=35,h=5,txt='Feria de Vivienda', border=0,  align='L', fill=0,)
        if med.feriav=='Feria de Vivienda':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=50,h=5,txt='Campaña de Promocion', border=0,  align='C', fill=0,)
        if med.campanap=='Campaña de Promoción':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=20,h=5,txt='Otros', border=0,  align='C', fill=0)
        if med.otros=='Otros':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=25,h=5,txt='Especifique:', border=0,  align='C', fill=0)
        pdf.multi_cell(w=0,h=5,txt=med.especifique if hasattr(med, 'especifique') else ''  , border='B',  align='C', fill=0) 
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.multi_cell(w=0,h=5,txt='Declaro que toda la informacion contenida en en la solicitud es verdadera y autorizo a la Asociacion HPH El Salvador para que realice las investigaciones respectivas.', border=0,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='La recepcion de la presente solicitud no significa compromiso alguno de La Asociacion con el solicitante.', border=0,  align='L', fill=0)
        
        #texto="Yo, "+ per.nombres +" " + per.apellidos +", de conformidad a los articulos 14 literal d) y 15 de la Ley de Regulación de los Servicios de Información sobre el Historial de Crédito de las personas y articulo 18 literal g) de la Ley de Protección al Consumidor, por este medio, "+"SI__ NO__ AUTORIZO Y CONSIENTO</b> para que, <b>"+var+"</b> recopile, transmita, comparte, acceda, consulte y verifique mi informacion personal y crediticia, para análisis presente y futuros relacionados con la contratación de servicios. Expreso en realación a la autorización y consentimiento consignado en este documento, que tengo pleno conocimiento y, por lo tanto, <b>SI__ NO__ AUTORIZO Y CONSIENTO:</b> a) Que <b>ASOCIACIÓN HPH EL SALVADOR</b> podra acceder, consultar y verificar mi informacion personal y crediticia que estuviere contenida en las bases de datos de Equifax, TransUnion y/o Infored, con las que <b>ASOCIACIÓN HPH EL SALVADOR</b>tuviere acuerdos de carácter comercial y/o contractual; b) Que <b>ASOCIACIÓN HPH EL SALVADOR</b> podra recopiilar, transmitir y compartir mi información personal y crediticia, con Equifax, TransUnion e Infored, a fin de tales datos pasen a formar parte de mi historial crediticio en las bases de datos que al efecto lleva Equifax, TransUnion e Infored; c) Que <b>ASOCIACION HPH EL SALVADOR</b> podra adicionar, modificar y/o actualizar, cualquier informacion personal y crediticia proporcionada por mi persona, incluyendo los de esta solicitud y cualquier otra información que <b>ASOCIACION HPH EL SALVADOR</b> requiera en un futuro tanto de caracter personal como crediticio; y d) Que la presente autorización y consentimiento tendra una vigencia igual al plazo que perdure la relacion contractual entre el suscrito y <b>ASOCIACION HPH EL SALVADOR,</b> o en su defecto que la ley establece para la duracion de las autorizaciones. Conozco y admito que la presente autorizacion no afecta ni afectara en modo alguno las condiciones juridicas y económicas del credito que eventualmente me otorgue <b>ASOCIACION HPH EL SALVADOR</b>"
        #pdf.multi_cell(w=175, h=5, txt=texto, border=0, align= 'J', fill=0)
        pdf.line(30, 265, 90, 265)
        pdf.text(x=45, y=270, txt='Firma Solicitante ')
        pdf.line(120, 265, 180, 265)
        pdf.text(x=135, y=270, txt='Firma Codeudor ')
        
        pdf.output('solicitudMicro.pdf', 'F')
        return FileResponse(open('solicitudMicro.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
        #return redirect("listaSolicitud")
