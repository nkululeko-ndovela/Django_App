from django.shortcuts import render
from .models import Add

# Create your views here.
def home(request):
    return render(request,'index.html')

