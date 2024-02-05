from django.db import models
import uuid

# Create your models here.


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    

class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length = 100)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100)
    desctription = models.CharField(max_length = 1000)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 100)
    desctription = models.CharField(max_length = 1000)
    link = models.CharField(max_length = 100)
    link_dithub = models.CharField(max_length = 100)

class Example(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Traveling_Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Ukrainian_Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)