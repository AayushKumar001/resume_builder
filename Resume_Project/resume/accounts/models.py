from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your models here.
class User(User,PermissionRequiredMixin):

    def __str__(self):
        return "@{}".format(self.username)
