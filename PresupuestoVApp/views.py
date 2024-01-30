import json
from django.contrib import messages
from django.shortcuts import render,redirect, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.generic import TemplateView
from PresupuestoVApp.models import *
from ConfiguracionApp.models import *
from ListaChequeoApp.models import listaChequeo
from TesisApp.views import registroBit

# Create your views here.

def presupuestov(request, id):
    sol= Presupuestovdg.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    if sol == True:
        solv= Presupuestovdg.objects.get(ids=id)
    
        return redirect('editarPV', id=solv.id)   
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
            d=  detalle.objects.get(idSolicitud=id)
        except detalle.DoesNotExist:
            d=""
        
        try:
            listam=Materiales.objects.filter(estado="activo")
        except Materiales.DoesNotExist:
            listam=""

    
        return render(request,"PresupuestoVApp/presupuesto.html", {"materiales":listam, "s":s, "do":do, "d":d})

# carga los datos del material seleccionado en los inputs
def get(request):
    id=request.GET['idmaterial']
    if request.is_ajax():
        material=Materiales.objects.get(id=id)
        serialized_data = serialize("json",[material])
        return HttpResponse(serialized_data, content_type="application/json")
    else:
       listam=Materiales.objects.filter(estado="activo")
       return render(request,"PresupuestoVApp/presupuesto.html", {"materiales":listam})

def registrarPV(request): 
    
 if request.is_ajax and request.method == "POST":
    dtig =json.loads(request.POST.get('valoresig'))
    print(dtig)
    for objif in dtig:
        ids=objif['ids']
        fecha=objif['fecha']
        tiempoconstruccion =objif['tiempoc']
        modelo =objif['modelo']
        dimensionviv =objif['dimension']
        cantidadvivienda =objif['cantv']
        costototalv =objif['costotv']
        
    
        print(fecha)
        print( modelo)
        print(dimensionviv)
        print( costototalv)
    

        idsol= solicitud.objects.get(id=ids)
        idsol.id=ids 

        presupuestodg= Presupuestovdg.objects.create(fecha=fecha,tiempoconstruccion=tiempoconstruccion,modelo=modelo,dimensionviv=dimensionviv,cantidadvivienda=cantidadvivienda,costototalv=costototalv,ids=idsol ) #
    

        idpdg= Presupuestovdg.objects.all().last() #obtengo el ultimo registro de los datos generales de presupuesto
        
        ###### para tabla de materiales
        
        datamt =json.loads( request.POST.get('valorestmt'))
        print(datamt)  
        for obj in datamt:
                idmp=obj['idm'] # id del material
                cantidad=obj['cantidad']
                preciouni=obj['preciouni']
                subtotal=obj['subtotal']
                
                idm= Materiales.objects.get(id=idmp)
                idm.id=idmp
                
                #ma=obj['idm']
                print(cantidad)
                print(preciouni)
                print(subtotal)
            
                PreMate = PresupuestovMateriales.objects.filter(idm=idm,idp=idpdg ).exists()
                print(PreMate)
                #PresupuestoMateriales()
                if PreMate== True:
                    presupuestoMateriales=PresupuestovMateriales.objects.get(idm=idm,idp=idpdg )
                
                    print(presupuestoMateriales.cantidad)
                    presupuestoMateriales.cantidad=presupuestoMateriales.cantidad+cantidad
                    presupuestoMateriales.preciouni=presupuestoMateriales.preciouni+preciouni
                    presupuestoMateriales.subtotal=presupuestoMateriales.subtotal+subtotal
                    presupuestoMateriales.save()
                else:
                    presupuestoMateriales= PresupuestovMateriales.objects.create(cantidad=cantidad, preciouni=preciouni, subtotal=subtotal,idm=idm,idp=idpdg)
  
  ###  para tabla mano de obra
        datamo =json.loads( request.POST.get('valorestmo'))
        print(datamo)  
        for obj in datamo:
                descripcion=obj['descripc'] # id del material
                unidad=obj['unidad']
                preciouni=obj['preciouni']
                cantidad=obj['cantidad']
                subtotal=obj['subtotal']
                
                print(descripcion)
                print(cantidad)
                print(preciouni)
                print(subtotal)
            
                PreMo = PresupuestovManoObra.objects.filter(idp=idpdg ).exists()
                print(PreMo)

                if PreMo== True:
                    presupuestoManoObra=PresupuestovManoObra.objects.get(idp=idpdg )
                
                    presupuestoManoObra.cantidad=presupuestoManoObra.cantidad+cantidad
                    presupuestoManoObra.preciouni=presupuestoManoObra.preciouni+preciouni
                    presupuestoManoObra.subtotal=presupuestoManoObra.subtotal+subtotal
                    presupuestoManoObra.save()
                else:
                    presupuestoManoObra= PresupuestovManoObra.objects.create(descripcion=descripcion,unidad=unidad,cantidad=cantidad, preciouni=preciouni, subtotal=subtotal,idp=idpdg)

   
        ### para otras especificaciones
        dtesp =json.loads(request.POST.get('valoresesp'))
        print(dtesp)
        for obje in dtesp:
            materiales=obje['material']
            manoobra=obje['manoob']
            transporte=obje['transporte']
            solucionsanit=obje['solucions']
            kitemerg=obje['kitemg']
            herramientas=obje['herramienta']
            totalcostosd=obje['totalcd']

            if(manoobra=="" ):
                manoobra = 0.00  
            if(transporte=="" ):
                transporte = 0.00  
            if(solucionsanit=="" ):
                solucionsanit = 0.00  
            if(kitemerg=="" ):
                kitemerg = 0.00  
            if(herramientas=="" ):
                herramientas = 0.00   


            print(materiales)
            print( manoobra)
            print(transporte)
            print(totalcostosd)

            
            presupvt= PresupuestovTotal.objects.create(materiales=materiales,manoobra=manoobra,transporte=transporte,solucionsanit=solucionsanit,kitemerg=kitemerg,herramientas=herramientas,totalcostosd=totalcostosd,idp=idpdg ) 

    
    #####################################################
    # para guardar en la lista de chequeo 
    lchequo= listaChequeo.objects.get(ids=idsol)
    lchequo.presupuestocons ="Si"
    lchequo.save()

    mensaje="Datos guardados"
    registroBit(request, "Se registro formulario Presupuesto de Vivienda " + idsol.perfil.dui, "Registro")
    messages.success(request, mensaje)
    #return JsonResponse(data=response_json, status=200)
    return redirect('administrarPerfil', id=presupuestodg.ids.perfil.id)  # id de perfil 
 
