import json
from django.shortcuts import render, redirect
from django.contrib import messages
from ConfiguracionApp.models import *
from InspeccionMejViviendaApp.models import *
from ListaChequeoApp.models import listaChequeo
from django.http import JsonResponse
from TesisApp.views import registroBit

# Create your views here.


def inspeccion(request, id ): 
    sol= InspeccionM.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    if sol == True:
        solv= InspeccionM.objects.get(ids=id)
    
        return redirect('editarIM', id=solv.id)   
    else:
        try:
            s=  solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s=""
        
    
        try:
            listaii=Infraestructura.objects.filter(tipo=2,tipolm="Mejora",estado="activo")
        except listaii.DoesNotExist:
            listaii=""

        try:
            listaee=Infraestructura.objects.filter(tipo=3,tipolm="Mejora",estado="activo")
        except listaee.DoesNotExist:
            listaee=""
        
        try:
            listava=Infraestructura.objects.filter(tipo=4,tipolm="Mejora",estado="activo")
        except listava.DoesNotExist:
            listava=""

        try:
            listasb=Infraestructura.objects.filter(tipo=5,tipolm="Mejora",estado="activo")
        except listasb.DoesNotExist:
            listasb=""
        
        try:
            listaif=Infraestructura.objects.filter(tipo=6,tipolm="Mejora",estado="activo")
        except listaif.DoesNotExist:
            listaif=""
        
        try:
            listar=Infraestructura.objects.filter(tipo=7,tipolm="Mejora",estado="activo")
        except listar.DoesNotExist:
            listar=""

        try:
            do= datosObra.objects.get(idSolicitud=id)
        except datosObra.DoesNotExist:
            do=""

    

        return render(request, "InspeccionMejViviendaApp/inspeccion.html", {"s":s,"listaii":listaii,"listaee":listaee,"listava":listava,"listasb":listasb,"listaif":listaif,"listar":listar,"do":do}) 

  
  
