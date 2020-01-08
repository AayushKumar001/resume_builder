from django.db import models
from personal_info.models import ContactInfo
from django.urls import reverse
from django.utils.timezone import localdate
from django.utils import timezone

# Create your models here.

class Experience(models.Model):
    user = models.ForeignKey(ContactInfo,related_name='has_experience',on_delete=models.CASCADE)
    employer = models.CharField(max_length=256)
    job_title = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    last_update_date = models.DateField(default=timezone.now)
    currently_work = models.BooleanField(default=False)
    description = models.TextField()
    career_field = models.TextField()
    career_subfield = models.TextField()

    def __str__(self):
        return self.employer

    def get_absolute_url(self): 
        return reverse('experience:list')
        #return reverse('experience:list',kwargs={'pk':self.pk})

    class Meta():
        ordering = ['employer']