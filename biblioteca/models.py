from django.db import models

class Livro(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

