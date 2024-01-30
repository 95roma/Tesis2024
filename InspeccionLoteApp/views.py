import json
from datetime import date
from django.shortcuts import render,redirect
from django.contrib import messages
from ConfiguracionApp.models import *
from InspeccionLoteApp.models import *
from PresupuestoVApp.models import *
from ListaChequeoApp.models import listaChequeo
from TesisApp.views import registroBit

# Create your views here.


def inspeccionl(request, id): 
    sol= Inspeccionl.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    if sol == True:
        solv= Inspeccionl.objects.get(ids=id)
    
        return redirect('editarIL', id=solv.id)   
    else:
        try:
            s=  solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s=""
        
        try:
            do= datosObra.objects.get(idSolicitud=id)
        except datosObra.DoesNotExist:
            do=""

        try:
            listad=Infraestructura.objects.filter(tipo=2,tipolm="Lote",estado="activo")
        except listad.DoesNotExist:
            listad=""

        try:
            listat=Infraestructura.objects.filter(tipo=3,tipolm="Lote",estado="activo")
        except listat.DoesNotExist:
            listat=""

        try:
            listac=Infraestructura.objects.filter(tipo=4,tipolm="Lote",estado="activo")
        except listac.DoesNotExist:
            listac=""
        try:
            listacn=Infraestructura.objects.filter(tipo=5,tipolm="Lote",estado="activo")
        except listacn.DoesNotExist: 
            listacn=""
        try:
            listase=Infraestructura.objects.filter(tipo=6,tipolm="Lote",estado="activo")
        except listase.DoesNotExist:
            listase=""

        return render(request, "InspeccionLoteApp/inspeccionl.html", {"s":s,"do":do, "listad":listad,"listat":listat,"listac":listac,"listacn":listacn,"listase":listase}) #, {"s":s,"d":d}

  
