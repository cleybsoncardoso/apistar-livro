from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)


class Book(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
