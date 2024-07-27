from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    src = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
