from django.urls import path
from NaturalApp import views
from ConozcaClienteApp import views as viewscca
from SolicitudInscripcionSApp import views as viewssia
from DeclaracionJurClienteApp import views as viewsdjca
from SolicitudesApp import views as viewsS
from Reportes import views as viewsnat
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
     path('solicitudNatural/', views.registrarSolicitudNatu, name='solicitudNatural'),
     path('registrarDatosN/', views.registroSolicitudN),
     path('listarSN/',views.listarSN, name="listarSN"),  
     path('listarSNC',views.listarSNC, name="listarSNC"),
     path('listarSN/editarSolicitudN/<idSolicitud>',views.editarSolicitudN),
     path('modDatosNatural/', views.modSoliNatural),

     # para los reportes de formulario de comite de credito y hoja de pre-aprobacion
    path('listaRFN/', views.listaRF, name="listaRFN"),
    # para reporte formulario de comite de credito
    path('listaRFN/formularioCN/<id>', viewsnat.formComiteCN, name="formularioCN"),
    # para reporte hoja de pre-aprobacion
    path('listaRFN/hojaPN/<id>', viewsnat.hojaPreAprobacionN, name="hojaPN"),
     
     
     # reporte solicitud   
     path('listarSNC/soliPer/<ids>', login_required(viewsnat.SolicitudPe), name="soliPer"),
        
     # para canozca a su cliente
     path('listarSNC/ccliente/<id>', login_required(viewscca.ccliente)),

     # para Solicitud de incripcion al seguro
     path('listarSNC/solicitudI/<id>', login_required(viewssia.solicitudI)),

     # para Declaración Jurada cliente
     path('listarSNC/declaracionjc/<id>', login_required(viewsdjca.declaracionjc)),

     # para  solicitudes pendientes de aprobacion
    path('listaSolicitudesPA/', views.listaSolicitudesPA, name="listaSolicitudesPAN"),
    # reporte de solicitudes pendientes de aprobacion
    path('listaSolicitudesPA/solP/<id>', viewsnat.solicPA, name="solP"), 
    path('listaSolicitudesPA/evaluarSol/<id>', viewsS.evaluarSol),
    #path('registrarEvaluacion/', views.registrarEvaluacion),

    # para  solicitudes observadas
    path('listaSolicitudesObs/', views.listaSolicitudesObs, name="listaSolicitudesObsN"),
    # reporte de solicitudes observadas
    path('listaSolicitudesObs/solObs/<id>', viewsnat.solicObs, name="solObs"), 

    # para  solicitudes denegadas
    path('listaSolicitudesDen/', views.listaSolicitudesDen, name="listaSolicitudesDenN"),
    # reporte de solicitudes denegadas
    path('listaSolicitudesDen/solDen/<id>', viewsnat.solicDen, name="solDen"), 

    path('obtenerRango/' ,views.obtenerRango, name='obtenerRango'),
     

]