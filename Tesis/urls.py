"""Tesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TesisApp.urls')),
    path('DireccionApp/', include('DireccionApp.urls')),
    path('ClienteApp/', include('ClienteApp.urls')),
    path('ConfiguracionApp/', include('ConfiguracionApp.urls')),
    path('SolicitudesApp/', include('SolicitudesApp.urls')),
    path('ConozcaClienteApp/', include('ConozcaClienteApp.urls')),
    path('NaturalApp/', include('NaturalApp.urls')),
    path('ReviApp/', include('ReviApp.urls')),
    path('DeclaracionJurClienteApp/', include('DeclaracionJurClienteApp.urls')),
    path('SolicitudInscripcionSApp/', include('SolicitudInscripcionSApp.urls')),
    path('InspeccionLoteApp/', include('InspeccionLoteApp.urls')),
    path('InspeccionMejViviendaApp/', include('InspeccionMejViviendaApp.urls')),
    path('GraficasApp/', include('GraficasApp.urls')),
    path('Reportes/', include('Reportes.urls')),
    path('EvaluacionIvEFApp/', include('EvaluacionIvEFApp.urls')),
    path('EvaluacionMicroApp/', include('EvaluacionMicroApp.urls')),
    path('HistorialApp/', include('HistorialApp.urls')),
    path('PresupuestoApp/', include('PresupuestoApp.urls')),
    path('PresupuestoVApp/', include('PresupuestoVApp.urls')),
    path('ListaChequeoApp/', include('ListaChequeoApp.urls')),
]
