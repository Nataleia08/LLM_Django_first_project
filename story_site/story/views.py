from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import TagForm, StoryForm, CategoryForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Story, Tag, Category, TypeStory


def ukrainian_story(request):
    ukrainian_story = Story.objects.filter(type = "U")
    return render(request, "ukrainian_story.html", {"ukrainian_story": ukrainian_story})

def traveling_story(request):
    traveling_story = Story.objects.filter(type = "T")
    return render(request, "traveling_story.html", {"traveling_story": traveling_story})

def stories(request):
    stories = Story.objects.all
    return render(request, "stories.html" , {"stories": stories})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='model_1_users:index')
        else:
            return render(request, 'tag.html', {'form': form})

    return render(request, 'tag.html', {'form': TagForm()})

@login_required
def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect(to='model_1_users:index')
        else:
            return render(request, 'category.html', {'form': form})

    return render(request, 'category.html', {'form': CategoryForm()})



def story_deteils(request, story_id):
    story_deteils = get_object_or_404(Story, pk=story_id)
    return render(request, 'story.html', {"story_deteils": story_deteils})

@login_required
def delete_story(request, story_id):
    Story.objects.get(pk=story_id, user=request.user).delete()
    return redirect(to='model_1_users:index')


@login_required
def create_story(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    typies = TypeStory.choices

    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            new_story = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_story.tags.add(tag)

            choice_categories = Category.objects.filter(name__in=request.POST.getlist('categories'))
            for category in choice_categories.iterator():
                new_story.categories.add(category)

            choice_type = TypeStory.value(name__in=request.POST.getlist('typies'))
            new_story.type.add(choice_type)

            return redirect(to='model_1_users:index')
        else:
            return render(request, 'create_story.html', {"tags": tags, 'categories': categories, 'type': typies, 'form': form})

    return render(request, 'create_story.html', {"tags": tags, 'categories': categories, 'type': typies, 'form': StoryForm()})

@login_required
def edit_story(request, story_id):
    new_story = get_object_or_404(Story, pk=story_id, user=request.user)

    tags = Tag.objects.all()
    categories = Category.objects.all()
    typies = TypeStory.choices

    if request.method == 'PUT':
        form = StoryForm(request.PUT)
        if form.is_valid():
            new_story = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_story.tags.add(tag)

            choice_categories = Category.objects.filter(name__in=request.POST.getlist('categories'))
            for category in choice_categories.iterator():
                new_story.categories.add(category)

            choice_type = TypeStory.value(name__in=request.POST.getlist('typies'))
            new_story.type.add(choice_type)

            return redirect(to='model_1_users:index')
        else:
            return render(request, 'edit_story.html', {"tags": tags, 'categories': categories, 'type': typies, 'form': form})

    return render(request, 'edit_story.html', {"tags": tags, 'categories': categories, 'type': typies, 'form': StoryForm()})