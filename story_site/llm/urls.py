from django.urls import path

from . import views

urlpatterns = [
    path('my_projects/', views.my_projects, name='my_projects'),
    path('project/<int:project_id>', views.project_view, name='project_view'),
    path('translater/', views.bot_translater, name='translater'), 
    path('examples/', views.examples, name='examples'),
    path('chat/', views.chat, name='chat')
    
]