
from django.shortcuts import render
from home.models import Project

def home_index(request):
    home = Project.objects.all()
    context = {
        'home': home
    }
    return render(request, 'home_index.html', context)

def home_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'home_detail.html', context)