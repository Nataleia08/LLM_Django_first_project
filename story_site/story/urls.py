from django.urls import path
import uuid
from uuid import UUID

from . import views

urlpatterns = [
    path('stories/', views.stories, name = "stories"),
    path('story_details/<str:story_id>', views.story_details, name='story_details'),
    path('stories/<str:story_id>', views.story_details, name='story_details'),
    path('traveling_stories/<str:story_id>', views.story_details, name='story_details'),
    path('ukrainian_stories/<str:story_id>', views.story_details, name='story_details'),
    path('tag/', views.tag, name = 'tag'),
    path('category/', views.category, name = 'category'),
    path('traveling_stories/', views.traveling_story, name = 'traveling_story'), 
    path('ukrainian_stories/', views.ukrainian_story, name='ukrainian_story'), 
    path('create_story/', views.create_story, name='create_story'), 
    path('edit_story/<str:story_id>', views.edit_story, name='edit_story'), 
    path('delete/<str:story_id>', views.delete_story, name='delete_story')
]