#mensaje="Datos guardados"
    #return JsonResponse(data=response_json, status=200)
    #return HttpResponse(response_json)
    #return redirect('/SolicitudesApp/listaSoli/presupuesto/1'+)

def listaPV(request): 
    listapm=PresupuestovTotal.objects.all()
    return render(request, "PresupuestoVApp/listaPV.html", {"listap":listapm})


def editarPV(request, id):# id presupuesto dg
    lista_materiales_json = []
    lista_mano_obra_json = []

    try:
        pvdg=  Presupuestovdg.objects.get(id=id)
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
        pvt=  PresupuestovTotal.objects.get(idp=id)
    except PresupuestovTotal.DoesNotExist:
        pvt=""

    try:
        lista_materiales= PresupuestovMateriales.objects.filter(idp=pvdg.id)
        datos=[]
        for item in lista_materiales:
            datos.append ( {'id': item.id, 'precio':item.preciouni,'cantida': item.cantidad,'total':item.subtotal,
            "nombre":item.idm.nombre,"descripcion":item.idm.descripcion,"unidad":item.idm.unidad,"idm":item.idm.id })
        lista_materiales_json = json.dumps(datos,default=str)
    except PresupuestovMateriales.DoesNotExist:
        lista_materiales=""

    try:
        lista_mano_obra= PresupuestovManoObra.objects.filter(idp=pvdg.id)
        datos=[]
        for item in lista_mano_obra:
            datos.append({
                "id":item.id,
                "descripcion":item.descripcion,
                "unidad":item.unidad,
                "preciouni":item.preciouni,
                "cantidad":item.cantidad,
                "total":item.subtotal,
            })
            lista_mano_obra_json = json.dumps(datos, default=str)
    except PresupuestovManoObra.DoesNotExist:
        lista_mano_obra=""
        lista_mano_obra_json=""

    
    return render(request,"PresupuestoVApp/editarPresupuesto.html", {"materiales":listam,"pvdg":pvdg,
                             "s":s, "do":do, "d":d,"pvt":pvt, "listMateriales":lista_materiales_json,
                             "lista_mano_obra_json":lista_mano_obra_json,})

