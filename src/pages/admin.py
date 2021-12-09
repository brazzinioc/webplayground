from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    
    # Inject css for CKEditor in Admin panel
    class Media:
    	css = {
    		'all' : ('pages/css/custom_ckeditor.css',)
    	}
    	#js = {
      #
      #}




admin.site.register(Page, PageAdmin)
