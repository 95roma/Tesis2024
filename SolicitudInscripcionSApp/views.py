from django.shortcuts import render, redirect
from django.contrib import messages
from ClienteApp.models import Perfil
from ListaChequeoApp.models import listaChequeo
from SolicitudesApp.models import *
from SolicitudInscripcionSApp.models import *
from django.db.models import Subquery
from django.db.models import Q
import json

from TesisApp.views import registroBit

# Create your views here.

def solicitudI(request, id):
    sol= Solicitudis.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    if sol == True:
        solv= Solicitudis.objects.get(ids=id)
    
        return redirect('editarSIS', id=solv.id)   
    else:
        try:
            s= solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s=""

        try:
            dp=datosPersonales.objects.get(idSolicitud=id)
        except datosPersonales.DoesNotExist:
            dp=""

        try:
            d=  domicilio.objects.get(idSolicitud=id, tipo="Solicitante")
        except domicilio.DoesNotExist:
            d=""
        
        try:
            dt=  detalle.objects.get(idSolicitud=id)
        except detalle.DoesNotExist:
            dt=""
            
        try:
            listae=SolicitudisEnfermedad.objects.filter(estado="activo")
        except SolicitudisEnfermedad.DoesNotExist:
            listae=""

        
        return render(request, "SolicitudInscripcionSApp/solicitud.html", {"s":s, "dp":dp, "d":d, "dt":dt,"enfermedades":listae})

def report(request):
    
    return redirect( "../../SolicitudInscripcionSApp/reporte.py")

