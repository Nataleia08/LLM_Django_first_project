from django.urls import path

from . import views

urlpatterns = [
    path('stories/', views.stories, name = "stories"),
    path('story_deteils/<int:story_id>', views.story_deteils, name='story_deteils'),
    path('tag/', views.tag, name = 'tag'),
    path('category/', views.category, name = 'category'),
    path('traveling_stories/', views.traveling_story, name = 'traveling_story'), 
    path('ukrainian_stories/', views.ukrainian_story, name='ukrainian_story'), 
    path('create_story/', views.create_story, name='create_story'), 
    path('edit_story/<int:story_id>', views.edit_story, name='edit_story')
]