from django.contrib import admin
from experience.models import Experience
# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id','employer','job_title','city','state','start_date','end_date','last_update_date','currently_work','description')
    list_display_links = ('id','employer')
    list_filter = ('employer',)
    list_editable = ('currently_work',)
    search_fields = ('employer','job_title','city','state')
    list_per_page = 25
admin.site.register(Experience,ExperienceAdmin)