def registrarDIM(request): 
    
    if request.is_ajax and request.method == "POST":
            dtig =json.loads(request.POST.get('valoresifm'))
            print(dtig)
            for objif in dtig:
                ids=objif['ids']
                fecha=objif['fecham']
                hora=objif['horam']
                telp=objif['telpm']
                tels=objif['telsm']
                terceraed=objif['terceraedm']
                adultos=objif['adultosm']
                ninos=objif['ninosm']
                personadis=objif['personadism']
                propietarioinm=objif['propietarioinmm']
                parentescosm=objif['parentescosm']
                latitud=objif['latitudm']
                longitud=objif['longitudm']
                inmueble=objif['inmueblem']
                usoact=objif['usoactm']
                exotrav=objif['exotravm']
                usoacotv=objif['usoacotvm']
                comentariosrl=objif['comentariosrl']
                
                
                print(ids)
                print(fecha)

                idsol= solicitud.objects.get(id=ids)
                idsol.id=ids

                inspeccionM=InspeccionM.objects.create(fecha=fecha,hora=hora,telefonop=telp,telefonos=tels,terceraedad=terceraed,adultos=adultos,ninos=ninos,personadisc=personadis,propietarioinm=propietarioinm,parentescosol=parentescosm,latitud=latitud,longitud=longitud,inmueble=inmueble,usoactual=usoact,existeotraviv=exotrav,usoactualotv=usoacotv,comentariosrelv=comentariosrl,ids=idsol)             
                registroBit(request, "Se registro formulario Inspeccion de Mejora " + idsol.perfil.dui, "Registro")
                #print(hora)
                #print(telp)
            
   
            idipm= InspeccionM.objects.all().last() #obtengo la ultima solicitud registrada 
    # idip= Inspeccionl.objects.get(id=4)

      #inicia Infraestructura de Imnueble
    
            data =json.loads( request.POST.get('valoresidi'))
            print(data)
            for obj in data:
                idc=obj['id']
                valor=obj['existeii']
                estado=obj['estadoii']
                tipo=obj['tiposist']
                idif= Infraestructura.objects.get(id=idc)
                idif.id=idc
                
                print(idc)
                print(valor)
                print(estado)
                print(tipo)
                
                infraestructuraInmuebleipm = InfraestructuraInmuebleipm.objects.create(idif=idif,existe=valor,estado=estado,tiposistema=tipo, idip=idipm)

    # fin

   #inicia espacios encontrados
    
            dataee =json.loads(request.POST.get('valoresee'))
            print(dataee)
            for obj in dataee:
                idce=obj['ide']
                valore=obj['valore']
                idife= Infraestructura.objects.get(id=idce)
                idife.id=idce
                
                print(idce)
                print(valore)

                inspeccionesirm = Inspeccionesirm.objects.create(idif=idife,existe=valore, idip=idipm)        
    # fin
    

      #inicia servicios basicos
    
            datasb =json.loads(request.POST.get('valoressbm'))
            print(datasb)
            for obj in datasb:
                idcs=obj['ids']
                valors=obj['valors']
                idifs= Infraestructura.objects.get(id=idcs)
                idifs.id=idcs
                
                print(idce)
                print(valore)

                inspeccionesirm = Inspeccionesirm.objects.create(idif=idifs,existe=valors, idip=idipm)        
    # fin

        #inicia infraestructura
    
            dataim =json.loads(request.POST.get('valoresim'))
            print(dataim)
            for obj in dataim:
                idci=obj['idi']
                valori=obj['valori']
                idifim= Infraestructura.objects.get(id=idci)
                idifim.id=idci
                
                print(idce)
                print(valore)

                inspeccionesirm = Inspeccionesirm.objects.create(idif=idifim,existe=valori, idip=idipm)        
    # fin

      #inicia vias de acceso
            dtv =json.loads(request.POST.get('valoresvm'))
            print(dtv)
            for obj in dtv:
                tipovia=obj['tipovia']
                print(tipovia)

            viasAccesoipm =  ViasAccesoipm.objects.create(tipovia=tipovia, idipl=idipm)  

    # fin

      #inicia riesgos
    
            datar =json.loads(request.POST.get('valorestbrm'))
            print(datar)
            for obj in datar:
                idcr=obj['idr']
                valorr=obj['valorr']
                idir= Infraestructura.objects.get(id=idcr)
                idir.id=idcr
                
                print(idcr)
                print(valorr)

                inspeccionesirmr = Inspeccionesirm.objects.create(idif=idir,existe=valorr, idip=idipm)        
    # fin

    #inicia distancia riesgos
            dtdr =json.loads(request.POST.get('valorestbdrm'))
            print(dtdr)
            for objif in dtdr:
                distanciatl=objif['distanciatlm']
                distanciarc=objif['distanciarcm']
                distancialc=objif['distancialcm']
                distanciata=objif['distanciatam']

            riesgosipm = Riesgosipm.objects.create(distaludes=distanciatl,disriosc=distanciarc,disladerasc=distancialc,distorresantenas=distanciata, idipl=idipm)  

    # 

    #inicia etapas del plan de mejoramiento
    
            dataet =json.loads(request.POST.get('valorestbetp'))
            print(dataet)
            for obj in dataet:
                valet=obj['valETP']
                etapa=obj['etapa']
               
                
                print(valet)
                print(etapa)

                planMejoramientoipm = PlanMejoramientoipm.objects.create(etapas=valet,descripcion=etapa, idip=idipm)        
    # fin

     #inicia factibilidades tecnicas mejora
            dttfm =json.loads(request.POST.get('valoresftm'))
            print(dttfm)
            for obj in dttfm:
                factpm=obj['factpm']
                print(factpm)

            factibilidadipm = Factibilidadipm.objects.create(detalle=factpm, idip=idipm)  

    #  

    #inicia descripción del mejoramiento acordado 
            dtdm =json.loads(request.POST.get('valoresdm'))
            print(dtdm)
            for obj in dtdm:
                descripcionma=obj['descripcionma']
                diasestm=obj['diasestm']
                print(descripcionma)

            dMejoramientoipm = DMejoramientoipm.objects.create(descripcion=descripcionma,diasestimados=diasestm, idip=idipm)  

    #

    #####################################################
    # para guardar en la lista de chequeo 
    lchequo= listaChequeo.objects.get(ids=idsol)
    lchequo.inspecciontec ="Si"
    lchequo.save()

    response_data = {'status': 'success', 'message': 'Archivos recibidos y procesados correctamente.'}
    return JsonResponse(response_data)


    #mensaje="Datos guardados"
    #messages.success(request, mensaje)
    #return redirect('administrarPerfil', id=inspeccionM.ids.perfil.id)  # id de perfil 


