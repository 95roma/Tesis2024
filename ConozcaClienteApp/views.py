from django.shortcuts import render,redirect, HttpResponse
from ClienteApp.models import Perfil
from ConozcaClienteApp.models import *
from SolicitudesApp.models import *
from DireccionApp.models import *
from datetime import date, datetime
from django.contrib import messages

from TesisApp.views import registroBit


# Create your views here.

def ccliente(request, id):
    sol= Clientedg.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    if sol == True:
        solv= Clientedg.objects.get(ids=id)
    
        return redirect('editarCliente', id=solv.iddg)
    else:
        try:
            s=  solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s=""
        
        try:
            d=  domicilio.objects.get(idSolicitud=id, tipo="Solicitante")
        except domicilio.DoesNotExist:
            d=""

        r= referencias.objects.filter(idSolicitud=id)
        #c=datosPersonales.objects.filter(idSolicitud=id, tipo="conyuge").exists()  

        try:
            dp=datosPersonales.objects.get(idSolicitud=id)
        except datosPersonales.DoesNotExist:
            dp=""

        try:
            dpcy=DatosPersonalesF.objects.get(idSolicitud=id, tipo="conyuge")
        except DatosPersonalesF.DoesNotExist:
            dpcy=""

        try:
            dpc=DatosPersonalesF.objects.get(idSolicitud=id, tipo="codeudor")
        except DatosPersonalesF.DoesNotExist:
            dpc=""

        sol = [s, d, r, dpcy, dp, dpc]

        return render(request, "ConozcaClienteApp/cclientedg.html", {"sol":sol}) 

def cclientedgf(request): # carga la vista para completar el formulario codeudor
    id=request.GET['idsol']

    try:
        d=  domicilio.objects.get(idSolicitud=id, tipo="codeudor")
    except domicilio.DoesNotExist:
        d=""

    try:
        dp=DatosPersonalesF.objects.get(idSolicitud=id, tipo="codeudor")
    except DatosPersonalesF.DoesNotExist:
        dp=""
  
    return render(request, "ConozcaClienteApp/cclientedgf.html",{"d":d,"dp":dp}) 


