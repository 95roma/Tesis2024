from django.shortcuts import render,redirect
from ClienteApp.models import *
from email import message
from django.contrib import messages

from EvaluacionIvEFApp.models import *
from SolicitudesApp.models import *
from TesisApp.views import registroBit

# Create your views here.
def evaluacionf(request, id):
    cliente = Perfil.objects.get(id=id)
    return render(request,"EvaluacionIvEFApp/evaluacionIvE.html", {"perfil":cliente})

def registrarEvaluacion(request): 
    # bienes 
    try:    
        numerob=request.POST.getlist('numerob')
    except :
        numerob=""    
    try:    
        descripcionbien=request.POST.getlist('descripcionbien')
    except :
        descripcionbien=""    
    try:    
        preciocop=request.POST.getlist('preciocop')
    except :
        preciocop=""    
    try:    
        cuotam=request.POST.getlist('cuotam')
    except :
        cuotam=""    

    print(numerob)

    # egresos
    idp=request.POST['idp']
    alimentaciongf=request.POST['alimentaciongf']
    educaciongf=request.POST['educaciongf']
    transporte=request.POST['transporte']
    saludiio=request.POST['saludiio']
    afpiio=request.POST['afpiio']
    servicios =request.POST['servicios']
    alquiler=request.POST['alquiler']
    planilla=request.POST['planilla']
    ventanilla=request.POST['ventanilla']
    hphes =request.POST['hphes']
    otrosdes=request.POST['otrosdes']
    recreacion=request.POST['recreacion']
    imprevistos =request.POST['imprevistos']
    totalp =request.POST['totalp']

    if(alimentaciongf=="" ):
        alimentaciongf = 0.00    
    if(educaciongf=="" ):
        educaciongf = 0.00
    if(transporte=="" ):
        transporte = 0.00
    if(saludiio=="" ):
        saludiio = 0.00
    if(afpiio=="" ):
        afpiio = 0.00
    if(servicios=="" ):
        servicios = 0.00
    if(alquiler=="" ):
        alquiler = 0.00
    if(planilla=="" ):
        planilla = 0.00
    if(ventanilla=="" ):
        ventanilla = 0.00
    if(hphes=="" ):
        hphes = 0.00
    if(otrosdes=="" ):
        otrosdes = 0.00
    if(recreacion=="" ):
        recreacion = 0.00
    if(imprevistos=="" ):
        imprevistos = 0.00
    if(totalp=="" ):
        totalp = 0.00

    # ingresos
    familiar =request.POST['familiar']
    otrosing =request.POST['otrosing']
    totald =request.POST['totald']

    if(familiar=="" ):
        familiar = 0.00

    if(otrosing=="" ):
        otrosing = 0.00

    if(totald=="" ):
        totald = 0.00

    #capacidad pago
    pendeudamientoa =request.POST['pendeudamientoa']
    disponible =request.POST['disponible']
    pdisponible =request.POST['pdisponible']
    cuota =request.POST['cuota']
    pcuota =request.POST['pcuota']
    superavit =request.POST['superavit']
    deficit =request.POST['deficit']

    if(pendeudamientoa=="" ):
        pendeudamientoa = '0.00%'   

    if(disponible=="" ):
        disponible = 0.00

    if(pdisponible==" " ):
        pdisponible = '0.00%'

    if(cuota=="" ):
        cuota = 0.00

    if(pcuota=="" ):
        pcuota = '0.00%'

    if(superavit=="" or superavit=="-"):
        superavit = 0.00

    if(deficit=="" or deficit=="-"):
        deficit = 0.00

    idperf=Perfil.objects.get(id=idp)
    idperf.id=idp

    egresosf=Egresosf.objects.create(alimentacion=alimentaciongf,educacion=educaciongf,transporte=transporte,salud=saludiio,AFP=afpiio,servicios=servicios,alquiler=alquiler,pplanilla=planilla,pventanilla=ventanilla,phplhes=hphes,otrosdesc=otrosdes,recreacion=recreacion,imprevistos=imprevistos ,total=totalp,estado=1,idp=idperf)
    #actualizo estado para administrar el perfil del cliente
    idperf.estadosoli=3
    idperf.save()
    
    ideg= Egresosf.objects.all().last() #obtengo el ultimo registro

    ingresosf=Ingresosf.objects.create(familiar=familiar,otrosingres=otrosing,totali=totald,ide=ideg)

    capacidadpagof=Capacidadpagof.objects.create(porcentajee=pendeudamientoa,disponible=disponible,porcentajedis=pdisponible,cuota=cuota,porcentajecuot=pcuota,superavit=superavit,deficit=deficit,estado="activo",ide=ideg)
    
    for i in range(len(numerob)):
        if (numerob[i] != ""):
            bienesh = Bienesh.objects.create( numero=numerob[i], descripcionbien=descripcionbien[i], 
            preciocompra=preciocop[i], cuotamensual=cuotam[i], ide=ideg)

    mensaje="Datos guardados"
    registroBit(request, "Se registro formulario de Evaluacion Ingresos vs Egresos " + idperf.dui, "Registro")
    messages.success(request, mensaje)

    return redirect('administrarPerfil', id=egresosf.idp.id)  # id de perfil 