def actualizar_presupuestoV(request):
    if request.is_ajax and request.method == "POST":
        dtig =json.loads(request.POST.get('valoresig'))
        for objif in dtig:
            ids=objif['ids']
            fecha=objif['fecha']
            tiempoconstruccion =objif['tiempoc']
            modelo =objif['modelo']
            dimensionviv =objif['dimension']
            cantidadvivienda =objif['cantv']
            costototalv =objif['costotv']                   
            presupuesto = objif['idPresupuesto']  
            
            idsol= solicitud.objects.get(id=ids)
            idsol.id=ids 
            presupuesto = Presupuestovdg.objects.get(id=presupuesto, ids=idsol.id)

            presupuestodg= Presupuestovdg.objects.update_or_create(ids=idsol, id=presupuesto.id ,
            defaults={
                "fecha":fecha,
             "tiempoconstruccion":tiempoconstruccion,
             "modelo":modelo,
             "dimensionviv":dimensionviv,
             "cantidadvivienda":cantidadvivienda,
             "costototalv":costototalv,
            "ids":idsol }) #
        
            idpdg= presupuesto #obtengo el ultimo registro de los datos generales de presupuesto
            
            ###### para tabla de materiales
            
            datamt =json.loads( request.POST.get('valorestmt'))
            lista_original = PresupuestovMateriales.objects.filter(
                idp=presupuesto.id)
            lista_actual = []  # el id que no este aqui se eliminara
            for obj in datamt:
                    idmp=obj['idm'] # id del material
                    cantidad=obj['cantidad']
                    preciouni=obj['preciouni']
                    subtotal=obj['subtotal']
                    
                    idm= Materiales.objects.get(id=idmp)
                    idm.id=idmp
                    lista_actual.append(idmp) 
                    PreMate = PresupuestovMateriales.objects.update_or_create(idm=idm, idp=presupuesto.id,
                        defaults={
                            "preciouni":preciouni,
                            "cantidad":cantidad,
                            "subtotal":subtotal,
                            "idm":idm,
                            "idp":idpdg,
                        })
            # ciclo para eliminar  material
            for item in lista_original:
                if ((item.idm.id in lista_actual) == False):
                    PreMate = PresupuestovMateriales.objects.get(
                        idm=item.idm, idp=presupuesto.id)
                    PreMate.delete()
        
    ###  para tabla mano de obra
            datamo = json.loads( request.POST.get('valorestmo'))
            lista_original = PresupuestovManoObra.objects.filter(
                idp=presupuesto.id)
            lista_actual = []
            for obj in datamo:
                    id =obj['id']
                    descripcion=obj['descripc'] 
                    unidad=obj['unidad']
                    preciouni=obj['preciouni']
                    cantidad=obj['cantidad']
                    subtotal=obj['subtotal']
                    
                    try: 
                        mano_obra = PresupuestovManoObra.objects.update_or_create( id=id, idp=presupuesto.id,
                                defaults={
                                "descripcion":descripcion, 
                                "unidad":unidad, 
                                "preciouni":preciouni, 
                                "cantidad":cantidad, 
                                "subtotal":subtotal, 
                                "idp":presupuesto, 
                                })  
                        lista_actual.append(int(id))
                    except Exception:
                        presupuestoManoObra= PresupuestovManoObra.objects.create(descripcion=descripcion,
                                unidad=unidad,cantidad=cantidad, 
                                preciouni=preciouni, 
                                subtotal=subtotal,
                                idp=idpdg)   
                        lista_actual.append(presupuestoManoObra.id)           
            # ciclo para eliminar mano de obra
            for item in lista_original:
                if ((item.id in lista_actual) == False):
                    PreMate = PresupuestovManoObra.objects.get(
                        id=item.id, idp=presupuesto.id)
                    PreMate.delete()
            ### para otras especificaciones
            dtesp = json.loads(request.POST.get('valoresesp'))
            
            for obje in dtesp:
                materiales=obje['material']
                manoobra=obje['manoob']
                transporte=obje['transporte']
                solucionsanit=obje['solucions']
                kitemerg=obje['kitemg']
                herramientas=obje['herramienta']
                totalcostosd=obje['totalcd']

                if(manoobra=="" ):
                    manoobra = 0.00  
                if(transporte=="" ):
                    transporte = 0.00  
                if(solucionsanit=="" ):
                    solucionsanit = 0.00  
                if(kitemerg=="" ):
                    kitemerg = 0.00  
                if(herramientas=="" ):
                    herramientas = 0.00  
                     
                presupvt= PresupuestovTotal.objects.update_or_create(idp=presupuesto.id,
                    defaults={
                        "materiales":materiales,
                        "manoobra":manoobra,
                        "transporte":transporte,
                        "solucionsanit":solucionsanit,
                        "kitemerg":kitemerg,
                        "herramientas":herramientas,
                        "totalcostosd":totalcostosd,
                        "idp":idpdg} ) 

        
        
    mensaje="Datos actualizados"
    registroBit(request, "Se actualizó Presupuesto de Vivienda " + idsol.perfil.dui, "Actualización")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=idsol.perfil.id)  # id de perfil ")
    

# para presupuesto de obras adicionales
def presupuestovoa(request, id):
    try:
        listam=Materiales.objects.filter(estado="activo")
    except Materiales.DoesNotExist:
        listam=""
    try:
        pdg=  Presupuestovdg.objects.get(id=id)
    except Presupuestovdg.DoesNotExist:
        pdg=""
    
    try:
        do= datosObra.objects.get(idSolicitud=pdg.ids.id)
    except datosObra.DoesNotExist:
        do=""
    return render(request,"PresupuestoVApp/presupuestoobra.html", {"materiales":listam,"pdg":pdg,"do":do})


# carga los datos del material seleccionado en los inputs
def obtenermt(request):
    id=request.GET['idmaterial']
    if request.is_ajax():
        material=Materiales.objects.get(id=id)
        serialized_data = serialize("json",[material])
        return HttpResponse(serialized_data, content_type="application/json")
    else:
       listam=Materiales.objects.filter(estado="activo")
       return render(request,"PresupuestoVApp/presupuestoobra.html", {"materiales":listam})
    
def registrarPVObra(request): 
    
 if request.is_ajax and request.method == "POST":
    dtig =json.loads(request.POST.get('valoresig'))
    print(dtig)
    for objif in dtig:
        idp=objif['idpvo']
        fecha=objif['fechaob']
        tipoobra =objif['tipoobra']
        costoobra =objif['costooba']
        solucionsa =objif['solucionsa']
        totalobraa =objif['costott']
    
        print(fecha)
        print(tipoobra)
        print( totalobraa)
    

        idpv= Presupuestovdg.objects.get(id=idp)
        idpv.id=idp

        presupuestodg= Presupuestovdgobra.objects.create(fecha=fecha,tipoobra=tipoobra,costoobra=costoobra,solucionsa=solucionsa,totalobraa=totalobraa,idpdg=idpv ) #
    
        idpdg= Presupuestovdgobra.objects.all().last() #obtengo el ultimo registro de los datos generales de presupuesto
        
        ###### para tabla de materiales
        
        datamt =json.loads( request.POST.get('valorestmt'))
        print(datamt)  
        for obj in datamt:
                idmp=obj['idm'] # id del material
                cantidad=obj['cantidad']
                preciouni=obj['preciouni']
                subtotal=obj['subtotal']
                
                idm= Materiales.objects.get(id=idmp)
                idm.id=idmp
                
                #ma=obj['idm']
                print(cantidad)
                print(preciouni)
                print(subtotal)
            
                PreMateO = PresupuestovMaterialesobra.objects.filter(idm=idm,idpo=idpdg ).exists()
                print(PreMateO)
                #PresupuestoMateriales()
                if PreMateO== True:
                    presupuestoMateriales=PresupuestovMaterialesobra.objects.get(idm=idm,idpo=idpdg )
                
                    print(presupuestoMaterialeso.cantidad)
                    presupuestoMaterialeso.cantidad=presupuestoMaterialeso.cantidad+cantidad
                    presupuestoMaterialeso.preciouni=presupuestoMaterialeso.preciouni+preciouni
                    presupuestoMaterialeso.subtotal=presupuestoMaterialeso.subtotal+subtotal
                    presupuestoMaterialeso.save()
                else:
                    presupuestoMaterialeso= PresupuestovMaterialesobra.objects.create(cantidad=cantidad, preciouni=preciouni, subtotal=subtotal,idm=idm,idpo=idpdg)
  
  ###  para tabla mano de obra
        datamo =json.loads( request.POST.get('valorestmo'))
        print(datamo)  
        for obj in datamo:
                descripcion=obj['descripc'] # id del material
                unidad=obj['unidad']
                preciouni=obj['preciouni']
                cantidad=obj['cantidad']
                subtotal=obj['subtotal']
                
                print(descripcion)
                print(cantidad)
                print(preciouni)
                print(subtotal)
            
                PreMoo = PresupuestovManoObraobra.objects.filter(idpo=idpdg ).exists()
                print(PreMoo)

                if PreMoo== True:
                    presupuestoManoObrao=PresupuestovManoObraobra.objects.get(idpo=idpdg )
                
                    presupuestoManoObrao.cantidad=presupuestoManoObrao.cantidad+cantidad
                    presupuestoManoObrao.preciouni=presupuestoManoObrao.preciouni+preciouni
                    presupuestoManoObrao.subtotal=presupuestoManoObrao.subtotal+subtotal
                    presupuestoManoObrao.save()
                else:
                    presupuestoManoObrao= PresupuestovManoObraobra.objects.create(descripcion=descripcion,unidad=unidad,cantidad=cantidad, preciouni=preciouni, subtotal=subtotal,idpo=idpdg)
    
    mensaje="Datos guardados"
    registroBit(request, "Se registro Presupuesto Obras adicionales " + presupuestodg.idpdg.ids.perfil.dui, "Registro")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=presupuestodg.idpdg.ids.perfil.id)  # id de perfil  
 
