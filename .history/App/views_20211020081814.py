from django.shortcuts import render
from .models import Projects
from D_


# Create your views here.
def home(request):
    return render(request,'index.html')

