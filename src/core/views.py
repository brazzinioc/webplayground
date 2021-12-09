from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):

	template_name = "core/home.html"
	
	def get(self, request, *args, **kwargs): # get() is alternative to get_context_data()
		return render(request, self.template_name, {'title':  'Welcome to WebPlayground :)'} )



class SamplePageView(TemplateView):

	template_name = "core/sample.html"