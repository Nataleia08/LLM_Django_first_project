from django.contrib import admin
from .models import UserProfile, Category, Story, Project, Example, Tag

admin.site.register(UserProfile)
admin.site.register(Story)
admin.site.register(Project)
admin.site.register(Example)
admin.site.register(Tag)
