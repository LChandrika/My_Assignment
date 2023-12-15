from django.db import models

# Create your models here.
class Movie(models.Model):
    movieid=models.IntegerField()
    name=models.CharField(max_length=20)
    release_date=models.DateField()
    Director=models.CharField(max_length=50)