import json
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.generic import TemplateView
from PresupuestoApp.models import *
from ListaChequeoApp.models import listaChequeo
from TesisApp.views import registroBit


# Create your views here.


def presupuesto(request, id):
    sol= Presupuestodg.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    if sol == True:
        solv= Presupuestodg.objects.get(ids=id)
    
        return redirect('modPresupuesto', id=solv.id)   
    else:
        try:
            s = solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s = ""
        try:
            do = datosObra.objects.get(idSolicitud=id)
        except datosObra.DoesNotExist:
            do = ""
        
        try:
            listam = Materiales.objects.filter(estado="activo")
        except Materiales.DoesNotExist:
            listam = ""

        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam, "s": s, "do": do})

# carga los datos del matrial seleccionado en los inputs


def get(request):
    id = request.GET['idmaterial']
    if request.is_ajax():
        material = Materiales.objects.get(id=id)
        serialized_data = serialize("json", [material])
        return HttpResponse(serialized_data, content_type="application/json")
    else:
        listam = Materiales.objects.filter(estado="activo")
        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam})


def registrarP(request):
    # bandera= request.POST['passGN']  # guarda datos de
    # if(bandera == '1'):

    if request.is_ajax and request.method == "POST":
        dtig = json.loads(request.POST.get('valoresig'))
        print(dtig)
        for objif in dtig:
            ids = objif['ids']
            fecha = objif['fecha']
            mejorarea = objif['mejora']
            diasestimadosc = objif['diases']

        # try:
        #   nitempresa=request.POST['nnitemp']
        # except :
        #    nitempresa=""

            print(fecha)
            print(mejorarea)
            print(diasestimadosc)

            idsol = solicitud.objects.get(id=ids)
            idsol.id = ids

            presupuestodg = Presupuestodg.objects.create(
                fecha=fecha, mejorarea=mejorarea, diasestimadosc=diasestimadosc, ids=idsol)
            

            # obtengo el ultimo registro de los datos generales de presupuesto
            idpdg = Presupuestodg.objects.all().last()

            # para tabla de materiales

            datamt = json.loads(request.POST.get('valorestmt'))
            print(datamt)
            for obj in datamt:
                idmp = obj['idm']  # id del material
                cantidad = obj['cantidad']
                preciouni = obj['preciouni']
                subtotal = obj['subtotal']

                idm = Materiales.objects.get(id=idmp)
                idm.id = idmp

                # ma=obj['idm']
                print(cantidad)
                print(preciouni)
                print(subtotal)

                PreMate = PresupuestoMateriales.objects.filter(
                    idm=idm, idp=idpdg).exists()
                print(PreMate)
                # PresupuestoMateriales()
                if PreMate == True:
                    presupuestoMateriales = PresupuestoMateriales.objects.get(
                        idm=idm, idp=idpdg)

                    print(presupuestoMateriales.cantidad)
                    presupuestoMateriales.cantidad = presupuestoMateriales.cantidad+cantidad
                    presupuestoMateriales.preciouni = presupuestoMateriales.preciouni+preciouni
                    presupuestoMateriales.subtotal = presupuestoMateriales.subtotal+subtotal
                    presupuestoMateriales.save()
                else:
                    presupuestoMateriales = PresupuestoMateriales.objects.create(
                        cantidad=cantidad, preciouni=preciouni, subtotal=subtotal, idm=idm, idp=idpdg)

  # para tabla mano de obra
            datamo = json.loads(request.POST.get('valorestmo'))
            print(datamo)
            for obj in datamo:
                descripcion = obj['descripc']  # id del material
                unidad = obj['unidad']
                preciouni = obj['preciouni']
                cantidad = obj['cantidad']
                subtotal = obj['subtotal']

                print(descripcion)
                print(cantidad)
                print(preciouni)
                print(subtotal)

                PreMo = PresupuestoManoObra.objects.filter(idp=idpdg).exists()
                print(PreMo)

                if PreMo == True:
                    presupuestoManoObra = PresupuestoManoObra.objects.get(
                        idp=idpdg)

                    presupuestoManoObra.cantidad = presupuestoManoObra.cantidad+cantidad
                    presupuestoManoObra.preciouni = presupuestoManoObra.preciouni+preciouni
                    presupuestoManoObra.subtotal = presupuestoManoObra.subtotal+subtotal
                    presupuestoManoObra.save()
                else:
                    presupuestoManoObra = PresupuestoManoObra.objects.create(
                        descripcion=descripcion, unidad=unidad, cantidad=cantidad, preciouni=preciouni, subtotal=subtotal, idp=idpdg)

        # para tabla otros
            dataot = json.loads(request.POST.get('valorestot'))
            print(dataot)
            for obj in dataot:
                descripcion = obj['descripc']  # id del material
                unidad = obj['unidad']
                preciouni = obj['preciouni']
                cantidad = obj['cantidad']
                subtotal = obj['subtotal']

                print(descripcion)
                print(cantidad)
                print(preciouni)
                print(subtotal)

                PreOtr = PresupuestoOtros.objects.filter(idp=idpdg).exists()
                # print(PreMate)
                # PresupuestoMateriales()
                if PreOtr == True:
                    presupuestoOtros = PresupuestoOtros.objects.get(idp=idpdg)

                #    print(presupuestoMateriales.cantidad)
                    presupuestoOtros.cantidad = presupuestoOtros.cantidad+cantidad
                    presupuestoOtros.preciouni = presupuestoOtros.preciouni+preciouni
                    presupuestoOtros.subtotal = presupuestoOtros.subtotal+subtotal
                    presupuestoOtros.save()
                else:
                    presupuestoOtros = PresupuestoOtros.objects.create(
                        descripcion=descripcion, unidad=unidad, cantidad=cantidad, preciouni=preciouni, subtotal=subtotal, idp=idpdg)

            # para otras especificaciones
            dtesp = json.loads(request.POST.get('valoresesp'))
            print(dtesp)
            for obje in dtesp:
                subtotal = obje['subtotal']
                asistenciatecn = obje['asistenciatc']
                comisionporot = obje['comisionot']
                consultabcredoto = obje['consultabc']
                cansaldopend = obje['cancelarsp']
                pcuota = obje['primerac']
                total = obje['total']
                notas = obje['notas']

                if(subtotal=="" ):
                    subtotal = 0.00  
                if(asistenciatecn=="" ):
                    asistenciatecn = 0.00  
                if(comisionporot=="" ):
                    comisionporot = 0.00  
                if(consultabcredoto=="" ):
                    consultabcredoto = 0.00  
                if(cansaldopend=="" ):
                    cansaldopend = 0.00  
                if(pcuota=="" ):
                    pcuota = 0.00  
                if(total=="" ):
                    total = 0.00  

                print(comisionporot)
                print(pcuota)
                print(notas)

                presup = Presupuesto.objects.create(subtotal=subtotal, asistenciatecn=asistenciatecn, comisionporot=comisionporot,
                                                    consultabcredoto=consultabcredoto, cansaldopend=cansaldopend, pcuota=pcuota, total=total, notas=notas, idp=idpdg)

        #####################################################
        # para guardar en la lista de chequeo 
        lchequo= listaChequeo.objects.get(ids=idsol)
        lchequo.presupuestocons ="Si"
        lchequo.save()

        registroBit(request, "Se registro formulario de Presupuesto Mejora " + presupuestodg.ids.perfil.dui, "Registro")
        # Suponiendo que quieres redirigir a una nueva página y devolver un mensaje JSON.
        response_data = {'message': 'Datos guardados correctamente.'}
        return JsonResponse(response_data)

        # Redirigir a una nueva página (modifica la URL según tu configuración)
        # redireccion = reverse('administrarPerfil', kwargs={'id': presupuestodg.ids.perfil.id})
        # return HttpResponseRedirect(redireccion)


       # mensaje = "Datos guardados"
       # messages.success(request, mensaje)
        #return redirect('administrarPerfil', id=presupuestodg.ids.perfil.id)  # id de perfil 


def modificarPresupuesto(request, id):
    lista_materiales_json = []
    lista_mano_obra_json = []
    lista_otros_json = []
    try:
        presupuesto_datos_generales = Presupuestodg.objects.get(id=id)
    except Presupuestodg.DoesNotExist:
        presupuesto_datos_generales = ""

    try:
        pre = Presupuesto.objects.get(idp=presupuesto_datos_generales.id)
    except:
        pre = ""

    try:
        s = solicitud.objects.get(id=presupuesto_datos_generales.ids.id)
    except solicitud.DoesNotExist:
        s = ""
    try:
        do = datosObra.objects.get(
            idSolicitud=presupuesto_datos_generales.ids.id)
    except datosObra.DoesNotExist:
        do = ""
    try:
        listam = Materiales.objects.filter(estado="activo")
    except Materiales.DoesNotExist:
        listam = ""

    try:
        lista_materiales = PresupuestoMateriales.objects.filter(
            idp=presupuesto_datos_generales.id)
        datos = []
        for item in lista_materiales:
            datos.append({'id': item.id, 'precio': item.preciouni, 'cantida': item.cantidad, 'total': item.subtotal,
                          "nombre": item.idm.nombre, "descripcion": item.idm.descripcion, "unidad": item.idm.unidad, "idm": item.idm.id})
        lista_materiales_json = json.dumps(datos, default=str)

    except PresupuestoMateriales.DoesNotExist:
        None

    try:
        lista_mano_obra = PresupuestoManoObra.objects.filter(
            idp=presupuesto_datos_generales.id)
        datos = []
        for item in lista_mano_obra:
            datos.append({
                "id": item.id,
                "descripcion": item.descripcion,
                "unidad": item.unidad,
                "preciouni": item.preciouni,
                "cantidad": item.cantidad,
                "total": item.subtotal,
            })
            lista_mano_obra_json = json.dumps(datos, default=str)

    except PresupuestoManoObra.DoesNotExist:
        lista_mano_obra = ""
        lista_mano_obra_json = []

    try:
        lista_otros = PresupuestoOtros.objects.filter(
            idp=presupuesto_datos_generales.id)
        datos = []
        for item in lista_otros:
            datos.append({
                "id": item.id,
                "descripcion": item.descripcion,
                "unidad": item.unidad,
                "preciouni": item.preciouni,
                "cantidad": item.cantidad,
                "total": item.subtotal,
            })
            lista_otros_json = json.dumps(datos, default=str)

    except PresupuestoManoObra.DoesNotExist:
        lista_otros = ""

    return render(request, "PresupuestoApp/modificaPresupuesto.html", {"materiales": listam, "s": s, "do": do,
                                                                       "datosGenerales": presupuesto_datos_generales, "pre": pre,
                                                                       "listMateriales": lista_materiales_json,
                                                                       "lista_mano_obra_json": lista_mano_obra_json,
                                                                       "lista_otros_json": lista_otros_json
                                                                       })