def registrarD(request): 
  
    ids=request.POST['ids']
    codigo=request.POST['codigo']
    calidadactua=request.POST['calidad']
    nombrecc=request.POST['nombre']
    try:
        conocidocomo=request.POST['conocidoc']
    except :
        conocidocomo=""
    try:
        profesiondui =request.POST['profesionsd']
    except :
        profesiondui="" 
    
    nacionalidad=request.POST['nacionalidad']
    docidentidad=request.POST['documento']
    numerodoc=request.POST['ndoc']
    fechavdoc=request.POST['fechavd']
    ocupacionaa=request.POST['ocupacion']
    direcciondomic=request.POST['direcciond']
    correoe=request.POST['correo']
    telcelular=request.POST['telefonoc']
    telfijo=request.POST['telefonof']
    estatusp=request.POST['estatusp']
    try:
        nombrecony=request.POST['nombrecony']
    except :
        nombrecony=""

    fecha= date.today()
    estado= request.POST['estadoM']
    

    idsol= solicitud.objects.get(id=ids)
    idsol.id=ids

    clientedg=Clientedg.objects.create(fecha=fecha,codigo=codigo,calidadactua=calidadactua,nombrecc=nombrecc,conocidocomo=conocidocomo,profesiondui=profesiondui,nacionalidad=nacionalidad,docidentidad=docidentidad,numerodoc=numerodoc,fechavdoc=fechavdoc,ocupacionaa=ocupacionaa,direcciondomic=direcciondomic,correoe=correoe,telcelular=telcelular,telfijo=telfijo,estatuspropiedad=estatusp,nombreconyuge=nombrecony,estado=estado,ids=idsol)
    #mensaje="Datos guardados"
    #messages.success(request, mensaje)
    registroBit(request, "Llenado de formulario Conozca a su cliente", nivel="Registro")

    iddgen= Clientedg.objects.all().last() #obtengo la ultima solicitud registrada 

   
    bandera= request.POST['passAED']  # guarda los datos de la empr
    if(bandera == '1'):
        tipoact= request.POST['tipoa']
        lugartrab= request.POST['lugart']
        cargodes= request.POST['cargode']         
        tiempolaborar= request.POST['tiempolab']
        procedenciafod= request.POST['procedenciafonda']
        rangoingresosemp= request.POST['rangoing']
        otrosingresos= request.POST['otingresos']
        try:
            procedenciaoi= request.POST['procedencia']
        except :
            procedenciaoi=""   

        estado="curso"

        clienteaec=Clienteaec.objects.create(iddg=iddgen,tipoact=tipoact,lugartrab=lugartrab,cargodes=cargodes,tiempolaborar=tiempolaborar, procedenciafod= procedenciafod,rangoingresosemp=rangoingresosemp,otrosingresos=otrosingresos,procedenciaoi=procedenciaoi,estado=estado)
   

    bandera= request.POST['passDN']  # guarda los datos de la empresa
    if(bandera == '1'):
        try:
            nombreneg= request.POST['nombreng'] 
        except :
            nombreneg==""
        try: 
            prodserv= request.POST['descps']
        except :
            prodserv=""
        try:
            direccionneg= request.POST['direccionneg']
        except :
            direccionneg=""
        try:
            fechaia= request.POST['fechaia']
        except :
            fechaia=""

        if(fechaia=="" ):
            fechaia = None 
        try:
            rangoingresos= request.POST['rangoimn']
        except :
            rangoingresos=""
        try:
            otrosingresos= request.POST['otrosidn']
        except :
            otrosingresos=""
        try:
            procedenciaoi= request.POST['procedenciadn']
        except :
            procedenciaoi=""   
    
        estado="curso"

        clientedn=Clientedn.objects.create(iddg=iddgen,nombreneg=nombreneg,prodserv=prodserv,direccionneg=direccionneg,fechaia=fechaia,rangoingresos=rangoingresos,otrosingresos=otrosingresos,procedenciaoi=procedenciaoi,estado=estado)
   
    bandera= request.POST['passRRF']  # guarda los datos de la empresa
    if(bandera == '1'):
        rremesa= request.POST['reciberf']  
        nombreremitente= request.POST.getlist('nombrer')
        parentesco= request.POST.getlist('parentescor')
        paisorigenr= request.POST.getlist('paisorg')
        monto= request.POST.getlist('montor') 
        estado="curso"    

        if(rremesa=="Si"):  
            for i in range(len(nombreremitente)):
                if (nombreremitente[i] != ""):
                    clienterrf=Clienterrf.objects.create(iddg=iddgen,rremesa=rremesa,nombreremitente=nombreremitente[i],parentesco=parentesco[i],paisorigenr=paisorigenr[i],monto=monto[i],estado=estado)
        elif(rremesa=="No"): 
            clienterrf=Clienterrf.objects.create(iddg=iddgen,rremesa=rremesa,nombreremitente=" ",parentesco=" ",paisorigenr=" ",monto=" ",estado=estado)
   

    bandera= request.POST['passDCF']  # guarda los datos del cliente o fiador
    if(bandera == '1'):
        try:
            clasifcredito= request.POST['clasificacionc']  
        except:
            clasifcredito=""
        try:
            montodc= request.POST['montodc']
        except:
            montodc=""
        try:        
            cuotadc= request.POST['cuotadc']
        except:
            cuotadc=""
            
        rpagosadic= request.POST['rpagosadic'] 

        try:
            procpagosadic= request.POST['procfondos']
        except:
            procpagosadic=""
    
        estado="curso"

        clientedc=Clientedc.objects.create(iddg=iddgen,clasifcredito=clasifcredito,montodc=montodc, cuotadc=cuotadc,rpagosadic=rpagosadic,procpagosadic=procpagosadic,estado=estado)
   
    bandera= request.POST['passBPEP']  # guarda los datos del cliente o fiador
    if(bandera == '1'):
        try:
            noaplica= request.POST['noaplica'] 
        except:
            noaplica="" 
        try:
            nombrecomp= request.POST['nombrecb']
        except:
            nombrecomp=""
        try:
            direccionp= request.POST['direcpermanente']
        except:
            direccionp=""
        try:
            tdocumento= request.POST['tdocumento']
        except:
            tdocumento=""
        try:
            ndocumento= request.POST['ndocumento']
        except:
            ndocumento=""
        try:
            benefpeps= request.POST['beneficiariopeps']
        except:
            benefpeps=""
        estado="curso"

        clientepbo=Clientepbo.objects.create(iddg=iddgen,noaplica=noaplica,nombrecomp=nombrecomp, direccionp=direccionp,tdocumento=tdocumento,ndocumento=ndocumento,benefpeps=benefpeps,estado=estado)
   

    bandera= request.POST['passPT']  # guarda los datos del perefil de transacciones
    if(bandera == '1'):
        try:
            prestamos= request.POST['prestamos']  
        except :
            prestamos=""
        try:
            espotros= request.POST['otrosesp']
        except :
            espotros=""
    
        estado="curso"

        clientept=Clientept.objects.create(iddg=iddgen,prestamos=prestamos,espotros=espotros,estado=estado)
   

    bandera= request.POST['passPEP']  # guarda los datos de las personas expuestas politicamente
    if(bandera == '1'):
        ustedpeps= request.POST['ustpeps']  
        relacionpeps= request.POST['relpeps']
        try:
            nombrep= request.POST['nombrep']
        except :
            nombrep=""
        try:
            puestdesemp= request.POST['puestodes']
        except :
            puestdesemp=""
        try:
            pergestiondesde= request.POST['periodogd']
        except :
            pergestiondesde=""
        try:
            pergestionhasta= request.POST['periodogh']
        except :
            pergestionhasta=""    
        try:
            grado= request.POST['grado']
        except :
            grado=""
        try:
            pparentesco= request.POST['pparentesco']
        except :
             pparentesco=""  
        try:
            sparentesco= request.POST['sparentesco']
        except :
            sparentesco=""

        if  grado== "Primero" and pparentesco != "":
            parentesco= pparentesco
        elif grado== "Segundo" and sparentesco != "":
            parentesco= sparentesco
        else:
            parentesco=""
        
    
        estado="curso"

        clientepeps=Clientepeps.objects.create(iddg=iddgen,ustedpeps=ustedpeps,relacionpeps=relacionpeps, nombrep=nombrep,puestdesemp=puestdesemp,pergestiondesde=pergestiondesde,pergestionhasta=pergestionhasta,grado=grado,parentesco=parentesco,estado=estado)
   
    bandera= request.POST['passCD']  # guarda de datos de comprobacion
    if(bandera == '1'):
        valedefnf= request.POST['validefnf']  
        veridireccion= request.POST['verdirec']
        verificadopor= request.POST['nombrever']
        codigoe= request.POST['codigoemp']
    
        estado="curso"

        clientepus=Clientepus.objects.create(iddg=iddgen,valedefnf=valedefnf,veridireccion=veridireccion, verificadopor=verificadopor,codigoe=codigoe,estado=estado)
   
        mensaje="Datos guardados"
        messages.success(request, mensaje)
    return redirect('administrarPerfil', id=clientedg.ids.perfil.id)  # id de perfil 
 