def listaEvaluacion(request):
    listae=Capacidadpagof.objects.filter(estado="activo")
    return render(request, "EvaluacionIvEFApp/listaEvaluacion.html", {"evaluaciones":listae})

def editarEvaluacion(request, id):
    ide=int(id)
    try:    
        egf=  Egresosf.objects.get(id=ide)
    except Egresosf.DoesNotExist:
        egf="" 
    try: 
        cliente = Perfil.objects.get(id=egf.idp.id)
    except Perfil.DoesNotExist:
        cliente=""        
    try:    
        igf=  Ingresosf.objects.get(ide=ide)
    except Ingresosf.DoesNotExist:
        igf="" 
    try:    
        cpf=  Capacidadpagof.objects.get(ide=ide)
    except Capacidadpagof.DoesNotExist:
        cpf="" 
    try:
        bns=Bienesh.objects.filter(ide=ide)
    except bns.DoesNotExist:
        bns=""
    return render(request,"EvaluacionIvEFApp/modificarEvaluacionIvE.html", {"perfil":cliente,"egresos":egf,"ingresos":igf,"cpago":cpf,"bienes":bns})

def modificarEvaluacion(request): 
    # egresos
    ide=request.POST['ide']
    alimentaciongf=request.POST['alimentaciongf']
    educaciongf=request.POST['educaciongf']
    transporte=request.POST['transporte']
    saludiio=request.POST['saludiio']
    afpiio=request.POST['afpiio']
    servicios =request.POST['servicios']
    alquiler=request.POST['alquiler']
    planilla=request.POST['planilla']
    ventanilla=request.POST['ventanilla']
    hphes =request.POST['hphes']
    otrosdes=request.POST['otrosdes']
    recreacion=request.POST['recreacion']
    imprevistos =request.POST['imprevistos']
    totalp =request.POST['totalp']

    if(alimentaciongf==" " ):
        alimentaciongf = 0.00    
    if(educaciongf==" " ):
        educaciongf = 0.00
    if(transporte==" " ):
        transporte = 0.00
    if(saludiio==" " ):
        saludiio = 0.00
    if(afpiio==" " ):
        afpiio = 0.00
    if(servicios==" " ):
        servicios = 0.00
    if(alquiler==" " ):
        alquiler = 0.00
    if(planilla==" " ):
        planilla = 0.00
    if(ventanilla==" " ):
        ventanilla = 0.00
    if(hphes==" " ):
        hphes = 0.00
    if(otrosdes==" " ):
        otrosdes = 0.00
    if(recreacion==" " ):
        recreacion = 0.00
    if(imprevistos==" " ):
        imprevistos = 0.00
    if(totalp==" " ):
        totalp = 0.00

    # ingresos
    familiar =request.POST['familiar']
    otrosing =request.POST['otrosing']
    totald =request.POST['totald']

    if(familiar==" " ):
        familiar = 0.00

    if(otrosing==" " ):
        otrosing = 0.00

    if(totald==" " ):
        totald = 0.00

    #capacidad pago
    pendeudamientoa =request.POST['pendeudamientoa']
    disponible =request.POST['disponible']
    pdisponible =request.POST['pdisponible']
    cuota =request.POST['cuota']
    pcuota =request.POST['pcuota']
    superavit =request.POST['superavit']
    deficit =request.POST['deficit']

    if(pendeudamientoa==" " ):
        pendeudamientoa = '0.00%'   

    if(disponible==" " ):
        disponible = 0.00

    if(pdisponible==" " ):
        pdisponible = '0.00%'

    if(cuota==" " ):
        cuota = 0.00

    if(pcuota==" " ):
        pcuota = '0.00%'

    if(superavit==" " or superavit=="-"):
        superavit = 0.00

    if(deficit==" " or deficit=="-"):
        deficit = 0.00
    
    #modificar egresos
    megf=Egresosf.objects.get(id=ide)
    megf.alimentacion=alimentaciongf
    megf.educacion=educaciongf
    megf.transporte=transporte
    megf.salud=saludiio
    megf.AFP=afpiio
    megf.servicios=servicios
    megf.alquiler=alquiler
    megf.pplanilla=planilla
    megf.pventanilla=ventanilla
    megf.phplhes=hphes
    megf.otrosdesc=otrosdes
    megf.recreacion=recreacion
    megf.imprevistos=imprevistos 
    megf.total=totalp
    megf.save()

    #modificar ingresos
    migf=Ingresosf.objects.get(ide=ide)
    migf.familiar=familiar
    migf.otrosingres=otrosing
    migf.totali=totald
    migf.save()

    #modificar capacidad de pago
    mcpf=Capacidadpagof.objects.get(ide=ide)
    mcpf.porcentajee=pendeudamientoa
    mcpf.disponible=disponible
    mcpf.porcentajedis=pdisponible
    mcpf.cuota=cuota
    mcpf.porcentajecuot=pcuota
    mcpf.superavit=superavit
    mcpf.deficit=deficit
    mcpf.save()

    #modificar bienes
    ide = Egresosf.objects.get(id=ide)
    idb=request.POST.getlist('idbns')
    nb=request.POST.getlist('numerob')
    descb =request.POST.getlist('descripcionbien') 
    preb =request.POST.getlist('preciocop')
    cuotab =request.POST.getlist('cuotam') 
    print(len(nb))
    for i in range(len(nb)):
        print('paso')
        if (descb[i] != ""):
            if(idb[i]==""):#si registro un nuevo bien ejecuta la orden sin enviar id de la tabla ya que no existe ese campo
                bns = Bienesh.objects.update_or_create(ide=ide,numero=nb[i],descripcionbien=descb[i],preciocompra=preb[i],
                defaults={'numero':nb[i],
                'descripcionbien':descb[i],
                'preciocompra':preb[i],
                'cuotamensual':cuotab[i],
                'ide':ide
                })            
            else: 
                bns = Bienesh.objects.update_or_create(ide=ide,id=idb[i],
                defaults={'numero':nb[i],
                'descripcionbien':descb[i],
                'preciocompra':preb[i],
                'cuotamensual':cuotab[i],
                'ide':ide
                })


    mensaje="Datos Actualizados"
    registroBit(request, "Se actualizó formulario de evaluacion de Ingreso vs Egresos " + ide.idp.dui, "Actualización")
    messages.success(request, mensaje)

    return redirect('administrarPerfil', id=megf.idp.id)  # id de perfil 

def darBajaF(request, id, idp): # id capacidad de pago, id de perfil
    estad="inactivo" 
    d=solicitud.objects.filter(perfil=idp,estadosoli=3).exists()
    cap= Capacidadpagof.objects.get(id=id)
    egr= Egresosf.objects.get(id=cap.ide.id)
    if d == True :
        mensaje="La Evaluación No puede darse de baja"
        messages.warning(request, mensaje)
    elif cap.estado=="activo" and egr.estado==1:          
        cap.estado =estad
        cap.save()
        egr.estado=0
        egr.save()
        mensaje="La Evaluación fue dada de baja "
        registroBit(request, mensaje + egr.idp.dui, "Desactivacion")
        messages.success(request, mensaje)
    return redirect('/EvaluacionIvEFApp/listaEvaluacion')
