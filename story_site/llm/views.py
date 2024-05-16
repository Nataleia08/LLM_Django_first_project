from django.shortcuts import render
from .models import Project, Example
from django.shortcuts import get_object_or_404

# Create your views here.

def my_projects(request):
    projects = Project.objects.all
    return render(request, "my_projects.html", {'projects': projects})

def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project.html', {"project": project})

def bot_translater(request):
    return render(request, "translater.html")

# def examples(request):
#     return render(request, "examples.html")

def chat(request):
    return render(request, "chat.html")

def examples(request):
    my_examples = Example.objects.all
    return render(request, "examples.html", {'my_examples': my_examples})

def exampl_view(request, exampl_id):
    exampl = get_object_or_404(Example, pk=exampl_id)
    return render(request, "exampl.html", {'exampl': exampl})