def registrarDIME(request): 
    
        if 'esquemaubicacions' in request.FILES:
            esquemaubicacions = request.FILES['esquemaubicacions']
        else:
            esquemaubicacions = None 

        if 'esquemaubicacionm' in request.FILES:
            esquemaubicacionm = request.FILES['esquemaubicacionm']
        else:
            esquemaubicacionm = None 

        idipm= InspeccionM.objects.all().last() #obtengo la ultima solicitud registrada 
        esquemasipm = Esquemasipm.objects.create(esquemasitio=esquemaubicacions,esquemamejora=esquemaubicacionm, idip=idipm)  
            
        response_data = {'status': 'success', 'message': 'Archivos recibidos y procesados correctamente.'}
        return JsonResponse(response_data)


    #mensaje="Datos guardados"
    #messages.success(request, mensaje)
    #return redirect('administrarPerfil', id=inspeccionM.ids.perfil.id)  # id de perfil 

def listaIM(request): 
    listaIm=Factibilidadipm.objects.all()
    return render(request, "InspeccionMejViviendaApp/listaim.html", {"listaim":listaIm})


def editarIM(request, id): # id de inspeccion mejora
    try:
        ipm=  InspeccionM.objects.get(id=id)
    except InspeccionM.DoesNotExist:
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
        vias_acceso= ViasAccesoipm.objects.get(idipl=ipm)
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
        listaii=Infraestructura.objects.filter(tipo=2,tipolm="Mejora",estado="activo")
    except listaii.DoesNotExist:
        listaii=""

    try:
        listaee=Infraestructura.objects.filter(tipo=3,tipolm="Mejora",estado="activo")
    except listaee.DoesNotExist:
        listaee=""
    
    try:
        listava=Infraestructura.objects.filter(tipo=4,tipolm="Mejora",estado="activo")
    except listava.DoesNotExist:
        listava=""

    try:
        listasb=Infraestructura.objects.filter(tipo=5,tipolm="Mejora",estado="activo")
    except listasb.DoesNotExist:
        listasb=""
    
    try:
        listaif=Infraestructura.objects.filter(tipo=6,tipolm="Mejora",estado="activo")
    except listaif.DoesNotExist:
        listaif=""
    
    try:
        listar=Infraestructura.objects.filter(tipo=7,tipolm="Mejora",estado="activo")
    except listar.DoesNotExist:
        listar=""

    

    #try:
    #    liip=InfraestructuraInmuebleipm.objects.filter(idip=ipm.id)
    #except liip.DoesNotExist:
    #    liip=""
    liip = InfraestructuraInmuebleipm.objects.filter(idip=ipm.id)
    liip_data = [
        {
            'existe': item.existe,
            'estado': item.estado,
            'tiposistema': item.tiposistema,
            'id': item.id,
            'idif':item.idif.id,
        }
        for item in liip
        ]

    liip_json = json.dumps(liip_data)

    lista_general=Inspeccionesirm.objects.filter(idip=ipm.id)

    lista_espacios_encontrados_datos=[]
    for item in lista_general:
        if item.idif.tipo == "3":
            lista_espacios_encontrados_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.id,})
    lista_espacios_encontrados_json = json.dumps(lista_espacios_encontrados_datos)

    lista_servicios_basicos_datos=[]
    for item in lista_general:
        if item.idif.tipo == "5":
            lista_servicios_basicos_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.id,})
    lista_servicios_basicos_json = json.dumps(lista_servicios_basicos_datos)

    lista_infraetructura_datos=[]
    for item in lista_general:
        if item.idif.tipo == "6":
            lista_infraetructura_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.id,})
    lista_infraetructura_json = json.dumps(lista_infraetructura_datos)

    lista_riesgos_datos=[]
    for item in lista_general:
        if item.idif.tipo == "7":
            lista_riesgos_datos.append ( {'existe': item.existe, 'id': item.id, 'idif':item.id,})
    lista_riesgos_json = json.dumps(lista_riesgos_datos)
    
    return render(request, "InspeccionMejViviendaApp/editarInspeccion.html", {"ipm":ipm,"s":s,"do":do,
        "listaii":listaii,"listaee":listaee,"listava":listava,"listasb":listasb,"listaif":listaif,
        "listar":listar,"liip_json": liip_json,"vias_acceso":vias_acceso,"riesgo_distancia":riesgo_distancia, 
        "lista_espacios_encontrados_json":lista_espacios_encontrados_json,"lista_plan":lista_plan,
        "lista_servicios_basicos_json":lista_servicios_basicos_json, "factibilida_tecnica":factibilida_tecnica,
        "lista_infraetructura_json":lista_infraetructura_json, "descripcion_mejora":descripcion_mejora,
        "lista_riesgos_json":lista_riesgos_json}) #

