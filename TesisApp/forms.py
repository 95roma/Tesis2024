from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from TesisApp.models import Usuario

class FormularioLogin(AuthenticationForm):
    #email= forms.CharField(label='Email', max_length=254, required=True)
    def __init__(self,  *args, **kwargs):
        super(FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Ingrese el usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Ingrese la contraseña'
        self.error_messages['invalid_login'] = 'Tu usuario y/o contraseña no son correctos.'

        '''
def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'       
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

# self.fields['email'].label = 'Email'
class FormularioUsuario(forms.ModelForm):
    
    passwod1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'passwod1',
            'required':'required'
        }
    ))

    passwod2 = forms.CharField(label='Contraseña de Confirmación',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña',
            'id': 'passwod2',
            'required':'required'
        }
    ))

class Meta:
    model= Usuario
    fields= ('email','nombre','apellido')
    widgets={
        'email':forms.EmailInput(
           attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el email',   
        }),  
        'nombre':forms.TextInput(
           attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el Nombre',   
        } 
        ),  
        'apellido':forms.TextInput(
           attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el Apellido',   
        } 
        )
    }
'''