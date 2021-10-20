from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class add(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    St_Number = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
