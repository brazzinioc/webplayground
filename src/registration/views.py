#from django.contrib.auth.forms import UserCreationForm #esto ya no lo usamos por que agregamos el field email en forms.py
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
	form_class = UserCreationFormWithEmail
	template_name = 'registration/signup.html'

	# Recupera la URL y añade parámetro por GET "register", para mostrar mensaje en el template.
	def get_success_url(self):
		return reverse_lazy('login') + '?register' # redirección a login

	def get_form(self, form_class=None):
		form = super(SignUpView, self).get_form() # obtiene el formulario
	
    # Modificación de widgest en tiempo de ejecución. Sobreescribe los atributos de cada input. No se hace esta modificación en Form por que estaría sobreescribiendo validaciones del mismo django.
		form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
		form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo electrónico'})
		form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Contraseña'})
		form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Repite la contraseña'})
		return form


# Vista para actualizar el perfil del usuario
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
  #model = Profile # model ya viene en el formulario
  form_class = ProfileForm
  success_url = reverse_lazy('profile')
  template_name = 'registration/profile_form.html'

  def get_object(self):
    # Recuperar el objeto que se va a editar
    profile, created = Profile.objects.get_or_create(user=self.request.user) # si no existe lo crea (get_or_create)
    return profile


# Vista para actualizar el email del usuario
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
  form_class = EmailForm
  success_url = reverse_lazy('profile')
  template_name = 'registration/profile_email_form.html'

  def get_object(self):
    # Recuperar el objeto user desde
    return self.request.user

  def get_form(self, form_class=None):
    # Modificación de widgest en tiempo de ejecución. Sobreescribe los atributos de cada input.
    form = super(EmailUpdate, self).get_form()
    form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo electrónico'})

    return form