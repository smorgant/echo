from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150,null=False, blank=True)
    year = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    poster = models.CharField(max_length=255)
    imdbrating = models.DecimalField(max_digits=2, decimal_places=1)
    imdbid = models.CharField(max_length=50)
    releasedate = models.DateTimeField('Date of Released')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Movietitle(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title