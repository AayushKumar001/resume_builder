from django.db import models
from personal_info.models import ContactInfo
from django.urls import reverse
# Create your models here.

class EducationInfo(models.Model):  

    user = models.ForeignKey(ContactInfo,related_name='educations',on_delete=models.CASCADE)
    school_name = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    degree = models.CharField(max_length=256,default="")
    specialization = models.CharField(max_length=256,default="")
    field = models.CharField(max_length=256)
    graduation_date = models.DateField(blank=True,null=True)
    present_check = models.BooleanField(default=False)
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.school_name

    def get_absolute_url(self): 
        print('Hello from model')
        return reverse('education:list')
    
