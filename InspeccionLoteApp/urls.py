from django.urls import path
from InspeccionLoteApp import views
from Reportes import views as viewsnat
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('',views.inspeccionl, name="inspeccionl"),
path('registrarDIL/',views.registrarDIL), 
path('listaI/', views.listaI, name="listaI"),
path('listaI/editarIL/<id>', views.editarIL, name="editarIL"),
path('modificarIL/', views.modificarIL),
#para reporte
path('listaI/inspeccionL/<id>', viewsnat.inspeccionL, name="inspeccionL"),

# primera inspeccion
path('listaI/pinspeccionl/<id>/<n>',views.pinspeccionl, name="pinspeccionl"),
path('registrarPIL/',views.registrarPIL), 
path('listaPIL/', views.listaPIL, name="listaPIL"),
path('listaPIL/editarPIL/<id>',views.editarPIL), 
path('modificarPIL/', views.modificarPIL),

# para reporte primera inspeccion esquema
path('listaPIL/pinspl/<id>', viewsnat.pinspecL, name="pinspl"),
# para reporte primera inspeccion ubicacion
path('listaPIL/pinsplU/<id>', viewsnat.pinspecLU, name="pinsplU"),
# para reporte primera inspeccion reporte fotografico
path('listaPIL/pinsplR/<id>', viewsnat.pinspecLR, name="pinsplR"),

]

## agregar esto cuando se trabaje con archivo en cada urls de cada app 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )