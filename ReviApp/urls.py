from django.urls import path
from ReviApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.revi, name="revi"),
    path('registrarDocu/',views.registrarDocu),
    path('listarDocu/',views.listarDocu, name="listarDocu"),
    path('docu/',views.docu), 
    path('modiDocu/<id>',views.modiDocu, name="modiDocu"),
    path('editDocu/',views.editDocu),
  
]
## agregar esto cuando se trabaje con archivo en cada urls de cada app 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
