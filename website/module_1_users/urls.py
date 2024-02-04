from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('story/', views.story, name = "story"),
    path('bot_translater/', views.bot_translater, name = "bot_translater"), 
    path('contacts/', views.contacts, name = 'contacts'), 
    path('examples/', views.examples, name = 'examples'), 
    path('traveling_story/', views.traveling_story, name = 'traveling_story'), 
    path('ukrainian_story/', views.ukrainian_story, name='ukrainian_story'), 
    path('my_project/', views.my_project, name='my_project')
]