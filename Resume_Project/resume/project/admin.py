from django.contrib import admin
from project.models import Project,Certification
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','user','title','description','technology','link_html','last_update_date')
    list_display_links = ('id','title')
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Project,ProjectAdmin)

class CertAdmin(admin.ModelAdmin):
    list_display = ('id','user','certification','certification_body','year','last_update_date')
    list_display_links = ('id','certification')
    list_filter = ('certification','certification_body')
    search_fields = ('certification','certification_body','year')
    list_per_page = 25

admin.site.register(Certification,CertAdmin)
