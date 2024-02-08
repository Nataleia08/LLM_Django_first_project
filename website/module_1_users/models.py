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



class Category(models.TextChoices):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return f"{self.name}"


class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length = 100)
    type = EnumField(TypeStory)
    tags = models.ManyToManyField(Tag)
    category = EnumField(Category)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 100)
    desctription = models.CharField(max_length = 1000)
    link = models.CharField(max_length = 100)
    link_dithub = models.CharField(max_length = 100)
    tags = models.ManyToManyField(Tag)
    category = EnumField(Category)


class Example(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tags = models.ManyToManyField(Tag)
    category = EnumField(Category)
    dataset = models.TextField()
    result = models.TextField()


