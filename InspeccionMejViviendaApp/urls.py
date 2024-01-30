from django.urls import path
from InspeccionMejViviendaApp import views
from Reportes import views as viewsnat
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('',views.inspeccion, name="inspeccion"),
path('registrarDIM/',views.registrarDIM), 
path('registrarDIME/',views.registrarDIME), 
path('listaIM/', views.listaIM, name="listaIM"),
path('listaIM/editarIM/<id>', views.editarIM,name='editarIM'),
path('actualizarIM/', views.actualizarIM),
# para reporte  
path('listaIM/inspeccionM/<id>', viewsnat.inspeccionM, name="inspeccionM"),

# primera inspeccion
path('listaIM/pinspeccion/<id>/<n>',views.pinspeccion, name="pinspeccion"),
path('registrarPIM/',views.registrarPIM), 
path('listaPIM/', views.listaPIM, name="listaPIM"),
path('listaPIM/editarPIM/<id>',views.editarPIM), 
path('modificarPIM/', views.modificarPIM),

# para reporte primera inspeccion ubicacion
path('listaPIM/pinspmU/<id>', viewsnat.pinspecMU, name="pinspmU"),
# para reporte primera inspeccion reporte fotografico
path('listaPIM/pinspmR/<id>', viewsnat.pinspecMR, name="pinspmR"),

]

## agregar esto cuando se trabaje con archivo en cada urls de cada app 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )