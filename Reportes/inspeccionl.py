import json
from fpdf import FPDF
from datetime import date
import locale
from ClienteApp.models import *
from django.http import FileResponse
from SolicitudesApp.models import *
from InspeccionLoteApp.models import *


class InspeccionL(FPDF):
    
    def inspeccionL(request, id):

        try:
            ipm=  Inspeccionl.objects.get(id=id)
        except Inspeccionl.DoesNotExist:
            ipm=""
        try:
            s=  solicitud.objects.get(id=ipm.ids.id)
        except solicitud.DoesNotExist:
            s=""
        
        try:
            do= datosObra.objects.get(idSolicitud=ipm.ids.id)
        except datosObra.DoesNotExist:
            do=""
        
        try:
            vias_acceso= ViasAccesoipl.objects.get(idipl=ipm)
        except ViasAccesoipl.DoesNotExist:
            vias_acceso=""

        try:
            riesgo_distancia= Riesgosipl.objects.get(idipl=ipm)
        except Riesgosipl.DoesNotExist:
            riesgo_distancia=""

        try:
            factibilida_tecnica= Factibilidadipl.objects.get(idipl=ipm)
        except Factibilidadipl.DoesNotExist:
            factibilida_tecnica=""

        try:
            descripcion_proyecto= DescripcionProyectoipl.objects.get(idipl=ipm)
        except DescripcionProyectoipl.DoesNotExist:
            descripcion_proyecto=""

        try:
            resp_sol=ResponSolicitanteipl.objects.get(idipl=ipm)
        except ResponSolicitanteipl.DoesNotExist:
            resp_sol=""

        try:
            comentarios= ComentariosObsipl.objects.get(idipl=ipm)
        except ComentariosObsipl.DoesNotExist:
            comentarios=""     

        try:
            liip=Inspeccionlcisr.objects.filter(idip=ipm.id)
        except liip.DoesNotExist:
            liip=""
        liip_data = [
            {
                'existe': item.existe,
                'id': item.id,
                'idif':item.idif.nombre,
            }
            for item in liip
            ]      

        lista_general=Inspeccionlcisr.objects.filter(idip=ipm.id)

        lista_espacios_construcciones=[]
        for item in lista_general:
            if item.idif.tipo == "2":
                lista_espacios_construcciones.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})
        
        lista_infraetructura_datos=[]
        for item in lista_general:
            if item.idif.tipo == "3":
                lista_infraetructura_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})
        
       
        lista_saneamiento_datos=[]
        for item in lista_general:
            if item.idif.tipo == "4":
                lista_saneamiento_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})
             
        lista_servicios_basicos_datos=[]
        for item in lista_general:
            if item.idif.tipo == "5":
                lista_servicios_basicos_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})
        
        lista_riesgos_datos=[]
        for item in lista_general:
            if item.idif.tipo == "6":
                lista_riesgos_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.idif.nombre,})
        

        
        locale.setlocale(locale.LC_TIME, 'es_ES')    
        pdf=FPDF(orientation='P', unit='mm', format='Letter') 
        pdf.add_page()
        
            
        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=7, y=1, w=40, h=28)#, link=url)
        pdf.set_font('Arial', 'B', 9)      
        pdf.set_x(50)
        
        pdf.set_fill_color(207,188,188) # 1   
        pdf.multi_cell(w=140, h=5, txt='HOJA DE INSPECCIÓN PARA LOTE', border=1, align='C', fill=True)
        pdf.set_x(50)
        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=20,h=8, txt='Agencia', border=1, fill=True)
        pdf.cell(w=50, h=8, txt=s.perfil.Agencia.nombre, border=1)
        pdf.cell(w=15, h=4, txt='DIA', border=1, fill=True)
        pdf.cell(w=25, h=4, txt='MES', border=1, fill=True)
        pdf.cell(w=15, h=4, txt='AÑO', border=1, fill=True)
        pdf.multi_cell(w=15, h=4, txt='HORA', border=1, fill=True)
        pdf.set_xy(120, 19) # para ubicar el multicel
        
        pdf.cell(w=55, h=4, txt= ipm.fecha.strftime("%A, %d de %B de %Y") if hasattr(ipm, 'fecha') else '' , border='TBR', align='C')
        pdf.multi_cell(w=15, h=4, txt=str(ipm.hora) if hasattr(ipm, 'hora') else '', border=1)
        pdf.ln(2)
        pdf.set_fill_color(207,188,188) # 1 
        pdf.multi_cell(w=0, h=5, txt='1. INFORMACIÓN GENERAL', border=1, align='C', fill=True)
        
        pdf.set_font('Arial', size=6)
        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=22, h=5, txt='SOLICITANTE', border=1 , fill=True)
        pdf.cell(w=121, h=5, txt=(s.perfil.nombres if hasattr(s.perfil, 'nombres') else '') +' '+ (s.perfil.apellidos if hasattr(s.perfil, 'apellidos') else ''), border=1)
        pdf.cell(w=19, h=5, txt='TELÉFONOS:', border='TL', fill=True)
        pdf.multi_cell(w=0, h=5, txt=(ipm.telefonop  if hasattr(ipm.telefonop, 'nombres') else '')+''+ (ipm.telefonos if hasattr(ipm.telefonos, 'nombres') else ''), border='TR')
        pdf.cell(w=25, h=5, txt='GRUPO FAMILIAR', border='TBL', align='C' , fill=True)
        pdf.cell(w=25, h=5, txt='TERCERA EDAD:', border='BT')
        pdf.cell(w=5, h=5, txt=ipm.terceraedad if hasattr(ipm, 'terceraedad') else '', border='BT')
        pdf.cell(w=17, h=5, txt='ADULTOS:', border='BT')
        pdf.cell(w=5, h=5, txt=ipm.adultos if hasattr(ipm, 'adultos') else '', border='BT')
        pdf.cell(w=13, h=5, txt='NIÑOS:', border='BT')
        pdf.cell(w=5, h=5, txt=ipm.ninos if hasattr(ipm, 'ninos') else '', border='BT')
        pdf.cell(w=48, h=5, txt='PERSONAS CON DISCAPACIDAD:', border='BT', align='C')
        pdf.multi_cell(w=0, h=5, txt=ipm.personadisc if hasattr(ipm, 'personadisc') else '', border='BTLR')
        #pdf.multi_cell(w=0, h=5, txt=ipm.telefonos, border='BLR')
        pdf.cell(w=22, h=8, txt='DIRECCIÓN', border=1, fill=True)
        pdf.cell(w=110, h=8, txt=str(do.direExacta) if hasattr(do, 'direExacta') else '', border=1)
        pdf.cell(w=0, h=4, txt='MUNICIPIO', border=1 , fill=True)
        pdf.set_xy(142, 44)
        pdf.multi_cell(w=0, h=4, txt=s.perfil.municipio.distri if hasattr(s, 'perfil') else '', border=1)
        
        pdf.cell(w=40, h=5, txt='PROPIETARIO DEL TERRENO', border=1, fill=True)
        pdf.multi_cell(w=0, h=5, txt=ipm.propietarioter if hasattr(ipm, 'propietarioter') else '' , border=1)
        pdf.cell(w=70, h=5, txt='LATITUD/LONGITUD', border=1, align='C' , fill=True)
        
        pdf.cell(w=25, h=10, txt='INMUEBLE', border=1, align='C', fill=True)
        pdf.cell(w=30, h=5, txt='RURAL', border='TL', align='L')
        pdf.set_fill_color(0,0,0) # color negro   
        if ipm.inmueble=='Urbano':
            pdf.ellipse(120,54,3,3, '') # rural
            pdf.ellipse(120,58.5,3,3, 'F') # urbano
        elif ipm.inmueble=='Rural':
            pdf.ellipse(120,54,3,3, 'F') # rural
            pdf.ellipse(120,58.5,3,3, '') # urbano
        else:
            pdf.ellipse(120,54,3,3, '') # rural
            pdf.ellipse(120,58.5,3,3, '') # urbano

        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=55, h=5, txt='EXISTEN OTRAS VIVIENDAS', border=1, align='C' , fill=True)
        
        pdf.multi_cell(w=0, h=5, txt=ipm.existeotraviv if hasattr(ipm, 'existeotraviv') else '', border=1, align='C')
        pdf.cell(w=70, h=5, txt=ipm.latitud +'; '+ipm.longitud, border=1, align='C')
        
        pdf.set_xy(105, 58)
        pdf.cell(w=30, h=5, txt='URBANO', border='BL', align='L')
        pdf.set_xy(135, 58)
        pdf.cell(w=55, h=5, txt='TERRENO AGRICOLA', border=1, align='C' , fill=True)
        pdf.multi_cell(w=0, h=5, txt=ipm.terrenoagricola if hasattr(ipm, 'terrenoagricola') else '', border=1, align='C')
        
        
        pdf.cell(w=80, h=5, txt='DIMENSIONES DISPONIBLES PARA CONSTRUIR VIVIENDA', border=1, align='L', fill=True)
        pdf.cell(w=20, h=5, txt='ANCHO(M):', border=1, align='L')
        pdf.cell(w=20, h=5, txt=ipm.anchocv if hasattr(ipm, 'ancchocv') else '', border=1, align='C')
        pdf.cell(w=20, h=5, txt='LARGO(M):', border=1, align='L')
        pdf.cell(w=20, h=5, txt=ipm.largocv if hasattr(ipm, 'largocv') else '', border=1, align='C')
        pdf.cell(w=20, h=5, txt='AREA(M2):', border=1, align='L')
        pdf.multi_cell(w=0, h=5, txt=ipm.areacv if hasattr(ipm, 'areacv') else '', border=1, align='C')
        pdf.cell(w=80, h=5, txt='DIMENSIONES DISPONIBLES PARA AMPLIACIONES FUTURAS', border=1, align='L', fill=True)
        pdf.cell(w=20, h=5, txt='ANCHO(M):', border=1, align='L')
        pdf.cell(w=20, h=5, txt=ipm.anchoaf if hasattr(ipm, 'anchoaf') else '', border=1, align='C')
        pdf.cell(w=20, h=5, txt='LARGO(M):', border=1, align='L')
        pdf.cell(w=20, h=5, txt=ipm.largoaf if hasattr(ipm, 'largoaf') else '', border=1, align='C')
        pdf.cell(w=20, h=5, txt='AREA(M2):', border=1, align='L')
        pdf.multi_cell(w=0, h=5, txt=ipm.areaaf if hasattr(ipm, 'areaaf') else '', border=1, align='C')
        pdf.ln(2)
        
        pdf.ln(1)
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1 
        pdf.cell(w=55, h=5, txt='2. CONSTRUCCIONES', border=1, align='L', fill=True)      
        pdf.cell(w=7.5, h=5, txt='SI', border='LBT', align='C', fill=True)
        pdf.cell(w=7.5, h=5, txt='NO', border='TBR', align='C', fill=True)
        #pdf.set_font('Arial', size=6)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.cell(w=3, h=5, txt='', border='LR')
        txi=pdf.get_x()
        pdf.set_fill_color(207,188,188) # 1 
        pdf.cell(w=45, h=5, txt='3. INFRAESTRUCTURA', border=1, align='C', fill=True)
        pdf.cell(w=7.5, h=5, txt='SI', border='LBT', align='C', fill=True)
        pdf.cell(w=7.5, h=5, txt='NO', border='TBR', align='C', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.set_font('Arial','B',size=7)
        pdf.cell(w=3, h=5, txt='', border='LR')
        txs=pdf.get_x()
        pdf.set_fill_color(207,188,188) # 1 
        pdf.cell(w=40, h=5, txt='4. SANEAMIENTO', border=1,  align='L', fill=True)
        pdf.cell(w=7.5, h=5, txt='SI', border='LBT', align='C', fill=True)
        pdf.multi_cell(w=0, h=5, txt='NO', border='TBR', align='C', fill=True)
        
        pdf.set_fill_color(0,0,0) # color negro 
        #Fila 1
        ty=pdf.get_y()
        y=pdf.get_y()
        
        #### TABLA CONSTRUCCIONES
        for esp in lista_espacios_construcciones:
            ex = esp["existe"]
            idif=esp["idif"]
            
            pdf.cell(w=55, h=4, txt=idif, border='LTB', align='L')
            pdf.cell(w=7.5, h=4, txt='', border='LBT', align='C')
            pdf.multi_cell(w=7.5, h=4, txt='', border='TBR', align='C')
            

            if (ex=='Si'):
                pdf.ellipse(67,y+0.5,3,3, 'F')
                pdf.ellipse(75,y+0.5,3,3, '')
            else:
                pdf.ellipse(67,y+0.5,3,3, '')
                pdf.ellipse(75,y+0.5,3,3, 'F')
            y=y+4

        ##### TABLA INFRAESTRUCTURA
        pdf.set_xy(txi, ty)
        y=ty
        for esp in lista_infraetructura_datos:
            ex = esp["existe"]
            
            idif=esp["idif"]
            pdf.set_x(txi)
            pdf.cell(w=45, h=4, txt=idif, border='LTB', align='L')
            pdf.cell(w=7.5, h=4, txt='', border='LBT', align='C')
            pdf.multi_cell(w=7.5, h=4, txt='', border='TBR', align='C')
            
            if (ex=='Si'):
                pdf.ellipse(130,y+0.5,3,3, 'F')
                pdf.ellipse(138,y+0.5,3,3, '')
            else:
                pdf.ellipse(130,y+0.5,3,3, '')
                pdf.ellipse(138,y+0.5,3,3, 'F')
            y=y+4


        #### TABLA SANEAMIENTO
        pdf.set_xy(txs, ty)
        y=ty
        for esp in lista_saneamiento_datos:
            ex = esp["existe"]
            #es= inm["estado"]
            idif=esp["idif"]
            pdf.set_x(txs)
            pdf.cell(w=40, h=4, txt=idif, border='LTB', align='L')
            pdf.cell(w=7.5, h=4, txt='', border='LBT', align='C')
            pdf.multi_cell(w=0, h=4, txt='', border='TBR', align='C')
            

            if (ex=='Si'):
                pdf.ellipse(188,y+0.5,3,3, 'F')
                pdf.ellipse(198,y+0.5,3,3, '')
            else:
                pdf.ellipse(188,y+0.5,3,3, '')
                pdf.ellipse(198,y+0.5,3,3, 'F')
            y=y+4

        #Fila 2
        

        #para hacer el for y que las rueditas se vayan moviendo de posicion tiene que crear una variable y=80.5 e irle sumando 4 cada vez que recorra el for

        pdf.ln(2)

        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(207,188,188) # 1 
        pdf.cell(w=55, h=5, txt='5. SERVICIOS BASICOS', border=1, align='L', fill=True)
        pdf.cell(w=7.5, h=5, txt='SI', border='LBT', align='C', fill=True)
        pdf.cell(w=7.5, h=5, txt='NO', border='TBR', align='C', fill=True)
        #pdf.set_font('Arial', size=6)
        pdf.set_fill_color(0,0,0) # color negro
        pdf.cell(w=3, h=5, txt='', border='LR')
        txi=pdf.get_x()
        pdf.set_fill_color(207,188,188) # 1 
        pdf.cell(w=45, h=5, txt='6. RIESGOS', border=1, align='C', fill=True)
        pdf.cell(w=7.5, h=5, txt='SI', border='LBT', align='C', fill=True)
        pdf.cell(w=7.5, h=5, txt='NO', border='TBR', align='C', fill=True)
        pdf.set_fill_color(0,0,0) # color negro
        pdf.set_font('Arial','B',size=7)  
        pdf.cell(w=3, h=5, txt='', border='LR')
        txs=pdf.get_x()
        pdf.set_fill_color(207,188,188) # 1 
        pdf.multi_cell(w=0, h=5, txt=' COMENTARIOS / OBSERVACIONES', border=1,  align='L', fill=True)

        pdf.set_fill_color(0,0,0) # color negro       
        #### TABLA CONSTRUCCIONES
        ty=pdf.get_y()
        y=ty
        for esp in lista_servicios_basicos_datos:
            ex = esp["existe"]
            #es= inm["estado"]
            idif=esp["idif"]
            #pdf.set_x(155)
            pdf.cell(w=55, h=4, txt=idif, border='LTB', align='L')
            pdf.cell(w=7.5, h=4, txt='', border='LBT', align='C')
            pdf.multi_cell(w=7.5, h=4, txt='', border='TBR', align='C')
            

            if (ex=='Si'):
                pdf.ellipse(67,y+0.5,3,3, 'F')
                pdf.ellipse(75,y+0.5,3,3, '')
            else:
                pdf.ellipse(67,y+0.5,3,3, '')
                pdf.ellipse(75,y+0.5,3,3, 'F')
            y=y+4
        pdf.multi_cell(w=70, h=5, txt='', border=1,  align='L')
        pdf.multi_cell(w=70, h=15, txt='', border=1,  align='L')
        ys=pdf.get_y()

        pdf.set_xy(txi, ty)
        y=ty
        for esp in lista_riesgos_datos:
            ex = esp["existe"]
            #es= inm["estado"]
            idif=esp["idif"]
            pdf.set_font('Arial','',size=6)
            pdf.set_x(txi)
            pdf.cell(w=45, h=4, txt=idif, border='LTB', align='L')
            pdf.cell(w=7.5, h=4, txt='', border='LBT', align='C')
            pdf.multi_cell(w=7.5, h=4, txt='', border='TBR', align='C')
            
            if (ex=='Si'):
                pdf.ellipse(130,y+0.5,3,3, 'F')
                pdf.ellipse(138,y+0.5,3,3, '')
            else:
                pdf.ellipse(130,y+0.5,3,3, '')
                pdf.ellipse(138,y+0.5,3,3, 'F')
            y=y+4
        
        pdf.set_x(txi)
        
        pdf.cell(w=45, h=4, txt='DISTANCIA A TALUDES(m)', border='LRT', align='L')
        pdf.multi_cell(w=15, h=4, txt=str(riesgo_distancia.distaludes) or '0', border=1,  align='C')
        
        pdf.set_x(txi)
        pdf.cell(w=45, h=4, txt='DISTANCIA A RIOS CERCANOS(m)', border='LR', align='L')
        pdf.multi_cell(w=15, h=4, txt=str(riesgo_distancia.disriosc) or '0', border=1,  align='C')
        
        pdf.set_x(txi)
        pdf.cell(w=45, h=4, txt='DISTANCIA A LADERAS CERCANAS(m)', border='LR', align='L')
        pdf.multi_cell(w=15, h=4, txt=str(riesgo_distancia.disladerasc) or '0', border=1,  align='C')
        
        pdf.set_x(txi)
        pdf.cell(w=45, h=4, txt='DISTANCIA A TORRES O ANTENAS(m)', border='LR', align='L')
        pdf.cell(w=15, h=4, txt=str(riesgo_distancia.distorresantenas) or '0', border=1,  align='C')
        
        pdf.set_x(txi)
        pdf.multi_cell(w=60, h=4, txt='', border='LRB',  align='L')
        yr=pdf.get_y()
        

        pdf.set_xy(txs, ty)
        y=ty
        pdf.multi_cell(w=0, h=4, txt=comentarios.comentario if hasattr(comentarios, 'comentario') else '', border='LTR', align='L')
        pdf.set_x(txs)
        pdf.multi_cell(w=0, h=4, txt=comentarios.observaciones if hasattr(comentarios, 'observaciones') else '', border='LRB', align='L')
        yc=pdf.get_y()
       
        if ys>yr and ys>yc:
            y=ys
        elif yr>ys and yr>yc:
            y=yr
        else:
            y=yc
        pdf.set_y(y)
        pdf.ln(2)
        pdf.set_font('Arial','B',size=7)
        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=27, h=5, txt='7. VIAS DE ACCESO', border='TLB', fill=True)
        pdf.set_font('Arial','',size=7)
        pdf.set_fill_color(0,0,0) # color negro 
        y=pdf.get_y()
        pdf.multi_cell(w=0, h=5, txt='                  CARRETERA / CALLE PAVIMENTADA                      CALLE RURAL                     SERVIDUMBRE                       PASAJE PEATONAL   ', border='TBR')
        
        ty=y+1
        if(vias_acceso.tipovia=='Carretera / Calle Paviment'):
            pdf.ellipse(46,ty, 3,3, 'F') # calle pavimentada
            pdf.ellipse(105,ty,3,3, '') # calle rural
            pdf.ellipse(136,ty,3,3, '') # servidumbre
            pdf.ellipse(170,ty,3,3, '') # pasaje peatonal
        elif(vias_acceso.tipovia=='Calle Rural'):
            pdf.ellipse(46,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(105,ty,3,3, 'F') # calle rural
            pdf.ellipse(136,ty,3,3, '') # servidumbre
            pdf.ellipse(170,ty,3,3, '') # pasaje peatonal
        elif(vias_acceso.tipovia=='Servidumbre'):
            pdf.ellipse(46,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(105,ty,3,3, '') # calle rural
            pdf.ellipse(136,ty,3,3, 'F') # servidumbre
            pdf.ellipse(170,ty,3,3, '') # pasaje peatonal
        elif(vias_acceso.tipovia=='Pasaje Peatonal'):
            pdf.ellipse(46,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(105,ty,3,3, '') # calle rural
            pdf.ellipse(136,ty,3,3, '') # servidumbre
            pdf.ellipse(170,ty,3,3, 'F') # pasaje peatonal
        else:
            pdf.ellipse(46,ty, 3,3, '') # calle pavimentada
            pdf.ellipse(105,ty,3,3, '') # calle rural
            pdf.ellipse(136,ty,3,3, '') # servidumbre
            pdf.ellipse(170,ty,3,3, '') # pasaje peatonal
        #pdf.cell(w=0, h=5, txt='', border=0, ln=1)
        #pdf.ln(2)
        pdf.set_font('Arial','B',size=7)
       
        
        pdf.ln(2)
        pdf.set_fill_color(207,188,188) # 1 
        pdf.multi_cell(w=0, h=4, txt='8.FACTIBILIDAD TECNICA DEL PROYECTO', border=1, align='C', fill=True)
        
        pdf.set_fill_color(0,0,0) # color negro 
        y=pdf.get_y()
        pdf.cell(w=10, h=4, txt='', border='TLB', align='C')
        pdf.cell(w=60, h=4, txt='PROCEDE', border='TB', align='L')
        
        pdf.cell(w=50, h=4, txt='NO PROCEDE', border='TB', align='C')
        pdf.multi_cell(w=0, h=4, txt=' PARA CASO ESPECIAL', border='TBR', align='C')
        y=y+0.5
        if (factibilida_tecnica.detalle =='Procede'):
            pdf.ellipse(17,y,3,3, 'F') # Procede
            #pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(92,y,3,3, '') #  No Procede
            pdf.ellipse(150.5,y,3,3, '') # Para Caso Especial
        
        elif(factibilida_tecnica.detalle=='No Procede'):
            pdf.ellipse(17,y,3,3, '') # Procede
            #pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(92,y,3,3, 'F') #  No Procede
            pdf.ellipse(150.5,y,3,3, '') # Para Caso Especial
        elif(factibilida_tecnica.detalle=='Para Caso Especial'):
            pdf.ellipse(17,y,3,3, '') # Procede
            #pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(92,y,3,3, '') #  No Procede
            pdf.ellipse(150.5,y,3,3, 'F') # Para Caso Especial
        else:
            pdf.ellipse(17,y,3,3, '') # Procede
            #pdf.ellipse(48.5,y,3,3, '') # Procede con Condicionamiento
            pdf.ellipse(92,y,3,3, '') #  No Procede
            pdf.ellipse(150.5,y,3,3, '') # Para Caso Especial

        pdf.ln(4)
        pdf.set_fill_color(207,188,188) # 1 
        pdf.multi_cell(w=0, h=4, txt='9. DESCRIPCIÓN DELPROYECTO', border=1, align='C', fill=True)
        pdf.set_fill_color(232,221,221) # 2
        pdf.cell(w=60, h=4, txt='MODELO DE VIVIENDA A CONSTRUIR', border=1, align='C', fill=True)
        pdf.multi_cell(w=0, h=4, txt=descripcion_proyecto.modeloviviedac if hasattr(descripcion_proyecto, 'modeloviviedac') else '', border=1, align='C')
        pdf.cell(w=60, h=4, txt='SOLUCION SANITARIA PROPUESTA', border=1, align='C', fill=True)
        pdf.multi_cell(w=0, h=4, txt=descripcion_proyecto.solucionsanitariap if hasattr(descripcion_proyecto, 'solucionsanitariap') else '', border=1, align='C')
        pdf.cell(w=60, h=4, txt='OBRAS ADICIONALES A CONSTRUIR', border=1, align='C', fill=True)
        x=pdf.get_x()
        pdf.multi_cell(w=0, h=4, txt=descripcion_proyecto.obrasadicionalesconst if hasattr(descripcion_proyecto, 'obrasadicionalesconst') else '', border=1, align='C')
        y=pdf.get_y()
        pdf.multi_cell(w=60, h=4, txt='OBSERVACIONES TECNICAS GENERALES Y/O CONDICIONAMIENTOS', border=1, align='C', fill=True)
        pdf.set_xy(x, y)
        pdf.multi_cell(w=0, h=8, txt=descripcion_proyecto.observtecnicas if hasattr(descripcion_proyecto, 'observtecnicas') else '', border=1, align='C')
        pdf.multi_cell(w=0, h=4, txt='DESCRIPCION DE ACTIVIDADES BAJO LA RESPONSABILIDAD DEL FUTURO PROPIETARIO ANTES DE INICIAR LA CONSTRUCCION:', border=1, align='C', fill=True)
        pdf.multi_cell(w=0, h=4, txt=descripcion_proyecto.actividadbrfp if hasattr(descripcion_proyecto, 'actividadbrfp') else '', border=1, align='C', fill=False)
        pdf.set_fill_color(207,188,188) # 1 
        pdf.multi_cell(w=0, h=4, txt='10. RESPONSABILIDADES DEL SOLICITANTE (EL O LA SOLICITANTE SE COMPROMETE A FACILITAR):', border=1, align='C', fill=True)
        pdf.set_fill_color(0,0,0) # color negro 
        pdf.set_font('Arial','',size=6)
        pdf.cell(w=40, h=4, txt='MOJONES DEL LOTE', border=1, align='C')
        y=pdf.get_y()
        pdf.cell(w=20, h=4, txt='SI  /  NO', border=1, align='C')
        pdf.cell(w=70, h=4, txt='RESGUARDO DE MATERIALES Y HERRAMIENTAS', border=1, align='C')
        pdf.cell(w=20, h=4, txt='SI  /  NO', border=1, align='C')
        pdf.cell(w=30, h=4, txt='AGUA POTABLE', border=1, align='C')
        pdf.multi_cell(w=0, h=4, txt='SI  /  NO', border=1, align='C')
        if resp_sol.mojoneslote == 'Si':
            pdf.ellipse(55,y,4,4, '')
        else:
            pdf.ellipse(60.5,y,4,4, '')
        
        if resp_sol.resguardomather == 'Si':
            pdf.ellipse(145,y,4,4, '')
        else:
            pdf.ellipse(150.5,y,4,4, '')

        if resp_sol.aguapotable == 'Si':
            pdf.ellipse(193,y,4,4, '')
        else:
            pdf.ellipse(198.5,y,4,4, '')
        pdf.cell(w=40, h=4, txt='LINDEROS DEL LOTE', border=1, align='C')
        y=pdf.get_y()
        pdf.cell(w=20, h=4, txt='SI  /  NO', border=1, align='C')
        pdf.cell(w=70, h=4, txt='AUXILIARES DE CONSTRUCCION', border=1, align='C')
        pdf.cell(w=20, h=4, txt='SI  /  NO', border=1, align='C')
        pdf.cell(w=30, h=4, txt='ENERGIA ELECTRICA', border=1, align='C')
        pdf.multi_cell(w=0, h=4, txt='SI  /  NO', border=1, align='C')
        #pdf.set_y(y)
        if resp_sol.linderoslote == 'Si':
            pdf.ellipse(55,y,4,4, '')
        else:
            pdf.ellipse(60.5, y,4,4, '')

        if resp_sol.auxiliaresconst == 'Si':
            pdf.ellipse(145,y,4,4, '')
        else:
            pdf.ellipse(150.5,y,4,4, '')
        
        if resp_sol.energiaelectrica== 'Si':
            pdf.ellipse(193,y,4,4, '')
        else:
            pdf.ellipse(198.5,y,4,4, '')
            
        
        pdf.ln(3)
        pdf.cell(w=70, h=3, txt='REALIZO LA INSPECCION', border='TLR')
        pdf.cell(w=25, h=3, txt='', border=0)
        pdf.cell(w=70, h=3, txt='ATENDIO LA VISITA', border=1)
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
        
        

        #pdf.set_fill_color(0,0,0) # agrega color a la ruedita
        #pdf.ellipse(10,10,5,5, 'F') # x, y, ancho, alto ... con la F toma el color 
            
        pdf.output('InspeccionLV.pdf', 'F')
        return FileResponse(open('InspeccionLV.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

