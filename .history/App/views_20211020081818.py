from django.shortcuts import render
from .models import Projects
from D_A


# Create your views here.
def home(request):
    return render(request,'index.html')