def registrarDs(request): 
  
    ids=request.POST['ids']
    montoaa=request.POST['montoaa']
    nuevoma=request.POST['nuevom']
    montot=request.POST['montot']
    plazo=request.POST['plazo']
    garantia=request.POST['garantia']
    estatura=request.POST['estatura']
    peso=request.POST['peso']
    dbeneficiario=request.POST['beneficiario']

    if(montoaa=="" ):
        montoaa = 0.00
    if(nuevoma=="" ):
        nuevoma = 0.00
    if(montot=="" ):
        montot = 0.00

    idsol= solicitud.objects.get(id=ids)
    idsol.id=ids 

    solicitudis=Solicitudis.objects.create(montoaa=montoaa,nuevoma=nuevoma,montot=montot,plazo=plazo,garantia=garantia,estatura=estatura,peso=peso,dbeneficiario=dbeneficiario,ids=idsol)

    idsi= Solicitudis.objects.all().last() #obtengo la ultima solicitud registrada 

    bandera= request.POST['passDS'] #inicia declaración de salud
    if(bandera == '1'):
       idsisenf =request.POST.getlist('idenf')
       idperfil =request.POST.getlist('idc') #identificador del cliente 
       fechap =request.POST.getlist('fechapad') 
       tratamientor =request.POST.getlist('tratamientor')
       situaciona =request.POST.getlist('situaciona')
       estado="activo"
       
       for i in range(len(fechap)):
        if (fechap[i] != ""):
            sispadecimiento = SolicitudisPadecimiento.objects.create(idsisenf=SolicitudisEnfermedad.objects.get(id=idsisenf[i]), idp=Perfil.objects.get(id=idperfil[i]), fechap=fechap[i],
             tratamientor =tratamientor[i],  situaciona=situaciona[i], estado=estado)
    #fin declaración de salud  

    # Inicia otro padecimiento
    try:
        personal=request.POST['personal']
    except :
        personal=""
    try:
        nombreenf=request.POST['padecimientoOt'].upper() 
    except :
        nombreenf=""

    estadoenf="activo" 
    enf=SolicitudisEnfermedad.objects.filter(nombreenf=nombreenf).exists()
    
    if enf == True:
            mensaje="la enfermedad o padecimiento ya existe"
            messages.warning(request, mensaje)
    elif nombreenf != "":
        enfermedades=SolicitudisEnfermedad.objects.create(nombreenf=nombreenf,estado=estadoenf,personal=personal)
        # Obtener el ID de la instancia de enfermedades
        siseid= SolicitudisEnfermedad.objects.get(id=enfermedades.id)
        siseid.id = enfermedades.id

        fechapO = request.POST.get('fechaOt', None) # si no se selecciona una fecha establece un valos vacio

        try:
            tratamientorO=request.POST['tratamientoOt']
        except :
            tratamientorO=""
        try:
            situacionaO=request.POST['situacionOt']
        except :
            situacionaO=""

        sispadecimientoOt = SolicitudisPadecimiento.objects.create(idsisenf=siseid, idp=Perfil.objects.get(id=request.POST['idpot']), fechap=fechapO,
                tratamientor =tratamientorO, situaciona=situacionaO, estado=estado)

    # fin otro padecimiento

    bandera= request.POST['passDO']  # guarda datos de declaracion de deformidades, amputaciones o defecto fisico
    if(bandera == '1'):
        tienedadf=request.POST['tiened']
        try:
            detallesdadf=request.POST['detalled']
        except :
            detallesdadf=""
        
        fumacp=request.POST['fumacp']
        try:
           cuantosd=request.POST['cuantosd']
        except :
            cuantosd=""
        
        bebidadalc=request.POST['ibebidas']
        try:
           frecuenciaalc=request.POST['frecuanciab']
        except :
            frecuenciaalc=""
       
        tratamientomd=request.POST['tratamientomd']
        try:
           detalletmd=request.POST['detalletm']
        except :
            detalletmd=""
        
        practicaad=request.POST['practicaadp']   
        try:
           clasead=request.POST['clase']
        except :
            clasead=""
        try:
          frecuenciaad=request.POST['frecuencia']
        except :
            frecuenciaad=""
        
        segurodd=request.POST['segurod']
   


    solicitudisdadf=Solicitudisdadf.objects.create(tienedadf=tienedadf,detallesdadf=detallesdadf,fumacp=fumacp,cuantosd=cuantosd,bebidadalc=bebidadalc,frecuenciaalc=frecuenciaalc,tratamientomd=tratamientomd,detalletmd=detalletmd,practicaad=practicaad,clasead=clasead,frecuenciaad=frecuenciaad,segurodd=segurodd,idsis=idsi)
    
     #####################################################
    # para guardar en la lista de chequeo 
    lchequo= listaChequeo.objects.get(ids=idsol)
    lchequo.declaracions ="Si"
    lchequo.save()
    
    mensaje="Datos guardados"
    registroBit(request, "Se registro formulario Inscrippcion Seguro " + idsol.perfil.dui, "Regisrtro")
    messages.success(request, mensaje)

    return redirect('administrarPerfil', id=solicitudis.ids.perfil.id)  # id de perfil 
 

def listaIs(request):
    lists=  Solicitudis.objects.all()
    #listper=Perfil.objects.filter(estado="activo")
    return render(request, "SolicitudInscripcionSApp/listaIS.html", {"lists":lists})


