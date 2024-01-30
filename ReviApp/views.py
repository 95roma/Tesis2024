from django.shortcuts import render,redirect
from ClienteApp.models import *
from ConfiguracionApp.models import *
from ReviApp.models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


# Create your views here.
def revi(request):
    cliente=Perfil.objects.all
    docu=TipoDocumento.objects.all
    return render(request, "ReviApp/revi.html",{"Perfil":cliente,"TipoDocumento":docu})

def registrarDocu(request):
     id=request.POST['cliente']
     idtipo=request.POST['docu']
     archivo=request.FILES['archivo']
     cliente=Perfil.objects.get(id=id)
     cliente.id=id
     docu=TipoDocumento.objects.get(idtipo=idtipo)
     docu.idtipo=idtipo
     consulta=DocumentosCliente.objects.filter(docu=idtipo).exists()

    
     if consulta==True :
        mensaje="El cliente ya tiene registrado el tipo de documento ya existe"
        messages.warning(request, mensaje)
        return redirect('listarDocu')
     else:
    
      crear= DocumentosCliente.objects.create(archivo=archivo,docu=docu,cliente=cliente)
      mensaje="Se ha guardado el documento al cliente"
      messages.success(request, mensaje)
      return redirect("revi")

def listarDocu(request):
    cliente=Perfil.objects.all
    print(cliente)
    return render(request, "ReviApp/listardocu.html",{"Perfil":cliente})

def docu(request):
    id=request.GET['id']
    print('este es el id')
    print(id)
    muni=DocumentosCliente.objects.filter(cliente=id)
    return render(request,"ReviApp/docu.html", {"DocumentoCliente":muni})

def modiDocu(request,id):
     documento=DocumentosCliente.objects.get(id=id)
     return render(request,"ReviApp/modiDocu.html",{"DocumentoCliente":documento})


def editDocu(request):
    id=request.POST['id']
    archivo=request.FILES['archivo']
    documento = DocumentosCliente.objects.get(id=id)
    documento.archivo=archivo
    documento.save()
    return redirect('/ReviApp/listarDocu')
    #return render(request, "ReviApp/listarDocu.html")
