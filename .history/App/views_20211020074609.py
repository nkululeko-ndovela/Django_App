from django.shortcuts import render
from .models import add
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
def home(request):
    return render(request,'index.html')

