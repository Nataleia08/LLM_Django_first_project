from django.urls import path

from . import views

urlpatterns = [
    path('my_project/', views.my_project, name='my_project'),
    path('translater/', views.bot_translater, name='translater')
    
]