from django.db import models
from personal_info.models import ContactInfo
from django.urls import reverse
# Create your models here.

class Summary(models.Model):
    user = models.ForeignKey(ContactInfo,related_name='has_summary',on_delete=models.DO_NOTHING)
    summary = models.TextField()
    history = models.TextField()
    last_update_date = models.DateField(blank=True,null=True)

    def __str__(self):
        x = self.summary
        return x[:20]

    def get_absolute_url(self):
        return reverse('review:list')    

