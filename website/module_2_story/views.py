from django.shortcuts import render

# Create your views here.

def story(request):
    return render(request, "story.html")

def examples(request):
    return render(request, "examples.html")

def ukrainian_story(request):
    return render(request, "ukrainian_story.html")

def traveling_story(request):
    return render(request, "traveling_story.html")