def listaConozcaC(request):
    listc=  Clientedg.objects.all()
    #listper=Perfil.objects.filter(estado="activo")
    return render(request, "ConozcaClienteApp/listaCC.html", {"listc":listc})



def editarCliente(request, id):
    try:    
        cdg=  Clientedg.objects.get(iddg=id)
    except Clientedg.DoesNotExist:
        cdg="" 
    
    #########################################
    try:
        s=  solicitud.objects.filter(id=cdg.ids.id)
    except solicitud.DoesNotExist:
        s=""
    idSol=cdg.ids.id
    try:
         d=  domicilio.objects.get(idSolicitud=idSol, tipo="Solicitante")
    except domicilio.DoesNotExist:
        d=""

    try:
        dpc=DatosPersonalesF.objects.get(idSolicitud=idSol,tipo = "codeudor")
    except Exception:
        dpc=""

    try:
        dp=datosPersonales.objects.get(idSolicitud=idSol)
    except datosPersonales.DoesNotExist:
        dp=""
   ##########################################

    try:
        cdaec=  Clienteaec.objects.get(iddg=id)
    except Clienteaec.DoesNotExist:
        cdaec=""
    try: 
        cddn= Clientedn.objects.get(iddg=id)
    except Clientedn.DoesNotExist:
        cddn="" 

    try:
        cdc=  Clientedc.objects.get(iddg=id)
    except Clientedc.DoesNotExist:
        cdc=""
    
    try:
        cdpbo=  Clientepbo.objects.get(iddg=id)
    except Clientepbo.DoesNotExist:
        cdpbo=""

    try:
        cpt=  Clientept.objects.get(iddg=id)
    except Clientept.DoesNotExist:
        cpt=""
    try:
        cpeps=  Clientepeps.objects.get(iddg=id)
    except Clientepeps.DoesNotExist:
        cpeps=""
    try:
        cpus=  Clientepus.objects.get(iddg=id)
    except Clientepus.DoesNotExist:
        cpus=""

    return render(request, "ConozcaClienteApp/editarCliente.html", {"cdg":cdg,"cdaec":cdaec,"cddn":cddn, "cdc":cdc , "cdpbo":cdpbo,"cpt":cpt, "cpeps":cpeps, "cpus":cpus, "s":s, "d":d, "dpc":dpc, "dp":dp   })


