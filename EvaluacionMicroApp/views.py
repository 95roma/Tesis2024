from django.shortcuts import render,redirect
from django.contrib import messages
from ClienteApp.models import *
from EvaluacionMicroApp.models import *
from SolicitudesApp.models import *
from TesisApp.views import registroBit

# Create your views here.
def evaluacionm(request, id):
    cliente = Perfil.objects.get(id=id)
    return render(request,"EvaluacionMicroApp/evaluacionM.html", {"perfil":cliente})

def registrarEvaluacionm(request): 
    
    idp=request.POST['idp']
    tiponegocio=request.POST['tiponeg']

    # activo
    tcirculantea=request.POST['circulantea']
    caja=request.POST['caja']
    bancos=request.POST['banco']
    cuentaspc=request.POST['cuentaspc']
    inventarios=request.POST['inventario']
    tfijoa=request.POST['fijoa']
    mobiliario=request.POST['mobiliario']
    terrenos=request.POST['terreno']
    vehiculos=request.POST['vehiculo']
    totalactivo=request.POST['totalact']

    if(tcirculantea=="" ):
        tcirculantea = 0.00
    if(caja=="" ):
        caja = 0.00
    if(bancos=="" ):
        bancos = 0.00
    if(cuentaspc=="" ):
        cuentaspc = 0.00
    if(inventarios=="" ):
        inventarios = 0.00
    if(tfijoa=="" ):
        tfijoa = 0.00
    if(mobiliario=="" ):
        mobiliario = 0.00
    if(terrenos=="" ):
        terrenos = 0.00
    if(vehiculos=="" ):
        vehiculos = 0.00
    if(totalactivo=="" ):
        totalactivo = 0.00
    
    # pasivo
    tcirculantep=request.POST['circulantep']
    proveedores=request.POST['proveedor']
    cuentaspp=request.POST['cuantaspp']
    prestamoscp=request.POST['prestamocp']
    fijop=request.POST['fijop']
    prestamoslp=request.POST['prestamolp']
    totalpasivo=request.POST['totalpasivo']
    patrimonio=request.POST['patrimonio']
    capital=request.POST['capital']
    pasivompatrim=request.POST['pasivopat']

    if(tcirculantep==""):
        tcirculantep = 0.00    
    if(proveedores==""):
        proveedores = 0.00
    if(cuentaspp==""):
        cuentaspp = 0.00
    if(prestamoscp==""):
        prestamoscp = 0.00
    if(fijop=="" ):
        fijop = 0.00
    if(prestamoslp==""):
        prestamoslp = 0.00
    if(totalpasivo=="" ):
        totalpasivo = 0.00
    if(patrimonio=="" ):
        patrimonio = 0.00
    if(capital=="" ):
        capital = 0.00
    if(pasivompatrim=="" ):
        pasivompatrim = 0.00

    # estado de resultado
    ventast=request.POST['ventastp']
    costovent=request.POST['costovt']
    utilidadbt=request.POST['utilidadb']
    gastosgral=request.POST['gastosg']
    transporteer=request.POST['transporteer']
    servicioser=request.POST['servicioser']
    impuestos=request.POST['impuestos']
    alquilerer=request.POST['alquilerer']
    cuotaprest=request.POST['cuotaprest']
    imprevistoser=request.POST['imprevistoser']
    utilidadneta=request.POST['utilidadn']
    mensual=request.POST['mensual']

    if(ventast==""):
        ventast = 0.00    
    if(costovent==""):
        costovent = 0.00
    if(utilidadbt==""):
        utilidadbt = 0.00
    if(gastosgral==""):
        gastosgral = 0.00
    if(transporteer=="" ):
        transporteer = 0.00
    if(servicioser==""):
        servicioser = 0.00
    if(impuestos=="" ):
        impuestos = 0.00
    if(alquilerer=="" ):
        alquilerer = 0.00
    if(cuotaprest=="" ):
        cuotaprest = 0.00
    if(imprevistoser=="" ):
        imprevistoser = 0.00
    if(utilidadneta=="" ):
        utilidadneta = 0.00
    if(mensual=="" ):
        mensual = 0.00

    # egresos
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
   
    if(alimentaciongf==""):
        alimentaciongf = 0.00    
    if(educaciongf==""):
        educaciongf = 0.00
    if(transporte==""):
        transporte = 0.00
    if(saludiio==""):
        saludiio = 0.00
    if(afpiio=="" ):
        afpiio = 0.00
    if(servicios==""):
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
    negocio =request.POST['negocio']
    remesas =request.POST['remesas']
    totald =request.POST['totald']

    if(negocio =="" ):
        negocio = 0.00

    if(remesas =="" ):
        remesas = 0.00

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

    if(pdisponible=="" ):
        pdisponible = '0.00%'

    if(cuota=="" ):
        cuota = 0.00

    if(pcuota=="" ):
        pcuota = '0.00%'

    if(superavit=="" or superavit=="-"):
        superavit = 0.00

    if(deficit=="" or deficit=="-"):
        deficit = 0.00

    idperm=Perfil.objects.get(id=idp)
    idperm.id=idp

    balancesm=Balancesm.objects.create(tiponegocio=tiponegocio,idp=idperm,estado=1)
    idperm.estadosoli=2
    idperm.save()

    idbs= Balancesm.objects.all().last() #obtengo el ultimo registro

    activobsm=Activobsm.objects.create(tcirculantea=tcirculantea,caja=caja,bancos=bancos,cuentaspc=cuentaspc,inventarios=inventarios,tfijoa=tfijoa,mobiliario=mobiliario,terrenos=terrenos,vehiculos=vehiculos,totalactivo=totalactivo,idbs=idbs)

    pasivobsm=Pasivobsm.objects.create(tcirculantep=tcirculantep,proveedores=proveedores,cuentaspp=cuentaspp,prestamoscp=prestamoscp,fijop=fijop,prestamoslp=prestamoslp,totalpasivo=totalpasivo,patrimonio=patrimonio,capital=capital,pasivompatrim=pasivompatrim ,idbs=idbs)


    estadorm=Estadorm.objects.create(ventast=ventast,costovent=costovent,utilidadbt=utilidadbt,gastosgral=gastosgral,transporte=transporteer,servicios=servicioser,impuestos=impuestos,alquiler=alquilerer,cuotaprest=cuotaprest,imprevistoser=imprevistoser,utilidadneta=utilidadneta,mensual=mensual,idb=idbs)


    egresosm=Egresosm.objects.create(alimentacion=alimentaciongf,educacion=educaciongf,transporte=transporte,salud=saludiio,AFP=afpiio,servicios=servicios,alquiler=alquiler,pplanilla=planilla,pventanilla=ventanilla,phplhes=hphes,otrosdesc=otrosdes,recreacion=recreacion,imprevistos=imprevistos ,total=totalp,idb=idbs)
    idem= Egresosm.objects.all().last() #obtengo el ultimo registro

    ingresosm=Ingresosm.objects.create(negocio=negocio,remesas=remesas,totali=totald,ide=idem)

    capacidadpagom=Capacidadpagom.objects.create(porcentajee=pendeudamientoa,disponible=disponible,porcentajedis=pdisponible,cuota=cuota,porcentajecuot=pcuota,superavit=superavit,deficit=deficit,estado="activo",ide=idem)
    
    mensaje="Datos guardados"
    registroBit(request, "Se registro formulario evaluacion Microempresa de Ingreso vs Egresos " + balancesm.idp.dui, "Registro")
    messages.success(request, mensaje)

    return redirect('administrarPerfil', id=balancesm.idp.id)  # id de perfil 

