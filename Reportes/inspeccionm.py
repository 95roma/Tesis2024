import json
from fpdf import FPDF
from datetime import date
import locale
from ClienteApp.models import *
from django.http import FileResponse
from SolicitudesApp.models import *
from InspeccionMejViviendaApp.models import *



class InspeccionMV(FPDF):
    
    def inspeccionM(request, id):

        try:
            ipm=  InspeccionM.objects.get(id=id)
        except InspeccionM.DoesNotExist:
            ipm=""
        try:
            s=  solicitud.objects.get(id=ipm.ids.id)
        except solicitud.DoesNotExist:
            s=""

        try:
            pim=pInspeccionm.objects.get(id=id)
        except pInspeccionm.DoesNotExist:
            pim=""

        try:
            imgpil= ImagenPInspeccionm.objects.get(idpim=id)
        except ImagenPInspeccionm.DoesNotExist:
            imgpil=""
        
        try:
            do= datosObra.objects.get(idSolicitud=ipm.ids.id)
        except datosObra.DoesNotExist:
            do=""
        
        try:
            vias_acceso= ViasAccesoipm.objects.get(idipl=ipm.id)
        except ViasAccesoipm.DoesNotExist:
            vias_acceso=""

        try:
            riesgo_distancia= Riesgosipm.objects.get(idipl=ipm)
        except Riesgosipm.DoesNotExist:
            riesgo_distancia=""

        try:
            factibilida_tecnica= Factibilidadipm.objects.get(idip=ipm)
        except Factibilidadipm.DoesNotExist:
            factibilida_tecnica=""

        try:
            descripcion_mejora= DMejoramientoipm.objects.get(idip=ipm)
        except DMejoramientoipm.DoesNotExist:
            descripcion_mejora=""

        try:
            lista_plan=PlanMejoramientoipm.objects.filter(idip=ipm)
        except PlanMejoramientoipm.DoesNotExist:
            lista_plan=""

        try:
            liip=InfraestructuraInmuebleipm.objects.filter(idip=ipm.id)
        except liip.DoesNotExist:
            liip=""
        liip_data = [
            {
                'existe': item.existe,
                'estado': item.estado,
                'tiposistema': item.tiposistema,
                'id': item.id,
                'idif':item.idif.nombre,
            }
            for item in liip
            ]

        lista_general=Inspeccionesirm.objects.filter(idip=ipm.id)

        lista_espacios_encontrados_datos=[]
        for item in lista_general:
            if item.idif.tipo == "3":
                lista_espacios_encontrados_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})

        lista_servicios_basicos_datos=[]
        for item in lista_general:
            if item.idif.tipo == "5":
                lista_servicios_basicos_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})

        lista_infraetructura_datos=[]
        for item in lista_general:
            if item.idif.tipo == "6":
                lista_infraetructura_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})

        lista_riesgos_datos=[]
        for item in lista_general:
            if item.idif.tipo == "7":
                lista_riesgos_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})
        
        locale.setlocale(locale.LC_TIME, 'es_ES')    
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        
            
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=7, y=1, w=40, h=28)#, link=url)
        pdf.set_font('Arial', 'B', 9)      
        pdf.set_x(50)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.multi_cell(w=0, h=5, txt='HOJA DE INSPECCIÓN PARA MEJORAMIENTOS DE VIVIENDAS', border=1, align='C', fill=True)
        pdf.set_x(50)
        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=20,h=8, txt='Agencia', border=1, fill=True)
        pdf.cell(w=60, h=8, txt=s.perfil.Agencia.nombre, border=1)
        pdf.cell(w=15, h=4, txt='DIA', border=1, fill=True)
        pdf.cell(w=25, h=4, txt='MES', border=1, fill=True)
        pdf.cell(w=15, h=4, txt='AÑO', border=1, fill=True)
        pdf.multi_cell(w=0, h=4, txt='HORA', border=1, fill=True)
        pdf.set_xy(130, 19) # para ubicar el multicel
        pdf.cell(w=15, h=4, txt=ipm.fecha.strftime(" %d ") if hasattr(ipm, 'fecha') else '', border=1)
        pdf.cell(w=25, h=4, txt=ipm.fecha.strftime(" %B ") if hasattr(ipm, 'fecha') else '', border=1)
        pdf.cell(w=15, h=4, txt= ipm.fecha.strftime(" %Y") if hasattr(ipm, 'fecha') else '' , border=1)
        pdf.multi_cell(w=0, h=4, txt=str(ipm.hora) if hasattr(ipm, 'hora') else '', border=1)
        pdf.ln(2)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.multi_cell(w=0, h=5, txt='1. INFORMACIÓN GENERAL', border=1, align='C', fill=True)
        #pdf.ln(1)
        pdf.set_font('Arial', size=6)
        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=22, h=5, txt='SOLICITANTE', border=1, fill=True)
        pdf.cell(w=121, h=5, txt=(s.perfil.nombres if hasattr(s.perfil, 'nombres') else '') +' '+ (s.perfil.apellidos if hasattr(s.perfil, 'apellidos') else ''), border=1)
        pdf.cell(w=19, h=5, txt='TELÉFONOS:', border='TL', fill=True)
        pdf.multi_cell(w=0, h=5, txt=ipm.telefonop if hasattr(ipm, 'telefonop') else '', border='TR')
        pdf.cell(w=22, h=5, txt='GRUPO FAMILIAR', border=1, fill=True)
        pdf.cell(w=24, h=5, txt='TERCERA EDAD:', border='BT')
        pdf.cell(w=5, h=5, txt=ipm.terceraedad if hasattr(ipm, 'terceraedad') else '', border='BT')
        pdf.cell(w=17, h=5, txt='ADULTOS:', border='BT')
        pdf.cell(w=5, h=5, txt=ipm.adultos if hasattr(ipm, 'adultos') else '', border='BT')
        pdf.cell(w=13, h=5, txt='NIÑOS:', border='BT')
        pdf.cell(w=5, h=5, txt=ipm.ninos if hasattr(ipm, 'ninos') else '', border='BT')
        pdf.cell(w=47, h=5, txt='PERSONAS CON DISCAPACIDAD:', border='BT')
        pdf.cell(w=5, h=5, txt=ipm.personadisc if hasattr(ipm, 'personadisc') else '', border='BTR')
        pdf.multi_cell(w=0, h=5, txt=ipm.telefonos if hasattr(ipm, 'telefonos') else '', border='BLR')
        pdf.cell(w=22, h=8, txt='DIRECCIÓN', border=1, fill=True)
        pdf.cell(w=110, h=8, txt=str(do.direExacta) if hasattr(do, 'direExacta') else '', border=1)
        pdf.cell(w=0, h=4, txt='MUNICIPIO', border=1, fill=True)
        pdf.set_xy(142, 44)
        pdf.multi_cell(w=0, h=4, txt=s.perfil.municipio.distri if hasattr(s, 'perfil') else '', border=1)
        pdf.cell(w=34, h=5, txt='PROPIETARIO DEL INMUEBLE', border=1, fill=True)
        pdf.cell(w=80, h=5, txt=ipm.propietarioinm if hasattr(ipm, 'propietarioinm') else '', border=1)
        pdf.cell(w=40, h=5, txt='PARENTESCO CON EL SOLICITANTE', border=1, fill=True)
        pdf.multi_cell(w=0, h=5, txt=ipm.parentescosol if hasattr(ipm, 'parentescosol') else '', border=1)
        pdf.cell(w=22, h=5, txt='LATITUD', border=1, fill=True)
        pdf.cell(w=53, h=5, txt=ipm.latitud if hasattr(ipm, 'latitud') else '', border=1)
        pdf.cell(w=13, h=10, txt='INMUEBLE', border=1, fill=True)
        pdf.cell(w=26, h=5, txt='RURAL', border='TL', align='L')
        pdf.set_fill_color(0,0,0) # color negro  
        if ipm.inmueble=='Urbano':
            pdf.ellipse(113,54,3,3, '') # rural
            pdf.ellipse(113,58.5,3,3, 'F') # urbano
        elif ipm.inmueble=='Rural':
            pdf.ellipse(113,54,3,3, 'F') # rural
            pdf.ellipse(113,58.5,3,3, '') # urbano
        else:
            pdf.ellipse(113,54,3,3, '') # rural
            pdf.ellipse(113,58.5,3,3, '') # urbano

        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=16, h=10, txt='USO ACTUAL', border=1, fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.cell(w=26, h=5, txt='HABITADO', border='T', align='L')
        pdf.multi_cell(w=0, h=5, txt='NO HABITADO', border='TR')
        if ipm.usoactual=='Habitado':
            pdf.ellipse(155,54,3,3, 'F') # habitado
            pdf.ellipse(155,58.5,3,3, '') # bodega
            pdf.ellipse(185,54,3,3, 'F') # no habitado
            pdf.ellipse(185,58.5,3,3, 'F') # otro
        if ipm.usoactual=='Bodega':
            pdf.ellipse(155,54,3,3, '') # habitado
            pdf.ellipse(155,58.5,3,3, 'F') # bodega
            pdf.ellipse(185,54,3,3, '') # no habitado
            pdf.ellipse(185,58.5,3,3, '') # otro
        elif ipm.usoactual=='No Habitado':
            pdf.ellipse(155,54,3,3, '') # habitado
            pdf.ellipse(155,58.5,3,3, '') # bodega
            pdf.ellipse(185,54,3,3, 'F') # no habitado
            pdf.ellipse(185,58.5,3,3, '') # otro
        else:
            pdf.ellipse(155,54,3,3, '') # habitado
            pdf.ellipse(155,58.5,3,3, '') # bodega
            pdf.ellipse(185,54,3,3, '') # no habitado
            pdf.ellipse(185,58.5,3,3, 'F') # otro

        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=22, h=5, txt='LONGITUD', border=1, fill=True)
        pdf.cell(w=53, h=5, txt=ipm.longitud if hasattr(ipm, 'longitud') else '', border=1)
        pdf.set_xy(98, 58)
        pdf.cell(w=26, h=5, txt='URBANO', border='BL', align='L')
        pdf.set_xy(140, 58)
        pdf.cell(w=26, h=5, txt='BODEGA', border='B', align='L')
        pdf.multi_cell(w=0, h=5, txt='OTRO', border='BR')
        
        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=59, h=5, txt='EXISTENCIA DE OTRA VIVIENDA DENTRO DEL LOTE', border=1, align='L', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.cell(w=29, h=5, txt='      SI                NO   ', border=1, align='L')
        if ipm.existeotraviv=='Si':
            pdf.ellipse(77.5,63.6,3,3, 'F') # si
            pdf.ellipse(89.5,63.6,3,3, '') # no
        else:
            pdf.ellipse(77.5,63.6,3,3, '') # si
            pdf.ellipse(89.5,63.6,3,3, 'F') # no

        pdf.set_fill_color(232,221,221) # 2  
        pdf.cell(w=16, h=5, txt='USO ACTUAL', border=1, align='L', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.cell(w=0, h=5, txt='      HABITADO                 NO HABITADO', border=1, align='L', ln=1)
        if ipm.usoactualotv=='Habitado':
            pdf.ellipse(130.5,63.6,3,3, 'F') # habitado
            pdf.ellipse(155,63.6,3,3, '') # No habitado
        else:
            pdf.ellipse(130.5,63.6,3,3, '') # habitado
            pdf.ellipse(155,63.6,3,3, 'F') # No habitado

        pdf.ln(1)
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1
        pdf.cell(w=140, h=5, txt='2. INFRAESTRUCTURA DEL INMUEBLE', border=1, align='C', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.set_font('Arial', size=6)
        pdf.cell(w=5, h=5, txt='', border='LR')
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1
        pdf.multi_cell(w=51, h=5, txt='3. ESPACIOS ENCONTRADOS', border=1,  align='L', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.set_font('Arial', size=6)
        pdf.cell(w=37, h=3, txt='', border='LT')
        pdf.cell(w=18, h=3, txt='EXISTE', border='T', align='C')
        pdf.cell(w=25, h=3, txt='ESTADO', border='T', align='C')
        pdf.cell(w=60, h=3, txt='TIPO / SISTEMA CONSTRUCTIVO', border='TLR')
        pdf.cell(w=5, h=3, txt='', border='LR')
        pdf.cell(w=30, h=3, txt='', border='TL')
        pdf.cell(w=10, h=3, txt='', border='T')
        pdf.multi_cell(w=0, h=3, txt='', border='TR')
        pdf.cell(w=37, h=3, txt='', border='LB')
        pdf.cell(w=9, h=3, txt='SI', border='B', align='C')
        pdf.cell(w=9, h=3, txt='NO', border='B', align='C')
        pdf.cell(w=8, h=3, txt='B', border='B', align='C')
        pdf.cell(w=8, h=3, txt='R', border='B', align='C')
        pdf.cell(w=9, h=3, txt='D', border='B', align='C')
        pdf.cell(w=60, h=3, txt='', border='BRL')
        pdf.cell(w=5, h=3, txt='', border='LR')

        pdf.cell(w=30, h=3, txt='', border='L')
        pdf.cell(w=10, h=3, txt='SI', border='B', align='C')
        pdf.multi_cell(w=0, h=3, txt='NO', border='BR', align='C')
        #Fila 1
        y=80.5
        for inm in liip_data:
            #primer_elemento = inm[1]
            ex = inm["existe"]
            es= inm["estado"]
            tiposis=inm["tiposistema"]
            idif=inm["idif"]

            pdf.cell(w=37, h=4, txt=idif, border='LB', align='R')
            pdf.cell(w=9, h=4, txt='', border='B', align='C')#si
            pdf.cell(w=9, h=4, txt='', border='B', align='C')#no
            pdf.cell(w=8, h=4, txt='', border='B', align='C')#B
            pdf.cell(w=8, h=4, txt='', border='B', align='C')#R
            pdf.cell(w=9, h=4, txt='', border='B', align='C')#D
        
            pdf.multi_cell(w=60, h=4, txt=tiposis, border=1)
            #pdf.cell(w=5, h=4, txt='', border='LR')
            if (ex == 'Si'):
            #pdf->SetFillColor(200, 200, 200);
            #pdf->Ellipse(100, 100, 50, 30, 'F');
                pdf.ellipse(50,y,3,3, 'F')
                pdf.ellipse(59,y,3,3, '')
            else:
                pdf.ellipse(50,y,3,3, '')
                pdf.ellipse(59,y,3,3, 'F')
            
            if (es=='B'):           
                pdf.ellipse(68,y,3,3, 'F')
                pdf.ellipse(75,y,3,3, '')
                pdf.ellipse(84,y,3,3, '')
            elif(es=='R'):
                pdf.ellipse(68,y,3,3, '')
                pdf.ellipse(75,y,3,3, 'F')
                pdf.ellipse(84,y,3,3, '')
            else:
                pdf.ellipse(68,y,3,3, '')
                pdf.ellipse(75,y,3,3, '')
                pdf.ellipse(84,y,3,3, 'F')
            y=y+4

        #Espacios encontrados
        pdf.set_xy(155, 80)
        y=80.5
        for esp in lista_espacios_encontrados_datos:
            ex = esp["existe"]
            #es= inm["estado"]
            idif=esp["idif"]
            pdf.set_x(155)
            pdf.cell(w=30, h=4, txt=idif, border='LTB', align='R')
            pdf.cell(w=10, h=4, txt='', border='TB', align='C')
            pdf.multi_cell(w=0, h=4, txt='', border='TBR', align='C')

            if (ex=='Si'):
                pdf.ellipse(189,y,3,3, 'F')
                pdf.ellipse(199,y,3,3, '')
            else:
                pdf.ellipse(189,y,3,3, '')
                pdf.ellipse(199,y,3,3, 'F')
            y=y+4


        #Fila 2
        

        #para hacer el for y que las rueditas se vayan moviendo de posicion tiene que crear una variable y=80.5 e irle sumando 4 cada vez que recorra el for

        pdf.ln(4)
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1
        pdf.cell(w=27, h=5, txt='4. VIAS DE ACCESO', border=1, fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.set_font('Arial','',size=6)
        pdf.cell(w=126, h=5, txt='     CARRETERA / CALLE PAVIMENTADA                CALLE RURAL                SERVIDUMBRE                PASAJE PEATONAL   ', border=1)
        y=pdf.get_y()
        ty=y+0.8
        if(vias_acceso.tipovia=='Carretera / Calle Paviment'):
            pdf.ellipse(79.5,ty, 3,3, 'F') # calle pavimentada
            pdf.ellipse(103,ty,3,3, '') # calle rural
            pdf.ellipse(128,ty,3,3, '') # servidumbre
            pdf.ellipse(158,ty,3,3, '') # pasaje peatonal
        elif(vias_acceso.tipovia=='Calle Rural'):
            pdf.ellipse(79.5,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(103,ty,3,3, 'F') # calle rural
            pdf.ellipse(128,ty,3,3, '') # servidumbre
            pdf.ellipse(158,ty,3,3, '') # pasaje peatonal
        elif(vias_acceso.tipovia=='Servidumbre'):
            pdf.ellipse(79.5,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(103,ty,3,3, '') # calle rural
            pdf.ellipse(128,ty,3,3, 'F') # servidumbre
            pdf.ellipse(158,ty,3,3, '') # pasaje peatonal
        elif(vias_acceso.tipovia=='Pasaje Peatonal'):
            pdf.ellipse(79.5,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(103,ty,3,3, '') # calle rural
            pdf.ellipse(128,ty,3,3, '') # servidumbre
            pdf.ellipse(158,ty,3,3, 'F') # pasaje peatonal
        else:
            pdf.ellipse(79.5,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(103,ty,3,3, '') # calle rural
            pdf.ellipse(128,ty,3,3, '') # servidumbre
            pdf.ellipse(158,ty,3,3, '') # pasaje peatonal
        pdf.cell(w=0, h=5, txt='', border=0, ln=1)
        pdf.ln(2)
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.cell(w=67, h=4, txt='5. SERVICIOS BÁSICOS                                SI       NO  ', border=1,  align='L', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.set_font('Arial','',size=6)
        pdf.cell(w=5, h=2, txt='', border='LR')
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.cell(w=55, h=4, txt='6. INFRAESTRUCTURA                  SI       NO  ', border=1,  align='L', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.set_font('Arial','',size=6)
        pdf.cell(w=5, h=2, txt='', border='LR')
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.cell(w=64, h=4, txt='7. RIESGOS                                                SI        NO  ', border=1,  align='L', fill=True, ln=1)
        pdf.set_fill_color(0,0,0) # color negro  
        pdf.set_font('Arial','',size=6)
        pdf.cell(w=67, h=4, txt=' ', border=1,  align='L')
        pdf.cell(w=5, h=2, txt='', border='LR')
        pdf.cell(w=55, h=4, txt='', border=1,  align='L')
        pdf.cell(w=5, h=2, txt='', border='LR')
        tx=pdf.get_x()
        ty=pdf.get_y()
        y=ty+0.5
        rx=0
        ry=0
        for rie in lista_riesgos_datos:
            pdf.set_x(tx)
            ex = rie["existe"]
            #es= rie["estado"]
            idif=rie["idif"]
            pdf.multi_cell(w=64, h=4, txt=idif, border=1,  align='L')
            if(ex=='Si'):
                pdf.ellipse(190,y,3,3, 'F') # si
                pdf.ellipse(198,y,3,3, '') #no
            else:
                pdf.ellipse(190,y,3,3, '') # si
                pdf.ellipse(198,y,3,3, 'F') #no
            y=y+4
        pdf.set_x(tx)
        
        pdf.cell(w=48, h=4, txt='DISTANCIA A TALUDES(m)', border='LRT', align='L')
        pdf.cell(w=11, h=4, txt=str(riesgo_distancia.distaludes) or '0', border=1,  align='C')
        pdf.multi_cell(w=0, h=4, txt='', border='LRT',  align='C')
        pdf.set_x(tx)
        pdf.cell(w=48, h=4, txt='DISTANCIA A RIOS CERCANOS(m)', border='LR', align='L')
        pdf.cell(w=11, h=4, txt=str(riesgo_distancia.disriosc) or '0', border=1,  align='C')
        pdf.multi_cell(w=0, h=4, txt='', border='LR',  align='C')
        pdf.set_x(tx)
        pdf.cell(w=48, h=4, txt='DISTANCIA A LADERAS CERCANAS(m)', border='LR', align='L')
        pdf.cell(w=11, h=4, txt=str(riesgo_distancia.disladerasc) or '0', border=1,  align='C')
        pdf.multi_cell(w=0, h=4, txt='', border='LR',  align='C')
        pdf.set_x(tx)
        pdf.cell(w=48, h=4, txt='DISTANCIA A TORRES O ANTENAS(m)', border='LR', align='L')
        pdf.cell(w=11, h=4, txt=str(riesgo_distancia.distorresantenas) or '0', border=1,  align='C')
        pdf.multi_cell(w=0, h=4, txt='', border='LR',  align='C')
        pdf.set_x(tx)
        pdf.multi_cell(w=64, h=4, txt='', border='LRB',  align='L')
        pdf.set_y(ty+4)
        y=ty+4.5
        for ser in lista_servicios_basicos_datos:
            #pdf.set_x(tx)
            ex = ser["existe"]
            idif=ser["idif"]
            pdf.multi_cell(w=67, h=4, txt=idif, border=1,  align='L')
            if(ex=='Si'):
                pdf.ellipse(61,y,3,3, 'F') # si
                pdf.ellipse(69,y,3,3, '') # no
            else:
                pdf.ellipse(61,y,3,3, '') # si
                pdf.ellipse(69,y,3,3, 'F') #no
            y=y+4
            x=82
        pdf.set_xy(82,ty+4)  #ubicar la tabla en xy 
        y=ty+4.5  
        for inf in lista_infraetructura_datos:
            pdf.set_x(x)
            ex = inf["existe"]
            idif=inf["idif"]
            pdf.multi_cell(w=55, h=4, txt=idif, border=1,  align='L')
            if(ex=='Si'):
                pdf.ellipse(122.5,y,3,3, 'F') # si
                pdf.ellipse(130,y,3,3, '') # no
            else:
                pdf.ellipse(122.5,y,3,3, '') # si
                pdf.ellipse(130,y,3,3, 'F') # no
            y=y+4
        

        pdf.ln(2)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.multi_cell(w=127, h=4, txt='COMENTARIOS DE RELEVANCIA:', border=1, align='L', fill=True)
        pdf.set_fill_color(0,0,0) # color negro  
        #pdf.cell(w=5, h=2, txt='', border='LR')
        #pdf.cell(w=64, h=4, txt='7. RIESGOS                                                            SI         NO  ', border=1,  align='L', ln=1)
        
        pdf.cell(w=127, h=6, txt='', border=1, align='L')
        pdf.ln(4)
        y=pdf.get_y()
        pdf.set_y(y+4.5)

        pdf.set_fill_color(207,188,188) # 1 
        pdf.multi_cell(w=0, h=4, txt='8.PLAN DE MEJORAMIENTO DE VIVIENDA', border=1, align='C', fill=True)
        pdf.set_fill_color(232,221,221) # 2
        pdf.ln(1)
        i=1
        if (lista_plan):
            for plan in lista_plan:
                pdf.cell(w=15, h=5, txt='ETAPA '+ plan.etapas if hasattr(plan, 'etapas') else 'ETAPA '+ i, border=1, align='L', fill=True)
                pdf.multi_cell(w=0, h=5, txt=plan.descripcion if hasattr(plan, 'descripcion') else '', border=1, align='C')
                i=i+1
        else:
            for i in range(1,4):
                pdf.cell(w=15, h=5, txt= 'ETAPA '+ str(i), border=1, align='L', fill=True)
                pdf.multi_cell(w=0, h=5, txt='', border=1, align='C')
                i=i+1
        #pdf.cell(w=15, h=5, txt='ETAPA 2', border=1, align='L')
        #pdf.multi_cell(w=0, h=5, txt='', border=1, align='C')
        #pdf.cell(w=15, h=5, txt='ETAPA 3', border=1, align='L')
        #pdf.multi_cell(w=0, h=5, txt='', border=1, align='C')
        pdf.ln(2)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.multi_cell(w=0, h=4, txt='9.FACTIBILIDAD TECNICA DEL PROYECTO', border=1, align='C', fill=True)
        pdf.set_fill_color(0,0,0) # color negro
        pdf.ln(2)
        y=pdf.get_y()
        pdf.cell(w=32, h=4, txt='PROCEDE', border=0, align='C')
        pdf.cell(w=60, h=4, txt='PROCEDE CON CONDICIONAMIENTO', border=0, align='C')
        pdf.cell(w=32, h=4, txt='NO PROCEDE', border=0, align='C')
        pdf.multi_cell(w=0, h=4, txt=' PARA VALORACION COMO CASO ESPECIAL', border=0, align='C')
        y=y+0.5
        if (factibilida_tecnica.detalle =='Procede'):
            pdf.ellipse(17,y,3,3, 'F') # Procede
            pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(107,y,3,3, '') #  No Procede
            pdf.ellipse(143.5,y,3,3, '') # Para Caso Especial
        elif(factibilida_tecnica.detalle=='Procede con Condicionamiento'):
            pdf.ellipse(17,y,3,3, '') # Procede
            pdf.ellipse(48.5,y,3,3, 'F') # Procede con Condicionamiento
            pdf.ellipse(107,y,3,3, '') #  No Procede
            pdf.ellipse(143.5,y,3,3, '') # Para Caso Especial
        elif(factibilida_tecnica.detalle=='No Procede'):
            pdf.ellipse(17,y,3,3, '') # Procede
            pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(107,y,3,3, 'F') #  No Procede
            pdf.ellipse(143.5,y,3,3, '') # Para Caso Especial
        elif(factibilida_tecnica.detalle=='Para Caso Especial'):
            pdf.ellipse(17,y,3,3, '') # Procede
            pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(107,y,3,3, '') #  No Procede
            pdf.ellipse(143.5,y,3,3, 'F') # Para Caso Especial
        else:
            pdf.ellipse(17,y,3,3, '') # Procede
            pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(107,y,3,3, '') #  No Procede
            pdf.ellipse(143.5,y,3,3, '') # Para Caso Especial
        pdf.ln(4)
        pdf.set_fill_color(207,188,188) # 1  
        pdf.cell(w=175, h=4, txt='10. DESCRIPCIÓN DE MEJORAMIENTO ACORDADO CON EL CLIENTE', border=1, align='C', fill=True)   
        y=pdf.get_y()
        pdf.multi_cell(w=0, h=3, txt='DÍAS DE CONSTRUCCIÓN ESTIMADOS', border=1, align='C', fill=True)
        pdf.set_fill_color(0,0,0) # color negro
        pdf.set_y(y)
        
        pdf.multi_cell(w=175, h=14, txt=descripcion_mejora.descripcion if hasattr(descripcion_mejora, 'descripcion') else '', border=1, align='C')
        y=pdf.get_y()
        pdf.set_xy(185, y-5)
        pdf.multi_cell(w=0, h=5, txt=str(descripcion_mejora.diasestimados) if hasattr(descripcion_mejora, 'diasestimados') else '', border=1, align='C')
        pdf.ln(3)
        pdf.cell(w=70, h=3, txt='REALIZO LA INSPECCION', border='TLR')
        pdf.cell(w=25, h=3, txt='', border=0)
        pdf.cell(w=70, h=3, txt='ATENCIO LA VISITA', border=1)
        pdf.multi_cell(w=0, h=3, txt='', border=0, align='C')
        pdf.cell(w=70, h=6, txt='F:', border='LBR', align='L')
        pdf.cell(w=25, h=6, txt='', border=0)
        pdf.cell(w=70, h=6, txt='F:', border='LBR')
        pdf.multi_cell(w=0, h=6, txt='', border=0, align='C')
        pdf.cell(w=70, h=6, txt='NOMBRE:', border='LBR', align='L')
        pdf.cell(w=25, h=6, txt='', border=0)
        pdf.cell(w=70, h=6, txt='NOMBRE:', border='LBR')
        pdf.multi_cell(w=0, h=6, txt='', border=0, align='C')
        pdf.cell(w=70, h=6, txt='DUI:', border='LBR', align='L')
        pdf.cell(w=25, h=6, txt='', border=0)
        pdf.cell(w=70, h=6, txt='DUI:', border='LBR')
        pdf.multi_cell(w=0, h=6, txt='', border=0, align='C')
        
        pdf.add_page()

        pdf.set_margins(10,20,10)
        pdf.ln()
        pdf.cell(w=0, h=6, txt='9. ESQUEMA DE UBICACION DEL SITIO', border=1, align='C', ln=1)
         #Margenes de la pagina

        pdf.rect(10, 22,196,250)
        pdf.set_line_width(0.1)

        try:  
            # Agregar la imagen desde la instancia pil
            img_path = pim.esquema.path # Asumiendo que es un campo FileField o ImageField
            x = 11  # Coordenada horizontal 
            y = 25  # Coordenada vertical... arriba
            w = 194 # Ancho de la imagen en puntos
            h = 100  # Altura de la imagen en puntos
            pdf.image(img_path , x=x, y=y, w=w, h=h)
        except:
            pass
        
        pdf.set_y(140)
        pdf.cell(w=0, h=6, txt='. ESQUEMA DE UBICACION DEL SITIO', border=1, align='C', ln=1)

        try:  
            # Agregar la imagen desde la instancia pil
            img_path = imgpil.imagen.path # Asumiendo que es un campo FileField o ImageField
            x = 11  # Coordenada horizontal 
            y = 150  # Coordenada vertical... arriba
            w = 194 # Ancho de la imagen en puntos
            h = 110  # Altura de la imagen en puntos
            pdf.image(img_path , x=x, y=y, w=w, h=h)
        except:
            pass
        #pdf.set_fill_color(0,0,0) # agrega color a la ruedita
        #pdf.ellipse(10,10,5,5, 'F') # x, y, ancho, alto ... con la F toma el color 
            
        pdf.output('InspeccionMV.pdf', 'F')
        return FileResponse(open('InspeccionMV.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

