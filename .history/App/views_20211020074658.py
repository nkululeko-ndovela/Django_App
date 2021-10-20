from django.shortcuts import render
from .models import add


# Create your views here.
def home(request):
    return render(request,'index.html')