def listaEvaluacionm(request):
    listaem=Capacidadpagom.objects.filter(estado="activo")
    return render(request, "EvaluacionMicroApp/listaEvaluacionM.html", {"evaluacionesm":listaem})

def editarEvaluacionm(request, id): # ide de egresos 
    ide=int(id)
    try:    
        egm=  Egresosm.objects.get(id=ide)
    except Egresosm.DoesNotExist:
        egm="" 
    try:    
        blm=  Balancesm.objects.get(id=egm.idb.id)
    except Balancesm.DoesNotExist:
        blm="" 

    try:    
        atm=  Activobsm.objects.get(idbs=egm.idb.id)
    except Activobsm.DoesNotExist:
        atm=""
    try:    
        psm=  Pasivobsm.objects.get(idbs=egm.idb.id)
    except Pasivobsm.DoesNotExist:
        psm=""
    try:    
        etm=  Estadorm.objects.get(idb=egm.idb.id)
    except Estadorm.DoesNotExist:
        etm="" 

    try: 
        cliente = Perfil.objects.get(id=egm.idb.idp.id)
    except Perfil.DoesNotExist:
        cliente=""        
    try:    
        igm=  Ingresosm.objects.get(ide=ide)
    except Ingresosm.DoesNotExist:
        igm="" 
    try:    
        cpm=  Capacidadpagom.objects.get(ide=ide)
    except Capacidadpagom.DoesNotExist:
        cpm="" 

    return render(request,"EvaluacionMicroApp/modificarEvaluacionM.html", {"perfil":cliente,"balance":blm,"activo":atm,"pasivo":psm,"estado":etm,"egresos":egm,"ingresos":igm,"cpago":cpm})

