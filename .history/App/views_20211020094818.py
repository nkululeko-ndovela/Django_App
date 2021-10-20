from django.shortcuts import render
from App.models import Projects
from django.contrib import messages



# Create your views here.

def show(request):
    res=Projects.objects.all() 
    return render(request, 'index.html',{"Project":res})

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
    else:
            return render(request, 'index.html')

def pedit(request,id):
    getprojects=Projects.objects.get(id=id)
    return render(request, 'edit.html ',{"Projects":getprojects})