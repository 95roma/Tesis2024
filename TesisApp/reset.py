
from django import forms
from TesisApp.models import Usuario


class ResetPasswordForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Ingrese un usuario',
        'class': 'form-control',
        'autocomplete':'off'
    }))

    def clean(self):
        cleaned= super().clean()
        if not Usuario.objects.filter(username=cleaned['username']).exists():
            #self.error_messages['error']
            self._errors['error']=self._errors.get('error', self.error_class())
            self._errors['error'].append('El usuario no existe')
            #raise forms.ValidationError('El usuario no existe')
        return cleaned
    
    def get_user(self):
        username=self.cleaned_data.get('username')
        return Usuario.objects.get(username=username)
    

class ChangePasswordForm(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Ingrese una contraseña',
        'class': 'form-control',
        'autocomplete':'off'
    }))

    confirmPassword=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repita la contraseña',
        'class': 'form-control',
        'autocomplete':'off'
    }))

    def clean(self):
        cleaned= super().clean()
        password=cleaned['password']
        confirmPassword=cleaned['confirmPassword']
        if password != confirmPassword:
            
            self._errors['error']=self._errors.get('error', self.error_class())
            self._errors['error'].append('El usuario no existe')
            #self.error_messages['error'] = 'Las contraseñas deben ser iguales'
            #raise forms.ValidationError('Las contraseñas deben ser iguales')
        return cleaned

    