def editarD(request): 
  
    iddgm=request.POST['iddgm']
    codigo=request.POST['codigo']
    calidadactua=request.POST['calidad']
    try:
        conocidocomo=request.POST['conocidoc']
    except :
        conocidocomo=""
    try:
        profesiondui =request.POST['profesionsd']
    except :
        profesiondui="" 
    
    nacionalidad=request.POST['nacionalidad']
    docidentidad=request.POST['documento']
    numerodoc=request.POST['ndoc']
    fechavdoc=request.POST['fechavd']
    ocupacionaa=request.POST['ocupacion']
    direcciondomic=request.POST['direcciond']
    correoe=request.POST['correo']
    telcelular=request.POST['telefonoc']
    telfijo=request.POST['telefonof']
    estatusp=request.POST['estatusp']
    try:
        nombrecony=request.POST['nombrecony']
    except :
        nombrecony=""
    
    cdg=Clientedg.objects.get(iddg=iddgm)
    cdg.codigo=codigo
    cdg.calidadactua=calidadactua
    cdg.conocidocomo=conocidocomo
    cdg.profesiondui=profesiondui
    cdg.nacionalidad=nacionalidad
    cdg.docidentidad=docidentidad    
    cdg.numerodoc=numerodoc
    cdg.fechavdoc=fechavdoc
    cdg.ocupacionaa=ocupacionaa
    cdg.direcciondomic=direcciondomic
    cdg.correoe=correoe
    cdg.telcelular=telcelular
    cdg.telfijo=telfijo
    cdg.estatuspropiedad=estatusp
    cdg.nombreconyuge=nombrecony
    cdg.save()


    bandera= request.POST['passAED']  # guarda los datos de la empr
    if(bandera == '1'):
        tipoact= request.POST['tipoa']
        lugartrab= request.POST['lugart']
        cargodes= request.POST['cargode']         
        tiempolaborar= request.POST['tiempolab']
        procedenciafod= request.POST['procedenciafonda']
        rangoingresosemp= request.POST['rangoing']
        otrosingresos= request.POST['otingresos']
        try:
            procedenciaoi= request.POST['procedencia']
        except :
            procedenciaoi=""   
               
        caec=Clienteaec.objects.get(iddg=iddgm)
        caec.tipoact=tipoact
        caec.lugartrab=lugartrab
        caec.cargodes=cargodes
        caec.tiempolaborar=tiempolaborar
        caec.procedenciafod= procedenciafod
        caec.rangoingresosemp=rangoingresosemp
        caec.otrosingresos=otrosingresos
        caec.procedenciaoi=procedenciaoi
        caec.save()

    bandera= request.POST['passDN']  # guarda los datos de la empresa
    if(bandera == '1'):
        try:
            nombreneg= request.POST['nombreng'] 
        except :
            nombreneg==""
        try: 
            prodserv= request.POST['descps']
        except :
            prodserv=""
        try:
            direccionneg= request.POST['direccionneg']
        except :
            direccionneg=""
        try:
            fechaia= request.POST['fechaia']
        except :
            fechaia=""
        
        if(fechaia=="" ):
            fechaia = None 

        try:
            rangoingresos= request.POST['rangoimn']
        except :
            rangoingresos=""
        try:
            otrosingresos= request.POST['otrosidn']
        except :
            otrosingresos=""
        try:
            procedenciaoi= request.POST['procedenciadn']
        except :
            procedenciaoi=""   
       
        cdn=Clientedn.objects.get(iddg=iddgm)
        cdn.nombreneg=nombreneg
        cdn.prodserv=prodserv
        cdn.direccionneg=direccionneg
        cdn.fechaia=fechaia
        cdn.rangoingresos=rangoingresos
        cdn.otrosingresos=otrosingresos
        cdn.procedenciaoi=procedenciaoi
        cdn.save()

    bandera= request.POST['passDCF']  # guarda los datos del cliente o fiador
    if(bandera == '1'):
        try:
            clasifcredito= request.POST['clasificacionc'] 
        except:
            clasifcredito="" 
        try:
            montodc= request.POST['montodc']
        except:
            montodc=""
        try:        
            cuotadc= request.POST['cuotadc']
        except:
            cuotadc=""
            
        rpagosadic= request.POST['rpagosadic'] 

        try:
            procpagosadic= request.POST['procfondos']
        except:
            procpagosadic=""
    

        cdc=Clientedc.objects.get(iddg=iddgm)
        cdc.clasifcredito=clasifcredito
        cdc.montodc=montodc
        cdc.cuotadc=cuotadc
        cdc.rpagosadic=rpagosadic
        cdc.procpagosadic=procpagosadic
        cdc.save()

    bandera= request.POST['passBPEP']  # guarda los datos 
    if(bandera == '1'):
        try:
            noaplica= request.POST['noaplica'] 
        except:
            noaplica="" 
        try:
            nombrecomp= request.POST['nombrecb']
        except:
            nombrecomp=""
        try:
            direccionp= request.POST['direcpermanente']
        except:
            direccionp=""
        try:
            tdocumento= request.POST['tdocumento']
        except:
            tdocumento=""
        try:
            ndocumento= request.POST['ndocumento']
        except:
            ndocumento=""

        try:
            benefpeps= request.POST['beneficiariopeps']
        except:
            benefpeps=""
        

        cpbo=Clientepbo.objects.get(iddg=iddgm)
        cpbo.noaplica=noaplica
        cpbo.nombrecomp=nombrecomp
        cpbo.direccionp=direccionp
        cpbo.tdocumento=tdocumento
        cpbo.ndocumento=ndocumento
        cpbo.benefpeps=benefpeps
        cpbo.save()


    bandera= request.POST['passPT']  # guarda los datos del perefil de transacciones
    if(bandera == '1'):
        prestamos= request.POST['prestamos']  
        espotros= request.POST['otrosesp']

        cpt=Clientept.objects.get(iddg=iddgm)
        cpt.prestamos=prestamos
        cpt.espotros=espotros
        cpt.save()
   

    bandera= request.POST['passPEP']  # guarda los datos de las personas expuestas politicamente
    if(bandera == '1'):
        ustedpeps= request.POST['ustpeps']  
        relacionpeps= request.POST['relpeps']
        try:
            nombrep= request.POST['nombrep']
        except :
            nombrep=""
        try:
            puestdesemp= request.POST['puestodes']
        except :
            puestdesemp=""
        try:
            pergestiondesde= request.POST['periodogd']
        except :
            pergestiondesde=""
        try:
            pergestionhasta= request.POST['periodogh']
        except :
            pergestionhasta=""
        try:
            grado= request.POST['grado']
        except :
            grado=""

        try:
            pparentesco= request.POST['pparentesco']
            sparentesco= request.POST['sparentesco']
        except :
            pparentesco=""
            sparentesco=""

        if pparentesco != "":
            parentesco= pparentesco
        elif sparentesco != "":
            parentesco= sparentesco
        else:
            parentesco=""
  

        cpeps=Clientepeps.objects.get(iddg=iddgm)
        ustedpeps=ustedpeps
        cpeps.relacionpeps=relacionpeps
        cpeps.nombrep=nombrep
        cpeps.puestdesemp=puestdesemp        
        cpeps.pergestiondesde=pergestiondesde
        cpeps.pergestionhasta=pergestionhasta
        cpeps.grado=grado
        cpeps.parentesco=parentesco
        cpeps.save()
   
    bandera= request.POST['passCD']  # guarda de datos de comprobacion
    if(bandera == '1'):
        valedefnf= request.POST['validefnf']  
        veridireccion= request.POST['verdirec']
        verificadopor= request.POST['nombrever']
        codigoe= request.POST['codigoemp']
    

        cpus=Clientepus.objects.get(iddg=iddgm)
        valedefnf=valedefnf
        cpus.veridireccion=veridireccion
        cpus.verificadopor=verificadopor
        cpus.codigoe=codigoe
        cpus.save()
    registroBit(request, "Actualización de datos de formulario conozca a su cliente " + cdg.codigo,"Actualización")    
    return redirect('administrarPerfil', id=cdg.ids.perfil.id)  # id de perfil 
    
