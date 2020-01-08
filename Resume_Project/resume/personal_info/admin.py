from django.contrib import admin
from . import models
# Register your models here.

class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','slug','address','city','state','zip_code','country','email','phone','created_date')
    list_display_links = ('id','first_name')
    list_filter = ('first_name','last_name','city','state')
    search_fields = ('first_name','last_name','city','state','zip_code','country','created_date')
    list_per_page = 25

admin.site.register(models.ContactInfo,PersonalInfoAdmin)
