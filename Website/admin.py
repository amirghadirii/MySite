from django.contrib import admin
from Website.models import contact
from Website.models import Newsletter
# Register your models here.

class contactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')
    
admin.site.register(contact,contactAdmin)
admin.site.register(Newsletter)