from django.db import models


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.title