def actualizarPresupuesto(request):
    if request.is_ajax and request.method == "POST":
        dtig = json.loads(request.POST.get('valoresig'))
        for objif in dtig:
            ids = objif['ids']
            idPresupuestoMejora = objif['idPresupuestoMejora']
            fecha = objif['fecha']
            mejorarea = objif['mejora']
            diasestimadosc = objif['diases']
            idsol = solicitud.objects.get(id=ids)
            idsol.id = ids

            presupuestodg = Presupuestodg.objects.update_or_create(ids=idsol, id=idPresupuestoMejora,
                                                                   defaults={
                                                                       "fecha": fecha,
                                                                       "mejorarea": mejorarea,
                                                                       "diasestimadosc": diasestimadosc,
                                                                       "ids": idsol,
                                                                   })
            # obtengo el ultimo registro de los datos generales de presupuesto
            idpdg = Presupuestodg.objects.get(id=idPresupuestoMejora)

        # para tabla de materiales
            datamt = json.loads(request.POST.get('valorestmt'))
            lista_original = PresupuestoMateriales.objects.filter(
                idp=idPresupuestoMejora)
            lista_actual = []  # el id que no este aqui se eliminara

            for obj in datamt:
                idmp = obj['idm']  # id del material
                cantidad = obj['cantidad']
                preciouni = obj['preciouni']
                subtotal = obj['subtotal']
                idm = Materiales.objects.get(id=idmp)
                idm.id = idmp
                lista_actual.append(idmp)
                PreMate = PresupuestoMateriales.objects.update_or_create(idm=idm, idp=idPresupuestoMejora,
                                                                         defaults={
                                                                             "preciouni": preciouni,
                                                                             "cantidad": cantidad,
                                                                             "subtotal": subtotal,
                                                                             "idm": idm,
                                                                             "idp": idpdg,
                                                                         })
        # ciclo para eliminar  material
            for item in lista_original:
                if ((item.idm.id in lista_actual) == False):
                    PreMate = PresupuestoMateriales.objects.get(
                        idm=item.idm, idp=idPresupuestoMejora)
                    PreMate.delete()

  # para tabla mano de obra
            datamo = json.loads(request.POST.get('valorestmo'))
            lista_original = PresupuestoManoObra.objects.filter(
                idp=idPresupuestoMejora)
            lista_actual = []  # el id que no este aqui se eliminara
            for obj in datamo:
                id = obj['id']
                descripcion = obj['descripc']  # id del material
                unidad = obj['unidad']
                preciouni = obj['preciouni']
                cantidad = obj['cantidad']
                subtotal = obj['subtotal']

                try:

                    PreMo = PresupuestoManoObra.objects.update_or_create(id=id, idp=idPresupuestoMejora,
                                                                         defaults={
                                                                             "descripcion": descripcion,
                                                                             "cantidad": cantidad,
                                                                             "subtotal": subtotal,
                                                                             "unidad": unidad,
                                                                             "preciouni": preciouni,
                                                                             "idp": idpdg,
                                                                         })
                    lista_actual.append(int(id))
                except Exception:
                    presupuestoManoObra = PresupuestoManoObra.objects.create(
                        descripcion=descripcion,
                        unidad=unidad,
                        cantidad=cantidad,
                        preciouni=preciouni,
                        subtotal=subtotal,
                        idp=idpdg)
                    lista_actual.append(presupuestoManoObra.id)
            # ciclo para eliminar  mano obra            
            for item in lista_original:
                if ((item.id in lista_actual) == False):
                    PreMate = PresupuestoManoObra.objects.get(
                        id=item.id, idp=idPresupuestoMejora)
                    PreMate.delete()

        # para tabla otros
            dataot = json.loads(request.POST.get('valorestot'))
            lista_original = PresupuestoOtros.objects.filter(
                idp=idPresupuestoMejora)
            lista_actual = []  # el id que no este aqui se eliminara
            for obj in dataot:
                id = obj['id']
                descripcion = obj['descripc']  # id del material
                unidad = obj['unidad']
                preciouni = obj['preciouni']
                cantidad = obj['cantidad']
                subtotal = obj['subtotal']

                PreOtr = PresupuestoOtros.objects.filter(idp=idpdg).exists()
                try:
                    PreOtr = PresupuestoOtros.objects.update_or_create(id=id, idp=idPresupuestoMejora,
                                                                       defaults={
                                                                           "descripcion": descripcion,
                                                                           "cantidad": cantidad,
                                                                           "subtotal": subtotal,
                                                                           "unidad": unidad,
                                                                           "preciouni": preciouni,
                                                                           "idp": idpdg,
                                                                       })
                    lista_actual.append(int(id))
                except Exception:
                    PreOtr = PresupuestoOtros.objects.create(
                        descripcion=descripcion,
                        unidad=unidad,
                        cantidad=cantidad,
                        preciouni=preciouni,
                        subtotal=subtotal,
                        idp=idpdg)
                    lista_actual.append( PreOtr.id)
                    
            # ciclo para eliminar  material
            for item in lista_original:
                if ((item.id in lista_actual) == False):
                    PreMate = PresupuestoOtros.objects.get(
                        id=item.id, idp=idPresupuestoMejora)
                    PreMate.delete()

        # para otras especificaciones
            dtesp = json.loads(request.POST.get('valoresesp'))
            for obje in dtesp:
                subtotal = obje['subtotal']
                asistenciatecn = obje['asistenciatc']
                comisionporot = obje['comisionot']
                consultabcredoto = obje['consultabc']
                cansaldopend = obje['cancelarsp']
                pcuota = obje['primerac']
                total = obje['total']
                notas = obje['notas']

                if(subtotal=="" ):
                    subtotal = 0.00  
                if(asistenciatecn=="" ):
                    asistenciatecn = 0.00  
                if(comisionporot=="" ):
                    comisionporot = 0.00  
                if(consultabcredoto=="" ):
                    consultabcredoto = 0.00  
                if(cansaldopend=="" ):
                    cansaldopend = 0.00  
                if(pcuota=="" ):
                    pcuota = 0.00  
                if(total=="" ):
                    total = 0.00  
                    
                print(notas)
                presup = Presupuesto.objects.update_or_create(idp=idPresupuestoMejora,
                    defaults={
                    "subtotal":subtotal,
                    "asistenciatecn":asistenciatecn,
                    "comisionporot":comisionporot,
                    "consultabcredoto":consultabcredoto,
                    "cansaldopend":cansaldopend,
                    "pcuota":pcuota, "total":total,
                    "notas":notas, "idp":idpdg
                    })

    mensaje = "Datos actualizados"
    registroBit(request, "Se actualizo formulario Presupuesto Mejora " + idsol.perfil.dui, "Actualizacion")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=idsol.perfil.id)  # id de perfil ")


def listaPM(request):
    listapm = Presupuesto.objects.all()
    return render(request, "PresupuestoApp/listaPM.html", {"listap": listapm})
