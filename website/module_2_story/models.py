from django.db import models
from module_1_users.models import UserProfile
import uuid
from django_enum import EnumField

# Create your models here.

class TypeStory(models.TextChoices):
    BASIC = "B", "basic"
    TRAVELING = "T", "traveling"
    UKRAINIAN = "U", "ukrainian"



class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25, null=False, unique=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, null=False, unique=True, default = "life")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name}"


class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length = 100)
    type = EnumField(TypeStory, default = "B")
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)