def actualizarIM(request):
     if request.is_ajax and request.method == "POST":
        dtig =json.loads(request.POST.get('valoresifm'))
        for objif in dtig:
                ids=objif['ids']
                idIM=objif['idIM']
                fecha=objif['fecham']
                hora=objif['horam']
                telp=objif['telpm']
                tels=objif['telsm']
                terceraed=objif['terceraedm']
                adultos=objif['adultosm']
                ninos=objif['ninosm']
                personadis=objif['personadism']
                propietarioinm=objif['propietarioinmm']
                parentescosm=objif['parentescosm']
                latitud=objif['latitudm']
                longitud=objif['longitudm']
                inmueble=objif['inmueblem']
                usoact=objif['usoactm']
                exotrav=objif['exotravm']
                usoacotv=objif['usoacotvm']
                comentariosrl=objif['comentariosrl']

                idsol= solicitud.objects.get(id=ids)
                idsol.id=ids
                inspeccionM=InspeccionM.objects.update_or_create(id=idIM,
            defaults={
            'fecha':fecha,'hora':hora,'telefonop':telp,'telefonos':tels,
            'terceraedad':terceraed,'adultos':adultos,'ninos':ninos,'personadisc':personadis,    
            'propietarioinm':propietarioinm,'parentescosol':parentescosm,'latitud':latitud,
            'longitud':longitud,'inmueble':inmueble,'usoactual':usoact,'existeotraviv':exotrav,
            'usoactualotv':usoacotv,'comentariosrelv':comentariosrl,'ids':idsol, 
            })
        registroBit(request, "Se actualizó formulario Inspeccion de Mejora " + idsol.perfil.dui, "Actualización")        
                
        data =json.loads( request.POST.get('valoresidi'))
        for obj in data:
            idc=obj['id']
            valor=obj['existeii']
            estado=obj['estadoii']
            tipo=obj['tiposist']
            idif= Infraestructura.objects.get(id=idc)
            idif.id=idc
            
            infraestructuraInmuebleipm = InfraestructuraInmuebleipm.objects.update_or_create(
            idif=idif,idip=idIM,defaults={
            'idif':idif,'existe':valor,'estado':estado,'tiposistema':tipo, 
            })
    #inicia espacios encontrados
        dataee =json.loads(request.POST.get('valoresee'))
        for obj in dataee:
                idce=obj['ide']
                valore=obj['valore']
                idife= Infraestructura.objects.get(id=idce)
                #idife.id=idce   
                inspeccionesirm = Inspeccionesirm.objects.update_or_create(idif=idife,idip=idIM,
                defaults={'existe':valore, }) 

    # fin
    #inicia servicios basicos    
        datasb =json.loads(request.POST.get('valoressbm'))
        for obj in datasb:
                idcs=obj['ids']
                valors=obj['valors']
                idifs= Infraestructura.objects.get(id=idcs)
                idifs.id=idcs
                inspeccionesirm = Inspeccionesirm.objects.update_or_create(idif=idifs,idip=idIM,
                defaults={'existe':valors, })             
    # fin

    #inicia infraestructura    
        dataim =json.loads(request.POST.get('valoresim'))
        for obj in dataim:
                idci=obj['idi']
                valori=obj['valori']
                idifim= Infraestructura.objects.get(id=idci)
                idifim.id=idci
                inspeccionesirm = Inspeccionesirm.objects.update_or_create(idif=idifim,idip=idIM,
                defaults={'existe':valori })          
    # fin

    #inicia vias de acceso
        dtv =json.loads(request.POST.get('valoresvm'))
        for obj in dtv:
                tipovia=obj['tipovia']
                viasAccesoipm =  ViasAccesoipm.objects.update_or_create(idipl=idIM,defaults={
                    'tipovia':tipovia, })    
    # fin

    #inicia riesgos    
        datar =json.loads(request.POST.get('valorestbrm'))
        for obj in datar:
                idcr=obj['idr']
                valorr=obj['valorr']
                idir= Infraestructura.objects.get(id=idcr)
                idir.id=idcr
                inspeccionesirmr = Inspeccionesirm.objects.update_or_create(idif=idir,idip=idIM,
                    defaults={'existe':valorr, })                 
    # fin

    #inicia distancia riesgos
        dtdr =json.loads(request.POST.get('valorestbdrm'))
        for objif in dtdr:
                distanciatl=objif['distanciatlm']
                distanciarc=objif['distanciarcm']
                distancialc=objif['distancialcm']
                distanciata=objif['distanciatam']

                riesgosipm = Riesgosipm.objects.update_or_create(idipl=idIM,
                    defaults={'distaludes':distanciatl,'disriosc':distanciarc,
                    'disladerasc':distancialc,'distorresantenas':distanciata, })  

    # fin

    #inicia etapas del plan de mejoramiento    
        dataet =json.loads(request.POST.get('valorestbetp'))
        for obj in dataet:
                valet=obj['valETP']
                etapa=obj['etapa']
                planMejoramientoipm = PlanMejoramientoipm.objects.update_or_create(idip=idIM,etapas=valet,
                    defaults={'etapas':valet,'descripcion':etapa, })        
    # fin

     #inicia factibilidades tecnicas mejora
        dttfm =json.loads(request.POST.get('valoresftm'))
        for obj in dttfm:
                factpm=obj['factpm']
                factibilidadipm = Factibilidadipm.objects.update_or_create(idip=idIM,
                    defaults={'detalle':factpm})  

    #  

    #inicia descripción del mejoramiento acordado 
        dtdm =json.loads(request.POST.get('valoresdm'))
        for obj in dtdm:
                descripcionma=obj['descripcionma']
                diasestm=obj['diasestm']
                dMejoramientoipm = DMejoramientoipm.objects.update_or_create(idip=idIM,
                    defaults={'descripcion':descripcionma,'diasestimados':diasestm})  

    #
     mensaje="Datos actualizados"
     messages.success(request, mensaje)
     return redirect('administrarPerfil', id=idsol.perfil.id)  # id de perfil 

             

