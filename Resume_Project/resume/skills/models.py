from django.db import models
from personal_info.models import ContactInfo
from django.urls import reverse
from django.utils.timezone import localdate
# Create your models here.

class KeySkill(models.Model):

    user = models.ForeignKey(ContactInfo,related_name='key_skills',on_delete=models.CASCADE)
    key_skill = models.TextField()
    last_update_date = models.DateField(blank=True,null=True)
    
    class Meta():
        ordering = ['-last_update_date']

    def __str__(self):
        return self.key_skill

    def get_absolute_url(self): 
        print('Hello from key skill model')
        return reverse('skills:list')    

class TechSkill(models.Model):

    user = models.ForeignKey(ContactInfo,related_name='tech_skills',on_delete=models.CASCADE)        
    tech_skill = models.CharField(max_length=255)
    tech_skill_description = models.TextField()
    version = models.DecimalField(max_digits=4,decimal_places=2)
    last_used = models.CharField(max_length=50,default="")
    experience = models.DecimalField(max_digits=4,decimal_places=2)
    rating = models.DecimalField(max_digits=4,decimal_places=2,default = 1.0)
    last_update_date = models.DateField(blank=True,null=True)  

    class Meta():
        ordering = ['-last_update_date']

    def __str__(self):
        return self.tech_skill

    def get_absolute_url(self): 
        print('Hello from key skill model')
        return reverse('skills:list')        