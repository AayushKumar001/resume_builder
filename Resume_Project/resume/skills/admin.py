from django.contrib import admin
from skills.models import TechSkill,KeySkill
# Register your models here.

class TechAdmin(admin.ModelAdmin):
    list_display = ('id','user','tech_skill','tech_skill_description','version','experience','rating','last_used','last_update_date')
    list_display_links = ('id','tech_skill')
    list_filter = ('tech_skill',)
    search_fields = ('tech_skill',)
    list_per_page = 25

admin.site.register(TechSkill,TechAdmin)

class KeyAdmin(admin.ModelAdmin):
    list_display = ('id','user','key_skill')
    list_display_links = ('id','key_skill')
    list_filter = ('key_skill',)
    search_fields = ('key_skill',)
    list_per_page = 25    

admin.site.register(KeySkill,KeyAdmin)
