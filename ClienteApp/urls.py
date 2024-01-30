from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ClienteApp import views
from EvaluacionIvEFApp import views as viewseie
from EvaluacionMicroApp import views as viewseiem
from SolicitudesApp import views as views1
from NaturalApp import views as viewsN
from Reportes import views as viewsnat


urlpatterns = [
    
   # path('',views.home, name="home"),
    path('',views.perfil, name="perfil"),# apunta a la raiz 
    path('perfil/',views.perfilc, name="perfilc"),
    path('registrarPerfil/',views.registrarPerfil),   
    path('listaPerfil/', views.listaPerfil, name="listaPerfil"),
    path('listaPerfil/eliminarPerfil/<id>', views.eliminar),
    path('listaPerfil/editarPerfil/<id>', views.editarPerfil),
    path('modificarPerfil/', views.modificarPerfil),

    path('municipio/',views.municipio),
    path('distrito/',views.distri),

    #para evaluacion de ingresos vs egresos familiares   
    path('listaPerfil/evaluacionf/<id>',viewseie.evaluacionf),

    #para evaluacion de ingresos vs egresos Microempresarios   
    path('listaPerfil/evaluacionm/<id>',viewseiem.evaluacionm),

    # para asignar zona
    path('solicitud/<id>',views.solicitud), 
    path('registrarDetalle/',views.registrarDetalle),
    
    # para administracion de perfil
    path('listaClientes/', views.listaClienets, name="listaClientes"),
    path('listaClientes/administrarPerfil/<id>', views.administrarPerfil, name='administrarPerfil'),

    #para solicitud micro
    path('consultaEvaluacionMicro/', views.consulta_evaliacion_micro, name='consultaEvaluacionMicro'),
    path('consultaEvaluacionNatural/', views.consulta_evaliacion_natural, name='consultaEvaluacionNatural'),
    path('consultaTipoSolicitud/', views.consulta_tipo_solicitud, name='consultaTipoSolicitud'),
    path('registrarDocumento/',views.Registrar_documento, name='registrarDocumento'),
    path('obtenerHistorial/',views.obtener_historial, name='obtenerHistorial'),
    path('completarSolicitud/',views.completar_solicitud, name='completarSolicitud'),
    path('completarSolicitudBase/',views.completar_solicitud_base, name='completarSolicitudBase'),
    path('denegarSolicitud/',views.denegar_solicitud, name='denegarSolicitud'),
   # path('solicitudMicro/', views1.registroSolicitudMicro, name='solicitudMicro'),

    # para perfiles que no aplican
    path('listaPerfilNA/', views.listaPerfilNA, name="listaPerfilNA"),
    # reporte de perfiles que no aplican
    path('listaPerfilNA/pelfilNA/<id>', viewsnat.perfilNA, name="pelfilNA"), 

   
]
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )