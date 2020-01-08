from django.contrib import admin
from education.models import EducationInfo
# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id','user','school_name','city','state','degree','specialization','field','graduation_date','present_check','slug')
    list_display_links = ('id','school_name')
    list_filter = ('school_name','city','state','degree','specialization')
    list_Editable = ('present_check',)
    search_fields = ('school_name','city','state','degree','specialization')
    list_per_page = 25

admin.site.register(EducationInfo,EducationAdmin)