def registrarDIL(request): 
    
    if request.is_ajax and request.method == "POST":
            dtig =json.loads(request.POST.get('valoresif'))
            print(dtig)
            for objif in dtig:
                ids=objif['ids']
                fechal=objif['fechal']
                hora=objif['horal']
                telp=objif['telp']
                tels=objif['tels']
                terceraed=objif['terceraed']
                adultos=objif['adultos']
                ninos=objif['ninos']
                personadis=objif['personadis']
                propietarioinm=objif['propietarioinm']
                latitud=objif['latitud']
                longitud=objif['longitud']
                inmueble=objif['inmueble']
                exotrav=objif['exotrav']
                terrenoagric=objif['terrenoagric']
                anchocv=objif['anchocv']
                largocv=objif['largocv']
                areacv=objif['areacv']
                anchoaf=objif['anchoaf']
                largoaf=objif['largoaf']
                areaaf=objif['areaaf']

                idsol= solicitud.objects.get(id=ids)
                idsol.id=ids

                inspeccionl=Inspeccionl.objects.create(fecha=fechal,hora=hora,telefonop=telp,telefonos=tels,terceraedad=terceraed,adultos=adultos,ninos=ninos,personadisc=personadis,propietarioter=propietarioinm,latitud=latitud,longitud=longitud,inmueble=inmueble,existeotraviv=exotrav,terrenoagricola=terrenoagric,anchocv=anchocv,largocv=largocv,areacv=areacv,anchoaf=anchoaf,largoaf=largoaf,areaaf=areaaf,ids=idsol)
                registroBit(request, "Se registro formulario Inspeccion de Lote " + idsol.perfil.dui, "Registro")
               # print(ids)
               # print(fechal)
                #print(hora)
                #print(telp)
            

   
            idip= Inspeccionl.objects.all().last() #obtengo la ultima solicitud registrada 
    # idip= Inspeccionl.objects.get(id=4)


    

    #inicia Construccones
    
            data =json.loads( request.POST.get('valores'))
            print(data)
            for obj in data:
                idc=obj['id']
                valor=obj['valor']
                idif= Infraestructura.objects.get(id=idc)
                idif.id=idc
                
                print(idc)
                print(valor)

                inspeccionlcisr = Inspeccionlcisr.objects.create(idif=idif,existe=valor, idip=idip)

    # fin

    #inicia infraestructura
    
            dataif =json.loads(request.POST.get('valorestbif'))
            print(dataif)
            for obj in dataif:
                idci=obj['idi']
                valori=obj['valori']
                idifi= Infraestructura.objects.get(id=idci)
                idifi.id=idci
                
                print(idci)
                print(valori)

                inspeccionlcisrif = Inspeccionlcisr.objects.create(idif=idifi,existe=valori, idip=idip)        
    # fin

      #inicia saneamiento
    
            datasa =json.loads(request.POST.get('valorestbsa'))
            print(datasa)
            for obj in datasa:
                idcs=obj['idi']
                valors=obj['valori']
                idisa= Infraestructura.objects.get(id=idcs)
                idisa.id=idcs
                
                print(idcs)
                print(valors)

                inspeccionlcisrsa = Inspeccionlcisr.objects.create(idif=idisa,existe=valors, idip=idip)        
    # fin

    
     #inicia saneamiento
    
            datasb =json.loads(request.POST.get('valorestbsb'))
            print(datasb)
            for obj in datasb:
                idcsb=obj['idb']
                valorsb=obj['valorb']
                idisb= Infraestructura.objects.get(id=idcsb)
                idisb.id=idcsb
                
                print(idcsb)
                print(valorsb)

                inspeccionlcisrsb = Inspeccionlcisr.objects.create(idif=idisb,existe=valorsb, idip=idip)        
    # fin

    
      #inicia riesgos
    
            datar =json.loads(request.POST.get('valorestbr'))
            print(datar)
            for obj in datar:
                idcr=obj['idr']
                valorr=obj['valorr']
                idir= Infraestructura.objects.get(id=idcr)
                idir.id=idcr
                
                print(idcr)
                print(valorr)

                inspeccionlcisrr = Inspeccionlcisr.objects.create(idif=idir,existe=valorr, idip=idip)        
    # fin

    #inicia distancia riesgos
            dtdr =json.loads(request.POST.get('valorestbdr'))
            print(dtdr)
            for objif in dtdr:
                distanciatl=objif['distanciatl']
                distanciarc=objif['distanciarc']
                distancialc=objif['distancialc']
                distanciata=objif['distanciata']

            riesgosipl = Riesgosipl.objects.create(distaludes=distanciatl,disriosc=distanciarc,disladerasc=distancialc,distorresantenas=distanciata, idipl=idip)  

    #
    #inicia comentarios y observaciones
            dtco =json.loads(request.POST.get('valoresco'))
            print(dtco)
            for obj in dtco:
                comentariosil=obj['comentariosil']
                observacionesil=obj['observacionesil']
                print(comentariosil)

            comentariosObsipl = ComentariosObsipl.objects.create(comentario=comentariosil,observaciones=observacionesil, idipl=idip)  

    #

    
     #inicia vias de acceso
            dtv =json.loads(request.POST.get('valoresv'))
            print(dtv)
            for obj in dtv:
                tipovia=obj['tipovia']

            viasAccesoipl = ViasAccesoipl.objects.create(tipovia=tipovia, idipl=idip)  

    #
     #inicia factibilidades tecnicas
            dttf =json.loads(request.POST.get('valoresft'))
            print(dttf)
            for obj in dttf:
                factp=obj['factp']
                print(factp)

            factibilidadipl = Factibilidadipl.objects.create(detalle=factp, idipl=idip)  

    #
     #inicia descripción del proyecto
            dtdp =json.loads(request.POST.get('valoresdp'))
            print(dtdp)
            for obj in dtdp:
                modelov=obj['modelov']
                solucions=obj['solucions']
                obrasa=obj['obrasa']
                obst=obj['obst']
                descripciona=obj['descripciona']
                print(descripciona)

            descripcionProyectoipl = DescripcionProyectoipl.objects.create(modeloviviedac=modelov,solucionsanitariap=solucions,obrasadicionalesconst=obrasa,observtecnicas=obst, actividadbrfp=descripciona, idipl=idip) 

    #
      #inicia responsabilidades del solicitante
            dtrs =json.loads(request.POST.get('valoresrs'))
            print(dtrs)
            for obj in dtrs:
                mojonesl=obj['mojonesl']
                linderosl=obj['linderosl']
                resguardom=obj['resguardom']
                auxiliarc=obj['auxiliarc']
                aguap=obj['aguap']
                energiae=obj['energiae']
                print(energiae)

            responSolicitanteipl = ResponSolicitanteipl.objects.create(mojoneslote=mojonesl,linderoslote=linderosl,resguardomather=resguardom,auxiliaresconst=auxiliarc, aguapotable=aguap,energiaelectrica=energiae , idipl=idip) 
    #

    #####################################################
    # para guardar en la lista de chequeo 
    lchequo= listaChequeo.objects.get(ids=idsol)
    lchequo.inspecciontec ="Si"
    lchequo.save()

    return redirect('administrarPerfil', id=inspeccionl.ids.perfil.id)  # id de perfil 

