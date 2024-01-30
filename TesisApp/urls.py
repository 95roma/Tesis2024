from django.urls import path
from TesisApp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from TesisApp.views import Login,logoutUsuario, ResetPasswordView, ChangePasswordView
from ClienteApp import views as viewsc

urlpatterns = [
    
     path('',login_required(views.home), name="home"),
     #urls de acceso
     path('accounts/login/', Login.as_view(), name='login'),
     path('logout/', login_required(logoutUsuario), name='logout' ),
     path('reset/password/', ResetPasswordView.as_view(), name='reset_password' ),
     path('change/password/<str:token>/', ChangePasswordView.as_view(), name='change_password' ),
     #path('login/', auth_views.LoginView.as_view(template_name='TesisApp/login.html'), name='login'),
     #path('logout/', auth_views.LogoutView.as_view(template_name='TesisApp/login.html'), name='logout' ),
     #url libreria
     path('registroUsuario',views.registroUsuario, name="registroUsuario"),
     #path('iniciosession',views.iniciosession, name="iniciosession"),
     path('insertar/', views.insertar),
     

      # para perfil de inicio 
     path('perfils',views.perfils, name="perfils,"),
     path('rPerfils/',viewsc.registrarPerfil),
     path('municipio/',views.municipio),

     #Bitacora
     path('bitacora/', views.listaB, name="listaBit"),
     path('fechas/', views.fechas),
     

     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]