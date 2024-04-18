from django.contrib import admin
from .models import Tag, TypeStory, Story, Category

# Register your models here.

admin.site.register(Tag)
admin.site.register(Story)
admin.site.register(Category)