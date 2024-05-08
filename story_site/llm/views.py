from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.

def my_projects(request):
    projects = Project.objects.all
    return render(request, "my_projects.html", {'projects', projects})

def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    return render(request, 'project.html', {"project": project})

def bot_translater(request):
    return render(request, "translater.html")

def examples(request):
    return render(request, "examples.html")

def chat(request):
    return render(request, "chat.html")