from django.shortcuts import render
from .models import add, home

# Create your views here.
def home(request):
    return render(request,'index.html')