def listaI(request): 
    listaI=Factibilidadipl.objects.all()
    return render(request, "InspeccionLoteApp/listail.html", {"listai":listaI})

def editarIL(request, id): #id inspeccion lote
    try:
        ipl=Inspeccionl.objects.get(id=id)
    except Inspeccionl.DoesNotExist:
        ipl=""

    try:
        s=  solicitud.objects.get(id=ipl.ids.id)
    except solicitud.DoesNotExist:
        s=""
    
    try:
        do= datosObra.objects.get(idSolicitud=ipl.ids.id)
    except datosObra.DoesNotExist:
        do=""

    try:
        listad=Infraestructura.objects.filter(tipo=2,tipolm="Lote",estado="activo")
    except listad.DoesNotExist:
        listad=""

    try:
        listat=Infraestructura.objects.filter(tipo=3,tipolm="Lote",estado="activo")
    except listat.DoesNotExist:
        listat=""

    try:
        listac=Infraestructura.objects.filter(tipo=4,tipolm="Lote",estado="activo")
    except listac.DoesNotExist:
        listac=""

    try:
        listacn=Infraestructura.objects.filter(tipo=5,tipolm="Lote",estado="activo")
    except listacn.DoesNotExist: 
        listacn=""

    try:
        listase=Infraestructura.objects.filter(tipo=6,tipolm="Lote",estado="activo")
    except listase.DoesNotExist:
        listase=""

    #try:
    #    liip = Inspeccionlcisr.objects.filter(idip=ipl.id)
    #    liip_data = [
    #    {
    #        'existe': item.existe,
    #        'estado': item.estado,
    #        'tiposistema': item.tiposistema,
    #        'id': item.id,
    #    }
    #    for item in liip
    #    ]

    #    liip_json = json.dumps(liip_data)
    #except liip.DoesNotExist:
    #    liip=""
    
    lista_general=Inspeccionlcisr.objects.filter(idip=ipl.id)

    lista_construcciones_datos=[]
    for item in lista_general:
        if item.idif.tipo == "2": # si el tipo 2 se encuentra en la lista_general se agrega  a su respectiva lista
            lista_construcciones_datos.append ( {'existe': item.existe, 'id': item.id, })
    lista_construcciones_json = json.dumps(lista_construcciones_datos)

    lista_infraestructura_datos=[]
    for item in lista_general:
        if item.idif.tipo == "3":
            lista_infraestructura_datos.append ( {'existe': item.existe, 'id': item.id, })
    lista_infraestructura_json = json.dumps(lista_infraestructura_datos)

    lista_saneamiento_datos=[]
    for item in lista_general:
        if item.idif.tipo == "4":
            lista_saneamiento_datos.append ( {'existe': item.existe, 'id': item.id, })
    lista_saneamiento_json = json.dumps(lista_saneamiento_datos)

    lista_servicios_basicos_datos=[]
    for item in lista_general:
        if item.idif.tipo == "5":
            lista_servicios_basicos_datos.append ( {'existe': item.existe, 'id': item.id, })
    lista_servicios_basicos_json = json.dumps(lista_servicios_basicos_datos)

    lista_riesgos_datos=[]
    for item in lista_general:
        if item.idif.tipo == "6":
            lista_riesgos_datos.append ( {'existe': item.existe, 'id': item.id, })
    lista_riesgos_json = json.dumps(lista_riesgos_datos)

    try:
        rs=  Riesgosipl.objects.get(idipl=id)
    except Riesgosipl.DoesNotExist:
        rs=""
    
    try:
        cm=  ComentariosObsipl.objects.get(idipl=id)
    except ComentariosObsipl.DoesNotExist:
        cm=""

    try:
        vs=  ViasAccesoipl.objects.get(idipl=id)
    except ViasAccesoipl.DoesNotExist:
        vs=""
    
    try:
        ft=  Factibilidadipl.objects.get(idipl=id)
    except Factibilidadipl.DoesNotExist:
        ft=""
        
    try:
        dp=  DescripcionProyectoipl.objects.get(idipl=id)
    except DescripcionProyectoipl.DoesNotExist:
        dp=""
    
    try:
        rps=  ResponSolicitanteipl.objects.get(idipl=id)
    except ResponSolicitanteipl.DoesNotExist:
        rps=""
      
    return render(request, "InspeccionLoteApp/editarInspeccionl.html", {"ipl":ipl,"s":s,"do":do,
            "listad":listad, "listat":listat,"listac":listac,"listacn":listacn,"listase":listase,
            "lista_construcciones_json":lista_construcciones_json,
            "lista_infraestructura_json":lista_infraestructura_json,
            "lista_saneamiento_json":lista_saneamiento_json,
            "lista_servicios_basicos_json":lista_servicios_basicos_json,
            "lista_riesgos_json":lista_riesgos_json,"rs":rs,"cm":cm,"vs":vs,"ft":ft,"dp":dp,"rps":rps}) 



