from fpdf import FPDF
from datetime import date
import locale
from ClienteApp.models import *
from django.http import FileResponse
from SolicitudesApp.models import *
from ClienteApp.models import Perfil
from django.db.models import Q


class solicitudPer(FPDF):
    
    def soliPer(request, ids):
        

        locale.setlocale(locale.LC_TIME, 'es_ES')
        fecha=date.today()
        
        print(fecha)
        try:
            sol=solicitud.objects.get(id=ids)
        except solicitud.DoesNotExist: 
            sol=""
          
        try:
            do=datosObra.objects.get(idSolicitud=ids)
        except datosObra.DoesNotExist: 
            do=""

        try:
            gf=grupoFamiliar.objects.filter(idSolicitud=sol.id)            
        except grupoFamiliar.DoesNotExist: 
            gf=""  

        try:
            dps=datosPersonales.objects.get(idSolicitud=sol.id)
        except datosPersonales.DoesNotExist: 
            dps=""

        try:
            dpf=DatosPersonalesF.objects.get(Q(idSolicitud=ids) & Q(Q(tipo ="conyuge") | Q(tipo="codeudor")))
        except DatosPersonalesF.DoesNotExist: 
            dpf=""
        
        try:
            ds=domicilio.objects.get(idSolicitud=ids, tipo="Solicitante")        
        except domicilio.DoesNotExist: 
            ds=domicilio()
            ds=""
        
        try:
            df=domicilio.objects.get(Q(idSolicitud=ids) & Q(Q(tipo ="conyuge") | Q(tipo="codeudor")))       
        except domicilio.DoesNotExist: 
            df=domicilio()
            df=""
       
        try:            
            det=detalle.objects.get(idSolicitud=sol.id)                   
        except detalle.DoesNotExist: 
            det=""

        try:            
            ec=experienciCrediticia.objects.filter(idSolicitud=sol.id)                    
        except experienciCrediticia.DoesNotExist: 
            ec=""

        try:           
            rp=referencias.objects.filter(idSolicitud=sol.id)                   
        except referencias.DoesNotExist: 
            rp=""

        try:           
            com=comentarios.objects.get(idSolicitud=sol.id)                    
        except comentarios.DoesNotExist: 
            com=""

        try:
            med=Medio.objects.get(idSolicitud=ids)
        except Medio.DoesNotExist:
            med=""

 
        
        r=74
        g=96
        b=45
        aux=[0, 1, 2, 3]
        aux2=[0, 1, 2]    
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=5, y=2, w=35, h=25)#, link=url)
        

        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(r,g,b)
        pdf.text(x=80, y=20, txt='SOLICITUD DE CREDITO.')
        pdf.text(x=30, y=25, txt='Para familias con ingresos provenientes de empleos y/o remesas familiares')
            
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
        pdf.cell(w=20,h=5,txt='Area: ', border=0, align='R', fill=False)
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
        pdf.cell(w=80,h=5,txt=sol.perfil.nombres if hasattr(sol, 'perfil') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dpf.nombrefia if hasattr(dpf, 'nombrefia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Apellidos', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=sol.perfil.apellidos if hasattr(sol, 'perfil') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dpf.apellidofia if hasattr(dpf, 'apellidofia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='DUI', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=sol.perfil.dui if hasattr(sol, 'perfil') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dpf.duifia if hasattr(dpf, 'duifia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Lugar y Fecha de Expedicion', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=(dps.lugarduiC  if hasattr(dps, 'lugarduiC') else '') +' '+(dps.fechaduiC.strftime("%d/%m/%Y") if hasattr(dps, 'fechaduiC') else '') , border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=(dpf.lugarduifia  if hasattr(dpf, 'lugarduifia') else '') +' '+ (dpf.fechaduifia.strftime("%d/%m/%Y") if hasattr(dpf, 'fechaduifia') else '' ), border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Lugar y Fecha de Nacimiento', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=(dps.lugarnaciC if hasattr(dps, 'lugarnaciC') else '')  +' '+(sol.perfil.fechan.strftime("%d/%m/%Y") if hasattr(sol, 'perfil') else '') , border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=(dpf.lugarnacifia  if hasattr(dpf, 'lugarnacifia') else '') +' '+(dpf.fechanacifia.strftime("%d/%m/%Y")  if hasattr(dpf, 'fechanacifia') else ''), border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Edad', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=str(sol.perfil.edad) if hasattr(sol, 'perfil') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=str(dpf.edadfia) if hasattr(dpf, 'edadfia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='NIT', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt='---------', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='---------', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Estado Civil', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=dps.estadocivilC if hasattr(dps, 'estadocivilC') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dpf.estadocivilfia if hasattr(dpf, 'estadocivilfia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Genero', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=dps.generoC if hasattr(dps, 'generoC') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dpf.generofia if hasattr(dpf, 'generofia') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Profesión u Oficio', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=80,h=5,txt=sol.perfil.idocu.ocupacion if hasattr(sol, 'perfil') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=dpf.profefia if hasattr(dpf, 'profefia') else '', border=1,  align='L', fill=0)
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
                pdf.cell(w=20,h=5,txt=str(i.edad) or '', border=1,  align='L', fill=0)
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
        pdf.cell(w=50,h=5,txt='Direccion actual del domicilio', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.direccion if hasattr(ds, 'direccion') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.direccion if hasattr(df, 'direccion') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Punto de refencia', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.referencia if hasattr(ds, 'referencia') else '', border=0,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.referencia if hasattr(df, 'referencia ') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Telefóno', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.telefono if hasattr(ds, 'telefono') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.telefono if hasattr(df, 'telefono ') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Reside desde', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.resideDesde if hasattr(ds, 'resideDesde') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.resideDesde if hasattr(df, 'resideDesde') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Condicion de la vivienda', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.condVivienda if hasattr(ds, 'condVivienda') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.condVivienda if hasattr(df, 'condVivienda') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Lugar de trabajo o negocio', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.lugarTrabajo if hasattr(ds, 'lugarTrabajo') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.lugarTrabajo if hasattr(df, 'lugarTrabajo') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Jefe inmediato', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.jefeInm if hasattr(ds, 'jefeInm') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.jefeInm if hasattr(df, 'jefeInm') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Tiempo de empleo', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=str(ds.tiempEmptiempFun) if hasattr(ds, 'tiempEmptiempFun') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=str(df.tiempEmptiempFun) if hasattr(df, 'tiempEmptiempFun') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Salario', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=str(ds.salarioIngreso) if hasattr(ds, 'salarioIngreso') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=str(df.salarioIngreso) if hasattr(df, 'salarioIngreso') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Dirección del trabajo', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.direccionTrabMicro if hasattr(ds, 'direccionTrabMicro') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.direccionTrabMicro if hasattr(df, 'direccionTrabMicro') else '', border=1,  align='L', fill=0)
        pdf.set_text_color(r,g,b)
        pdf.cell(w=50,h=5,txt='Telefono del trabajo', border=1,  align='L', fill=0)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=70,h=5,txt=ds.telefonoTrabMicro if hasattr(ds, 'telefonoTrabMicro') else '', border=1,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt=df.telefonoTrabMicro if hasattr(df, 'telefonoTrabMicro') else '', border=1,  align='L', fill=0)
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
        pdf.multi_cell(w=0,h=15, txt=com.CSN if hasattr(com, 'CSN') else '', border=1,  align='C', fill=0)
        pdf.set_text_color(255,255,255)
        pdf.multi_cell(w=0,h=5,txt='Comentario sobre la evaluación y estabilidad de los ingresos (Capacidad de pago, actividad productiva, referencias crediticias y alternativas de pago por pérdida de fuente de ingreso actual)', border=1, align='C', fill=1)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=20,txt=com.CEE if hasattr(com, 'CEE') else '', border=1,  align='C', fill=0)
        pdf.set_text_color(255,255,255)
        pdf.multi_cell(w=0,h=5,txt='Comentario sobre la garantía ofrecida', border=1, align='C', fill=1)
        pdf.set_text_color(0,0,0)
        pdf.multi_cell(w=0,h=25,txt=com.CGO if hasattr(com, 'CGO') else '', border=1,  align='C', fill=0)
        ########
        pdf.ln(3)
        pdf.set_text_color(r,g,b)
        pdf.multi_cell(w=0,h=5,txt='Medio por el cual se infomo del servicio crediticio de HPHES', border=0,  align='C', fill=0,)
        pdf.ln(5)
        pdf.cell(w=30,h=5,txt='Redes Sociales', border=0,  align='L', fill=0,)
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
        pdf.cell(w=40,h=5,txt='Perofoneo', border=0,  align='C', fill=0)
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
        pdf.cell(w=35,h=5,txt='Feria de Vivienda', border=0,  align='L', fill=0)
        if med.feriav=='Feria de Vivienda':
            pdf.cell(w=5,h=5,txt='X', border=1,  align='C', fill=0)
        else:
            pdf.cell(w=5,h=5,txt='', border=1,  align='C', fill=0)
        pdf.cell(w=50,h=5,txt='Campaña de Promocion', border=0,  align='C', fill=0)
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
        pdf.multi_cell(w=0,h=5,txt=med.especifique if hasattr(med, 'especifique') else '', border='B',  align='C', fill=0)
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 9.5)
        pdf.multi_cell(w=0,h=5,txt='Declaro que toda la informacion contenida en en la solicitud es verdadera y autorizo a la Asociacion HPH El Salvador para que realice las investigaciones respectivas.', border=0,  align='L', fill=0)
        pdf.multi_cell(w=0,h=5,txt='La recepcion de la presente solicitud no significa compromiso alguno de La Asociacion con el solicitante.', border=0,  align='L', fill=0)
        
        
        pdf.line(30, 265, 90, 265)
        pdf.text(x=45, y=270, txt='Firma Solicitante ')
        pdf.line(120, 265, 180, 265)
        pdf.text(x=135, y=270, txt='Firma Codeudor ')
        
        pdf.output('solicitudPer.pdf', 'F')
        return FileResponse(open('solicitudPer.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
        #return redirect("listaSolicitud")