def editarSIS(request, id): # id de Solicitudis
    try:
        si=  Solicitudis.objects.get(id=id)
    except Solicitudis.DoesNotExist:
        si=""
    try:
        sid=  Solicitudisdadf.objects.get(idsis=si.id)
    except Solicitudisdadf.DoesNotExist:
        sid=""
    
    idSol=si.ids.id
    try:
        s=  solicitud.objects.get(id=idSol)
    except solicitud.DoesNotExist:
        s=""

    try:
        dp=datosPersonales.objects.get(idSolicitud=idSol)
    except datosPersonales.DoesNotExist:
        dp=""

    try:
        d=  domicilio.objects.get(idSolicitud=idSol, tipo="Solicitante")
    except domicilio.DoesNotExist:
        d=""
    
    try:
        listae=SolicitudisEnfermedad.objects.filter(estado="activo", personal="No")
    except SolicitudisEnfermedad.DoesNotExist:
        listae=""
    
    #pad=SolicitudisPadecimiento.objects.filter(idp=s.perfil.id)
    #padgen=SolicitudisEnfermedad.objects.filter(estado="activo", personal="No", id__in=Subquery(pad))
    #padper=SolicitudisEnfermedad.objects.filter(estado="activo", personal="Si", id__in=Subquery(pad))
    #print(pad)

    # Consulta para obtener registros con personal="No" o personal="Si"
    resultados = SolicitudisPadecimiento.objects.filter(Q(idp=s.perfil.id)  &  Q(idsisenf__personal="No") ).distinct()

    lista_padecimientos=[]
    # Itera sobre los resultados
    for resultado in resultados:
        lista_padecimientos.append({'id':resultado.id,'idenf':resultado.idsisenf.id,'enfermedad':resultado.idsisenf.nombreenf,'fecha':(resultado.fechap).isoformat(),'tratamiento':resultado.tratamientor,'situacion':resultado.situaciona,})
    lista_padecimientos_json = json.dumps(lista_padecimientos)
    #print(lista_padecimientos_json)
        # Accede a los datos que necesitas, por ejemplo:
        #print(f"ID: {resultado.id},enfermedad: {resultado.idsisenf.nombreenf}, Fecha: {resultado.fechap}, Tratamiento: {resultado.tratamientor}, Situación: {resultado.situaciona}")
    
    
    # compruebo si la solicitud tiene una enfermedad personal
    conSi = SolicitudisPadecimiento.objects.filter(Q(idp=s.perfil.id)  &  Q(idsisenf__personal="Si")).exists()

    if conSi==True:
        # Consulta para obtener registros con  personal="Si"
        resultadosSi = SolicitudisPadecimiento.objects.get(Q(idp=s.perfil.id)  &  Q(idsisenf__personal="Si"))
        #for rS in resultadosSi:
        #print(f"ID: {resultadosSi.idsisenf.nombreenf}")
    else:
        resultadosSi =""


    
    return render(request, "SolicitudInscripcionSApp/editarSolicitud.html", {"s":s, "dp":dp, "d":d,"si":si,"sid":sid,"enfermedades":listae,"reSi":resultadosSi,"lista_padecimientos_json":lista_padecimientos_json})