def listaPVO(request): 
    listapo=Presupuestovdgobra.objects.all()
    return render(request, "PresupuestoVApp/listaPVO.html", {"listapo":listapo})

def editarPVO(request, id):# id Presupuestovdgobra
    lista_materiales_json = []
    lista_mano_obra_json = []

    try:
        pvdgo=  Presupuestovdgobra.objects.get(id=id)
    except Presupuestovdgobra.DoesNotExist:
        pvdgo=""

    try:
        pdg=  Presupuestovdg.objects.get(id=pvdgo.idpdg.id)
    except Presupuestovdg.DoesNotExist:
        pdg=""
    
    try:
        do= datosObra.objects.get(idSolicitud=pdg.ids.id)
    except datosObra.DoesNotExist:
        do=""
  
    try:
        listam=Materiales.objects.filter(estado="activo")
    except Materiales.DoesNotExist:
        listam=""

    try:
        lista_materiales= PresupuestovMaterialesobra.objects.filter(idpo=pvdgo.id)
        datos=[]
        for item in lista_materiales:
            datos.append ( {'id': item.id, 'precio':item.preciouni,'cantida': item.cantidad,'total':item.subtotal,
            "nombre":item.idm.nombre,"descripcion":item.idm.descripcion,"unidad":item.idm.unidad,"idm":item.idm.id })
        lista_materiales_json = json.dumps(datos,default=str)
    except PresupuestovMaterialesobra.DoesNotExist:
        lista_materiales=""

    try:
        lista_mano_obra= PresupuestovManoObraobra.objects.filter(idpo=pvdgo.id)
        datos=[]
        for item in lista_mano_obra:
            datos.append({
                "id":item.id,
                "descripcion":item.descripcion,
                "unidad":item.unidad,
                "preciouni":item.preciouni,
                "cantidad":item.cantidad,
                "total":item.subtotal,
            })
            lista_mano_obra_json = json.dumps(datos, default=str)
    except PresupuestovManoObraobra.DoesNotExist:
        lista_mano_obra=""
        lista_mano_obra_json=""

    
    return render(request,"PresupuestoVApp/editarPresupuestoObra.html", {"materiales":listam,"pvdgo":pvdgo,
                             "pdg":pdg, "do":do, "listMateriales":lista_materiales_json,
                             "lista_mano_obra_json":lista_mano_obra_json,})


