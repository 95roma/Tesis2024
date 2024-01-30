
from tkinter import CASCADE
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 
from ConfiguracionApp.models import Agencia
import uuid

class UsuarioManager(BaseUserManager): #metodos consultas cre
    def create_user(self,email,username,nombre,apellido,password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')

        user=self.model(username=username,nombre=nombre,apellido=apellido,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user ## si creamos un usuario normal

    def create_superuser(self,email,username,nombre,apellido,password):
        user=self.create_user(
            email,username=username,nombre=nombre,apellido=apellido,password=password)
        user.usuario_administrador=True
        user.save()
        return user ## si creamos un usuario normal

# Create your models here.

class Usuario(AbstractBaseUser):
    iduser=models.AutoField(primary_key=True)#autoincrementable
    username=models.CharField('Nombre del usuario',unique=True,max_length=200)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=70)
    cargo=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=500)
    agencia=models.ForeignKey(Agencia, on_delete=models.CASCADE)
    usuario_administrador=models.BooleanField(default= False)
    token=models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    objects = UsuarioManager()
   
    USERNAME_FIELD='username'  #Inicio de sesion del administrador de django
    
    REQUIRED_FIELDS= ['email','nombre','apellido'] #campos que son requeridos

    #para que me retorne estos campos
    def __str__(self):
        return f'{self.username}' #f'{self.nombre},{self.apellido},{self.email},{self.agencia}'

    #al reescribir user porque se esta utilizando usuario obliga la clase AbstractBaseUser
    def has_perm(self,perm,obj=None):
        return True

    #admin de django
    def has_module_perms(self,app_label):
        return True
    #si el usuario es admin o no 
    @property
    def is_staff(self):
        return self.usuario_administrador


class Bitacora(models.Model):
    id= models.AutoField(primary_key=True)
    fechaHora= models.DateTimeField(auto_now_add=False)
    actividad= models.CharField(max_length=80)
    nivel= models.CharField(max_length=15)
    idusuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)   
    

    class Meta:
        verbose_name='bitacora'
        verbose_name_plural='bitacoras'
        db_table= 'bitacora'
    
    