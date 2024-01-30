from django.urls import path
from ConfiguracionApp import views
#from .views import registrarDepto
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
   # path('',views.home, name="home"),
    path('salario',login_required(views.salario), name="salario"),# apunta a la raiz 
    path('registrarSalario/',login_required(views.registrarSalario)),  
    path('listaSalario/', login_required(views.listaSalario), name="listaSalario"),
    path('listaSalario/darBaja/<id>',login_required(  views.salarioB)),
    path('listaSalario/editarSalario/<id>', views.editarSalario),
    path('modificarSalario/', views.modificarSalario),
    
    path('ocupacion/',login_required(views.ocupacion), name="ocupacion"),
    path('registrarOcupacion/',login_required(views.registrarOcupacion)), 
    path('listaOcupacion/', login_required(views.listaOcupacion), name="listaOcupacion"),
    path('listaOcupacion/eliminarOcupacion/<id>', login_required(views.eliminarO)),
    path('listaOcupacion/editarOcupacion/<id>',login_required(  views.editarOcupacion)),
    path('ModificarOcupacion/',login_required(  views.ModificarOcupacion)),

# para asignar zonas
    path('zonaAgencia',login_required(views.zonaAgencia), name="zonaAgencia"),
    path('registrarZona/', login_required(views.registrarZona)), 
    path('asignarZona',login_required(views.asignarZona), name="asignarZona"),
    path('registrarZona1/', login_required(views.registrarZona1)), 
    path('mu/',views.mu),
    path('dis/',views.dist),


# para agencia
    path('',views.registroAgencias, name="registroAgencias"),# apunta a la raiz, esto no sirve
    path('registrarAgencia/',views.registrarAgencia),  
    path('listarAgencias/',login_required(views.listaAgencias), name='listarAgencias'),
    path('listarAgencias/editarAgencia/<idAgencia>',login_required(views.editarAgencia)),  
    path('modificarAgencia/', login_required(views.modificarAgencia)), 
    path('municipio/',login_required(views.municipio)),
    path('distrito/',login_required(views.distri)),
    path('con/', login_required(views.con), name='con'),  

# para documentos
    path('Documento',views.Documento, name="Documento"),
    path('registrarD/', views.registrarD),
    

# para enfermedades de solicitud de inscripcion al seguro
    path('enfermedad/',login_required(views.enfermedad), name="enfermedad"),
    path('registrarEnfermedad/',login_required(views.registrarEnfermedad)), 
    path('listaEnfermedades/', login_required(views.listaEnfermedades), name="listaEnfer"),
    path('listaEnfermedades/eliminarE/<id>', login_required( views.eliminarE)),
    path('listaEnfermedades/editarEnf/<id>', login_required( views.editarEnf)),
    path('ModificarE/', login_required( views.ModificarE)),

# para materiales de construcción
    path('materiales/',login_required(views.materiales), name="materiales"),
    path('registrarMaterial/',login_required(views.registrarMaterial)), 
    path('listaMateriales/', login_required(views.listaMateriales), name="listaMater"),
    path('listaMateriales/eliminarM/<id>', login_required( views.eliminarM)),
    path('listaMateriales/editarMat/<id>', login_required( views.editarMat)),
    path('ModificarMat/', login_required( views.ModificarMat)),

   # para tipo de operación declaración jurada
    path('toperacion/',login_required(views.toperacion), name="toperacion"),
    path('registrarTOperacion/',login_required(views.registrarTOperacion)), 
    path('listaToperaciones/', login_required(views.listaToperaciones), name="listaToperaciones"),
    path('listaToperaciones/eliminarTO/<id>', login_required( views.eliminarTO)),
    path('listaToperaciones/editarTO/<id>',login_required(  views.editarTO)),
    path('ModificarTO/',login_required(  views.ModificarTO)),

# para infraestructura de inspeccion para lote
    path('infraestructura/',login_required(views.infraestructura), name="infraestructura"),
    path('registrarInfraestructura/',login_required(views.registrarInfraestructura)), 
    path('listaInfraestructura/', login_required(views.listaInfraestructura), name="listaInfra"),
    path('listaInfraestructura/eliminarInf/<id>', login_required( views.eliminarInf)),
    path('listaInfraestructura/editarInf/<id>', login_required( views.editarInf)),
    path('ModificarInf/', login_required( views.ModificarInf)),

# para infraestructura de inspeccion para mejoramientos de viviendas
    path('infraestructuram/',login_required(views.infraestructuram), name="infraestructuram"),
    path('registrarInfraestructuram/',login_required(views.registrarInfraestructuram)), 
    path('listaInfraestructuram/', login_required(views.listaInfraestructuram), name="listaInfram"),
    path('listaInfraestructuram/eliminarInfm/<id>', login_required( views.eliminarInfm)),
    path('listaInfraestructuram/editarInfm/<id>', login_required( views.editarInfm)),
    path('ModificarInfm/', login_required( views.ModificarInfm)),

# Tasa de interes
    path('tasa',views.tasa, name="tasa"),
    path('registrartasa/',views.registrartasa),
    path('listarTasa',views.listarTasa, name="listarTasa"),

# Alternativas de vivienda
    path('alternativa',views.alternativa, name="alternativa"), 
    path('registraral/',views.registraral),  
    path('listarAl',views.listarAl, name="listarAl"), 

# Rangos de financiamientos
    path('rangoFinanciamiento',views.rangoFinanciamiento, name="rangoFinan"), 
    path('registrarRanFin/',views.registrarRanFin), 
    path("listaRanFin/", views.listarRanFin, name="listaRanFin"), 
    path('lisAltRan/',views.lisAltRan, name="listaRanAlt"),
    path('modiRanFin/<id>', views.modRanFin),
    path('editRanFin/',views.editRanFin),
    
#para tipos de viviendas
    path('tvivienda/',login_required(views.tvivienda), name="tvivienda"),
    path('registrarModeloV/',login_required(views.registrarModeloV)), 
    path("listaModeloV/", login_required( views.listarModeloV), name="listaModeloV"), 
    path('listaModeloV/editarModeloV/<id>',login_required(views.editarMV)),
    path('modificarMV/', views.modificarMV),

]

## agregar esto cuando se trabaje con archivo en cada urls de cada app 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )