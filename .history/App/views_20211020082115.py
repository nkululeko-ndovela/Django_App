from django.shortcuts import render
from .models import Projects
from App.models import Project


# Create your views here.
def home(request):
    return render(request,'index.html')

def add(request):
    if request.method == 'POST':
        if request.POST.get('Project').request.POST.get('project').request.POST.get('project')