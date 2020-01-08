from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django import template
from personal_info.models import ContactInfo
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your models here.

register = template.Library()

class Project(models.Model):
    user = models.ForeignKey(ContactInfo,related_name='has_project',on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.TextField()
    link_html = models.CharField(max_length=100)
    github_link = models.CharField(max_length=255,default='',editable=False)
    last_update_date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project:list')
  

class Certification(models.Model):
    user = models.ForeignKey(ContactInfo,related_name='has_cert',on_delete=models.CASCADE)
    certification = models.CharField(max_length=255)
    certification_body = models.TextField()
    year = models.CharField(max_length=4)
    last_update_date = models.DateField()

    def __str__(self):
        return self.certification

    def get_absolute_url(self): 
        return reverse('project:list')
        