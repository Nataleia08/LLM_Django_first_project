from django.db import models
import uuid
from django_enum import EnumField


class TypeStory(models.TextChoices):
    BASIC = "B", "basic"
    TRAVELING = "T", "traveling"
    UKRAINIAN = "U", "ukrainian"

# Create your models here.
class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)


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
    category = models.ManyToManyField(Category)


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


