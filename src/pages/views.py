from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from .forms import PageForm

from .models import Page


class StaffRequiredMixin(object): # object is the base class of all classes in Python.
    """ Este mixin requirirá que el usuario sea miembro del staff """
    
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        '''if not request.user.is_staff: # si el usuario no es del staff. comentado por que estamos usando el decorador del mismo django
            return redirect(reverse_lazy('admin:login')) #Redireccion al login del admin'''
        return super(StaffRequiredMixin, self).dispatch(request,*args, **kwargs)


# View to show a List of model Page. Use page_list.html template
class PageListView(ListView):
	model = Page


# View to show a One row of model Page. Use page_detail.html template
class PageDetailView(DetailView): 
	model = Page


# View to show page_form and create a new Page.
@method_decorator(staff_member_required, name="dispatch") # using mixin class without inheritance
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages') # redirect to List pages.


# View to update a Page row.
class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    # Alternative to success_url
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok' # get id of page and add '?ok' to url


# View to delete a Page row.
class PageDelete(StaffRequiredMixin, DeleteView):
	model = Page
	success_url = reverse_lazy('pages:pages')

