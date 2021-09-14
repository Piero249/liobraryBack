from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    published_year = models.CharField(max_length=4)
    edition = models.CharField(max_length=4)
    image = models.TextField()
    stock = models.IntegerField()