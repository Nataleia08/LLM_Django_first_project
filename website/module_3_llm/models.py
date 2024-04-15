from django.db import models
from module_2_story.models import Category, Tag
import uuid

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 100)
    desctription = models.CharField(max_length = 1000)
    link = models.CharField(max_length = 100)
    link_dithub = models.CharField(max_length = 100)
    tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)


class Example(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    dataset = models.TextField(default= "")
    result = models.TextField(default= "")