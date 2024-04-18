from django.urls import path

from . import views

urlpatterns = [
    path('stories/', views.story, name = "story"),
    path('examples/', views.examples, name = 'examples'), 
    path('traveling_stories/', views.traveling_story, name = 'traveling_story'), 
    path('ukrainian_stories/', views.ukrainian_story, name='ukrainian_story'), 
    path('create_story/', views.create_story, name='create_story')
]