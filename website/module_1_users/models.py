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

    