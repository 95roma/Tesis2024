from django.urls import path
from EvaluacionMicroApp import views
from SolicitudesApp import views as views1
from Reportes import views as viewsnat

urlpatterns = [
    
    path('evaluacionm/',views.evaluacionm, name="evaluacionm"),  
    path('registrarEvaluacionm/',views.registrarEvaluacionm), 
    path('listaEvaluacionm/', views.listaEvaluacionm, name="listaMicro"),
    path('listaEvaluacionm/editarEvaluacionm/<id>', views.editarEvaluacionm),
    path('listaEvaluacionm/darBajaM/<id>/<idp>', views.darBajaM),
    path('modificarEvaluacionm/', views.modificarEvaluacionm),

    #para solicitud micro
    path('listaEvaluacionm/solicitudMicro/<idCliente>',views1.registrarSolicitud, name="solicitudMicro"),

    # para reporte
    path('listaEvaluacionm/evaluacionIM/<id>', viewsnat.evaluacionM, name="evaluacionIM"),

  
]