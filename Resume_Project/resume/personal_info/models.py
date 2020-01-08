from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class ContactInfo(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    slug = models.SlugField(allow_unicode = True,unique = True)
    address = models.CharField(max_length = 500)
    city = models.CharField(max_length = 256)
    state = models.CharField(max_length = 256)
    zip_code = models.PositiveIntegerField()
    country = models.CharField(max_length = 256)
    email = models.EmailField(max_length = 256,unique=True)
    phone = models.CharField(max_length = 20)
    profile_pic = models.ImageField(upload_to='profile_pic/%Y/%m/%d/',blank = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True,null = True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def get_absolute_url(self):
        
        return reverse('experience:experience_index',kwargs={'slug':self.slug})
        #return reverse('experience:experience_index')
    
    def __str__(self):
        return self.first_name

    class Meta():
        ordering = ['email']
        unique_together = ('first_name','email')