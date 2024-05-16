from django.urls import path

from . import views

urlpatterns = [
    path('my_projects/', views.my_projects, name='my_projects'),
    path('my_projects/<str:project_id>', views.project_view, name='project_view'),
    path('translater/', views.bot_translater, name='translater'), 
    path('examples/', views.examples, name='examples'),
    path('examples/<str:exampl_id>', views.exampl_view, name='exampl_view'),
    path('chat/', views.chat, name='chat')
    
]