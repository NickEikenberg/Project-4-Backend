from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=32)
    message = models.CharField(max_length=280)
    title = models.CharField(max_length=24, default='')
    likes = models.IntegerField(default=0)