def modificarIL(request): 
    
    if request.is_ajax and request.method == "POST":
            dtig =json.loads(request.POST.get('valoresif'))
            print(dtig)
            for objif in dtig:
                ids=objif['ids']
                idIL=objif['idIL']
                fechal=objif['fechal']
                hora=objif['horal']
                telp=objif['telp']
                tels=objif['tels']
                terceraed=objif['terceraed']
                adultos=objif['adultos']
                ninos=objif['ninos']
                personadis=objif['personadis']
                propietarioinm=objif['propietarioinm']
                latitud=objif['latitud']
                longitud=objif['longitud']
                inmueble=objif['inmueble']
                exotrav=objif['exotrav']
                terrenoagric=objif['terrenoagric']
                anchocv=objif['anchocv']
                largocv=objif['largocv']
                areacv=objif['areacv']
                anchoaf=objif['anchoaf']
                largoaf=objif['largoaf']
                areaaf=objif['areaaf']

                idsol= solicitud.objects.get(id=ids)
                idsol.id=ids

                inspeccionl=Inspeccionl.objects.update_or_create(id=idIL,
                defaults={ 'fecha':fechal,'hora':hora,'telefonop':telp,'telefonos':tels,'terceraedad':terceraed,
                          'adultos':adultos,'ninos':ninos,'personadisc':personadis,'propietarioter':propietarioinm,
                          'latitud':latitud,'longitud':longitud,'inmueble':inmueble,'existeotraviv':exotrav,
                          'terrenoagricola':terrenoagric,'anchocv':anchocv,'largocv':largocv,'areacv':areacv,
                          'anchoaf':anchoaf,'largoaf':largoaf,'areaaf':areaaf,'ids':idsol,})
                
                registroBit(request, "Se actualizó formulario Inspeccion de Lote " + idsol.perfil.dui, "Actualización") 
   

               # print(ids)
               # print(fechal)
                #print(hora)
                #print(telp)
   
          #  idip= Inspeccionl.objects.all().last() #obtengo la ultima solicitud registrada 
    # idip= Inspeccionl.objects.get(id=4)

    #inicia Construccones
    
            data =json.loads( request.POST.get('valores'))
            print(data)
            for obj in data:
                idc=obj['id']
                valor=obj['valor']
                idif= Infraestructura.objects.get(id=idc)
                idif.id=idc
                
                print(idc)
                print(valor)

                inspeccionlcisr = Inspeccionlcisr.objects.update_or_create(idif=idif,idip=idIL,
                                  defaults={'existe':valor,})

    # fin

    #inicia infraestructura
    
            dataif =json.loads(request.POST.get('valorestbif'))
            print(dataif)
            for obj in dataif:
                idci=obj['idi']
                valori=obj['valori']
                idifi= Infraestructura.objects.get(id=idci)
                idifi.id=idci
                
                print(idci)
                print(valori)

                inspeccionlcisrif = Inspeccionlcisr.objects.update_or_create(idif=idifi,idip=idIL,
                                    defaults={'existe':valori,})      
    # fin

      #inicia saneamiento
    
            datasa =json.loads(request.POST.get('valorestbsa'))
            print(datasa)
            for obj in datasa:
                idcs=obj['idi']
                valors=obj['valori']
                idisa= Infraestructura.objects.get(id=idcs)
                idisa.id=idcs
                
                print(idcs)
                print(valors)

                inspeccionlcisrsa = Inspeccionlcisr.objects.update_or_create(idif=idisa,idip=idIL,
                                    defaults={'existe':valors,})       
    # fin

    
     #inicia servicios basicos
    
            datasb =json.loads(request.POST.get('valorestbsb'))
            print(datasb)
            for obj in datasb:
                idcsb=obj['idb']
                valorsb=obj['valorb']
                idisb= Infraestructura.objects.get(id=idcsb)
                idisb.id=idcsb
                
                print(idcsb)
                print(valorsb)

                inspeccionlcisrsb = Inspeccionlcisr.objects.update_or_create(idif=idisb,idip=idIL,
                                    defaults={'existe':valorsb, })         
    # fin

    
      #inicia riesgos
    
            datar =json.loads(request.POST.get('valorestbr'))
            print(datar)
            for obj in datar:
                idcr=obj['idr']
                valorr=obj['valorr']
                idir= Infraestructura.objects.get(id=idcr)
                idir.id=idcr
                
                print(idcr)
                print(valorr)

                inspeccionlcisrr = Inspeccionlcisr.objects.update_or_create(idif=idir,idip=idIL,
                                   defaults={'existe':valorr,})         
    # fin

    #inicia distancia riesgos
            dtdr =json.loads(request.POST.get('valorestbdr'))
            print(dtdr)
            for objif in dtdr:
                distanciatl=objif['distanciatl']
                distanciarc=objif['distanciarc']
                distancialc=objif['distancialc']
                distanciata=objif['distanciata']

            riesgosipl = Riesgosipl.objects.update_or_create(idipl=idIL,
                      defaults={'distaludes':distanciatl,'disriosc':distanciarc,'disladerasc':distancialc,'distorresantenas':distanciata, })  

    #
    #inicia comentarios y observaciones
            dtco =json.loads(request.POST.get('valoresco'))
            print(dtco)
            for obj in dtco:
                comentariosil=obj['comentariosil']
                observacionesil=obj['observacionesil']
                print(comentariosil)

            comentariosObsipl = ComentariosObsipl.objects.update_or_create(idipl=idIL,
                              defaults={'comentario':comentariosil,'observaciones':observacionesil, })

    #

    
     #inicia vias de acceso
            dtv =json.loads(request.POST.get('valoresv'))
            print(dtv)
            for obj in dtv:
                tipovia=obj['tipovia']

            viasAccesoipl = ViasAccesoipl.objects.update_or_create(idipl=idIL,
                           defaults={'tipovia':tipovia, })

    #
     #inicia factibilidades tecnicas
            dttf =json.loads(request.POST.get('valoresft'))
            print(dttf)
            for obj in dttf:
                factp=obj['factp']
                print(factp)

            factibilidadipl = Factibilidadipl.objects.update_or_create(idipl=idIL,
                              defaults={ 'detalle':factp, }) 

    #
     #inicia descripción del proyecto
            dtdp =json.loads(request.POST.get('valoresdp'))
            print(dtdp)
            for obj in dtdp:
                modelov=obj['modelov']
                solucions=obj['solucions']
                obrasa=obj['obrasa']
                obst=obj['obst']
                descripciona=obj['descripciona']
                print(descripciona)

            descripcionProyectoipl = DescripcionProyectoipl.objects.update_or_create(idipl=idIL,
                defaults={'modeloviviedac':modelov,'solucionsanitariap':solucions,'obrasadicionalesconst':obrasa,
                'observtecnicas':obst, 'actividadbrfp':descripciona, })

    #
      #inicia responsabilidades del solicitante
            dtrs =json.loads(request.POST.get('valoresrs'))
            print(dtrs)
            for obj in dtrs:
                mojonesl=obj['mojonesl']
                linderosl=obj['linderosl']
                resguardom=obj['resguardom']
                auxiliarc=obj['auxiliarc']
                aguap=obj['aguap']
                energiae=obj['energiae']
                print(energiae)

            responSolicitanteipl = ResponSolicitanteipl.objects.update_or_create(idipl=idIL,
                defaults={'mojoneslote':mojonesl,'linderoslote':linderosl,'resguardomather':resguardom,
                          'auxiliaresconst':auxiliarc, 'aguapotable':aguap,'energiaelectrica':energiae , })
    #
    return redirect('administrarPerfil', id=idsol.perfil.id)  # id de perfil 
  


############  Primera inspeccion

def pinspeccionl(request, id, n): # id de la tabla inspeccion
    try:
        inspeccionl=Inspeccionl.objects.get(id=id)
    except Inspeccionl.DoesNotExist:
        inspeccionl=""
    try:
        do= datosObra.objects.get(idSolicitud=inspeccionl.ids.id)
    except datosObra.DoesNotExist:
        do=""       
    try:
        DPipl = DescripcionProyectoipl.objects.get(idipl=id)
    except DescripcionProyectoipl.DoesNotExist:
        DPipl=""
    try:
        pdg= Presupuestovdg.objects.get(ids=inspeccionl.ids.id)
    except Presupuestovdg.DoesNotExist:
        pdg=""
    return render(request,"InspeccionLoteApp/pinspeccionl.html", {"ipl":inspeccionl,"do":do,"dpi":DPipl,"pdg":pdg, "n":n})

def registrarPIL(request):
    idil=request.POST['idi']
    try:
        ninspeccion=request.POST['ninspeccion']
    except :
        ninspeccion=""
    try:
        fecha=request.POST['pfecha']
    except :
        fecha=""
    try:
        esquema=request.FILES['archivoesq']
    except :
        esquema=""
    try:
        ubicacion=request.FILES['archivoubic']
    except :
        ubicacion=""
    try:
        reportef=request.FILES.getlist('archivorepf')
    except :
        reportef=""

    idipl= Inspeccionl.objects.get(id=idil)
    idipl.id=idil 

    pil= pInspeccionl.objects.create(ninspeccion=ninspeccion,fecha=fecha,esquema=esquema,ubicacion=ubicacion,idil=idipl)

    # Obtener el ID de la instancia de pInspeccion
    pilid= pInspeccionl.objects.get(id=pil.id)
    pilid.id = pil.id

    for i in range(len(reportef)): #verifica el numero de imagenes que llegan
        if (reportef[i] != ""):
            print(reportef[i])
            print('llego')
            im =ImagenPInspeccionl.objects.create(reportef=reportef[i],idpil=pilid)
    registroBit(request, "Se registro formulario "+ pilid.ninspeccion + " Inspeccion de Lote " + idipl.ids.perfil.dui, "Registro")
    
    return redirect('administrarPerfil', id=pil.idil.ids.perfil.id)  # id de perfil 

def listaPIL(request): 
    listapI=pInspeccionl.objects.all()
    return render(request, "InspeccionLoteApp/listapil.html", {"listapi":listapI})

def editarPIL(request, id): # id de la tabla pInspeccionl
    try:
        pil=pInspeccionl.objects.get(id=id)
    except pInspeccionl.DoesNotExist:
        pil=""
    try:
        inspeccionl=Inspeccionl.objects.get(id=pil.idil.id)
    except Inspeccionl.DoesNotExist:
        inspeccionl=""
    try:
        do= datosObra.objects.get(idSolicitud=inspeccionl.ids.id)
    except datosObra.DoesNotExist:
        do=""       
    try:
        DPipl = DescripcionProyectoipl.objects.get(idipl=inspeccionl.id)
    except DescripcionProyectoipl.DoesNotExist:
        DPipl=""
    try:
        pdg= Presupuestovdg.objects.get(ids=inspeccionl.ids.id)
    except Presupuestovdg.DoesNotExist:
        pdg=""

    try:
        imgpil= ImagenPInspeccionl.objects.filter(idpil=id)
    except ImagenPInspeccionl.DoesNotExist:
        imgpil=""

        
    return render(request,"InspeccionLoteApp/editarPinspeccionl.html", {"pil":pil,"ipl":inspeccionl,"do":do,"dpi":DPipl,"pdg":pdg, "imgpil":imgpil})