############  Primera inspeccion

def pinspeccion(request,id,n): # id de la tabla inspeccion
    try:
        inspeccionM=InspeccionM.objects.get(id=id)
    except InspeccionM.DoesNotExist:
        inspeccionM=""
    try:
        do= datosObra.objects.get(idSolicitud=inspeccionM.ids.id)
    except datosObra.DoesNotExist:
        do=""
    try:
        DMipm = DMejoramientoipm.objects.get(idip=id)
    except DMejoramientoipm.DoesNotExist:
        DMipm=""
    
    return render(request,"InspeccionMejViviendaApp/pinspeccion.html", {"ipm":inspeccionM,"do":do,"dpi":DMipm, "n":n})



def registrarPIM(request):
    idim=request.POST['idm']
    try:
        ninspeccion=request.POST['ninspeccionm']
    except :
        ninspeccion=""
    try:
        fecha=request.POST['fecham']
    except :
        fecha=""
    try:
        mejoraar=request.POST['mejoraarm']
    except :
        mejoraar=""
    try:
        esquemam=request.FILES['esquemam']
    except :
        esquemam=""
    try:
        imagen=request.FILES.getlist('imagen')
    except :
        imagen=""
    #try:
    #    simagen=request.FILES['imagens']
    #except :
    #    simagen=""    
    #try:
    #    timagen=request.FILES['imagent']
    #except :
    #    timagen=""

    idipm= InspeccionM.objects.get(id=idim)
    idipm.id=idim 

    pim= pInspeccionm.objects.create(ninspeccion=ninspeccion,fecha=fecha,mejoraar=mejoraar,esquema=esquemam,idim=idipm)
    
    # Obtener el ID de la instancia de pInspeccionm
    pimid= pInspeccionm.objects.get(id=pim.id)
    pimid.id = pim.id
    registroBit(request, "Se registro formulario "+ pimid.ninspeccion + " Inspeccion de Mejora " + pimid.idim.ids.perfil.dui, "Registro")

    for i in range(len(imagen)): #verifica el numero de imagenes que llegan
        if (imagen[i] != ""):
            print(imagen[i])
            print('llego')
            im =ImagenPInspeccionm.objects.create(imagen=imagen[i],idpim=pimid)

    mensaje="Datos guardados"
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=pim.idim.ids.perfil.id)  # id de perfil 

