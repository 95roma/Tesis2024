from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import path
from SolicitudesApp import views
from ConozcaClienteApp import views as viewscc
from SolicitudInscripcionSApp import views as viewssi
from DeclaracionJurClienteApp import views as viewsdjc
from InspeccionLoteApp import views as viewsil
from InspeccionMejViviendaApp import views as viewsimv
from PresupuestoApp import views as viewsp
#from PresupuestoVApp import views as viewspv
from Reportes import views as viewsnat
from PresupuestoApp import views as viewsp
from PresupuestoVApp import views as viewspv

#from .views import
urlpatterns = [
   # path('modificarAgencia/', views.modificarAgencia),
    path('solicitudMicro/', views.registroSolicitudMicro, name='solicitudMicro'),
    path('registrarDatos/', views.registroSolicitud),
    path('modDatos/', views.modSoli),
    path('listaSoli/', views.listaSolicitud, name="listaSolicitud"),
    path('listaSoli/modificarSolicitudMicro/<idSolicitud>',views.modificarSolicitud),

    path('listaSC/', views.listaSC, name="listaSC"),
    path('listaSCA/<id>', views.listaSCA, name="listaSCA"),

    # para los reportes de formulario de comite de credito y hoja de pre-aprobacion
    path('listaRF/', views.listaRF, name="listaRF"),
    # para reporte formulario de comite de credito
    path('listaRF/formularioC/<id>', viewsnat.formComiteC, name="formularioC"),
    # para reporte hoja de pre-aprobacion
    path('listaRF/hojaP/<id>', viewsnat.hojaPreAprobacion, name="hojaP"),
    
    # para canozca a su cliente
    path('listaSC/ccliente/<id>', viewscc.ccliente),

    # para Solicitud de incripcion al seguro
    path('listaSC/solicitudI/<id>', viewssi.solicitudI),

    # para Declaración Jurada cliente
    path('listaSC/declaracionjc/<id>', viewsdjc.declaracionjc),

    # para reporte
    path('listaSC/historial/<id>',viewsnat.historialC, name="historial"),
    path('listaSC/solic/<ids>/<idp>',viewsnat.solicitudMicro, name="solic"),
    path('listaSC/soliPer/<idp>', viewsnat.SolicitudPe, name="soliPer"),

    # para Inspeccion lote
    path('listaSC/inspeccionl/<id>', viewsil.inspeccionl),

     # para Inspeccion mejora vivienda 
    path('listaSC/inspeccion/<id>', viewsimv.inspeccion), 

    # para Declaración Jurada cliente
    path('listaSoli/presupuesto/<id>', viewsp.presupuesto),

    # para Declaración Jurada cliente
    #path('listaSoli/presupuestov/<id>', viewspv.presupuestov),

    # para presupuesto mejora
    path('listaSC/presupuesto/<id>', viewsp.presupuesto),

    # para Presupuesto vivienda
    path('listaSC/presupuestov/<id>', viewspv.presupuestov),

    # para  solicitudes pendientes de aprobacion
    path('listaSolicitudesPA/', views.listaSolicitudesPA, name="listaSolicitudesPA"),
    # reporte de solicitudes pendientes de aprobacion
    path('listaSolicitudesPA/solP/<id>', viewsnat.solicPA, name="solP"), 
    path('listaSolicitudesPA/evaluarSol/<id>', views.evaluarSol),
    path('registrarEvaluacion/', views.registrarEvaluacion),

    # para  solicitudes observadas
    path('listaSolicitudesObs/', views.listaSolicitudesObs, name="listaSolicitudesObs"),
    # reporte de solicitudes observadas
    path('listaSolicitudesObs/solObs/<id>', viewsnat.solicObs, name="solObs"), 

    # para  solicitudes denegadas
    path('listaSolicitudesDen/', views.listaSolicitudesDen, name="listaSolicitudesDen"),
    # reporte de solicitudes denegadas
    path('listaSolicitudesDen/solDen/<id>', viewsnat.solicDen, name="solDen"), 

    path('obtenerRango/' ,views.obtenerRango, name='obtenerRango'),
   
]