def modificarPIL(request):
    idpil=request.POST['idpi']
    try:
        ninspeccion=request.POST['ninspeccion']
    except :
        ninspeccion=""
    try:
        fecha=request.POST['pfecha']
    except :
        fecha=""
        
    datoesq=request.POST['desquema']
    
    try:
        esquemam=request.FILES['archivoesq']
    except :
        esquemam=""

    datoubi=request.POST['dubicacion']    

    try:
        ubicacionm=request.FILES['archivoubic']
    except :
        ubicacionm=""
    idimgp =request.POST.getlist('idimg')
    try:
        reportef=request.FILES.getlist('archivorepf')
    except :
        reportef=""

    mpil= pInspeccionl.objects.get(id=idpil)
    mpil.ninspeccion=ninspeccion
    mpil.fecha=fecha

    if datoesq == "" :
        mpil.esquema=esquemam

    if datoesq != "" and esquemam !="":
        mpil.esquema=esquemam

    if datoubi == "" :
        mpil.ubicacion=ubicacionm

    if datoubi != "" and ubicacionm !="":
        mpil.ubicacion=ubicacionm

    mpil.save()

        
    # Iterar a través de reportef y crear objetos en la base de datos
    for i in range(len(reportef)):
        if i < len(idimgp) and idimgp[i] != "":
            # Si hay un valor válido en idimgp, actualizar el objeto existente
            pInspeccion_obj = ImagenPInspeccionl.objects.get(id=idimgp[i])
            mim = ImagenPInspeccionl.objects.update_or_create(id=pInspeccion_obj.id, idpil=mpil, defaults={'reportef': reportef[i], 'idpil': mpil})
        elif reportef[i] != "":
            # Si idimgp está vacío o no hay un valor válido en idimgp, crear un nuevo objeto
            mim = ImagenPInspeccionl.objects.create(idpil=mpil, reportef=reportef[i])


    mensaje="Datos Actualizados"
    registroBit(request, "Se actualizo formulario "+ mpil.ninspeccion +" Inspeccion de Lote " + mpil.idil.ids.perfil.dui, "Actualizacion")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=mpil.idil.ids.perfil.id)  # id de perfil 
