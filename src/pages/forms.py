from django import forms
from .models import Page


class PageForm(forms.ModelForm):

	class Meta:
		model = Page # this form is for the Page model
		fields = ['title', 'content', 'order'] # inputs to edit in the form
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Título'}), #HTML + Clase de Bootstrap para el input Title
			'content': forms.Textarea(attrs={'class':'form-control' }),
			'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Orden'}),
		}
		#labels = { # hide or rename labels
		#	'title': '',
		#	'order': '',
		#	'content': ''
		#}