def modificarSIS(request): 
  
    idsi=request.POST['idsi']
    montoaa=request.POST['montoaa']
    nuevoma=request.POST['nuevom']
    montot=request.POST['montot']
    plazo=request.POST['plazo']
    garantia=request.POST['garantia']
    estatura=request.POST['estatura']
    peso=request.POST['peso']
    dbeneficiario=request.POST['beneficiario']


    solicitudis=Solicitudis.objects.get(id=idsi)
    solicitudis.montoaa=montoaa
    solicitudis.nuevoma=nuevoma
    solicitudis.montot=montot
    solicitudis.plazo=plazo
    solicitudis.garantia=garantia
    solicitudis.estatura=estatura
    solicitudis.peso=peso
    solicitudis.dbeneficiario=dbeneficiario
    solicitudis.save()

    bandera= request.POST['passDS'] #inicia declaración de salud
    #print(bandera)
    if(bandera == '1'):
       idpd =request.POST.getlist('idpad')
       idsisenf =request.POST.getlist('idenf')
       idperfil =request.POST.getlist('idc') #identificador del cliente 
       fechap =request.POST.getlist('fechapad') 
       tratamientor =request.POST.getlist('tratamientor')
       situaciona =request.POST.getlist('situaciona')
       estado="activo"
      # print(idpd)

        # Iterar sobre los datos para crear o actualizar registros
    for i in range(len(idpd)):
        if i < len(fechap) and idpd[i] != "":
            # Si hay un valor válido en idsisenf, actualizar el objeto existente
            ssp_obj = SolicitudisPadecimiento.objects.get(id=idpd[i])
            msispadecimiento= SolicitudisPadecimiento.objects.update_or_create( id=ssp_obj.id, 
                defaults={
                # 'idp': idperfil[i],
                    'fechap': fechap[i],
                    'tratamientor': tratamientor[i],
                    'situaciona': situaciona[i]
                }
            )
        elif fechap[i] != "":  # Si idimgp está vacío o no hay un valor válido en idpd, crear un nuevo objeto
            msispadecimiento = SolicitudisPadecimiento.objects.create(idsisenf=SolicitudisEnfermedad.objects.get(id=idsisenf[i]), idp=Perfil.objects.get(id=idperfil[i]), fechap=fechap[i],
             tratamientor =tratamientor[i],  situaciona=situaciona[i], estado=estado)
       
    #fin declaración de salud

     # Inicia otro padecimiento
    try:
        personal=request.POST['personal']
    except :
        personal=""
    try:
        nombreenf=request.POST['padecimientoOt'].upper() 
    except :
        nombreenf=""
   
    idpotp= request.POST['idpotp'] # id del padecimiento ingresado por el cliente
    fechapO = request.POST.get('fechaOt', None)
    try:
        tratamientorO=request.POST['tratamientoOt']
    except :
        tratamientorO=""
    try:
        situacionaO=request.POST['situacionOt']
    except :
        situacionaO=""

    estadoenf="activo" 
    enf=SolicitudisEnfermedad.objects.filter(nombreenf=nombreenf).exists()
    
    if  idpotp !="" :
        msispadecimientoOt = SolicitudisPadecimiento.objects.get(id=idpotp) # modifica los datos del padecimiento
        msispadecimientoOt.fechap=fechapO
        msispadecimientoOt.tratamientor =tratamientorO 
        msispadecimientoOt.situaciona=situacionaO
        msispadecimientoOt.save()

        menfermedades=SolicitudisEnfermedad.objects.get(id=msispadecimientoOt.idsisenf.id)
        menfermedades.nombreenf=nombreenf
        menfermedades.save()
    elif enf == False and nombreenf != "" :
        enfermedades=SolicitudisEnfermedad.objects.create(nombreenf=nombreenf,estado=estadoenf,personal=personal)
        # Obtener el ID de la instancia de enfermedades
        siseid= SolicitudisEnfermedad.objects.get(id=enfermedades.id)
        siseid.id = enfermedades.id

        sispadecimientoOt = SolicitudisPadecimiento.objects.create(idsisenf=siseid, idp=Perfil.objects.get(id=request.POST['idpot']), fechap=fechapO,
                tratamientor =tratamientorO, situaciona=situacionaO, estado=estado)
    
    # fin otro padecimiento


    bandera= request.POST['passDO']  # guarda datos de declaracion de deformidades, amputaciones o defecto fisico
    if(bandera == '1'):
        tienedadf=request.POST['tiened']
        try:
            detallesdadf=request.POST['detalled']
        except :
            detallesdadf=""
        
        fumacp=request.POST['fumacp']
        try:
           cuantosd=request.POST['cuantosd']
        except :
            cuantosd=""
        
        bebidadalc=request.POST['ibebidas']
        try:
           frecuenciaalc=request.POST['frecuanciab']
        except :
            frecuenciaalc=""
       
        tratamientomd=request.POST['tratamientomd']
        try:
           detalletmd=request.POST['detalletm']
        except :
            detalletmd=""
        
        practicaad=request.POST['practicaadp']   
        try:
           clasead=request.POST['clase']
        except :
            clasead=""
        try:
          frecuenciaad=request.POST['frecuencia']
        except :
            frecuenciaad=""
        
        segurodd=request.POST['segurod']
   


    solicitudisdadf=Solicitudisdadf.objects.get(idsis=idsi)
    solicitudisdadf.tienedadf=tienedadf
    solicitudisdadf.detallesdadf=detallesdadf
    solicitudisdadf.fumacp=fumacp
    solicitudisdadf.cuantosd=cuantosd
    solicitudisdadf.bebidadalc=bebidadalc
    solicitudisdadf.frecuenciaalc=frecuenciaalc
    solicitudisdadf.tratamientomd=tratamientomd
    solicitudisdadf.detalletmd=detalletmd
    solicitudisdadf.practicaad=practicaad
    solicitudisdadf.clasead=clasead
    solicitudisdadf.frecuenciaad=frecuenciaad
    solicitudisdadf.segurodd=segurodd
    solicitudisdadf.save()

    mensaje="Datos Actualizados"
    registroBit(request, "Se actualizo formulario Inscripcion seguro " + solicitudis.ids.perfil.dui, "Actualizacion")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=solicitudis.ids.perfil.id)  # id de perfil 
 