def modificarEvaluacionm(request): 
    
    idb=request.POST['idb']
    tiponegocio=request.POST['tiponeg']

    # activo
    tcirculantea=request.POST['circulantea']
    caja=request.POST['caja']
    bancos=request.POST['banco']
    cuentaspc=request.POST['cuentaspc']
    inventarios=request.POST['inventario']
    tfijoa=request.POST['fijoa']
    mobiliario=request.POST['mobiliario']
    terrenos=request.POST['terreno']
    vehiculos=request.POST['vehiculo']
    totalactivo=request.POST['totalact']

    if(tcirculantea=="" ):
        tcirculantea = 0.00
    if(caja=="" ):
        caja = 0.00
    if(bancos=="" ):
        bancos = 0.00
    if(cuentaspc=="" ):
        cuentaspc = 0.00
    if(inventarios=="" ):
        inventarios = 0.00
    if(tfijoa=="" ):
        tfijoa = 0.00
    if(mobiliario=="" ):
        mobiliario = 0.00
    if(terrenos=="" ):
        terrenos = 0.00
    if(vehiculos=="" ):
        vehiculos = 0.00
    if(totalactivo=="" ):
        totalactivo = 0.00
    
    # pasivo
    tcirculantep=request.POST['circulantep']
    proveedores=request.POST['proveedor']
    cuentaspp=request.POST['cuantaspp']
    prestamoscp=request.POST['prestamocp']
    fijop=request.POST['fijop']
    prestamoslp=request.POST['prestamolp']
    totalpasivo=request.POST['totalpasivo']
    patrimonio=request.POST['patrimonio']
    capital=request.POST['capital']
    pasivompatrim=request.POST['pasivopat']

    if(tcirculantep==""):
        tcirculantep = 0.00    
    if(proveedores==""):
        proveedores = 0.00
    if(cuentaspp==""):
        cuentaspp = 0.00
    if(prestamoscp==""):
        prestamoscp = 0.00
    if(fijop=="" ):
        fijop = 0.00
    if(prestamoslp==""):
        prestamoslp = 0.00
    if(totalpasivo=="" ):
        totalpasivo = 0.00
    if(patrimonio=="" ):
        patrimonio = 0.00
    if(capital=="" ):
        capital = 0.00
    if(pasivompatrim=="" ):
        pasivompatrim = 0.00

    # estado de resultado
    ventast=request.POST['ventastp']
    costovent=request.POST['costovt']
    utilidadbt=request.POST['utilidadb']
    gastosgral=request.POST['gastosg']
    transporteer=request.POST['transporteer']
    servicioser=request.POST['servicioser']
    impuestos=request.POST['impuestos']
    alquilerer=request.POST['alquilerer']
    cuotaprest=request.POST['cuotaprest']
    imprevistoser=request.POST['imprevistoser']
    utilidadneta=request.POST['utilidadn']
    mensual=request.POST['mensual']

    if(ventast==""):
        ventast = 0.00    
    if(costovent==""):
        costovent = 0.00
    if(utilidadbt==""):
        utilidadbt = 0.00
    if(gastosgral==""):
        gastosgral = 0.00
    if(transporteer=="" ):
        transporteer = 0.00
    if(servicioser==""):
        servicioser = 0.00
    if(impuestos=="" ):
        impuestos = 0.00
    if(alquilerer=="" ):
        alquilerer = 0.00
    if(cuotaprest=="" ):
        cuotaprest = 0.00
    if(imprevistoser=="" ):
        imprevistoser = 0.00
    if(utilidadneta=="" ):
        utilidadneta = 0.00
    if(mensual=="" ):
        mensual = 0.00

    # egresos
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
   
    if(alimentaciongf==""):
        alimentaciongf = 0.00    
    if(educaciongf==""):
        educaciongf = 0.00
    if(transporte==""):
        transporte = 0.00
    if(saludiio==""):
        saludiio = 0.00
    if(afpiio=="" ):
        afpiio = 0.00
    if(servicios==""):
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
    negocio =request.POST['negocio']
    remesas =request.POST['remesas']
    totald =request.POST['totald']

    if(negocio =="" ):
        negocio = 0.00

    if(remesas =="" ):
        remesas = 0.00

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

    if(pdisponible=="" ):
        pdisponible = '0.00%'

    if(cuota=="" ):
        cuota = 0.00

    if(pcuota=="" ):
        pcuota = '0.00%'

    if(superavit=="" or superavit=="-"):
        superavit = 0.00

    if(deficit=="" or deficit=="-"):
        deficit = 0.00

    # modificar balance micro
    mbm=Balancesm.objects.get(id=idb)
    mbm.tiponegocio=tiponegocio
    mbm.save()

    # modificar activos micro
    mam=Activobsm.objects.get(idbs=idb)
    mam.tcirculantea=tcirculantea
    mam.caja=caja
    mam.bancos=bancos
    mam.cuentaspc=cuentaspc
    mam.inventarios=inventarios
    mam.tfijoa=tfijoa
    mam.mobiliario=mobiliario
    mam.terrenos=terrenos
    mam.vehiculos=vehiculos
    mam.totalactivo=totalactivo
    mam.save()

    # modificar pasivos micro
    mpm=Pasivobsm.objects.get(idbs=idb)
    mpm.tcirculantep=tcirculantep
    mpm.proveedores=proveedores
    mpm.cuentaspp=cuentaspp
    mpm.prestamoscp=prestamoscp
    mpm.fijop=fijop
    mpm.prestamoslp=prestamoslp
    mpm.totalpasivo=totalpasivo
    mpm.patrimonio=patrimonio
    mpm.capital=capital
    mpm.pasivompatrim=pasivompatrim 
    mpm.save()
    

    # modificar estado de resultados micro
    merm=Estadorm.objects.get(idb=idb)
    merm.ventast=ventast
    merm.costovent=costovent
    merm.utilidadbt=utilidadbt
    merm.gastosgral=gastosgral
    merm.transporte=transporteer
    merm.servicios=servicioser
    merm.impuestos=impuestos
    merm.alquiler=alquilerer
    merm.cuotaprest=cuotaprest
    merm.imprevistoser=imprevistoser
    merm.utilidadneta=utilidadneta
    merm.mensual=mensual
    merm.save()
    

    # modificar egresos micro
    megm=Egresosm.objects.get(idb=idb)
    megm.alimentacion=alimentaciongf
    megm.educacion=educaciongf
    megm.transporte=transporte
    megm.salud=saludiio
    megm.AFP=afpiio
    megm.servicios=servicios
    megm.alquiler=alquiler
    megm.pplanilla=planilla
    megm.pventanilla=ventanilla
    megm.phplhes=hphes
    megm.otrosdesc=otrosdes
    megm.recreacion=recreacion
    megm.imprevistos=imprevistos 
    megm.total=totalp
    megm.save()


    # modificar ingresos micro
    migm=Ingresosm.objects.get(ide=megm.id)
    migm.negocio=negocio
    migm.remesas=remesas
    migm.totali=totald
    migm.save()

    # modificar capacidad de pago micro
    mcpgm=Capacidadpagom.objects.get(ide=megm.id)
    mcpgm.porcentajee=pendeudamientoa
    mcpgm.disponible=disponible
    mcpgm.porcentajedis=pdisponible
    mcpgm.cuota=cuota
    mcpgm.porcentajecuot=pcuota
    mcpgm.superavit=superavit
    mcpgm.deficit=deficit
    mcpgm.save()
    
    mensaje="Datos actualizados"
    registroBit(request, "Se actualizó formulario de evaluacion Microempresa Ingreso vs Egresos " + mbm.idp.dui, "Actualización")
    messages.success(request, mensaje)

    return redirect('administrarPerfil', id=mbm.idp.id)  # id de perfil 

def darBajaM(request, id, idp): # id capacidad de pago, id de perfil
    estad="inactivo" 
    d=solicitud.objects.filter(perfil=idp,estadosoli=3).exists()
    cap= Capacidadpagom.objects.get(id=id)
    egrm= Egresosm.objects.get(id=cap.ide.id)
    bal= Balancesm.objects.get(id=egrm.idb.id)
    print(bal)
    if d == True :
        mensaje="La Evaluación No puede darse de baja"
        messages.warning(request, mensaje)
    elif cap.estado=="activo" and bal.estado == 1:          
        cap.estado =estad
        cap.save()
        bal.estado = 0
        bal.save()
        mensaje="La Evaluación fue dada de baja"
        registroBit(request, "Se dio de baja formulario de Ingreso vs Egresos " + bal.idp.dui, "Desactivacion")
        messages.success(request, mensaje)
    return redirect('/EvaluacionMicroApp/listaEvaluacionm')