def modificarPVO(request):
    if request.is_ajax and request.method == "POST":
        dtig =json.loads(request.POST.get('valoresig'))
        for objif in dtig:
            idp=objif['idpv']
            fecha=objif['fechaob']
            tipoobra =objif['tipoobra']
            costoobra =objif['costooba']
            solucionsa =objif['solucionsa']
            totalobraa =objif['costott']
            presupuesto = objif['idPresupuesto']  

            idpv= Presupuestovdg.objects.get(id=idp)
            idpv.id=idp
            idsol= solicitud.objects.get(id=idpv.ids.id)
            
            presupuesto = Presupuestovdgobra.objects.get(id=presupuesto, idpdg=idpv.id)

            presupuestodg= Presupuestovdgobra.objects.update_or_create(idpdg=idpv, id=presupuesto.id ,
            defaults={
                "fecha":fecha,
             "tipoobra":tipoobra,
             "costoobra":costoobra,
             "solucionsa":solucionsa,
             "totalobraa":totalobraa,
            "idpdg":idpv }) #
        
            idpdg= presupuesto #obtengo el ultimo registro de los datos generales de presupuesto
            
            ###### para tabla de materiales
            
            datamt =json.loads( request.POST.get('valorestmt'))
            lista_original = PresupuestovMaterialesobra.objects.filter(
                idpo=presupuesto.id)
            lista_actual = []  # el id que no este aqui se eliminara
            for obj in datamt:
                    idmp=obj['idm'] # id del material
                    cantidad=obj['cantidad']
                    preciouni=obj['preciouni']
                    subtotal=obj['subtotal']
                    
                    idm= Materiales.objects.get(id=idmp)
                    idm.id=idmp
                    lista_actual.append(idmp) 
                    PreMate = PresupuestovMaterialesobra.objects.update_or_create(idm=idm, idpo=presupuesto.id,
                        defaults={
                            "preciouni":preciouni,
                            "cantidad":cantidad,
                            "subtotal":subtotal,
                            "idm":idm,
                            "idpo":idpdg,
                        })
            # ciclo para eliminar  material
            for item in lista_original:
                if ((item.idm.id in lista_actual) == False):
                    PreMate = PresupuestovMaterialesobra.objects.get(
                        idm=item.idm, idpo=presupuesto.id)
                    PreMate.delete()
        
    ###  para tabla mano de obra
            datamo = json.loads( request.POST.get('valorestmo'))
            lista_original = PresupuestovManoObraobra.objects.filter(
                idpo=presupuesto.id)
            lista_actual = []
            for obj in datamo:
                    id =obj['id']
                    descripcion=obj['descripc'] 
                    unidad=obj['unidad']
                    preciouni=obj['preciouni']
                    cantidad=obj['cantidad']
                    subtotal=obj['subtotal']
                    
                    try: 
                        mano_obra = PresupuestovManoObraobra.objects.update_or_create( id=id, idpo=presupuesto.id,
                                defaults={
                                "descripcion":descripcion, 
                                "unidad":unidad, 
                                "preciouni":preciouni, 
                                "cantidad":cantidad, 
                                "subtotal":subtotal, 
                                "idpo":presupuesto, 
                                })  
                        lista_actual.append(int(id))
                    except Exception:
                        presupuestoManoObra= PresupuestovManoObraobra.objects.create(descripcion=descripcion,
                                unidad=unidad,cantidad=cantidad, 
                                preciouni=preciouni, 
                                subtotal=subtotal,
                                idpo=idpdg)   
                        lista_actual.append(presupuestoManoObra.id)           
            # ciclo para eliminar mano de obra
            for item in lista_original:
                if ((item.id in lista_actual) == False):
                    PreMate = PresupuestovManoObraobra.objects.get(
                        id=item.id, idpo=presupuesto.id)
                    PreMate.delete()

            
        
    mensaje="Datos actualizados"
    registroBit(request, "Se actualizó Presupuesto de Vivienda Obras adicionales " + idsol.perfil.dui, "Actualización")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=idsol.perfil.id)  # id de perfil ")
 
