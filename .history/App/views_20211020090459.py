from django.shortcuts import render
from .models import Projects
from App.models import Project
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'index.html')
    

def add(request):
    if request.method == 'POST':
        if request.POST.get('Project_Name_Name').request.POST.get('Upload_by').request.POST.get('dated'):
            savest=Projects()
            savest.Project_Name=request.POST.get('Project_Name')
            savest.Upload_By=request.POST.get('Upload_By')
            savest.dated=request.POST.get('dated')
            savest.save()
            messages.success(request,'The Record'+savest.Porject_Name+"is added successful")
            return render(request, 'index.html')
    else
            return render(request, 'index.html')