def listaPIM(request): 
    listaPIm=pInspeccionm.objects.all()
    return render(request, "InspeccionMejViviendaApp/listapim.html", {"listapim":listaPIm})

def editarPIM(request,id): # id de la tabla pInspeccionm
    try:
        pim=pInspeccionm.objects.get(id=id)
    except pInspeccionm.DoesNotExist:
        pim=""
    try:
        inspeccionM=InspeccionM.objects.get(id=pim.idim.id)
    except InspeccionM.DoesNotExist:
        inspeccionM=""
    try:
        do= datosObra.objects.get(idSolicitud=inspeccionM.ids.id)
    except datosObra.DoesNotExist:
        do=""
    try:
        DMipm = DMejoramientoipm.objects.get(idip=inspeccionM.id)
    except DMejoramientoipm.DoesNotExist:
        DMipm=""

    try:
        imgpil= ImagenPInspeccionm.objects.filter(idpim=id)
    except ImagenPInspeccionm.DoesNotExist:
        imgpil=""
    
    return render(request,"InspeccionMejViviendaApp/editarPinspeccion.html", {"pim":pim,"ipm":inspeccionM,"do":do,"dpi":DMipm, "imgpil":imgpil})


def modificarPIM(request):
    idpim=request.POST['idim']
    try:
        ninspeccion=request.POST['ninspeccionm']
    except :
        ninspeccion=""
    try:
        fecha=request.POST['fecham']
    except :
        fecha=""
    try:
        mejoraar=request.POST['mejoraarm']
    except :
        mejoraar=""
    datoesq=request.POST['desquema']
    try:
        esquemam=request.FILES['esquemam']
    except :
        esquemam=""
    idimgp =request.POST.getlist('idimg')
    try:
        imagen=request.FILES.getlist('imagen')
    except :
        imagen=""
    

    mpim= pInspeccionm.objects.get(id=idpim)
    mpim.ninspeccion=ninspeccion
    mpim.fecha=fecha
    mpim.mejoraar=mejoraar

    if datoesq == "" :
        mpim.esquema=esquemam

    if datoesq != "" and esquemam !="":
        mpim.esquema=esquemam
    
    mpim.save()
    

    for i in range(len(imagen)): #verifica el numero de imagenes que llegan
        if i < len(idimgp) and idimgp[i] != "":
            # Si hay un valor válido en idimgp, actualizar el objeto existente
            pInspeccionm_obj = ImagenPInspeccionm.objects.get(id=idimgp[i])
            mim = ImagenPInspeccionm.objects.update_or_create(id=pInspeccionm_obj.id, idpim=mpim, defaults={'imagen': imagen[i], 'idpim': mpim})
        elif (imagen[i] != ""):
            print(imagen[i])
            im =ImagenPInspeccionm.objects.create(imagen=imagen[i],idpim=mpim)

    mensaje="Datos actualizados"
    registroBit(request, "Se actualizo formulario "+ mpim.ninspeccion +" Inspeccion de Mejora " + mpim.idim.ids.perfil.dui, "Actualizacion")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=mpim.idim.ids.perfil.id)  # id de perfil           
                
                
                
 
