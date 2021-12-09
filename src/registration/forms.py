from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile

# Formulario para la creación de usuario con Email
class UserCreationFormWithEmail(UserCreationForm):
	email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres máximp y debe ser válido') # añade el campo email en el form

	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2'] # Email ya es un campo en el modelo User.

	# validando email en la BD. Obligatorio que debe iniciar con clean y terminar con un campo válido del Modelo.
	def clean_email(self):
		email = self.cleaned_data.get('email') # Recupera el email enviado en el form
		if User.objects.filter(email=email).exists(): # Valida en la BD
			raise forms.ValidationError("El email ya está registrado, prueba con otro") # Si existe manda el error, INVOCA UN ERROR DE VALIDACION
		return email



# Formulario para Actualización de Perfil
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio', 'avatar', 'link'] # Campos que se van a mostrar en el formulario
    widgets = {
      'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-1'}),
      'bio': forms.Textarea(attrs={'class':'form-control mt-1', 'rows':3, 'placeholder':'Biografía'}),
      'link': forms.URLInput(attrs={'class':'form-control mt-1', 'placeholder':'Enlace'}),
    }




# Formulario para actualizar email
class EmailForm(forms.ModelForm):
  email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres máximp y debe ser válido') # añade el campo email en el form

  class Meta:
    model = User
    fields = [ 'email' ]

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if 'email' in self.changed_data: # Si el email fue modificado
      if User.objects.filter(email=email).exists(): # valida email único en la BD
        raise forms.ValidationError("El email ya está registrado, prueba con otro")
    return email